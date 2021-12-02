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
    return (stripped, parts)


def merge(stripped, parts):
    return stripped.format(*parts)



parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )







