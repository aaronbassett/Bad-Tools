import random
import yaml


def get_excuse():
    stream = open("excuses.yaml", 'r')
    excuses = yaml.load(stream)
    return random.choice(excuses["excuses"])
