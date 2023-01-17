#!/usr/bin/python3
"""
Task 1:
Displays value of the X-Request-Id variable
1-hbtn_header.py
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        body = str(response.info())
        if "X-Request-Id: " in body:
            body = body.split("X-Request-Id: ")[1]
            answer = body.split('\n')[0]
            print(answer)
