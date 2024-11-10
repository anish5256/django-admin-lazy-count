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
pip install git+https://github.com/yourusername/django-lazy-admin-pagination.git
```

**Or, install from PyPI (if published there):**

```bash
pip install django-lazy-admin-pagination
```

### Step 2: Add to `INSTALLED_APPS`

Add `django_lazy_admin_pagination` to the `INSTALLED_APPS` list in your Django project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...,
    'django_lazy_admin_pagination',
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

### Step 2: Verify Template Overrides

Ensure that the `lazy_pagination.html` template is available in your project's template path:

- **Default path in the package:**
  ```
  django_lazy_admin_pagination/templates/admin/your_app/yourmodel/lazy_pagination.html
  ```
- **Custom template directory (optional):** If needed, you can override or customize the template in your project by placing it in your own `templates/admin/your_app/yourmodel/` directory.

### Step 3: Static Files

Make sure to collect static files if you have any custom styles or scripts:

```bash
python manage.py collectstatic
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

## Customization and Advanced Usage

### Customizing the Template

If you want to modify how the pagination appears or behaves:

1. Copy the `lazy_pagination.html` template from the package directory to your project's `templates/admin/your_app/yourmodel/`.
2. Modify the copied template as desired.

### Adding CSS or JavaScript

To style or add custom JavaScript to your pagination controls:

- Place your custom CSS files in `django_lazy_admin_pagination/static/css/custom_styles.css`.
- Ensure you link them in your overridden templates if additional styles are needed.

### Caching the Total Count

For better performance on large datasets, the package uses a caching mechanism:

- **Cache Backend**: Ensure you have a caching backend configured in your Django settings (e.g., `Memcached`, `Redis`, or Django's default cache).
- **Custom Timeout**: You can adjust the cache timeout in `admin.py` when caching the total count.

```python
from django.core.cache import cache

# Example usage in get_total_count method
cache.set(cache_key, total_count, timeout=300)  # Adjust the timeout as needed
```

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

For any issues or questions, please submit a ticket on the [GitHub issues page](https://github.com/anish5256/django-lazy-admin-pagination/issues).

---