def check_password(username, password):
    # Simulate checking the password for a given username
    # For example, you could integrate with an API or check a local system
    print(f"Checking password for {username}: {password}")
    correct_password = "1234"  # Example correct password for a test user
    if password == correct_password:
        return True
    else:
        return False