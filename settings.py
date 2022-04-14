class Settings:
    """Settings for kukuk.py."""

    def __init__(self) -> None:
        """Initialize the settings."""
        # Screen settings
        self.window_size = (400, 300)
        self.bg_color = (101,67,33)
        self.window_caption = "Kukuk"

        # Sound settings
        self.kuku_sound = 'sounds/keukuk03.wav'

        # Draw settings
        self.first_color = (250, 250, 250)