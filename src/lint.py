# This script serves will lint yaml files using the yamale tool.
# It will lint them, using a given yamale schema. 
# If the schema is not given, it will use the default one.
# The schema can be given as a path or as a string.
# The yaml to lint can be given as a path or as a string.
# There can be muliple yaml files to lint.
# If the linting fails, the script will exit with a non-zero code.
# If the linting succeeds, the script will exit with a zero code.

import os
import yamale
import yaml
from yamlinclude import YamlIncludeConstructor

# create Loader Class for loading data
class Loader(yaml.SafeLoader):
    """YAML Loader with `!include` constructor."""

    def __init__(self, stream: IO) -> None:
        """Initialise Loader."""
        try:
            self._root = os.path.split(stream.name)[0]
        except AttributeError:
            self._root = os.path.curdir
        super().__init__(stream)


def load_yaml(location):
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir='yaml_files')
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, location)
    with open(abs_file_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__  == '__main__':
    # get the schema path from the environment variable
    schema_path = os.environ['INPUT_SCHEMA']
    # get the directory of the yaml files from the environment variable
    yaml_dir = os.environ['INPUT_DIR']

    # print both variables
    print("Schema path: " + schema_path)
    print("Yaml directory: " + yaml_dir)
    
    schema_object = load_yaml(schema_path)
    # print the schema object
    print("printing values of schema object:")
    print(schema_object)

    
    