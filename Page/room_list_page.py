from Common.Base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
import Config.config as gc
from Page.login_page import LoginPage
import configparser

# 读取配置文件
con = configparser.ConfigParser()
con.read(gc.bsConfing, encoding="utf-8")
path = "/#/login"
room_list_path = "/#/chatroom/roomlist"
# 获取配置文件下指定section下指定option的值，相当于key_value
url = con.get("testServer","host") + path
room_list_url = con.get("testServer","host") + room_list_path

# 页面元素
# 创建聊天室按钮
create_chatroom_button = (By.CSS_SELECTOR, 'div.el-col.el-col-16 > div > button.el-button.el-button--primary.el-button--medium > span')
# 类型选择下拉框，默认聊天室
type1_select = (By.CSS_SELECTOR,'input[placeholder="选择类型"]')
# 类别选择下拉框，默认狗号
type2_select = (By.CSS_SELECTOR,'input[placeholder="选择类别"]')
# 狗号、房间号输入框
chatroom_input = (By.CSS_SELECTOR,'input[placeholder="请输入"]')
# 标签选择下拉框
tag_select = (By.CSS_SELECTOR,'input[placeholder="选择标签"]')
# 搜索按钮
tag_select = (By.CSS_SELECTOR,'i[class="el-icon-search"]')
# 时间清空按钮 v
clear_time = (By.CSS_SELECTOR,'i.el-input__icon.el-range__close-icon')
# clear_time = (By.CSS_SELECTOR,'button.el-button.el-picker-panel__link-btn.el-button--text.el-button--mini > span')
# 添加聊天室弹窗页面元素
gou_hao_box = (By.CSS_SELECTOR,'input[placeholder="请输入房主狗号"]')
phone_box = (By.CSS_SELECTOR,'input[placeholder="请输入手机号"]')
name_box = (By.CSS_SELECTOR,'input[placeholder="请输入真实姓名"]')
id_card_box = (By.CSS_SELECTOR,'input[placeholder="请输入身份证号"]')
list_room_template = ["","","交友","派单","电台","新标准","约会","视频","点歌","新电台","10人新标准","10人点唱","新交友","拍卖厅"]
room_template = (By.CSS_SELECTOR,'div:nth-child(5) > div > label:nth-child({0}) > span.el-radio__label'.format(list_room_template.index("拍卖厅")))
terminal_selection = (By.CSS_SELECTOR,'div:nth-child(9) > div > label:nth-child(1) > span.el-checkbox__label')
yin_zhi = (By.CSS_SELECTOR,'div:nth-child(10) > div > label:nth-child(1) > span.el-radio__label')
que_ren = (By.CSS_SELECTOR,'div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--medium > span')

# 验证页面元素
loginpage_ver_login = (By.CSS_SELECTOR, 'div.clearfix > div.info-container > span.display_name')

class RoomList(Base):
    # 动作/操作
    def open_room_list_page(self):
        '''打开房间列表页面'''
        self.login = LoginPage(self.driver)
        self.login.loginpage_loginBusiness()
        self.openUrl(room_list_url)


    def room_list_page_verify(self):
        '''验证房间列表页面是否正常打开'''
        try:
            result = self.is_element_exsit(create_chatroom_button)
            print(result)
            return result
        except:
            print('异常了')
            return False

    def create_chatroom(self,gouhao,phone,name,id_card):
        """创建一个新聊天室"""
        self.open_room_list_page()
        self.click(create_chatroom_button)
        self.sendKeys(gou_hao_box,gouhao)
        self.sendKeys(phone_box, phone)
        self.sendKeys(name_box, name)
        self.sendKeys(id_card_box, id_card)
        self.click(room_template)
        self.click(terminal_selection)
        self.click(yin_zhi)
        import time
        time.sleep(5)
        self.click(que_ren)
        time.sleep(10)

    def chatroom_verify(self):
        '''验证聊天室是否创建成功'''
        pass

    def search_chatroom(self):
        '''搜索聊天室'''
        self.select_by_text()





