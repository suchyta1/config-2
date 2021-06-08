#!/usr/bin/env python3

import shutil
import os


def LinkConfig(src, dest):
    destdir = os.path.dirname(dest)
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    if not os.path.exists(dest):
        os.symlink(src, dest)


if __name__ == "__main__":

    thisdir = os.path.abspath(os.path.dirname(__file__))
    homedir = os.path.join(thisdir, "home")
    userdir = os.path.expanduser("~")
    
    filenames = os.listdir(homedir)
    for filename in filenames:
        LinkConfig(os.path.join(homedir, filename), os.path.join(userdir, filename))

    LinkConfig(os.path.join(thisdir, "ssh-config"), os.path.join(userdir, ".ssh", "config"))
    LinkConfig(os.path.join(thisdir, "matplotlib.suchyta.style"), os.path.join(userdir, ".matplotlib", "matplotlibrc"))
    LinkConfig(os.path.join(thisdir, "matplotlib.suchyta.style"), os.path.join(userdir, ".config", "matplotlib", "matplotlibrc"))
