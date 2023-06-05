import tkinter as tk
import folium
import webbrowser
from tkinter.ttk import Label

# Create a Tkinter window
root = tk.Tk()

# Create a Folium map
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Convert the Folium map to HTML
html = m._repr_html_()

# Open the HTML page in the default browser
with open("map.html", "w") as f:
    f.write(html)
webbrowser.open("map.html")

# Display the HTML in a Tkinter Label widget
label = Label(root, text=html, justify="left")
label.pack()

# Run the Tkinter event loop
root.mainloop()
