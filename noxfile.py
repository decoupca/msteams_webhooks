import nox

nox.options.error_on_missing_interpreters = False
nox.options.stop_on_first_error = False
nox.options.default_venv_backend = "venv"


@nox.session(python=["3.9", "3.10", "3.11"])
def unit_tests(session) -> None:
    session.install(".", "pytest")
    session.run("pytest")


@nox.session(python="3.11")
def linting(session) -> None:
    session.install(".", "ruff", "black")
    session.run("ruff", "check", "msteams_webhooks/")
    session.run("black", "--check", "msteams_webhooks/")
