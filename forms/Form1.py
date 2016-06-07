from anvil import *
import google.auth, google.drive
from google.drive import app_files

class Form1(Form1Template):

  def __init__(self):
    # This sets up a variable for every component on this form.
    # For example, if we've drawn a button called "send_button", we can
    # refer to it as self.send_button:
    self.init_components()

  def btn_say_hello_click(self, sender, **event_args):
    # This function gets called when the button "hello_btn" gets clicked
    self.lbl_hello.text = "Hello, how are you? " + self.txt_name.text
