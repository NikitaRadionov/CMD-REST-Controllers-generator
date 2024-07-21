import os
from jinja2 import Environment, FileSystemLoader
import subprocess
from pathlib import Path
import click


def generate_models(input_path, output_path):
    s = subprocess.getstatusoutput(f"datamodel-codegen --input {input_path} --output {output_path} --output-model-type pydantic_v2.BaseModel")


def get_templates() -> dict:

    env = Environment(
        loader=FileSystemLoader('templates')
    )

    tm_filenames = [
        "__init__.py",
        "crud.py",
        "database.py",
        "main.py",
        "models.py"
    ]

    templates = {filename: env.get_template(filename) for filename in tm_filenames}

    return templates

def generate_rest_app(schemas_path, dest_path):

    templates = get_templates()

    for filename, template in templates.items():
        with open(os.path.join(dest_path, filename), 'w') as f:
            if filename == "main.py" or filename == "crud.py":
                f.write(template.render(path=schemas_path))
            else:
                f.write(template.render())


@click.command()
def main():
    pass



    


if __name__ == "__main__":
    main()

