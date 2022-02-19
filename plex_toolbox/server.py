import logging

from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer


def get_plex_resource(server: str, account: MyPlexAccount) -> PlexServer:
    logging.info(f"Connecting to {account.username}@{server}")
    plex_server = account.resource(server).connect()
    return plex_server
