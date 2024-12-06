from pynput.keyboard import Listener

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")
    if key == 'q':  # Press 'q' to stop the listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
