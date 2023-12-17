import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

# Create main window
root = tk.Tk()
root.title("AI Image Finder: A tkinter-Powered Image Search Tool")
root.geometry("600x400")  # Set initial window size

# Create input field and search button
query_entry = tk.Entry(root)
query_entry.grid(row=0, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=lambda: search_image(query_entry.get()))
search_button.grid(row=0, column=1, padx=10, pady=10)

# Create label widget to display image or message
image_label = tk.Label(root)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def search_image(query):
    try:
        # Get image URL from API
        response = requests.get(f"https://getimg-uuqx.onrender.com/search?query={query}")
        response.raise_for_status()  # Check for HTTP request errors

        image_data = requests.get(response.json()["image_url"]).content
        image = Image.open(io.BytesIO(image_data))

        # Create tkinter-compatible image object
        tk_image = ImageTk.PhotoImage(image)

        # Set image to label widget
        image_label.config(image=tk_image)
        image_label.image = tk_image  # Keep a reference to the image

    except requests.exceptions.RequestException as e:
        image_label.config(text="Error: Network request failed.")
    except (IOError, KeyError):
        image_label.config(text="Error: Image not found.")

# Display GUI
root.mainloop()
