from django.urls import path
from django.http import JsonResponse
from django.core.paginator import Paginator


class LazyCountPaginator(Paginator):
    """
    Custom paginator that simulates a large total count for optimized
    performance and handles pagination dynamically to prevent page errors.
    """

    @property
    def count(self):
        """
        Simulate a large total count to improve initial page load performance.
        """
        return 99999999999999999999

    def calculate_count(self):
        """
        Calculate and cache the actual total count when required.
        Resets the number of pages to ensure recalculation.
        """
        if not hasattr(self, '_count'):
            self._count = super().count
            self._num_pages = None
        return self._count


class LazyLoadPaginationMixin:
    """
    Mixin for Django admin to enable lazy loading of paginated results,
    including custom count handling and a template for pagination UI.
    """

    paginator = LazyCountPaginator
    change_list_template = "django_admin_lazy_count/lazy_pagination.html"

    def get_urls(self):
        """
        Return custom URLs, including an endpoint for retrieving the total count.
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                "get-total-count/",
                self.admin_site.admin_view(self.get_total_count),
                name="%s_%s_get_total_count" % (
                    self.model._meta.app_label,
                    self.model._meta.model_name,
                ),
            ),
        ]
        return custom_urls + urls

    def get_total_count(self, request):
        """
        Return the total count of records in the queryset as a JSON response.
        """

        cl = self.get_changelist_instance(request)
        return JsonResponse({"total_count": cl.paginator.calculate_count()})


    def changelist_view(self, request, extra_context=None):
        """
        Render the changelist view with additional context for custom pagination behavior.
        """
        if extra_context is None:
            extra_context = {}
        extra_context["opts"] = self.model._meta
        return super().changelist_view(request, extra_context=extra_context)