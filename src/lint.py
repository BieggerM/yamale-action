import sys
import os
import yaml
import yamale
import glob


def load_yaml(location):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, location)
    with open(abs_file_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def lint_file(schema, filename):
    try:
        data = yamale.make_data(filename)
        yamale.validate(schema, data)
        return True
    except ValueError as e:
        print(e)
        return False

if __name__ == '__main__':
    schema_paths = os.environ['INPUT_SCHEMA'].split(',')
    base_dir = os.path.join(os.environ['GITHUB_WORKSPACE'], os.environ['INPUT_BASE_DIR'])
    filename = os.environ['INPUT_FILENAME'] if os.environ['INPUT_FILENAME'] else '*.yaml'
    include_subdir = os.environ['INPUT_INCLUDE_SUBDIR'] if os.environ['INPUT_INCLUDE_SUBDIR'] else 'false'

    if include_subdir == 'true':
        filename = '**/' + filename

    files = glob.glob(os.path.join(base_dir, filename), recursive=True)

    results = []
    for schema_path in schema_paths:
        schema = yamale.make_schema(os.path.join(os.environ['GITHUB_WORKSPACE'], schema_path.strip()))
        results.extend([lint_file(schema, file) for file in files])

    if any(result is False for result in results):
        sys.exit(1)