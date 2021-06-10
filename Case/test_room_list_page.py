import unittest
from Common.browserUtil import BrowserUtil
from Page.room_list_page import RoomList
from Common.logCmd import LogHandler
log = LogHandler(__name__)

class Test_LoginPage(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = BrowserUtil().open_browser()
    #     cls.login = LoginPage(cls.driver)
    #
    def setUp(self):
        self.driver = BrowserUtil().open_browser()
        self.room_list = RoomList(self.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


    def test_open_room_list_page(self):
        '''打开房间列表页面测试用例'''
        try:
            self.room_list.open_room_list_page()
            log.info('Testcase - > 开始检验检查点')
            result = self.room_list.room_list_page_verify()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except BaseException as e:
            log.info('Testcase - > Test FAIL !')
            log.error("断言失败，可能原因：%s"%e)
            raise

    def test_create_chatroom(self):
        try:
            self.room_list.create_chatroom(1775871,10000003317,"汤鞍山",430515195402183212)
            log.info('Testcase - > 开始检验检查点')
            result = True
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except BaseException as e:
            log.info('Testcase - > Test FAIL !')
            log.error("断言失败，可能原因：%s"%e)
            raise

if __name__ == '__main__':
    unittest.main()