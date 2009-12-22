"""
Pinder

Pinder is a client library for Campfire, the chat application from 37Signals.
"""
from campfire import Campfire, VERSION as __version__
from room import Room
from exc import HTTPUnauthorizedException, HTTPNotFoundException

__author__ = "Lawrence Oluyede <l.oluyede@gmail.com>"
__copyright__ = "Copyright (c) 2009, Lawrence Oluyede"
__license__ = "BSD"
