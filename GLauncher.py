# main.py
import os
import tkinter as tk
from tkinter import filedialog
from switch import SwitchConfig
import subprocess

class SwitchLauncherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Switch Game Launcher")
        self.master.attributes('-fullscreen', True)

        self.switch_config = SwitchConfig()
        self.supported_formats = self.switch_config.get_supported_formats()

        self.sidebar = tk.Frame(self.master, width=200, bg="lightgray")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.launch_button = tk.Button(self.sidebar, text="Switch", command=self.load_switch_info)
        self.launch_button.pack(pady=10)

        self.games_listbox = tk.Listbox(self.master)
        self.games_listbox.pack(expand=True, fill=tk.BOTH)

        self.load_supported_games()

    def load_supported_games(self):
        roms_path = "roms/switch"
        for file in os.listdir(roms_path):
            if file.endswith(tuple(self.supported_formats)):
                self.games_listbox.insert(tk.END, file)

    def load_switch_info(self):
        selected_game_index = self.games_listbox.curselection()
        if selected_game_index:
            selected_game = self.games_listbox.get(selected_game_index)
            emulator_command = self.switch_config.get_emulator_command(0) 
            full_path = os.path.join("roms/switch", selected_game)
            subprocess.run(emulator_command.split() + [full_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = SwitchLauncherApp(root)
    root.mainloop()
