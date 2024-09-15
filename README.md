# blogCLI - 
blogCLI is a simple, command-line based blogsite.

It features secure user data storage with password encryption, and do all of the CRUD [Create, Read, Update, Delete] functionalities

## Setup
- run `setup.py`
- then run `main.py`

## Files 
1. `setup.py` : Contains code for setting up database and creating tables. By default, it generates a `data.db` in the same folder level as `setup.py`

2. `crud.py` : Contains code for all `CREATE`,`READ`,`UPDATE` and `DELETE` functions needed for the database.

3. `.venv` : Python virtual environment for running code in systems without `Python` preinstalled.

4. `data.db` : Database where all user and blog related data are stored. Has 2 tables `uesrs` and `blogs`

5. `main.py` : The main file of `blogCLI`. Run `setup.py` atleast once before running this file.

# Used libraries
- `bcrypt` for password encryption
- `sqlite3` for database management and operations
- `getpass` for secure password input