# Migration Guide: Updating from Old Structure

This guide helps existing PyKitMoney users migrate to the new package structure.

## What Changed?

The project has been reorganized into a proper Python package (`pykitmoney/`) with improved structure, testing, and documentation. Your configuration files and e-paper display will continue to work with minimal changes.

## Migration Steps

### Step 1: Update Your Repository

Pull the latest changes:

```bash
cd PyKitMoney
git pull origin main
```

### Step 2: Update Your Virtual Environment

If you have an existing virtual environment, reinstall the package:

```bash
# Activate your existing virtual environment
source .venv/bin/activate

# Reinstall with the new structure
pip install -e ".[pi]"
```

Or create a fresh virtual environment:

```bash
# Deactivate old environment if active
deactivate

# Remove old environment (optional but recommended)
rm -rf .venv

# Create new environment
python3 -m venv .venv
source .venv/bin/activate

# Install with new structure
pip install -e ".[pi]"
```

### Step 3: Update Your Systemd Service

If you're using the systemd service, update your service file:

**Old command:**
```bash
ExecStart=/home/user/PyKitMoney/.venv/bin/python3 /home/user/PyKitMoney/main.py
```

**New command:**
```bash
ExecStart=/home/user/PyKitMoney/.venv/bin/python3 -m pykitmoney.main
```

To apply changes:

```bash
# Edit the service file
sudo nano /etc/systemd/system/pykitmoney.service

# Reload systemd
sudo systemctl daemon-reload

# Restart the service
sudo systemctl restart pykitmoney

# Check status
sudo systemctl status pykitmoney
```

### Step 4: Verify Configuration Files

Your configuration files should remain in the same location:
- `resources/settings.json` - Contains child's name
- `resources/accesstoken.txt` - Contains Starling API token

These files are unchanged and will work with the new structure.

### Step 5: Test the New Setup

Test manually:

```bash
source .venv/bin/activate
pykitmoney
# or
python -m pykitmoney.main
```

You should see the same behavior as before - your child's balance and transactions on the e-paper display.

## What's New?

### Entry Point

You can now run PyKitMoney in three ways:

```bash
# 1. Using the installed command
pykitmoney

# 2. Using module execution
python -m pykitmoney.main

# 3. Direct execution (legacy, still works)
python pykitmoney/main.py
```

### Development Features

If you're developing or modifying the code:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black pykitmoney tests

# Check code quality
pylint pykitmoney
```

## Troubleshooting

### "Module not found" errors

If you see errors like `ModuleNotFoundError: No module named 'pykitmoney'`:

1. Make sure you've reinstalled: `pip install -e ".[pi]"`
2. Verify you're in the correct directory: `cd /path/to/PyKitMoney`
3. Check your virtual environment is activated: `which python` should show `.venv/bin/python`

### E-paper display not working

The display code is unchanged. If you see display issues:

1. Verify SPI is still enabled: `sudo raspi-config`
2. Check the display model in `pykitmoney/epaper_drawing.py` (line 18)
3. Ensure GPIO permissions are correct

### Systemd service not starting

Check the service logs:

```bash
sudo journalctl -u pykitmoney.service -n 50
```

Common issues:
- Path to virtual environment is incorrect
- Path to project directory is wrong
- Virtual environment needs reinstalling

## Rolling Back (If Needed)

If you need to revert to the old structure temporarily:

1. The old files still exist in the root directory
2. Update systemd to use old path: `ExecStart=.../.venv/bin/python3 .../main.py`
3. No reinstallation needed for old structure

However, we recommend using the new structure for better maintainability.

## Benefits of Migration

After migration, you'll have:

- ✅ Modern Python package structure
- ✅ Proper module imports
- ✅ Better error messages and logging
- ✅ Easier to update and maintain
- ✅ Access to development tools (tests, linting)
- ✅ Future-proof for Python updates

## Need Help?

If you encounter issues:

1. Check the [IMPROVEMENTS.md](IMPROVEMENTS.md) for detailed changes
2. Review [CONTRIBUTING.md](CONTRIBUTING.md) for development setup
3. Open an issue on GitHub with details about your problem

## Summary

The migration is straightforward:
1. Pull latest changes
2. Reinstall package: `pip install -e ".[pi]"`
3. Update systemd service command
4. Restart service
5. Verify it works

Your configuration and display setup remain unchanged!
