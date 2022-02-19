import argparse


def add_server_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("-s", "--server", required=True, help="The Plex server name.")
    parser.add_argument(
        "-u", "--username", required=True, help="The Plex username / email."
    )
    parser.add_argument(
        "-p",
        "--password",
        default=None,
        help="The Plex password. Warning: passing your password literally is security risk.",
    )
    return parser
