# Changelog

All notable changes to PyKitMoney will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-24

### Added
- Restructured project to follow Python best practices
- Created `pykitmoney` package with proper module structure
- Added `pyproject.toml` for modern Python packaging
- Comprehensive test suite with pytest
- Added type hints and improved docstrings (Google style)
- Created CONTRIBUTING.md with development guidelines
- Added API documentation in docs/API.md
- Development dependencies configuration (Black, Pylint, MyPy)
- GitHub Actions-ready testing configuration

### Changed
- Moved all source code into `pykitmoney/` package
- Improved code formatting and PEP 8 compliance
- Enhanced error handling throughout codebase
- Updated imports to use absolute package imports
- Improved logging with structured format
- Updated docstrings to Google style format
- Better separation of concerns in modules

### Fixed
- Fixed exception handling in `epaper_drawing.py`
- Removed debug print statement from `settings.py`
- Corrected logging format string in `base_api.py`
- Fixed code style issues (line lengths, whitespace)

## [0.1.0] - Initial Release

### Added
- Basic functionality for Starling Kite display
- E-paper display support for Waveshare 2.13"
- Starling Bank API integration
- Systemd service configuration
- Basic README with setup instructions
