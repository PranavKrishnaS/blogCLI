import sqlite3
import getpass
import bcrypt
DB_FILE = "data.db"

# user login / registration
def register():
    # Register new user with encrypted password
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    username = input("Enter username: ").strip()
    
    # Check if the username exists
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    if c.fetchall() != []:
        print("Username already exists. Please choose another one.")
        conn.close()
        return
    
    password = getpass.getpass("Enter password: ").encode('utf-8')
    confirm_password = getpass.getpass("Confirm password: ").encode('utf-8')
    
    if password != confirm_password:
        print("Passwords do not match. Try again.")
        conn.close()
        return

    # Hash the password
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    
    # Insert new user into the users table
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password.decode('utf-8')))
    conn.commit()
    conn.close()
    
    print("User registered successfully!")

def login():

    """Authenticate the user with username and password."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").encode('utf-8')
    
    # Check if the user exists
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    
    if user is None:
        print("Username not found.")
        conn.close()
        return None
    
    # Validate password
    stored_password = user[2].encode('utf-8')  # User table: id, username, password
    if bcrypt.checkpw(password, stored_password):
        print(f"Logged in as {username}")
        conn.close()
        return user[0]  # Return user ID on successful login
    else:
        print("Incorrect password.")
        conn.close()
        return None

# Blog CRUD
# Create new blog
def createBlog(user_id):
    """Create a new blog post for the logged-in user."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    title = input("Enter blog title: ").strip()
    content = input("Enter blog content: ").strip()
    
    c.execute("INSERT INTO blogs (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
    conn.commit()
    conn.close()
    
    print("Blog post created successfully!")   

# View all blogs
def viewBlogs(user_id):
    """View all blog posts created by the logged-in user."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    c.execute("SELECT * FROM blogs ")
    blogs = c.fetchall()
    
    if not blogs:
        print("No blog posts.")
    else:
        for blog in blogs:
            print(f"\nBlog ID: {blog[0]} | User ID: {blog[1]} | Title: {blog[2]}")
            print(f"Content: {blog[3]}")
    
    conn.close()

# Modify your own blog
def modifyBlog(user_id):
    """Modify an existing blog post created by the logged-in user."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    blog_id = int(input("Enter the Blog ID to modify: "))
    
    # Check if the blog belongs to the user
    c.execute("SELECT * FROM blogs WHERE id = ? AND user_id = ?", (blog_id, user_id))
    blog = c.fetchone()
    
    if blog is None:
        print("Blog post not found or you are not authorized to modify this post.")
        conn.close()
        return
    
    # Update blog title and content
    new_title = input("Enter new title: ").strip()
    new_content = input("Enter new content: ").strip()
    
    c.execute("UPDATE blogs SET title = ?, content = ? WHERE id = ?", (new_title, new_content, blog_id))
    conn.commit()
    conn.close()
    
    print("Blog post updated successfully!")

# Delete blog
def deleteBlog(user_id):
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    blog_id = int(input("Enter the Blog ID to delete: "))
    
    # Check if the blog belongs to the user
    c.execute("SELECT * FROM blogs WHERE id = ? AND user_id = ?", (blog_id, user_id))
    blog = c.fetchall()
    
    if blog == []:
        print("Blog post not found or you are not authorized to delete this post.")
        conn.close()
        return
    
    # Delete the blog post
    c.execute("DELETE FROM blogs WHERE id = ?", (blog_id,))
    conn.commit()
    conn.close()
    
    print("Blog post deleted successfully!")