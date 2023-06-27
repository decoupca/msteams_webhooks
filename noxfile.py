import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def unit_tests(session) -> None:
    session.install(".", "pytest")
    session.run("pytest")
