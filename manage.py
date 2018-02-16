import os
import unittest
from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

# Define the migration command to always be preceded by the word "db"
# Usage: python manage.py db init
manager.add_command('db', MigrateCommand)


# define our command for testing called "test"
# Usage: python manage.py test
@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

if __name__ == '__main__':
    manager.run()
