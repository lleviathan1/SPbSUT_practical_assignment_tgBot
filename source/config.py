import json


def parse(file_name):
    with open(file_name, "r") as read_file:
        config = json.load(read_file)
    return config
