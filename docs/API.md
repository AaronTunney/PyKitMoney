# API Documentation

## Starling Bank API

PyKitMoney uses the Starling Bank API to retrieve account and transaction data.

### Required OAuth Scopes

- `account:read` - Read account information
- `account-list:read` - List all accounts
- `savings-goal-transfer:read` - Read recurring transfer information
- `space:read` - Read space information
- `transaction:read` - Read transaction feed

### API Modules

#### `starling.accounts`

Functions for accessing account and space information.

**`get_accounts(access_token)`**
- Returns all accounts for the authenticated user
- Returns: Dictionary with 'accounts' list

**`get_spaces(access_token, account_uid)`**
- Returns all spaces (including Kite spaces) for an account
- Parameters:
  - `account_uid`: Account unique identifier
- Returns: Dictionary with 'spendingSpaces' and 'savingsGoals' lists

**`get_recurring_transfer(access_token, account_uid, space_uid)`**
- Returns recurring transfer information for a space
- Parameters:
  - `account_uid`: Account unique identifier
  - `space_uid`: Space unique identifier
- Returns: Dictionary with transfer details

#### `starling.feed`

Functions for accessing transaction feed.

**`get_transactions_for_category(access_token, account_uid, category_uid)`**
- Returns transactions for a specific space/category
- Automatically filters to last 3 months
- Parameters:
  - `account_uid`: Account unique identifier
  - `category_uid`: Space/category unique identifier
- Returns: Dictionary with 'feedItems' list

### Utility Functions

#### `utils.py`

**`find_spending_space(name, spaces)`**
- Finds a spending space by name
- Returns: Space dictionary or None

**`find_first_account_uid(accounts_data)`**
- Extracts the first account UID from accounts response
- Returns: Account UID string or None

**`currency_string(minor_units)`**
- Converts minor currency units (pence) to formatted string
- Parameters:
  - `minor_units`: Integer amount in pence
- Returns: Formatted currency string (e.g., "£12.34")

**`is_raspberry_pi()`**
- Detects if code is running on a Raspberry Pi
- Returns: Boolean

**`date_from_iso_8601_string(date_str)`**
- Parses ISO 8601 date string
- Returns: datetime object

### Drawing Functions

#### `draw_utils.py`

**`font_with_size(size)`**
- Returns ImageFont object with specified size
- Parameters:
  - `size`: Font size in points
- Returns: PIL ImageFont object

**`largest_font_for(text, font, max_width, max_height)`**
- Calculates largest font that fits text in rectangle
- Returns: PIL ImageFont object

**`size_of_text(text, font)`**
- Measures rendered text dimensions
- Returns: Tuple (width, height)

**`origin_to_center_text(text, font, width, height)`**
- Calculates coordinates to center text
- Returns: Tuple (x, y)

**`longest_text(texts, font)`**
- Finds longest text in list when rendered
- Returns: Text string

## Configuration

### `resources/settings.json`

```json
{
    "name": "ChildName"
}
```

- `name`: Name of the Kite space holder

### `resources/accesstoken.txt`

Contains the Starling Bank API access token (one line, no formatting).

## E-Paper Display

The project uses a Waveshare 2.13" E-Paper display (250x122 pixels).

### Display Layout

- **Top Left**: Child's name
- **Bottom Left**: Current balance (large font)
- **Top Right**: Next recurring transfer amount
- **Bottom Right**: Last 3 transactions

The display refreshes on the schedule defined in `pykitmoney.timer` (default: hourly).
