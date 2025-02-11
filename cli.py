import typer
import asyncio
from chat.generate import stream, chat as generate

app = typer.Typer()

@app.command()
def hello(name: str):
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")

@app.command()
def bye(name: str):
    """Say bye to someone."""
    typer.echo(f"Bye, {name}!")
    
@app.command()
def chat(message: str):
    asyncio.run(stream(message))

if __name__ == "__main__":
    app()
