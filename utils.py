from os import path as ospath
import config as config


def load_input(fname, input_type):
    """
    Loads file with data to process

    Depending on input_type provided will load from different directories.
    * `mouse` for task with mouse classifying
    * `median` for task that counts list median

    :param input_file: name of file located inside data directory
    :return: file contents
    """
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
