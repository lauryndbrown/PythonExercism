#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    """
    Given: an input string name
    Returns: "Hello, <name>!" or "Hello, World!" if no name is given
    """
    if name:
        return "Hello, {}!".format(name)
    else:
        return "Hello, World!"
