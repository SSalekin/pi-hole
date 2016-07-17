#!/usr/bin/env python3
# Copyright (c) 2016 Jacob Salmela
# Pi-hole: a DNS based ad-blocker [https://www.pi-hole.net]
#
# Update Pi-hole Core
#
# The Pi-Hole is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


# DOCOPT


"""
Update Pi-hole Core

Usage: pihole updateCore
"""


# IMPORTS


import pihole_vars
from docopt import docopt


# SCRIPT


def main(argv):
    if argv is None:
        args = docopt(__doc__)
    else:
        args = docopt(__doc__, argv=argv)


if __name__ == "__main__":
    main(None)
