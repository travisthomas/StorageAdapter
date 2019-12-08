#!/usr/bin/env python3

import boto
from ..builds import Build

s3_bucket_name = "storage-adapter-tthomas"


class BuildStorageUnit:
    def __init__(self, build_type, version):
        self._set_key(build_type, version)

    def _set_key(self, build_type, version):
        self.key = "/".join("build", build_type, version)

    def get(self, output_path: str):
        """
        Gets the build and writes it to a file at output_path.
        """
        s3 = boto.connect_s3()
        s3.Object(s3_bucket_name, self.key).download_file(output_path)

    def put(self, local_path: str):
        """
        Puts the build artifact from the local path to the configured bucket
        at the configured key.
        """
        s3 = boto.connect_s3()
        obj = s3.Object(s3_bucket_name, self.key)
        with open(local_path, "r") as content:
            obj.put(content.read())
