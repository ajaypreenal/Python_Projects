from flask import Flask
from config import Config
from model import db
from routes import TaskRoutes

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Set up routes
app.add_url_rule('/', 'home', TaskRoutes.home)
app.add_url_rule('/tasks', 'get_tasks', TaskRoutes.get_tasks, methods=['GET'])
app.add_url_rule('/add', 'add_task', TaskRoutes.add_task, methods=['POST'])
app.add_url_rule('/complete/<int:task_id>', 'complete_task', TaskRoutes.complete_task, methods=['POST'])
app.add_url_rule('/delete/<int:task_id>', 'delete_task', TaskRoutes.delete_task, methods=['DELETE'])

# Initialize the database (create tables)
with app.app_context():
    try:
        db.create_all()
        print("Database created successfully!")
    except Exception as e:
        print(f"Error creating database: {e}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
