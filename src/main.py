import tkinter as tk
import requests
import json
import tkintermapview
import os
from dotenv import load_dotenv
load_dotenv()

# Create the main window
root = tk.Tk()
root.title("Simple Application")

# Set the size of the window
root.geometry("400x400")

map_widget = tkintermapview.TkinterMapView(root, width=200, height=200, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a text box
text_box = tk.Entry(root)
text_box.pack()


def show_weather_info(response_text):
    # Parse the response into a JSON object
    data = json.loads(response_text)

    # set current widget position and zoom
    map_widget.set_position(data["coord"]["lat"], data["coord"]["lon"])
    map_widget.set_zoom(100)

    # Create a new Tkinter window
    window = tk.Toplevel()
    window.geometry("400x400")

    # Create labels for each piece of weather information
    tk.Label(window, text="City:").grid(row=0, column=0)
    tk.Label(window, text=data["name"]).grid(row=0, column=1)

    tk.Label(window, text="Temperature:").grid(row=1, column=0)
    F = data['main']['temp']
    tk.Label(window, text=f"{((F-32)*5)/9  }°C").grid(row=1, column=1)

    tk.Label(window, text="Weather Description:").grid(row=2, column=0)
    tk.Label(window, text=data["weather"][0]["description"]).grid(row=2, column=1)

    tk.Label(window, text="Humidity:").grid(row=3, column=0)
    tk.Label(window, text=f"{data['main']['humidity']}%").grid(row=3, column=1)

    tk.Label(window, text="Pressure:").grid(row=4, column=0)
    tk.Label(window, text=f"{data['main']['pressure']} hPa").grid(row=4, column=1)

    tk.Label(window, text="Wind Speed:").grid(row=5, column=0)
    tk.Label(window, text=f"{data['wind']['speed']} km/h").grid(row=5, column=1)


# Create a button
def button_clicked():
    user_input = text_box.get()
    url = f"https://open-weather13.p.rapidapi.com/city/{user_input}"
    headers = {
        "X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    try:
        show_weather_info(response.text)
    except json.JSONDecodeError:
        tk.END



button = tk.Button(root, text="Click me!", command=button_clicked)
button.pack()

# Start the main loop
root.mainloop()
