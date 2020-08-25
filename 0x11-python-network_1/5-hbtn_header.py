#!/usr/bin/python3
"""Python script that sends requests URL and displyas X-Request-Id
with requests package"""
if __name__ == "__main__":
    import requests
    from sys import argv
    webpage = requests.get(argv[1]).headers.get('X-Request-Id')
    print(webpage)
