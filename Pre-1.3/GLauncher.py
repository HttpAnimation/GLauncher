import os
import tkinter as tk
from tkinter import filedialog
import pygame

def get_switch_games(directory):
    switch_games = [file for file in os.listdir(directory) if file.endswith(('.xci', '.nsp'))]
    return switch_games

# Function to launch Ryujinx with the selected ROM
def launch_ryujinx(rom_path):
    os.system(f"flatpak run org.ryujinx.Ryujinx '{rom_path}'")

# Function to update the listbox with Switch games
def update_listbox():
    switch_games = get_switch_games("roms/switch")
    listbox.delete(0, tk.END)
    for game in switch_games:
        listbox.insert(tk.END, game)

# Function to handle the selection event
def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_game = listbox.get(selected_index[0])
        rom_path = os.path.join("roms/switch", selected_game)
        launch_ryujinx(rom_path)

# Initialize Tkinter window
root = tk.Tk()
root.title("GLauncher")

# Create a sidebar with a button to load Switch games
sidebar = tk.Frame(root, width=100, bg='gray')
sidebar.pack(side=tk.LEFT, fill=tk.Y)

switch_button = tk.Button(sidebar, text="Switch", command=update_listbox)
switch_button.pack(pady=10)

# Create a listbox to display Switch games
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(expand=True, fill=tk.BOTH)

# Bind the selection event to the on_select function
listbox.bind("<<ListboxSelect>>", on_select)

# Run the Tkinter main loop
root.mainloop()
