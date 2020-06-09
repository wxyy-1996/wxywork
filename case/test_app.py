import unittest


class TestWeb(unittest.TestCase):
    def setUp(self):
        print("打开浏览器")

    def test_login_app(self):
        """app端用户登录"""
        print("输入app用户名:\n输入密码")
        self.assertEqual(1, 1)

    def test_register_app(self):
        """app端用户注册"""
        print("输入app用户名:\n输入电话\n输入邮箱")
        self.assertEqual(2, 2)
        
    def test_order_app(self):
        """app端用户下单"""
        print("购买商品:\n输入数量\n输入金额")
        self.assertEqual(2, 2)

    def tearDown(self):
        print("关闭浏览器")
