from json import dumps


def json(data):
    return dumps(data, indent=2)
