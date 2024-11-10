from setuptools import setup, find_packages

setup(
    name='django-lazy-admin-pagination',
    version='1.0.0',
    description='A Django package for lazy-loading pagination in the admin interface.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Anish Kumar',
    author_email='anish5256@gmail.com',
    url='https://github.com/anish5256/django-lazy-admin-pagination',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
