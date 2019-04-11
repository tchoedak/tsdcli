import click
import os
from ..core import Command, pre


@click.command()
def push():
    branch = pre('''git branch | grep \* | cut -d ' ' -f2''')
    cmd = Command(f'git push origin {branch}', msg=f'pushing to remote branch {branch}')
    result = cmd.exec(shell=False)
    print(cmd)
