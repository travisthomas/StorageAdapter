from StorageAdapter import builds


def test_build_upgrader():
    build = builds.Upgrader("0.0.1", "data/garbage.one")
    assert build.build_type == "upgrader"
    assert build.version == "0.0.1"
    assert build.path == "data/garbage.one"


def test_build_upgrader_put():
    build = builds.Upgrader("0.0.1", "data/garbage.one")
    build.put()


def test_build_upgrader_get():
    build = builds.Upgrader("0.0.1", "data/garbage.one")
    build.get()


def test_build_upgrader_put_repeatedly():
    """
    This test should give insight into how repeated puts behave
    """
    build = builds.Upgrader("0.0.1", "data/garbage.one")
    build.put()
    # what is the output of .put()?
    build.put()
    build.put()
