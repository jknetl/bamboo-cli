import argparse


def get(args):
    print("getting " + args.resource_type)


def main():
    parser = argparse.ArgumentParser()  # todo: add description
    sub_parsers = parser.add_subparsers()

    get_parser = sub_parsers.add_parser("get")
    get_parser.add_argument("resource_type")
    get_parser.set_defaults(func=get)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
