import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk
import os

# Function to search for a Pokémon
def search_pokemon():
    query = search_entry.get().lower()
    # Search for the Pokémon in the CSV data
    for pokemon in pokemon_data:
        if query == pokemon['number'].lower() or query == pokemon['name'].lower():
            display_pokemon_info(pokemon)
            display_pokemon_image(pokemon['name'])
            return
    messagebox.showinfo("Pokémon Not Found", f"No Pokémon found with number or name: {query}")

# Function to display Pokémon information in the GUI
def display_pokemon_info(pokemon):
    name_label.config(text=pokemon['name'])
    if pokemon['type2']:
        typing_label.config(text=f"Typing: {pokemon['type1']} / {pokemon['type2']}")
    else:
        typing_label.config(text=f"Typing: {pokemon['type1']}")
    base_stats_label.config(text=f"Total: {pokemon['total']}\nHP: {pokemon['hp']}\nAttack: {pokemon['attack']}\nDefense: {pokemon['defense']}\nSpecial Attack: {pokemon['sp_attack']}\nSpecial Defense: {pokemon['sp_defense']}\nSpeed: {pokemon['speed']}")

# Function to display Pokémon image
def display_pokemon_image(pokemon_name):
    pokemon_name_lower = pokemon_name.lower()
    image_path = os.path.join('images', f"{pokemon_name_lower}.png")
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            # Resize the image to a larger size
            image = image.resize((500, 500), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
            image_label.config(image=None)
    else:
        print(f"Image not found: {image_path}")
        image_label.config(image=None)


# Load Pokémon data from CSV
pokemon_data = []
with open('Pokemon.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pokemon_data.append(row)

# Create the main window
window = tk.Tk()
window.title("Pokédex GUI")

# Create the frames
search_frame = tk.Frame(window, bg="red", bd=5, relief="ridge")
image_frame = tk.Frame(window, bg="red", bd=5, relief="ridge")
info_frame = tk.Frame(window, bg="red", bd=5, relief="ridge")
typing_frame = tk.Frame(info_frame, bg="red", bd=5, relief="ridge")
base_stats_frame = tk.Frame(info_frame, bg="red", bd=5, relief="ridge")

# Frame 1 (search frame)
search_label = tk.Label(search_frame, text="Enter National Pokédex number or name")
search_entry = tk.Entry(search_frame)
search_button = tk.Button(search_frame, text="Search", width=25, height=2, command=search_pokemon, bg="blue")

search_label.pack(side=tk.LEFT, padx=5, pady=5)
search_entry.pack(side=tk.LEFT, padx=5, pady=5)
search_button.pack(side=tk.LEFT, padx=5, pady=5)

# Frame 2 (image frame)
image_label = tk.Label(image_frame, bg="white")
image_label.pack(padx=10, pady=10)

# Frame 3 (info frame)
name_label = tk.Label(info_frame, text="Pokemon Name", bg="black", fg="white")
name_label.pack(padx=5, pady=5)

typing_label = tk.Label(typing_frame, text="Typing ", bg="black", fg="white")
typing_label.pack(padx=10, pady=10)

base_stats_label = tk.Label(base_stats_frame, text="Base Stats", bg="black", fg="white")
base_stats_label.pack(padx=10, pady=10)

# Pack the frames
search_frame.pack(fill=tk.X, padx=10, pady=5)
image_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
info_frame.pack(fill=tk.X, padx=10, pady=5)
typing_frame.pack(fill=tk.X)
base_stats_frame.pack(fill=tk.X)

# Start the main event loop
window.mainloop()
