import tkinter as tk
from tkinter import filedialog, messagebox


def generate_opml():
    title = title_entry.get().strip() or "My Telegram Feeds"
    base_url = base_url_entry.get().strip()
    channels_text = channels_textbox.get("1.0", tk.END)

    if not base_url:
        messagebox.showerror("Error", "Please provide the base RSS link")
        return

    channel_lines = [line.strip() for line in channels_text.splitlines() if line.strip()]
    outlines = []
    for ch in channel_lines:
        channel_id = ch.lstrip('@')
        xml_url = f"{base_url}{channel_id}"
        outline = f'    <outline text="{channel_id}" title="{channel_id}" type="rss" xmlUrl="{xml_url}" />'
        outlines.append(outline)

    outlines_str = "\n".join(outlines)
    opml_content = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<opml version=\"2.0\">
  <head>
    <title>{title}</title>
  </head>
  <body>
{outlines_str}
  </body>
</opml>
"""

    file_path = filedialog.asksaveasfilename(defaultextension=".opml", filetypes=[("OPML files", "*.opml")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(opml_content)
        messagebox.showinfo("Success", f"OPML file saved to {file_path}")


root = tk.Tk()
root.title("OPML Generator")

# Title field
tk.Label(root, text="Title:").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(root, width=40)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Base RSS link:").grid(row=1, column=0, sticky="w")
base_url_entry = tk.Entry(root, width=40)
base_url_entry.insert(0, "https://rsshub.hellodword.top/telegram/channel/")
base_url_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Telegram channels (one per line):").grid(row=2, column=0, sticky="nw")
channels_textbox = tk.Text(root, width=40, height=10)
channels_textbox.grid(row=2, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate OPML", command=generate_opml)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

