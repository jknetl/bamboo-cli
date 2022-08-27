import argparse
import os
import configparser
import appdirs

from src.client import create_bamboo_client
from src.data import ResourceType

APP_NAME = "bamboo-cli"
CONFIG_INI = "config.ini"

RESOURCE_TYPE_ARG = "resource_type"
RESOURCE_TYPE_CHOICES = ResourceType.PLAN.value + ResourceType.DEPLOYMENT.value


def get(args):
    client = create_bamboo_client(args)
    client.get(args.key)


def search(args):
    client = create_bamboo_client(args)
    client.search(args.name, args.output)


def toggle_enabled(args):
    client = create_bamboo_client(args)
    client.toggle_enabled(args.key, args.enabled)


def delete(args):
    client = create_bamboo_client(args)
    client.delete(args.key)


def main():

    config_dir = appdirs.user_config_dir(APP_NAME)
    config = configparser.ConfigParser()
    config.read(config_dir + "/" + CONFIG_INI)

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", default=os.environ.get("BAMBOO_SERVER") or config.get('BAMBOO', 'server'))
    parser.add_argument("-u", "--user", default=os.environ.get("BAMBOO_USER") or config.get('BAMBOO', 'user'))
    parser.add_argument("-p", "--password", default=os.environ.get("BAMBOO_PASSWORD") or config.get('BAMBOO', 'password'))
    parser.add_argument("-k", "--ssl-no-verify", default=False, action='store_true')
    sub_parsers = parser.add_subparsers()

    get_parser = sub_parsers.add_parser("get")
    get_parser.add_argument(RESOURCE_TYPE_ARG, choices=RESOURCE_TYPE_CHOICES)
    get_parser.add_argument("key")
    get_parser.set_defaults(func=get)

    search_parser = sub_parsers.add_parser("search")
    search_parser.add_argument(RESOURCE_TYPE_ARG, choices=RESOURCE_TYPE_CHOICES)
    search_parser.add_argument("name")
    search_parser.add_argument("-o", "--output", default="table")
    search_parser.set_defaults(func=search)

    enable_parser = sub_parsers.add_parser("enable")
    enable_parser.add_argument(RESOURCE_TYPE_ARG, choices=RESOURCE_TYPE_CHOICES)
    enable_parser.add_argument("key")
    enable_parser.set_defaults(func=toggle_enabled, enabled=True)

    disable_parser = sub_parsers.add_parser("disable")
    disable_parser.add_argument(RESOURCE_TYPE_ARG, choices=RESOURCE_TYPE_CHOICES)
    disable_parser.add_argument("key")
    disable_parser.set_defaults(func=toggle_enabled, enabled=False)

    delete_parser = sub_parsers.add_parser("delete")
    delete_parser.add_argument(RESOURCE_TYPE_ARG, choices=RESOURCE_TYPE_CHOICES)
    delete_parser.add_argument("key")
    delete_parser.set_defaults(func=toggle_enabled, enabled=False)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
        parser.exit()


if __name__ == "__main__":
    main()
