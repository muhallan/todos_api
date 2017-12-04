from app import db
from sqlalchemy.exc import SQLAlchemyError


class Todo(db.Model):
    """
    This class represents the task table
    """
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    done_status = db.Column(db.Boolean, default=False)

    def __init__(self, title, description):
        """initialize a task."""
        self.title = title
        self.description = description

    def save(self):
        """Save an instance of the model to the database."""
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    @staticmethod
    def get_all():
        """Get all the Tasks in the model"""
        return Todo.query.all()

    def delete(self):
        """
        Delete a task from the table
        :return:
        """
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    def __repr__(self):
        return "<Task: {}>".format(self.title)

