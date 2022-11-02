import argparse
import os
import re
import requests


def wget(url, filename):
    # allow redirects - in case file is relocated
    resp = requests.get(url, allow_redirects=True)
    # this can also be 2xx, but for simplicity now we stick to 200
    # you can also check for `resp.ok`
    if resp.status_code != 200:
        print(resp.status_code, resp.reason, 'for', url)
        return
    
    # just to be cool and print something
    print(*[f"{key}: {value}" for key, value in resp.headers.items()], sep='\n')
    print()
    
    # try to extract filename from url
    if filename is None:
        # start with http*, ends if ? or # appears (or none of)
        m = re.search("^http.*/([^/\?#]*)[\?#]?", url)
        filename = m.group(1)
        if not filename:
            raise NameError(f"Filename neither given, nor found for {url}")

    # what will you do in case 2 websites store file with the same name?
    if os.path.exists(filename):
        raise OSError(f"File {filename} already exists")
    
    with open(filename, 'wb') as f:
        f.write(resp.content)
        print(f"File saved as {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='download file.')
    parser.add_argument("-O", type=str, default=None, dest='filename', help="output file name. Default -- taken from resource")
    parser.add_argument("url", type=str, default=None, help="Provide URL here")
    args = parser.parse_args()
    wget(args.url, args.filename)
