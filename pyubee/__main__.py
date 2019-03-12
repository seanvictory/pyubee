"""Run PyUbee from the command-line."""
import argparse
import sys

from pyubee import SUPPORTED_MODELS
from pyubee import Ubee


def main():
    """Scan for devices and print results."""
    parser = argparse.ArgumentParser(description='pyubee')
    parser.add_argument('host', help='Host')
    parser.add_argument('username', help='Username')
    parser.add_argument('password', help='Password')
    parser.add_argument('--model', default="EVW32C-0N",
                        help='Model, supported models: ' + ', '.join(SUPPORTED_MODELS))
    args = parser.parse_args()

    ubee = Ubee(host=args.host,
                username=args.username,
                password=args.password,
                model=args.model)

    if not ubee.session_active():
        if not ubee.login():
            print('Could not login')
            sys.exit(1)

    devices = ubee.get_connected_devices()
    for device in devices:
        print("%s\t%s" % (device, devices[device]))


if __name__ == '__main__':
    main()
