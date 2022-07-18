"Command line testing"
from mock import MagicMock
import os 
import sys
path = os.path.abspath(os.getcwd())
finalpath =  os.path.join(path, "pystandalonehtml")
print("The path is ",finalpath)
sys.path.insert(0,finalpath)
from cli import *

def test_cli():
    "Testing Command line"
    cli.docopt = MagicMock(return_value={
        '<input_file.html>':'value1',
        '<output_file.html>':'value2',
    })
    htmlcoverter_mock = cli.make_html_images_inline = MagicMock()

    # Execute
    cli.main()

    # Verify
    htmlcoverter_mock.assert_called_with('value1', 'value2')

