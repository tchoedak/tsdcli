import click

from ..core import pre, Command, Chain


@click.command()
@click.argument('path')
@click.argument('ip')
@click.option('-d', '--destination', default=None)
def push_file(path, ip, destination):
    '''
    Push a file, either accepting a path or dir from `from_`
    to a path `to`
    '''
    if destination is None:
        destination = '/home/hadoop/'
    cmd = Command(f'scp -i ~/.ssh/id_rsa.pub {path} hadoop@{ip}:{destination}')
    cmd.exec()


@click.command()
@click.argument('path')
@click.argument('ip')
@click.pass_context
def install_remotely(ctx, path, ip):
    '''
    Install a package from path to a remote IP
    '''
    ctx.invoke(push_file, path=path, ip=ip)

    cmd = Command(f'ssh -i ~/.ssh/id_rsa.pub')
    cmd.exec()

    install_path = util.find_destination('/home/hadoop', path)

    cmds = Chain(
        Command('sudo su root'),
        Command(f'pip install {install_path}'),
        Command('exit')
    )


@click.command()
def uninstall_remotely():
    pass    
