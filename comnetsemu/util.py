#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
About: Utility/helper functions for ComNetsEmu.
"""

import re

from mininet.log import error


def parsePing(pingOutput):
    "Parse ping output and return packets sent, received."
    # Check for downed link
    if "connect: Network is unreachable" in pingOutput:
        return 1, 0
    r = r"(\d+) packets transmitted, (\d+)( packets)? received"
    m = re.search(r, pingOutput)
    if m is None:
        error("*** Error: could not parse ping output: %s\n" % pingOutput)
        return 1, 0
    sent, received = int(m.group(1)), int(m.group(2))
    return sent, received
