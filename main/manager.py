# This is a useless file :)

from main import app, db
# from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

# cli = FlaskGroup(app)

# @cli.command(‘test’)
# @click.argument(‘test_case’, default=’test*.py’)
# def test(test_case=’test*.py’):


if __name__ == "__main__":
    manager.run()


time = 0.50
