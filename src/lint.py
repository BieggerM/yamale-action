# This script serves will lint yaml files using the yamale tool.
# It will lint them, using a given yamale schema. 
# If the schema is not given, it will use the default one.
# The schema can be given as a path or as a string.
# The yaml to lint can be given as a path or as a string.
# There can be muliple yaml files to lint.
# If the linting fails, the script will exit with a non-zero code.
# If the linting succeeds, the script will exit with a zero code.

import os
from pathlib import Path
import logging
import yaml
import glob
import yamale


def load_yaml(location):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, location)
    with open(abs_file_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    # get the schema path from the environment variable
    schema_path = os.path.join(os.environ['GITHUB_WORKSPACE'], os.environ['INPUT_SCHEMA'])

    # get the directory of the yaml files from the environment variable
    base_dir = os.path.join(os.environ['GITHUB_WORKSPACE'], os.environ['INPUT_BASE_DIR'])

    # check if environment variable is set
    # if not set, use the default filename '*.yaml'
    # that means every yaml file in the current directory will be linted
    if 'INPUT_FILENAME' is not None:
        filename = os.environ['INPUT_FILENAME']
    else:
        filename = '*.yaml'

    # same for include subdir variable
    if 'INPUT_INCLUDE_SUBDIR' is not None:
        include_subdir = os.environ['INPUT_INCLUDE_SUBDIR']
    else:
        include_subdir = 'false'

    if include_subdir == 'true':
        # add hint to include subdir to filename
        filename = '**/' + filename

    # print all defined variables
    print('schema_path: ' + schema_path)
    print('base_dir: ' + base_dir)
    print('filename: ' + filename)
    print('include_subdir: ' + include_subdir)

    # if subdirs are not included, the base_dir is the directory of the yaml files
    # we look for the yaml files in the base_dir that end with the filename
    lint_valid = True
    for path in Path(base_dir).glob(filename):
        # now we can lint the yaml file
        # if the linting fails, the script will exit with a non-zero code
        try:
            yamale.validate(yamale.make_schema(schema_path), yamale.make_data(path))
        except yamale.YamaleError as e:
            logging.error(e)
            lint_valid = False
    if lint_valid:
        exit(0)
    else:
        exit(1)
