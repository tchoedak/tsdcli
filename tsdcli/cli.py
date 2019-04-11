import click

from .commands import git


@click.group()
def cli():
    pass


cli.add_command(git.push)
