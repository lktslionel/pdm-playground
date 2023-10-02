import pathlib
import sys
from os.path import dirname

import tomli


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    project_config = {}

    root_dir_path = pathlib.Path(dirname(__file__))
    pyproject_file = pathlib.Path.resolve(
        root_dir_path.parent.parent / "pyproject.toml"
    )
    with pyproject_file.open() as f:
        print("")
        project_config = tomli.loads(f.read())

    try:
        project_version = project_config["project"]["version"]
        print(f"pdmctl Version: {project_version}")

    except Exception:  # KeyError
        pass


if __name__ == "__main__":
    sys.exit(main())
