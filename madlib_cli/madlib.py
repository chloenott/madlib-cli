



def read_template(path):
    with open(path) as file:
        contents = file.read().strip()
    print(contents)
    return contents

def parse_template(string):
    return ("It was a {} and {} {}.", ("Adjective", "Adjective", "Noun"))

def merge():
    pass











