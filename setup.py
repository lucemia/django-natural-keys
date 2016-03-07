import os
import sys
from setuptools import setup, find_packages

LONG_DESCRIPTION = """
Enhanced support for natural keys in Django and Django REST Framework
"""


def parse_markdown_readme():
    """
    Convert README.md to RST via pandoc, and load into memory
    (fallback to LONG_DESCRIPTION on failure)
    """
    # Attempt to run pandoc on markdown file
    import subprocess
    try:
        subprocess.call(
            ['pandoc', '-t', 'rst', '-o', 'README.rst', 'README.md']
        )
    except OSError:
        return LONG_DESCRIPTION

    # Attempt to load output
    try:
        readme = open(os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        ))
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()


setup(
    name='natural-keys',
    version='0.1.0-dev',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='https://github.com/wq/django-natural-keys',
    license='MIT',
    packages=['natural_keys'],
    description=LONG_DESCRIPTION.strip(),
    long_description=parse_markdown_readme(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database',
    ],
    test_suite='tests',
    tests_require=[
        'djangorestframework'
    ],
)