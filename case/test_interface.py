import unittest


class TestWeb(unittest.TestCase):
    def setUp(self):
        print("打开浏览器")

    def test_login_interface(self):
        """用户登录接口"""
        print("输入用户名:\n输入密码")
        self.assertEqual(1, 1)

    def test_register_interface(self):
        """用户注册接口"""
        print("输入用户名:\n输入电话\n输入邮箱")
        self.assertEqual(2, 2)

    def tearDown(self):
        print("关闭浏览器")
