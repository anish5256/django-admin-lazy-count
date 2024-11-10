Here's a comprehensive guide for using the `django-lazy-admin-pagination` package, including installation, setup, and usage. This documentation can be added to your `README.md` or used as a separate documentation file.

---

# Django Lazy Admin Pagination

**django-lazy-admin-pagination** is a Django package designed to provide lazy-loading pagination for Django's admin interface. It enhances user experience by loading total counts asynchronously and updating pagination dynamically, improving performance on large datasets.

## Features

- **Lazy-loaded total count:** Avoids counting total records during initial page load, improving performance.
- **Dynamic pagination controls:** Updated via AJAX to reflect the correct number of pages.
- **Compatible with Django's standard admin interface.**

## Installation

### Step 1: Install the Package

You can install the package directly from GitHub or PyPI:

**Install from GitHub:**

```bash
pip install git+https://github.com/anish5256/django-lazy-admin-pagination.git
```

### Step 2: Add to `INSTALLED_APPS`

Add `django_lazy_admin_pagination` to the `INSTALLED_APPS` list in your Django project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...,
    'django_admin_lazy_count',
]
```

## Usage

### Step 1: Import and Use `LazyLoadPaginationMixin`

In your `admin.py`, modify your model admin class to include `LazyLoadPaginationMixin`.

```python
from django.contrib import admin
from django_lazy_admin_pagination.admin import LazyLoadPaginationMixin
from .models import YourModel

@admin.register(YourModel)
class YourModelAdmin(LazyLoadPaginationMixin, admin.ModelAdmin):
    list_per_page = 100  # Customize the number of items per page as needed
```


## Example Project Setup

Here's an example `admin.py` configuration for a Django project using the package:

```python
# admin.py
from django.contrib import admin
from django_lazy_admin_pagination.admin import LazyLoadPaginationMixin
from .models import Product

@admin.register(Product)
class ProductAdmin(LazyLoadPaginationMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    list_per_page = 50
```

### Explanation of the Code

- **`LazyLoadPaginationMixin`**: This mixin adds lazy-loading pagination functionality to the admin class.
- **`list_per_page`**: Specifies the number of items displayed per page. Adjust this value as needed.



## How It Works

1. **Initial Load**: The page loads with basic pagination controls, including "Previous" and "Next" buttons, while showing "Count is loading..."
2. **AJAX Call**: A JavaScript function makes an AJAX call to fetch the total count and updates the pagination controls once the data is received.
3. **Dynamic Update**: The pagination controls are updated to reflect the total number of pages, and the count is displayed in the admin search form.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support and Issues

For any issues or questions, please submit a ticket on the [GitHub issues page](https://github.com/anish5256/django-admin-lazy-count.git/issues).

---