#!/usr/bin/python3
"""documentation yet to be added, hope commit makes up for it"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
              format(type(content),
                     content,
                     content.decode('utf-8')))
