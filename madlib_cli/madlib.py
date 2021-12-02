import re

TEMPLATE_PATH = "assets/make_me_a_video_game_template.txt"
MADLIB_OUTPUT_PATH = "assets/madlib_output.txt"

def read_template(path):
    """Accepts a string representing a file path as an input. Returns the contents of the file."""
    try:
        with open(path) as file:
            contents = file.read().strip()
        return contents
    except:
        raise FileNotFoundError

def write_template(path, text):
    """Writes the passed in text to the passed in file path (string)"""
    with open(path, 'w') as file:
        contents = file.write(text)

def parse_template(string):
    """
    Returns a tuple consisting of the parsed template (string) and parts (tuple of strings).

    "A {Adjective} and {Adjective} {Noun}" -> ("A {} and {} {}", ("Adjective", "Adjective", "Noun")
    """
    regex = r"{([^{}]*)}"
    parts = tuple(re.findall(regex, string))
    stripped = re.sub(regex, '{}', string)
    return (stripped, parts)

def merge(template, words):
    """
    ("A {} and {} {}", ("dark", "stormy", "night") -> "A dark and stormy night."
    """
    return template.format(*words)

# Print a welcome message to the user, explaining the Madlib process and command line interactions
print("Welcome User! Enter in some words and we'll create a fictional masterpiece out of it for you!")

# Read a template Madlib file (Example), and parse that file into usable parts.
template = read_template(TEMPLATE_PATH)
template_parsed, parts = parse_template(template)

# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
user_inputs = []
for part in parts:
    user_inputs.append(input(part + ': '))

# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
madlib = merge(template_parsed, user_inputs)

# After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
print(madlib)

# Write the completed text (Example)to a new file on your file system (in the repo).
write_template(MADLIB_OUTPUT_PATH, madlib)











