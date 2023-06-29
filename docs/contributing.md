
# Overview

Contributions are welcome and encouraged!

Development of `msteams_webhooks` uses:

* [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for all public modules, classes, and functions
* [black](https://github.com/psf/black) - Code auto-formatting (100-character line limit)
* [ruff](https://beta.ruff.rs/) - Linting and some auto-formatting, e.g., replaces `isort`
* [pyright](https://github.com/microsoft/pyright) - Static type checking
* [pytest](https://docs.pytest.org/) - Unit test suite
* [nox](https://nox.thea.codes/) - Testing and linting automation

# Development Environment

## Install Python Versions

All code must work (and pass unit tests) on Python 3.9 and above. This means you must have interpreters installed for all applicable versions of Python.

Installing Python versions varies by platform. This example will install Python 3.9, 3.10, and 3.11 on macOS using Homebrew (assumes `bash` shell):

```bash
brew install python@3.{9..11}
```

## Fork & Clone Repo
[Fork](https://github.com/decoupca/msteams_webhooks/fork) the main repo into your GitHub account. Then, clone your repo locally: 

```sh
git clone https://github.com/your-username/msteams_webhooks.git
cd msteams_webhooks
```

## Build Virtual Environment

Virtual environments (venvs) provide a way to isolate Python environments from other projects. Use of a venv during development is not strictly required, but strongly encouraged.

```sh
# Create venv
python3 -m venv venv
# Activate venv
source venv/bin/activate
```

## Install Development Tools

```sh
pip install --upgrade pip
pip install -r dev-requirements.txt
```

## Create an Issue

No pull requests will be accepted without an associated issue. This helps organize discussion around the issue and focus each PR on a specific change. [Open an issue on GitHub](https://github.com/decoupca/msteams_webhooks/issues/new) before submitting a pull request. If you want to address multiple issues, open a separate issue for each one.

## Create a Branch

All contributions should use a separate git branch. Never submit pull requests directly to the `master` or `develop` branches; they will be rejected.

Prefix your branch name with the issue number, followed by a brief description of the proposed change, e.g.:

```sh
git checkout -B 123-add-new-card-type
```

## Make Changes

Make all changes to the codebase relevant to the issue you opened above. Remember to keep the changes scoped to that specific issue.

## Run Tests & Linting

Tests are automated with `nox`. Assuming you have installed all prerequisites above, simply run `nox` in the project directory to execute all tests and linting. If it returns errors, address them before submitting a PR. If you forget this step before submitting your PR, you can still push a new commit to the same branch--no need to open a new PR.

## Commit Changes

Use the following commit message convention:

```sh
git commit -m "Closes #123: Added new card type"
```

This ensures the issue is automatically closed when your PR is merged.

## Submit Pull Request

Go to the main project's [pull request tab](https://github.com/decoupca/msteams_webhooks/pulls) (or the pull request tab on your fork) and follow the instructions to start a pull request.

A maintainer will review the request and provide feedback. Once approved, they will merge the request. After merging, you may safely delete your branch and fork, if you wish.

Thank you in advance for your contributions!
