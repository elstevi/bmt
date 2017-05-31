import subprocess

def shell(command, simple_return=False):
    """ Execute a command on the host system """
    try:
        process = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        raise
    return process

def screen_exec(vm_name, command):
    return shell('~/src/bmt/bmt exec %s "%s"' % (vm_name, command))
