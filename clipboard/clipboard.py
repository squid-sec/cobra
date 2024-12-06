import pyperclip

def get_clipboard_contents():
    """
    Retrieves and prints the current contents of the clipboard.
    """
    try:
        clipboard_content = pyperclip.paste()
        print(f"Clipboard contains: {clipboard_content}")
    except Exception as e:
        print(f"Error accessing clipboard: {e}")

if __name__ == "__main__":
    get_clipboard_contents()
