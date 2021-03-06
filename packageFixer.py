#!/usr/bin/env python

"""
Any version of Python

For people using repacks built on Java 7 or earlier,
their scripts are likely interpreted using Rhino.

Java 8+ brings us a new Javascript engine, Nashorn.

This script is one of two scripts
(the other being linePrepender.py)
that can be run on the old scripts in order to make
them function with Nashorn.

Must be run from the root directory of the server with
access to /scripts/.

NOTE: This is a bandaid fix, old scripts should be
further assimilated into Nashorn's style once they are
minimally working, e.g. use ``Java.type()`` for imports.
"""

import os

for dirpath, dirnames, filenames in os.walk("./scripts"):
    for file in filenames:
        if file[len(file) - 3:] == ".js":
            lines = []
            with open(os.path.join(dirpath, file), "r") as f:
                lines = f.readlines()
            for i in range(len(lines)):
                if "net.sf." in lines[i] and "Packages" not in lines[i]:
                    lines[i] = lines[i].replace("net.sf.", "Packages.net.sf.")
            with open(os.path.join(dirpath, file), "w") as f:
                f.writelines(lines)
