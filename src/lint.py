# This script serves will lint yaml files using the yamale tool.
# It will lint them, using a given yamale schema. 
# If the schema is not given, it will use the default one.
# The schema can be given as a path or as a string.
# The yaml to lint can be given as a path or as a string.
# There can be muliple yaml files to lint.
# If the linting fails, the script will exit with a non-zero code.
# If the linting succeeds, the script will exit with a zero code.

import yamale
import yaml

if __name__  == '__main__':
    # print out the environment variables
    print('\n'.join(['{}={}'.format(k, v) for k, v in sorted(os.environ.items())]))
    
