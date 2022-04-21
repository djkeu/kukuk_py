import toga
from alarms import quarterly_alarms, hourly_alarms, minutely_alarms


def build(app):
    box = toga.Box()

    minutely_alarms()

    return box


def main():
    return toga.App('Kukuk', 'nl.djkeu.kukuk', startup=build)


if __name__ == '__main__':
    main().main_loop()
