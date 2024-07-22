import click
import os
import subprocess
from .tools import get_templates

@click.command(help="Generates pydantic models from json-schema")
@click.option("--json-schema", required=True, type=str, help="Absolute path for json-schema")
@click.option("--out-dir", required=True, type=str, help="Destination absolute path")
def gen_models(json_schema, out_dir):
    out_file = os.path.join(out_dir, 'schemas.py')
    subprocess.getstatusoutput(f"datamodel-codegen --input {json_schema} --output {out_file} --output-model-type pydantic_v2.BaseModel")


@click.command(help="Generates REST controllers for json-schema")
@click.option("--models", required=True, type=str, help="Absolute path for generated schemas")
@click.option("--rest-routes", required=True, type=str, help="Destination absolute path for code of REST controllers")
def gen_rest(models, rest_routes):
    templates = get_templates()

    for filename, template in templates.items():
        with open(os.path.join(rest_routes, filename), 'w') as f:
            if filename == "main.py" or filename == "crud.py":
                f.write(template.render(path=models))
            else:
                f.write(template.render())
