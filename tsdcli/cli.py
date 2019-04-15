import click

from .commands import emr, git

@click.group()
def cli():
    pass


cli.add_command(git.push)
cli.add_command(git.merge)
cli.add_command(emr.push_file)
cli.add_command(emr.install_remotely)
