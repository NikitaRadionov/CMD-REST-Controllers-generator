import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def get_templates() -> dict:

    env = Environment(
        loader=FileSystemLoader(os.path.join(Path(__file__).resolve().parent, 'templates'))
    )

    tm_filenames = [
        "__init__.txt",
        "crud.txt",
        "database.txt",
        "main.txt",
        "models.txt"
    ]

    templates = {filename.replace(".txt", ".py"): env.get_template(filename) for filename in tm_filenames}

    return templates