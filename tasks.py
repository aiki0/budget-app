from invoke import task

@task
def build(ctx):
    """Alustaa tietokannan."""
    ctx.run("python src/database/initialize_database.py", env={"PYTHONPATH": "src"}, pty=False)

@task
def start(ctx):
    """Käynnistää sovelluksen."""
    ctx.run("python src/index.py", env={"PYTHONPATH": "src"}, pty=False)

@task
def test(ctx):
    """Suorittaa testit."""
    ctx.run("pytest src", env={"PYTHONPATH": "src"}, pty=False)

@task
def lint(ctx):
    """Suorittaa koodin laadunvalvonnan (Pylint)."""
    ctx.run("pylint src", env={"PYTHONPATH": "src"}, pty=False)

@task
def coverage(ctx):
    """Kerää testikattavuuden (sisältää haarautumakattavuuden)."""
    ctx.run("coverage run --branch -m pytest src", env={"PYTHONPATH": "src"}, pty=False)

@task(coverage)
def coverage_report(ctx):
    """Generoi HTML-muotoisen testikattavuusraportin."""
    ctx.run("coverage html", pty=False)