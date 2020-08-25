#!/usr/bin/python3
"""documentation yet to be added, hope commit makes up for it"""
if __name__ == "__main__":
    import requests
    page = requests.get('https://intranet.hbtn.io/status')
    content = page.text
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".
          format(type(content),
                 content))
