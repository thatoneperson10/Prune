import time
import threading
import re
import pyperclip
from cleaner import clean_url
import pystray
from pystray import MenuItem as item
from PIL import Image
import sys
import os

URL_PATTERN = re.compile(
    r"(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s\)\]\}\.,!?:;'\"<>]*)?"
)

last = ""

def normalize_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url

def looks_like_code(text):
    return any(x in text for x in ["def ", "import ", "class ", "{", "}", "#include"])

def clipboard_loop():
    global last

    while True:
        current = pyperclip.paste()

        if current == last:
            time.sleep(0.2)
            continue

        if looks_like_code(current):
            last = current
            continue

        if not current or len(current) < 4:
            last = current
            continue

        if "." not in current:
            last = current
            continue

        def replacer(m):
            return clean_url(normalize_url(m.group(0)))

        cleaned = URL_PATTERN.sub(replacer, current)

        if cleaned != current:
            pyperclip.copy(cleaned)
            last = cleaned
            print("Cleaned:", cleaned)
        else:
            last = current

        time.sleep(0.2)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def create_image():
    return Image.open(resource_path("icon.ico"))

def exit_app(icon, _):
    icon.stop()

def setup_tray():
    icon = pystray.Icon(
        "Clipboard Cleaner",
        create_image(),
        title="Clipboard Cleaner",
        menu=pystray.Menu(
            item("Exit", exit_app)
        )
    )

    threading.Thread(target=clipboard_loop, daemon=True).start()
    icon.run()

setup_tray()