from pathlib import Path

import rich_click as click
from rich.console import Console

con = Console()

click.rich_click.STYLE_COMMANDS_TABLE_EXPAND = False
click.rich_click.STYLE_OPTIONS_TABLE_EXPAND = False
click.rich_click.MAX_WIDTH = 100


@click.group(chain=True, help="Acquire, preprocess, and calibrate data.")
@click.rich_config({"theme": "dracula-box"})
@click.option("--id", "id", required=True, help="Dataset identifier.")
@click.option("--path", type=click.Path(path_type=Path), required=True, help="Working directory.")
@click.pass_context
def cli(ctx, id, path):
    ctx.obj = {"id": id, "path": path}


@cli.command(help="Acquire the dataset.")
@click.pass_obj
def acquisition(config):
    con.print("[bold red]Acquisition step with config:[/]", config)


@cli.command(help="Preprocess the dataset.")
@click.pass_obj
def preprocessing(config):
    con.print("Preprocessing step with config:", config)


@cli.command(help="Calibrate the dataset.")
@click.pass_obj
def calibration(config):
    con.print("Calibration step with config:", config)


@cli.command(help="Run the full pipeline.")
@click.pass_obj
def full(config):
    con.print("Running full pipeline with config:", config)


if __name__ == "__main__":
    cli()
