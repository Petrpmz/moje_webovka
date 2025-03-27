import tkinter as tk
from tkinter import ttk

# Create a new window
root = tk.Tk()
root.title("My Tkinter App")

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create two frames for the tabs
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

# Create a text widget for each tab
text1 = tk.Text(frame1)
text1.pack(fill='both', expand=True)

text2 = tk.Text(frame2)
text2.pack(fill='both', expand=True)

# Add the frames to the notebook
notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")

# Start the event loop
root.mainloop()