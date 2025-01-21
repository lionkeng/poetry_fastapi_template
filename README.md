# poetry_fastapi_template

a fastAPI template for implementing a web service

## tooling

- python
- virtual environment
- poetry
- fastapi

## cloning this repo and using poetry to install dependencies

This project was created with poetry for dependency management and isolation of a virtual environment to run the version of the Python interpreter for this project.

0. Install poetry

1. After cloning this repo, go to the root directory and run the following to install the dependencies:

```bash
poetry install
```

Poetry will:

- Create a virtual environment (if one doesn't already exist).
- Install the project dependencies defined in pyproject.toml.

2. Activate the virtual environment

If you are developing with vscode, the workspace file `settings.json` should be sufficient to instruct VS Code to use python from the virtual environment. You can confirm this by opening up a terminal in VS Code and check `which python`. It should be using python from the `.venv` folder in the root directory of the project.

If you are not using VS Code, try the following additional instructions.

To activate the virtual environment Poetry created, use:

```bash
poetry shell
```

3. Optional step

You can check the virtual environment with:

```bash
poetry env info
```

4.  To exit the virtual environment

Type the following from the terminal where you have activated the virtual environment.

```bash
deactivate
```

## adding a package, use poetry

```bash
poetry add <name_of_package>
```

e.g.

```bash
poetry add "fastapi[standard]"
```

## run poetry_fastapi_template with poetry

From the root directory of the project:

```bash
poetry run uvicorn poetry_fastapi_template.main:app --reload
```

## add a package as a development dependency

```bash
poetry add --group dev <package_name>
```

e.g.

```bash
poetry add --group dev pytest-asyncio
```

## testing

We are using pytest

1.  Write your test file as `test_<name_of_your_file>.py` and put them in the `/tests` directory.

```bash
poetry run pytest -s
```

2. Run a specific test in a specific test file

```bash
poetry run pytest -s tests/test_basic.py::test_example
```
