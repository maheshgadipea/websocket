# gunicorn_cli.py
import subprocess
from flask.cli import FlaskGroup
from application.app import app

def run_gunicorn():
    # Command to run Gunicorn with the given configuration
    command = [
        "gunicorn",
        "--config", "/application/application/gunicorn.py",  # Path to your Gunicorn config file
        "--reload",  # Enable auto-reloading of the app
         "app:app"  # Flask application object (app.py contains 'app')
    ]
    subprocess.run(command, check=True)  # Run the Gunicorn command

# Create a FlaskGroup instance with your Flask app
cli = FlaskGroup(app)

# Register the 'gunicorn' command with Flask CLI
@cli.command("gunicorn")
def gunicorn_command():
    """Run Gunicorn server with the specified config."""
    run_gunicorn()

if __name__ == "__main__":
    cli()
