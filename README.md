# telegram-keywords-parser

A Telegram application - python script - that parses messages from a list of public channels/chats and takes only those messages that contain your keywords.


## Requirements

- Python 3.12 or newer
- uv
- Telegram API credentials (`api_id` and `api_hash`)

## Installation

```bash
uv sync
```

Without uv, install the dependencies with pip:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your Telegram credentials:

```dotenv
TG_API_ID=1234567
TG_API_HASH=0123456789abcdef0123456789abcdef
TG_SESSION_NAME=my_session
```

`TG_SESSION_NAME` is optional and sets the name of the session file `.session` (default: `keywords_parser`).

Create two text files in the project root, one entry per line:

- `chats.txt` - public usernames of the channels and chats to scan.
- `keywords.txt` - keywords to look for.

How many days back to search is set by `DAYS_BACK` in `core/constants.py` (default: 2).

## Usage

```bash
uv run main.py
```

The first run asks for your phone number and a login code, then saves the session to a `*.session` file, so later runs start without a prompt.

## How matching works

A message matches when one of its words is equal to a keyword. The comparison ignores case and treats a hyphenated word such as `full-time` as a single word. Other word forms are not matched, so list each form you need on its own line. Multi-word phrases are not supported.

## Limitations

Only public channels and chats that have a username are supported. Private chats and channels are not.

## Project layout

```
main.py             entry point: builds the objects and starts the search
core/
  constants.py      run parameters
  settings.py       credentials loaded from .env
  models.py         data classes
  interfaces.py     abstract contracts
  services.py       search logic
  adapters.py       Telegram and terminal implementations
  exceptions.py     application exceptions
  utils.py          helpers
```
