import tkinter as tk

root = tk.Tk()
root.title("URL Shortener")
root.geometry("300x300")

# Create and pack widgets
lurl_label = tk.Label(root, text="Enter the long URL:")
lurl_label.pack(pady=5)  # Add some padding for better spacing

lurl_entry = tk.Entry(root, width=40)
lurl_entry.pack(pady=5)

short_label = tk.Label(root, text="Output shortened link:")
short_label.pack(pady=5)

short_entry = tk.Entry(root, width=40)
short_entry.pack(pady=5)

short_btn = tk.Button(root, text="Shorten URL", command=shorten_url)
short_btn.pack(pady=10)

root.mainloop()
