import shutil
import logging
import os

active_db_file = 'ai_dev/app.db'
backup_db_file = 'ai_dev/backup.db'

# Configure logging
logging.basicConfig(level=logging.INFO)


def backup_db(active_db_file: str, backup_db_file: str) -> None:
    try:
        if not os.path.isfile(active_db_file):
            logging.error(f"Active database file does not exist: {
                          active_db_file}")
            return

        shutil.copy(active_db_file, backup_db_file)
        logging.info(f"Backed up {active_db_file} to {backup_db_file}")
    except shutil.SameFileError:
        logging.error("Source and destination represents the same file.")
    except IsADirectoryError:
        logging.error("Destination is a directory.")
    except PermissionError:
        logging.error("Permission denied.")
    except Exception as e:
        logging.error(f"Failed to backup database: {e}")


def restore_db(backup_db_file: str, active_db_file: str) -> None:
    try:
        if not os.path.isfile(backup_db_file):
            logging.error(f"Backup database file does not exist: {
                          backup_db_file}")
            return

        shutil.copy(backup_db_file, active_db_file)
        logging.info(f"Restored {backup_db_file} as {active_db_file}")
    except shutil.SameFileError:
        logging.error("Source and destination represents the same file.")
    except IsADirectoryError:
        logging.error("Destination is a directory.")
    except PermissionError:
        logging.error("Permission denied.")
    except Exception as e:
        logging.error(f"Failed to restore database: {e}")


def main():
    print("1. Backup DB")
    print("2. Restore DB")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        backup_db(active_db_file, backup_db_file)
    elif choice == '2':
        restore_db(backup_db_file, active_db_file)
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == '__main__':
    main()