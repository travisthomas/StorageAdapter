#!/usr/bin/env python3

import boto

s3_bucket_name = "storage-adapter-tthomas"


class BuildStorageUnit:
    def __init__(self):
        self.key = None

    def set_key(self, build_type: str, version: str):
        """
        The Key is the path within the storage bucket where the object will be
        stored. 
        """
        self.key = "/".join("build", build_type, version)

    def check_key(self):
        if self.key == None:
            raise UnknownKeyException("Object key has not been set.")

    def get(self, output_path: str):
        """
        Gets the build and writes it to a file at output_path.
        """
        self.check_key()
        s3 = boto.connect_s3()
        s3.Object(s3_bucket_name, self.key).download_file(output_path)

    def put(self, local_path: str):
        """
        Puts the build artifact from the local path to the configured bucket
        at the configured key.
        """
        self.check_key()
        s3 = boto.connect_s3()
        obj = s3.Object(s3_bucket_name, self.key)
        with open(local_path, "r") as content:
            obj.put(content.read())
        return {"last_modified": obj.last_modified}


class StorageException:
    pass


class UnknownKeyException(StorageException):
    pass

