import subprocess
import os
import django

# Set up environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'achievementhq.settings')

# Initialize Django
django.setup()

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
    # Install dependencies (assuming pip and requirements.txt are used)
    run_command('pip install -r requirements.txt')

    # Run initial migrations
    run_command('python manage.py migrate')

    # Create superuser if it does not exist
    run_command('python manage.py create_superuser_if_not_exists')

    # Inject Fake Data (Optional)
    # Uncomment if you have additional scripts or setup commands
    # run_command('python manage.py shell')

    # Delete all users except for the admin user
    run_command('python manage.py delete_non_admin_users')

    # Create Fake Users
    run_command('python manage.py create_users')

    # Create Fake Posts
    run_command('python manage.py create_posts')

    # Create Fake Comments
    run_command('python manage.py create_comments')

    # Clear Polls Table
    run_command('python manage.py clear_polls_table')

    # Create Fake Polls
    run_command('python manage.py populate_questions')

    # List all users with their details
    list_users()

if __name__ == '__main__':
    main()
