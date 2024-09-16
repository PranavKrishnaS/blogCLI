import bcrypt
import sqlite3
import getpass
import crud

# TERMINAL BASED BlogSite with all the basic 
# CRUD facilities

# Author : PranavKrishnaS

# SQL FILE NAME
DB_FILE = "data.db"


def main_menu(user_id):
    
    # Options for different operations
    while True:
        print("\n--- Blog Menu ---")
        print("1. Create a new blog post")
        print("2. View blog posts")
        print("3. Modify an existing blog post")
        print("4. Delete a blog post")
        print("5. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            crud.createBlog(user_id)

        elif choice == '2':
            crud.viewBlogs(user_id)

        elif choice == '3':
            crud.modifyBlog(user_id)

        elif choice == '4':
            crud.deleteBlog(user_id)
            
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    
    #  1. For register
    #  2. For login
    #  3: Exit
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            crud.register()
        elif choice == '2':
            user_id = crud.login()
            if user_id:
                main_menu(user_id)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()