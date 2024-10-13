import json


def readFileAsJson(file_name: str):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def readFileByLines(file_name: str):
    with open(file_name) as f:
        data = f.readlines()
    return data
