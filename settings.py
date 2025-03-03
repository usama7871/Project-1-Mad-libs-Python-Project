# settings.py

class Settings:
    def __init__(self):
        self.theme = "light"  # Default theme
        self.sound_effects = True  # Sound effects enabled by default

    def set_theme(self, theme):
        self.theme = theme

    def toggle_sound_effects(self):
        self.sound_effects = not self.sound_effects

    def get_settings(self):
        return {
            "theme": self.theme,
            "sound_effects": self.sound_effects
        }
