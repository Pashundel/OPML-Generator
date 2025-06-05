# OPML-Generator

This project provides a simple desktop application for macOS (and other platforms) that generates OPML files containing RSS links to Telegram channels.

## Requirements

- Python 3 (tested with Python 3.11)

Tkinter is included with the standard Python distribution on macOS. No additional dependencies are required.

## Running the App

Execute the application with Python:

```bash
python3 opml_generator_app.py
```

Fill in the title, the base RSS link (for example `https://rsshub.hellodword.top/telegram/channel/`), and paste Telegram channel names (one per line). Channel names may start with `@`; the `@` will be removed in the generated links. Choose a location to save the generated `.opml` file when prompted.

The resulting file follows a structure similar to:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
  <head>
    <title>My Telegram Feeds</title>
  </head>
  <body>
    <outline text="ukraine_now" title="ukraine_now" type="rss" xmlUrl="https://rsshub.hellodword.top/telegram/channel/ukraine_now" />
  </body>
</opml>
```
