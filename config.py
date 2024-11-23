import string

# Configuration for brute-force cracking
TARGET_USERNAME = "admin"  # Target username to crack
PASSWORD_LENGTH = 6        # Set the maximum password length to try
NUM_THREADS = 6            # Number of threads to use for parallel processing
# CHARSET = string.ascii_lowercase   # Charset: lowercase letters + digits


CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# # Charset includes lowercase, uppercase, digits, and punctuation symbols.