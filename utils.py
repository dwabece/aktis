from os import path as ospath
import config as config


def load_input(fname, input_type):
    types = {
        'mouse': config.MOUSE_DIR,
        'median': config.MEDIAN_DIR,
    }

    fpath = ospath.join(types.get(input_type), fname)
    try:
        with open(fpath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass
