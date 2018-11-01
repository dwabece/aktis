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
    data_file_path = ospath.join(config.DATA_PATH, data_file)
    with open(data_file_path, 'r') as f:
        return NaiveBayesClassifier(f, format='json')


def _if_animal(sentence, classifier):
    blob = TextBlob(sentence, classifier=classifier)
    return True if blob.classify() == 'pos' else False


def _process_input(input_str):
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
