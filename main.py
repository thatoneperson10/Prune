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
    r"https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(?:/[^\s()<>]*)*"
)

last_copied = ""

def normalize_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url

def looks_like_code(text):
    return any(x in text for x in ["def ", "import ", "class ", "{", "}", "#include"])

def clipboard_loop():
    global last_copied

    while True:
        try:
            current = pyperclip.paste()
        except Exception:
            time.sleep(0.3)
            continue

        if current == last_copied or not current or len(current) < 10:
            time.sleep(0.3)
            continue

        if looks_like_code(current):
            last_copied = current
            continue

        def replacer(m):
            return clean_url(normalize_url(m.group(0)))

        try:
            cleaned = URL_PATTERN.sub(replacer, current)
            
            if cleaned != current:
                pyperclip.copy(cleaned)
                last_copied = cleaned
            else:
                last_copied = current
        except Exception:
            last_copied = current

        time.sleep(0.3)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def create_image():
    try:
        return Image.open(resource_path("icon.ico"))
    except FileNotFoundError:
        return Image.new("RGB", (64, 64), color=(0, 120, 215))

def exit_app(icon, _):
    icon.stop()
    os._exit(0)

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

if __name__ == "__main__":
    setup_tray()