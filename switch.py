import os
import json

def get_supported_formats():
    try:
        with open('configs/formats/switch.json', 'r') as formats_file:
            formats = json.load(formats_file)
            return formats.get('supported_formats', ['.xci', '.nsp'])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return ['.xci', '.nsp'] 

def get_emulator_command(emulator_name):
    try:
        with open('configs/switch.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get(emulator_name, "")
    except (FileNotFoundError, json.JSONDecodeError):
        return ""

def get_switch_games(directory):
    supported_formats = get_supported_formats()
    switch_games = [file for file in os.listdir(directory) if file.endswith(tuple(supported_formats))]
    return switch_games
