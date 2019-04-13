import click
import os
from ..core import Command, pre, Chain


@click.command()
def push():
    '''
    Push the current branch to remote
    '''
    branch = pre('''git branch | grep \* | cut -d ' ' -f2''')
    cmd = Command(f'git push origin {branch}', msg=f'pushing to remote branch {branch}')
    result = cmd.exec(shell=False)
    print(cmd)


@click.command()
def merge():
    branch = pre('''git branch | grep \* | cut -d ' ' -f2''')
    
    commands = Chain(
        Command('git checkout master', shell=False),
        Command('git pull', shell=False),
        Command(f'git checkout {branch}'),
        Command('git merge master')
    )

    commands.exec()
