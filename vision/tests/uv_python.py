import sys


def python_command(*args):
    """why: tests re-run the current interpreter, and Python starts only through uv."""
    return ['uv', 'run', '--no-project', '--python', sys.executable, 'python', *map(str, args)]
