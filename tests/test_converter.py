"Tes files to convert some code"
import os
import tempfile
import filecmp
from pystandalonehtml import converter

def test_guess_type():
    "Function to guess the type"
    # Prepare
    basedir = os.path.dirname(__file__)
    img = '10.1.jpg'
    mypath = os.path.join(basedir, img)

    # Execute
    mime = converter.guess_type(mypath)

    # Verify
    assert 'image/jpeg' == mime


def test_file_to_base64():
    "Function to guess the type base 64"
    # Prepare
    basedir = os.path.dirname(__file__)
    img = '10.1.jpg'
    mypath = os.path.join(basedir, img)

    # Execute
    basestr = converter.file_to_base64(mypath)

    with open("line.txt", "r", encoding="utf8") as file:
        content = file.read()
        print(content)
    # Verify
    assert content == basestr

def second_test_file_to_base64():
    "Testing the file base64"
    # Prepare
    current = os.getcwd()
    basedir = os.path.dirname(__file__)
    img = 'test.html'
    expected = 'expected_output.html'
    with tempfile.NamedTemporaryFile(delete=False) as output:
        #output = tempfile.NamedTemporaryFile(delete=False)
        os.chdir(basedir)

    # Execute
    converter.make_html_images_inline(img, output.name)

    # Verify
    assert filecmp.cmp(expected, output.name)

    # clean
    output.close()
    os.unlink(output.name)
    os.chdir(current)
