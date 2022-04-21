import toga


def build(app):
    box = toga.Box

    return box


def main():
    return toga.App('Kukuk', 'nl.djkeu.kukuk', startup=build)


if __name__ == '__main__':
    main.main_loop()
