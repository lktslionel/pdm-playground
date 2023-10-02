# PDM Playground


## Build

```
$ pdm build -d .workdir/dist

```

## Install the wheel

```
$ pip install .\.workdir\dist\pdmctl-1.0.2rc101-py3-none-any.whl
```

## Examples

### Using Hatchling build backend 

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"


[tool.hatch.build.targets.wheel]
only-include = [
  "src/cli",
  "pyproject.toml",
]
sources = ["src"]
```
