import tkinter as tk
import tkinterweb as tkweb
import folium

# create a tkinter window
root = tk.Tk()

# create a folium map
m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# create a WebView widget
w = tkweb.WebView(root)
w.pack(fill=tk.BOTH, expand=tk.YES)

# display the folium map in the WebView widget
w.load_html(m._repr_html_())

# run the tkinter event loop
root.mainloop()
