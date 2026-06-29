# Prune

Prune is a lightweight background utility that automatically detects URLs copied to the clipboard and removes tracking parameters and identifying information in real time.

It runs in the system tray and helps keep copied links clean and privacy-friendly.

---

## Features

- Automatically detects copied URLs
- Removes tracking parameters such as UTM tags, gclid, and fbclid
- Runs in the background with minimal performance impact
- System tray integration for Windows
- Privacy-focused clipboard cleaning

---

## How it works

When you copy a link, Prune performs the following steps:

1. Detects whether the clipboard content is a URL
2. Parses and removes tracking parameters including:
   - utm_source
   - utm_medium
   - utm_campaign
   - utm_term
   - utm_content
   - fbclid
   - gclid
3. Replaces the clipboard content with the cleaned URL

---

## Usage

Run the script directly:

    python main.py

Or build an executable:

    python -m PyInstaller --onefile --noconsole main.py

---

## Requirements

Install dependencies with:

    pip install pyperclip pystray pillow

- pyperclip
- pystray
- pillow

---

## Why Prune exists

Modern URLs often include tracking parameters used by advertising platforms and analytics tools. These parameters can be used to identify where a link was clicked from and how a user interacted with it.

Prune exists to automatically remove these tracking elements so that copied links are cleaner, more privacy-respecting, and easier to share. It eliminates the need to manually edit URLs before sending them to others.

---

## Icon credit

Clipboard icon by Vincent Le Moign  
https://icon-icons.com/authors/514-vincent-le-moign  

---

## License

This project is licensed under the MIT License.

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.