#!/usr/bin/env python
from argparse import ArgumentParser
from os import path as ospath
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import config
import utils


parser = ArgumentParser()
parser.add_argument(
    '-i', '--inputfile', dest='filename',
    required=True,
    help='Fixture to be loaded and processed.')


def _get_classifier(data_file):
    """
    Returns classifier filled with data
    :param data_file: name of a file containing textblob data
    :return: classifier object
    """
    data_file_path = ospath.join(config.DATA_PATH, data_file)
    with open(data_file_path, 'r') as f:
        return NaiveBayesClassifier(f, format='json')


def _if_animal(sentence, classifier):
    """
    Determines if sentence is mentioning computer mouse or an animal.
    Returns True if textblob classifies it as an animal.

    :param sentence: sentence do be analyzed
    :param classifier: classifier object
    :return bool: bool indicating if we're having a pest over here
    """
    blob = TextBlob(sentence, classifier=classifier)
    return True if blob.classify() == 'pos' else False


def _process_input(input_str):
    """
    Splits file contents to sentences

    :param input_str: file contents
    :return: list of sentences
    :rtype: list
    """
    return input_str.splitlines()[1:]


def run(fname):
    sentences = utils.load_input(fname, 'mouse')
    sentences_list = _process_input(sentences)
    if not sentences:
        print('couldnt load input file')

    try:
        mouse_classifier = _get_classifier('trained_mouses.json')
    except Exception:
        raise SystemExit('Can\'t classify your mouse, lad :(')

    for sen in sentences_list:
        is_animal = _if_animal(sen, mouse_classifier)
        print('animal' if is_animal else 'computer-mouse')


if __name__ == '__main__':
    args = parser.parse_args()
    run(args.filename)
