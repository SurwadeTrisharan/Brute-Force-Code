import socket
import time
from concurrent.futures import ThreadPoolExecutor

def check_username(username, host="hackazon.samsclass.info"):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("10.10.48.1", 80))
            req = f"HEAD /{username} HTTP/1.1\r\nHost: {host}\r\n\r\n"
            s.send(req.encode())  # Encode the request to bytes
            r = s.recv(8192)[9:12]
            if r != b"404":  # Compare with byte string
                return f"{username}: {r.decode()}"  # Decode the response for printing
    except socket.error as e:
        return f"Error with {username}: {e}"

def main():
    a = []
    t0 = time.time()
    
    with open("D:\\Hacking\\wordlist-master\\wordlist-master\\usernames.txt", "r") as f:
        a = [line.rstrip('\n') for line in f]

    n = len(a)
    
    # Using ThreadPoolExecutor to send requests concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_username, a)

    for result in results:
        if result:
            print(result)

    print("Guesses: ", n, " Elapsed time: ", time.time() - t0, " sec.")

if __name__ == "__main__":
    main()
