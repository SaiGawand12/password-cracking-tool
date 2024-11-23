import itertools
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import check_password
from config import CHARSET, PASSWORD_LENGTH, NUM_THREADS

def attempt_password(password_tuple):
    """
    Attempts a single password in the list of permutations. This function is used for threading.
    """
    password = ''.join(password_tuple)
    if check_password("admin", password):
        return password
    return None

def brute_force_password(password_length, charset, num_threads=NUM_THREADS):
    """
    This function attempts to crack the password by splitting the task across multiple threads.
    """
    attempts = 0
    found_password = None

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = list(executor.map(attempt_password, itertools.product(charset, repeat=password_length)))

        for result in futures:
            attempts += 1
            if result:
                found_password = result
                break

    return found_password, attempts

def main():
    start_time = time.time()
    password, attempts = brute_force_password(PASSWORD_LENGTH, CHARSET)
    end_time = time.time()

    if password:
        print(f"Password found: {password}")
        print(f"Number of attempts: {attempts}")
        print(f"Time taken: {end_time - start_time} seconds")
    else:
        print("Password not found")

if __name__ == "__main__":
    main()