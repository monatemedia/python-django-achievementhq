import subprocess
import os
import time
import psycopg2
from psycopg2 import OperationalError

# Set up environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'achievementhq.settings')

def run_command(command):
    """Run a shell command and print its output."""
    print(f"Running: {command}")
    subprocess.run(command, check=True)

def delete_all_databases():
    """Delete all databases except the default ones."""
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_user = os.getenv("POSTGRES_USER", "root")  # Ensure we use root for administrative tasks
    db_password = os.getenv("POSTGRES_PASSWORD", "DrivewaySubduedOverlookRelapsing")

    # Connect to the PostgreSQL server as a superuser (root)
    try:
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default database
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        conn.autocommit = True  # Allow execution of commands like DROP DATABASE
        cursor = conn.cursor()

        # Get the list of all databases except system ones
        cursor.execute("SELECT datname FROM pg_database WHERE datname NOT IN ('postgres', 'template0', 'template1')")
        databases = cursor.fetchall()

        # Drop all user databases
        for db in databases:
            db_name = db[0]
            print(f"Dropping database: {db_name}")
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")

        # Create new database
        new_db_name = os.getenv("POSTGRES_DB", "laragigs-db")
        cursor.execute(f"CREATE DATABASE {new_db_name}")
        
        # Recreate user with the proper privileges
        new_db_user = os.getenv("POSTGRES_USER", "myprojectuser")
        new_db_password = os.getenv("POSTGRES_PASSWORD", "DrivewaySubduedOverlookRelapsing")
        cursor.execute(f"""
            CREATE USER {new_db_user} WITH PASSWORD '{new_db_password}';
            ALTER ROLE {new_db_user} SET client_encoding TO 'utf8';
            ALTER ROLE {new_db_user} SET default_transaction_isolation TO 'read committed';
            ALTER ROLE {new_db_user} SET timezone TO 'UTC';
            GRANT ALL PRIVILEGES ON DATABASE {new_db_name} TO {new_db_user};
        """)

        # Close the connection
        cursor.close()
        conn.close()
        print(f"Database {new_db_name} created and user {new_db_user} granted privileges.")
        
    except OperationalError as e:
        print(f"Error while deleting databases or creating new one: {e}")

def main():

    # Clear databases and recreate necessary ones
    delete_all_databases()

    # Proceed with the Django commands
    run_command('python manage.py create_superuser_if_not_exists')
    run_command('python manage.py create_users')
    run_command('python manage.py create_posts')
    run_command('python manage.py create_comments')
    run_command('python manage.py populate_questions')

if __name__ == '__main__':
    main()
