#!/usr/bin/env python3

import requests
import sys

"""Provide the end URL to which a user has been redirected
along with the response history for the redirect.

The goal is prevent unknown URLs from executing unknown javascript, etc. in a
users browser capable of the execution before the end goal URL redirect domain
is seen by the user.

Useful in retrieving links from email of unknown origin.

"""


def get_url(provided_url=None):
    """get the url"""
    if provided_url is None:
        provided_url = "https://bit.ly/1km0cRx"

    resp = requests.get(provided_url)

    return resp


if __name__ == "__main__":

    if len(sys.argv) > 1:
        resp = get_url(sys.argv[1])
        print(resp.history)
        print(resp.url)
    else:
        print("USAGE: {} <provided_url>".format(sys.argv[0]))
