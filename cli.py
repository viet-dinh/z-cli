import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")

@app.command()
def bye(name: str):
    """Say bye to someone."""
    typer.echo(f"Bye, {name}!")

if __name__ == "__main__":
    app()
