import click
from flask import current_app
from ..models.User import db


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    with current_app.app_context():
        db.create_all()
    click.echo("Initialized the database.")


def register_comands(app):
    app.cli.add_command(init_db_command)
