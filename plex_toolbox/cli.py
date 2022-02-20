import argparse
import getpass
import os.path

import plexapi.utils


def add_server_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("-s", "--server", required=True, help="The Plex server name.")
    parser.add_argument(
        "-u", "--username", required=True, help="The Plex username / email."
    )
    parser.add_argument(
        "-p",
        "--password",
        default=None,
        type=str,
        help="The Plex password or a file path to a text file that contains it. "
        "Warning: passing your password literally is security risk.",
    )
    return parser


def maybe_query_password(config: argparse.Namespace) -> str:
    if not config.password:
        return getpass.getpass("Password: ")
    else:
        file_path = os.path.expanduser(config.password)
        if os.path.exists(file_path):
            # A local file path is provided which shall contain the password.
            with open(file_path, "r") as password_file:
                password = password_file.read().strip()
            return password
        else:
            return config.password
