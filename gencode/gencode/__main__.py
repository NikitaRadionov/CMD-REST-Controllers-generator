import click

from . import commands

@click.group()
def cli():
    pass

cli.add_command(commands.gen_models)
cli.add_command(commands.gen_rest)