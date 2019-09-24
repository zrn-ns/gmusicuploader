#!/usr/bin/env python

import sys
import os

from gmusicapi import Musicmanager

def main():
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Invalid file path. %s" % path)
        return

    api = Musicmanager() 
    api.login()

    if not api.is_authenticated():
        print("Login Error\n")
        return

    print("start upload...\n")
    upload_info = api.upload(path)
    print(upload_info)
    print("upload is completed.\n")

    api.logout()


if __name__ == '__main__':
    main()
