#!/usr/bin/env python3

from adapters import s3 as Current

class BuildFactory:
    def __init__ (self, adapter):
        self.adapter = adapter
        self.test_adapter()

    def upgrader(self, version, build_type, path):
        return Upgrader(version, build_type, path)

    def installer(self, version, build_type, path):
        return Installer(version, build_type, path)

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
