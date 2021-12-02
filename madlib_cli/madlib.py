import re


def read_template(path):
    with open(path) as file:
        contents = file.read().strip()
    print(contents)
    return contents


def parse_template(string):
    regex = r"{(\w*)}"
    parts = tuple(re.findall(regex, string))
    stripped = re.sub(regex, '{}', string)
    return ("It was a {} and {} {}.", parts)


def merge():
    pass



parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )







