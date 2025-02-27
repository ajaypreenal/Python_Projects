from flask_sqlalchemy import SQLAlchemy

# Initialize the database, Will allow us to define Database models in Object Oriented way instead of using raw SQL
db = SQLAlchemy()

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.task}>"