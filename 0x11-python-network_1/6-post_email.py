#!/usr/bin/python3
"""Pythos script that sends a post request to a passed URL
with requests package"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    values = {'email', argv[2]}
    the_page = requests.post(url, values)
    print(the_page.text)
