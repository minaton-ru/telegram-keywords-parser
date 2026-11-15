# Telegram chats keywords parser

Telegram application - python script - that parses messages from a list of public channels/chats and takes only those messages that contain your keywords.

## Technology Stack
- telethon
- pydantic

## Project Setup and Management
- Dependency management: `uv` and `pyproject.toml`
- Run the script with `uv run main.py`.
- Create branch from `master` according to the project's branch naming convention with the command `git checkout master && git pull && git checkout -b <type>-<short-description>`.
- Don't stage, commit or push without being asked.

## Testing
- Tests - only `pytest`, functions. No `unittest.TestCase`.
- Mocks - only Fake classes. No `MagicMock`, `patch`, `unittest.mock`.
- Unit tests must be fast and isolated.
- Do not use shared state between tests.
- If a method should return no entity - check for `is None`.
- For errors use `pytest.raises(..., match=...)`.
- Test names should follow the `test_...` style.
- Don’t chase 100% coverage by adding unnecessary or low-value tests. Focus on tests that protect important behavior.

### Unit tests
- Happy path.
- Edge cases: empty string, `None`, whitespace.
- Error cases: invalid input, missing entity, network errors.
- Each test creates its own service instance via the factory.

### Integration tests
- The test environment state must be reset before tests.
- For this, it is convenient to use `pytest.fixture(autouse=True)`.

## Code Style
- Write clear, short code without unnecessary complexity.
- If logic repeats - extract it into helper functions.
- Follow PEP 8 for formatting (99 characters per line, snake_case for functions/variables, PascalCase for classes, UPPER_SNAKE for constants).
- Use descriptive, unambiguous names for variables. Use descriptive names that start with a verb for functions. Functions and methods must consist of at least two words.
- Type annotations - required everywhere, including `-> None`.
- Do not add unused imports.
- All exception raises must be logged.
- Apply KISS, DRY and SOLID principles to the code.

## Definition of done (quality gates)
Declare a task done only after docstrings are updated, README.md is updated, and all of these pass green:
  - `uv run ruff format .`
  - `uv run ruff check --fix .`

## Constraints
- Never edit: lock files, `.env`.
- Never commit `.env` files.
- Ask before adding dependencies.
- Before starting coding work, create a new git branch from up to date `master` according to the project's branch naming convention.
- If a mismatch causes you to think for too long, ask the user this question and suggest possible next steps.
- Do not look at the `__pycache__` folder unless the user has explicitly asked you to do so.
- Do not look at git branches other than `master` unless the user has explicitly asked you to do so.

## Git branch naming convention
Branches should be named according to the type of task.

Git branch name format: `<type>-<short-description>`, where:
- `type` - task type: `feat`, `fix`, `test`, `refactor`, `docs`, `ci`, `chore`, `style`, according to the Conventional Commits
- `short-description` - a short description in the style of `kebab-case`

## Commit tag rules
Each commit must be marked with a tag in square brackets at the beginning of the message:
- `[agent]` - the diff from the agent was accepted without significant edits
- `[assisted]` - the agent did the bulk of the work, but the developer rewrote or suggested a significant portion (logic, structure, >20% of lines)
- `[manual]` - the code was written manually without the agent's assistance

Each commit must include the Conventional Commits type after the tag so following such format `[tag] type: description`.
