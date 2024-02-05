import json

class SwitchConfig:
    def __init__(self, config_path="configs/formats/switch.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def get_supported_formats(self):
        return self.config["supported_formats"]

    def get_emulator_command(self, index):
        return self.config[index]["Switch"]
