# Z - Python CLI Project

This is a simple command-line interface (CLI) project built using [Typer](https://typer.tiangolo.com/).

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd python_cli_project
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the CLI application with:
```sh
python cli.py
```

### Available Commands

- `hello NAME` - Greets the user.
- `bye NAME` - Greets the user.

Example:
```sh
python cli.py hello Alice
python cli.py bye Alice
```

## License

This project is licensed under the MIT License.

