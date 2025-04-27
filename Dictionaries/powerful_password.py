
import hashlib

# Let's assume this is the provided hash_password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Stored logins with email as the key and hashed password as the value
stored_logins = {
    "user@example.com": hash_password("my_secure_password"),
    "johndoe@website.com": hash_password("another_password123"),
}

# Function to log in
def login(email, password_to_check):
    # Hash the password to check
    hashed_password_to_check = hash_password(password_to_check)
    
    # Check if the email exists in stored logins and if the password hash matches
    if email in stored_logins and stored_logins[email] == hashed_password_to_check:
        return True
    else:
        return False

# Test cases (to show how the function works)
print(login("user@example.com", "my_secure_password"))  # True
print(login("user@example.com", "wrong_password"))  # False
