#!/usr/bin/python3
"""
doc
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info()['X-Request-Id'])
