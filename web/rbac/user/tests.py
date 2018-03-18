from django.test import TestCase
from django.contrib.auth.hashers import make_password
from common.utils import read_json_file
from authorization.models import URLOperation
from authorization.models import Authorization
from role.models import Role
from user.models import User
from user.services import user_service


# Create your tests here.

class InitUserAuthTestDataMixin(object):
    def _user_file_path(self):
        return 'user/test_data/user.json'

    def init_url_user_auth_data(self):
        user_ids = []
        users = read_json_file(self._user_file_path())['users']

        for user in users:
            roles = []
            for role in user['roles']:
                auth_objects = []
                for auth in role['authorizations']:
                    # 创建授权和资源
                    url = URLOperation(**auth['resource'])
                    url.save()
                    auth_obj, created = Authorization.objects.get_or_create(
                        name=auth['name'],
                        resource_id=url.pk,
                        type=auth['type']
                    )
                    auth_objects.append(auth_obj)

                role_obj, created = Role.objects.get_or_create(
                    name=role['name']
                )
                for auth in auth_objects:
                    role_obj.authorizations.add(auth)
                roles.append(role_obj)
            password = make_password(user['password'], user['salt'])
            user_obj = User(
                name=user['name'],
                password=password,
                salt=user['salt']
            )
            user_obj.save()
            for role in roles:
                user_obj.roles.add(role)
            user_ids.append(user_obj.pk)
        return user_ids


class UserAuthTestCase(TestCase, InitUserAuthTestDataMixin):
    """用户授权测试用例"""

    def setUp(self):
        self.user_ids = self.init_url_user_auth_data()

    def test_user_auth(self):
        user_auth_list = []
        for user_id in self.user_ids:
            user_auth = user_service.get_auth(user_id)
            user_auth_list.append(user_auth)
        print(user_auth_list)