import subprocess
import os

# Set up environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'achievementhq.settings')

def run_command(command):
    """Run a shell command and print its output."""
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

def list_users():
    """List all users and indicate which one is the superuser."""
    from django.contrib.auth.models import User

    users = User.objects.all()
    if not users:
        print("No users found.")
        return

    print("\nUsers:")
    for user in users:
        user_type = "Superuser" if user.is_superuser else "Regular user"
        print(f"Username: {user.username}, Email: {user.email}, Type: {user_type}")

def main():
    # Create virtual environment and install dependencies from Pipfile
    run_command('pipenv install')  # This will create the venv and install all dependencies specified in the Pipfile

    # Run initial migrations
    run_command('pipenv run python manage.py migrate')

    # Create superuser if it does not exist
    run_command('pipenv run python manage.py create_superuser_if_not_exists')

    # Inject Fake Data (Optional)
    # Uncomment if you have additional scripts or setup commands
    # run_command('pipenv run python manage.py shell')

    # Delete all users except for the admin user
    run_command('pipenv run python manage.py delete_non_admin_users')

    # Create Fake Users
    run_command('pipenv run python manage.py create_users')

    # Create Fake Posts
    run_command('pipenv run python manage.py create_posts')

    # Create Fake Comments
    run_command('pipenv run python manage.py create_comments')

    # Create Fake Polls
    run_command('pipenv run python manage.py populate_questions')

    # Run server
    run_command('pipenv run python manage.py runserver')

    # List all users with their details
    list_users()

if __name__ == '__main__':
    main()
