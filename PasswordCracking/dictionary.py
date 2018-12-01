import itertools


def generate_dict(alph=[], length=0, name=None):
    """
    [name] if name is present a file will be created
    """
    opts = itertools.product(alph, repeat=6)
    dict = []

    for opt in opts:
        dict.append(''.join(opt))

    print("Generating {} options".format(len(dict)))

    if name is not None:
        with open(name, mode="w") as pwd_file:
            pwd_file.write('\n'.join(dict))
    return dict
