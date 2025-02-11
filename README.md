# Z - Python CLI Project

This is a simple command-line interface (CLI) project built using [Typer](https://typer.tiangolo.com/).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/viet-dinh/z-cli
   cd z-cli
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
4. Run ollama docker and pull llm model
   ```sh
   docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   docker exec -it ollama ollama run llama3.2:1b
   ```

## Usage

Run the CLI application with:
```sh
python cli.py
```

### Available Commands

- `hello NAME` - Greets the user.
- `bye NAME` - Greets the user.
- `chat "question"` - Response chat

Example:
```sh
python cli.py hello Alice
python cli.py bye Alice
python cli.py chat "xin chào"
```

## License

This project is licensed under the MIT License.

