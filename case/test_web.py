import unittest

class TestWeb(unittest.TestCase):
    def setUp(self):
        print("打开浏览器")

    def test_login_web(self):
        """web端用户登录"""
        print("输入web用户名:\n输入密码")
        self.assertEqual(1,1)

    def test_register_web(self):
        """web端用户注册"""
        print("输入web用户名:\n输入电话\n输入邮箱")
        self.assertEqual(2,2)
    
    def test_order_web(self):
        """web端下单"""
        print("选择商品:\n选择数量\n选择样式")
        self.assertEqual(2,3)
        
    def test_pay_web(self):
        """web端支付"""
        print("消费金额")
        self.assertEqual(2,2)

    def tearDown(self):
        print("关闭浏览器")
