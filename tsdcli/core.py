import os
import subprocess
from functools import wraps


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def parse_args(pos=0):
    '''
    Decorator for converting an args arg into a list of strings
    '''
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            args = list(args)
            if not isinstance(args[pos], list):
                args[pos] = args[pos].split(' ')
            return fn(*args, **kwargs)

        return wrapper
    return decorator


#@parse_args()
def pre(pre_command):
    '''
    Executes a command and captures the stdout

    NOTE:
        only single line returns are expected
    '''
    val = subprocess.check_output(pre_command, shell=True).decode('utf-8')
    return val.strip('\n')



class Command():

    @parse_args(pos=1)
    def __init__(self, args, msg=None, shell=False):
        self.args = args
        self.msg = msg
        self.shell = shell
        self.executed = False
        self.successful = False

    def exec(self, shell=False):
        execute_in_shell = shell if self.shell is None else self.shell
        self.successful = subprocess.call(self.args, shell=execute_in_shell) == 0
        self.executed = True
        print(self)

    @property
    def command(self):
        return ' '.join(self.args)

    def __repr__(self):
        return (
            f'{bcolors.HEADER} Command: {bcolors.OKBLUE}{self.command}. '
            f'{bcolors.ENDC} Executed? {bcolors.OKGREEN} {self.executed}'
            f'{bcolors.ENDC} Successful? {bcolors.OKGREEN} {self.successful}'
            f'{bcolors.ENDC}'
        )


class RemoteCommand(Command):

    
    def __init__(self, args, msg=None, shell=True):
        self.args = args.split(';')
        self.msg = msg
        self.shell = shell
        self.executed = False
        self.successful = False

    def exec(self, shell=True):
        execute_in_shell = shell if self.shell is None else self.shell
        process = subprocess.Popen(self.args[0], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                   universal_newlines=True, bufsize=0, shell=execute_in_shell)

        for args in self.args[1:]:
            process.stdin.write(f'{args} .\n')

        process.stdin.write('echo ENDED REMOTE\n')
        process.stdin.write('exit\n')
        
        stdout = process.communicate()[0].strip()
        process.stdin.close()
        self.executed = True
        self.successful = process.returncode == 0
        print(stdout)
        print(self)


class Chain():
    def __init__(self, *commands):
        self.commands = commands

    def exec(self, shell=True):
        for command in self.commands:
            command.exec(shell=shell)
            if not command.successful:
                raise Exception('Command is bad')
