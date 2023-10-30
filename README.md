# Yamale-Action
This Action provides you with a very light-weight and easy to understand yaml linter. It's meant to be validating 
your yaml files against a custom schema that is defined, using the popular
[Yamale](https://github.com/23andMe/Yamale) library. 

## Input
The Linter requires you to provide it with two parameters:
- `base_dir`: The base direction of your yaml files relative to your `$GITHUB_WORKSPACE`.
- `schema`: The directory containing the schema file relative to your `$GITHUB_WORKSPACE`.

On top of that, you can provide the following optional parameters:
- `filename`: specify your yaml file with a filename. By adding a wildcard `*` to the filename, you can specify multiple 
files that use the same naming. If you don't specify a filename, the action will look for all files called `*.yaml`.
- `include_subdir`: if you want to include all matching yaml files in the subdirectories of `base_dir`, you can set this to `true`.

## Usage
The action will look for all matching yaml files in the `base_dir` directory. If you want to include all files matching 
files in the subdirectories, you can set the `include_subdir` parameter to `true`.

Specify a custom schema against which the files are linted by using the 
[Yamale Schema Documentation](https://github.com/23andMe/Yamale#schema). Once created, 
I'd recommend you to store your schema in the `.lint` directory. I feel this is a 

### Example
```yaml
name: yamale-action
# You will probably want to run this on PRs only.
on:
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:
jobs:
  lint-yaml:
    runs-on: ubuntu-latest
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
        name: checkout
      # Runs the linter
      - uses: bieggerm/yamale-action@v1
        name: lint-yaml
        with:
          base_dir: "path/to/yaml/"
          schema: ".lint/schema.yaml" 
          include_subdir: true  
          filename: "*matching.yaml"
```
## Changes

It is now possible to validate using multiple schemas. Every file gets linted against every schema. If all schemas see a files syntax as invalid, the script fails. If one schema sees the syntax as valid, it passes. 
Multiple schemas can be used as by seperating them with a comma:
```yaml
- uses: bieggerm/yamale-action@v1
        name: lint-yaml
        with:
          base_dir: "path/to/yaml/"
          schema: ".lint/schema.yaml,.lint/schema2.yaml" 
          include_subdir: true  
          filename: "*matching.yaml"
```

## Upcoming Features
- [x] Add support for multiple schemas in an either or way.
- [ ] Create an Output for other actions to depend on.


## Contributing :nerd_face:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
