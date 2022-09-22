#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    """Add infinite number of arguments"""
    import sys
    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    print("{}".format(total))
