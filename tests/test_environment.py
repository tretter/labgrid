import pytest
from labgrid import Environment, NoConfigFoundError


class TestEnvironment:
    def test_noconfig_instance(self):
        with pytest.raises(NoConfigFoundError):
            e = Environment()

    def test_instance(self, tmpdir):
        p = tmpdir.join("config.yaml")
        p.write("""
        test1:
          - keks
        test2:
          - cookie
        """)
        e = Environment(str(p))
        assert(isinstance(e, Environment))

    def test_get_target(self, tmpdir):
        p = tmpdir.join("config.yaml")
        p.write("""
        test1:
          - keks
        test2:
          - cookie
        """)
        e = Environment(str(p))
        assert(e.get_target("test1"))
        assert(e.get_target("test2"))

    def test_instance_invalid_yaml(self, tmpdir):
        p = tmpdir.join("config.yaml")
        p.write("""
        I a(m) no yaml:
          - keks
          cookie
        """)
        with pytest.raises(NoConfigFoundError):
            e = Environment(str(p))
