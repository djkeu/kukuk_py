import toga
from alarms import quarterly_alarms, hourly_alarms


def build(app):
    box = toga.Box()

    quarterly_alarms()
    hourly_alarms()

    return box


def main():
    return toga.App('Kukuk', 'nl.djkeu.kukuk', startup=build)


if __name__ == '__main__':
    main().main_loop()
