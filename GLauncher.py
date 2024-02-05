import os
import tkinter as tk
from tkinter import filedialog
import pygame
import json
import time

def get_switch_games(directory):
    switch_games = [file for file in os.listdir(directory) if file.endswith(('.xci', '.nsp'))]
    return switch_games

def get_emulator_command(emulator_name):
    try:
        with open('configs/config.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get(emulator_name, "")
    except (FileNotFoundError, json.JSONDecodeError):
        return ""

def launch_emulator(emulator_name, rom_path):
    command = get_emulator_command(emulator_name)
    if command:
        os.system(f"{command} '{rom_path}'")

def update_listbox():
    switch_games = get_switch_games("roms/switch")
    listbox.delete(0, tk.END)
    for game in switch_games:
        listbox.insert(tk.END, game)

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_game = listbox.get(selected_index[0])
        rom_path = os.path.join("roms/switch", selected_game)
        launch_emulator("Switch", rom_path)

try:
    with open('config/Sidebar.json', 'r') as sidebar_config_file:
        sidebar_config = json.load(sidebar_config_file)
        sidebar_width = sidebar_config.get('width', 200)
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    sidebar_width = 200  

root = tk.Tk()
root.title("GLauncher")

root.attributes('-fullscreen', True)

root.configure(bg='#2E2E2E')

text_color = 'white'

sidebar = tk.Frame(root, width=sidebar_width, bg='#2E2E2E')  
sidebar.pack(side=tk.LEFT, fill=tk.Y)

switch_button = tk.Button(sidebar, text="Switch", command=update_listbox, bg='#404040', fg=text_color)
switch_button.pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg='#2E2E2E', fg=text_color)  
listbox.pack(expand=True, fill=tk.BOTH)

listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
