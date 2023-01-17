#!/usr/bin/python3
"""
Task 6:
Sends POST request with an email as a parameter
To display the body of the response
6-post_email.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
