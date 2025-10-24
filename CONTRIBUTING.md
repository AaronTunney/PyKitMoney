# Contributing to PyKitMoney

Thank you for your interest in contributing to PyKitMoney!

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/AaronTunney/PyKitMoney.git
cd PyKitMoney
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Running Tests

Run the test suite with:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=pykitmoney --cov-report=html
```

## Code Style

This project uses:
- **Black** for code formatting
- **Pylint** for linting
- **MyPy** for type checking (optional)

Format your code before committing:
```bash
black pykitmoney tests
```

Check code quality:
```bash
pylint pykitmoney
```

## Project Structure

```
PyKitMoney/
├── pykitmoney/           # Main package
│   ├── starling/        # Starling Bank API modules
│   ├── resources/       # Configuration and secrets
│   ├── pic/             # Font resources
│   ├── main.py          # Entry point
│   ├── utils.py         # Utility functions
│   ├── draw_utils.py    # Drawing utilities
│   └── epaper_drawing.py # E-paper display logic
├── tests/               # Test suite
├── service/             # Systemd service files
└── docs/                # Documentation

```

## Pull Request Process

1. Create a new branch for your feature or bugfix
2. Write tests for your changes
3. Ensure all tests pass
4. Format your code with Black
5. Update documentation if needed
6. Submit a pull request

## Code of Conduct

Be respectful and constructive in all interactions.
