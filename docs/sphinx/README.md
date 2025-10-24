# PyKitMoney Documentation

This directory contains the Sphinx documentation for PyKitMoney.

## Building the Documentation

### Prerequisites

Install development dependencies:

```bash
pip install -e ".[dev]"
```

### Build HTML Documentation

```bash
cd docs/sphinx
make html
```

Or use sphinx-build directly:

```bash
sphinx-build -b html source build
```

The generated HTML will be in `build/html/`.

### View Documentation

Open `build/html/index.html` in your web browser:

```bash
open build/html/index.html  # macOS
xdg-open build/html/index.html  # Linux
start build/html/index.html  # Windows
```

### Clean Build Files

```bash
cd docs/sphinx
make clean
```

## Documentation Structure

```
docs/sphinx/
├── source/              # Source files
│   ├── conf.py         # Sphinx configuration
│   ├── index.rst       # Main page
│   ├── installation.rst
│   ├── configuration.rst
│   ├── usage.rst
│   ├── troubleshooting.rst
│   ├── development.rst
│   ├── testing.rst
│   ├── api.rst
│   └── api/            # API reference
│       ├── modules.rst
│       ├── pykitmoney.rst
│       ├── starling.rst
│       └── resources.rst
├── build/              # Generated files (not in git)
└── Makefile            # Build commands
```

## Configuration

Documentation is configured in `source/conf.py`:

- **Theme**: sphinx_rtd_theme (Read the Docs)
- **Extensions**: autodoc, napoleon, viewcode, intersphinx
- **Docstring Style**: Google format
- **API Documentation**: Auto-generated from docstrings

## Writing Documentation

### ReStructuredText

Documentation files use reStructuredText (.rst) format.

Example:

```rst
Section Title
=============

Subsection
----------

**Bold text** and *italic text*.

Code block:

.. code-block:: python

   def example():
       return "Hello"

Link: :doc:`other_page`
```

### Docstrings

Use Google-style docstrings in Python code:

```python
def function(param1, param2):
    """
    Brief description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1.
        param2: Description of param2.
        
    Returns:
        Description of return value.
    """
    pass
```

## Continuous Documentation

Documentation is automatically:

- Extracted from Python docstrings
- Built from .rst files
- Linked to GitHub repository
- Versioned with code

## Publishing

Documentation can be hosted on:

- **Read the Docs**: https://readthedocs.org/
- **GitHub Pages**: As static HTML
- **Local**: For offline reference

To publish to Read the Docs:

1. Connect GitHub repository
2. Configure build (uses conf.py)
3. Documentation builds on every commit

## Troubleshooting

### Build Errors

**Missing modules**: Ensure package is installed

```bash
pip install -e ".[dev]"
```

**Import errors**: Check sys.path in conf.py

**Theme not found**: Install sphinx-rtd-theme

```bash
pip install sphinx-rtd-theme
```

### Warnings

Most warnings are about:
- Missing references (check filenames)
- Formatting issues (check .rst syntax)
- Docstring problems (check Google format)

To see full warnings:

```bash
sphinx-build -b html -W source build
```

## Resources

- Sphinx Documentation: https://www.sphinx-doc.org/
- reStructuredText Primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
- Read the Docs: https://docs.readthedocs.io/
- Napoleon (Google/NumPy docstrings): https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
