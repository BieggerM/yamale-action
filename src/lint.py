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

if __name__  == '__main__':
    # get the schema path from the environment variable
    schema_path = os.environ['INPUT_SCHEMA']
    # get the directory of the yaml files from the environment variable
    yaml_dir = os.environ['INPUT_DIR']

    # print both variables
    print("Schema path: " + schema_path)
    print("Yaml directory: " + yaml_dir)
    
    
