import argparse
import os

from client import BambooClient


def get(args):
    if args.resource_type == "plan" or args.resource_type == "p":
        client = BambooClient(args.server, args.user, args.password, ssl_verify=(not args.ssl_no_verify))
        client.get_plan(args.key)
    elif args.resource_type == "deployment" or args.resource_type == "d":
        raise Exception("Working with deployments in not implement yet!")
    else:
        raise Exception("Unknown resource_type!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", default=os.environ.get("BAMBOO_SERVER"))
    parser.add_argument("-u", "--user", default=os.environ.get("BAMBOO_USER"))
    parser.add_argument("-p", "--password", default=os.environ.get("BAMBOO_PASSWORD"))
    parser.add_argument("-k", "--ssl-no-verify", default=False, action='store_true')
    sub_parsers = parser.add_subparsers()

    get_parser = sub_parsers.add_parser("get")
    get_parser.add_argument("resource_type", choices=["p", "plan", "d", "deployment"])
    get_parser.add_argument("key")
    get_parser.set_defaults(func=get)

    args = parser.parse_args()


    args.func(args)


if __name__ == "__main__":
    main()
