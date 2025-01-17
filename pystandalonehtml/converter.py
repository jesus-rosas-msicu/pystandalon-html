"Files that converts a file from an image"
import os
import urllib.request
import base64
import mimetypes
from bs4 import BeautifulSoup
#Testing CI/CD

def guess_type(filepath):
    """
    Return the mimetype of a file, given it's path.
    :type filepath: str
    :return: Mimetype string.
    :rtype: str
    """
    print("Testing CI/CD")
    return mimetypes.guess_type(filepath)[0]


def file_to_base64(filepath):
    """
    Returns the content of a file as a Base64 encoded string.
    :param filepath: Path to the file.
    :type filepath: str
    :return: The file content, Base64 encoded.
    :rtype: str
    """
    with open(filepath, 'rb',encoding="utf-8") as file:
        encoded_str = base64.b64encode(file.read())
    return encoded_str.decode()

def url_to_base64(url):
    """
    Returns the content of a file as a Base64 encoded string.
    :param url: URL to the file.
    :type url: str
    :return: The file content, Base64 encoded.
    :rtype: str
    """
    #file = urllib.request.urlopen(url)
    with urllib.request.urlopen(url) as file:
        encoded_str = base64.b64encode(file.read())
    return encoded_str.decode()


def splitme(string):
    "Splits a string"
    if string[0] == "\\":
        string = string[1:]
    return string

def make_html_images_inline(in_filepath, out_filepath):
    """
    Takes an HTML file and writes a new version with inline Base64 encoded
    images.
    :param in_filepath: Input file path (HTML)
    :type in_filepath: str
    :param out_filepath: Output file path (HTML)
    :type out_filepath: str
    """
    basepath = os.path.split(in_filepath.rstrip(os.path.sep))[0]
    #soup = BeautifulSoup(open(in_filepath, 'r',encoding="utf-8"), 'html.parser')
    with open(in_filepath, 'r',encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html.parser')

    for img in soup.find_all('img'):
        img_path = os.path.join(basepath, img.attrs['src'])
        mimetype = guess_type(img_path)
        src = splitme(img.attrs['src'])
        if src.startswith('http') or src.startswith('file:'):
            #img.attrs['src'] = "data:%s;base64,%s" % (mimetype, url_to_base64(src))
            data = (mimetype, file_to_base64(src))
            img.attrs['src'] = f"{data[0] and data[1]}"
        elif not src.startswith('data'):
            print(src)
            #img.attrs['src'] = "data:%s;base64,%s" % (mimetype, file_to_base64(src))
            data = (mimetype, file_to_base64(src))
            img.attrs['src'] = f"{data[0] and data[1]}"

    with open(out_filepath, 'w',encoding="utf-8") as file:
        file.write(str(soup))
