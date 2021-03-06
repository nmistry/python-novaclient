from novaclient import exceptions
from novaclient.v1_1 import security_groups
from tests.v1_1 import fakes
from tests import utils


cs = fakes.FakeClient()


class SecurityGroupsTest(utils.TestCase):
    def test_list_security_groups(self):
        sgs = cs.security_groups.list()
        cs.assert_called('GET', '/os-security-groups')
        for sg in sgs:
            self.assertTrue(isinstance(sg, security_groups.SecurityGroup))

    def test_get_security_groups(self):
        sg = cs.security_groups.get(1)
        cs.assert_called('GET', '/os-security-groups/1')
        self.assertTrue(isinstance(sg, security_groups.SecurityGroup))

    def test_delete_security_group(self):
        sg = cs.security_groups.list()[0]
        sg.delete()
        cs.assert_called('DELETE', '/os-security-groups/1')
        cs.security_groups.delete(1)
        cs.assert_called('DELETE', '/os-security-groups/1')
        cs.security_groups.delete(sg)
        cs.assert_called('DELETE', '/os-security-groups/1')

    def test_create_security_group(self):
        sg = cs.security_groups.create("foo", "foo barr")
        cs.assert_called('POST', '/os-security-groups')
        self.assertTrue(isinstance(sg, security_groups.SecurityGroup))
