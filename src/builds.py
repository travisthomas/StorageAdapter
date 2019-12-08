#!/usr/bin/env python3

from adapters import s3 as Current


class Build:
    def __init__(self, version, build_type, path):
        self.version = version
        self.path = path
        self.storage = Current.BuildStorageUnit(build_type, version)

    def put(self):
        self.storage.put(self.path)

    def get(self):
        self.storage.get(self.path)


class Upgrader(Build):
    build_type = "upgrader"


class Installer(Build):
    build_type = "installer"
