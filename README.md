# Smart Virtual Assistant — Team 05

A collaborative project for CSC10014 — Smart Virtual Assistant.

This repository contains the shared development environment for Team 05,
including the Python backend, sample data, user interface planning,
automated tests, and project documentation.

Note: This repository is being initialized through individual
team member pull requests. The Run and Test instructions
will be fully functional once the backend, data, and tests
have been merged into the main branch.

## Prerequisites

Before setting up the project, make sure you have:

- Python 3.10 or newer
- Git
- Visual Studio Code (recommended)
- A GitHub account

## Setup

Follow these instructions to set up the project on your computer.

### macOS / Linux

**Step 1: Clone the repository**

Open Terminal and run:

```bash
mkdir -p ~/projects/csc10014
cd ~/projects/csc10014
git clone https://github.com/vinhdu1233-tech/assistant-team05.git
cd assistant-team05
```

**Step 2: Create a virtual environment**

Check your Python version:

```bash
python3 --version
```

Make sure Python 3.10 or newer is installed.

Create a virtual environment:

```bash
python3 -m venv .venv
```

If `python3` points to an older Python version, use a newer installed version instead. For example, on macOS with Python 3.13:

```bash
python3.13 -m venv .venv
```

**Step 3: Activate the virtual environment**

```bash
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your Terminal prompt.

Verify the Python version:

```bash
python --version
```

**Step 4: Install dependencies**

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

### Windows (PowerShell)

Clone the repository:

```powershell
git clone https://github.com/vinhdu1233-tech/assistant-team05.git
cd assistant-team05
```

Check that your Python version is 3.10 or newer:

```powershell
py -3 --version
```

Create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Run

Make sure the virtual environment is activated.

Run the assistant using:

```bash
python -m assistant "where is the IT helpdesk?"
```

Expected output:

```text
IT Helpdesk: room E.005, open Mon-Fri 08:00-17:00.
```

You can also start the assistant in interactive mode:

```bash
python -m assistant
```

Type a question to interact with the assistant.

Type `quit` to exit.

## Test

Run the automated tests using:

```bash
pytest -q
```

Expected result: All automated tests pass successfully.

All tests should pass without errors.

To check the development environment, run:

```bash
python scripts/check_env.py
```

All environment checks should display `[ OK ]`.

## Project structure

- `src/assistant/` — Main Python source code for the assistant.
- `tests/` — Automated tests for the application.
- `data/` — Sample data containing office information.
- `docs/` — Project documentation.
- `ui/` — User interface resources.
- `scripts/` — Helper scripts for checking the environment.
- `README.md` — Instructions for setting up and running the project.
- `requirements.txt` — Required Python dependencies.
- `pyproject.toml` — Python project configuration.
- `.gitignore` — Files and folders excluded from Git tracking.

## Troubleshooting

### 1. Python version is too old

Problem:

The project requires Python 3.10 or newer, but the virtual environment may use an older version.

Solution:

Check the Python version:

```bash
python --version
```

On macOS, if Python 3.13 is installed, recreate the virtual environment using:

```bash
deactivate
python3.13 -m venv --clear .venv
source .venv/bin/activate
```

Check the version again and reinstall the dependencies.

### 2. pip version is outdated

Problem:

An older version of pip may not support installing the project in editable mode using `pyproject.toml`.

Solution:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

### 3. No module named assistant

Problem:

The project package has not been installed correctly.

Solution:

Activate the virtual environment and run:

```bash
python -m pip install -e .
```

### 4. Virtual environment is not activated

Problem:

Python may use packages installed outside the project environment.

Solution:

On macOS / Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. VS Code uses the wrong Python interpreter

Solution:

Open the Command Palette in VS Code and select:

Python: Select Interpreter

Choose the Python interpreter located inside the `.venv` folder.

### Dataset validation tests

Run the office dataset validation tests with:

```bash
python -m pytest -q tests/test_offices_validation.py