from Common.Base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
import Config.config as gc
import configparser

# 读取配置文件
con = configparser.ConfigParser()
con.read(gc.bsConfing, encoding="utf-8")
path = "/#/login"
home_page_path = "/#/dashboard"
# 获取配置文件下指定section下指定option的值，相当于key_value
url = con.get("testServer","host") + path
_url = con.get("testServer","host") + home_page_path


# 页面元素
loginpage_usernameBox = (By.CSS_SELECTOR, 'input[placeholder="手机号"]')
loginpage_passwordeBox = (By.CSS_SELECTOR, 'input[placeholder="密码"]')
loginpage_codeBox = (By.CSS_SELECTOR, 'input[placeholder="验证码"]')
loginpage_loginButton = (By.CSS_SELECTOR, 'form > button > span')
# # 点击登录按钮后的滑动验证按钮
# loginpage_verifyButton = (By.CSS_SELECTOR, 'div.verify-move-block')
# loginpage_registerButton = (By.XPATH, '//a[text()="立即注册"]')

# 验证页面元素
loginpage_ver_login = (By.CSS_SELECTOR, 'div.clearfix > div.info-container > span.display_name')

# loginpage_ver_register= (By.XPATH, '//*[text()="手机注册"]')
# loginpage_ver_forgetpwd = (By.XPATH,'//*[text()="找回密码"]')
# loginpage_ver_returnmain_links = 'https://www.ipaylinks.com/cn/'


class LoginPage(Base):
    # 动作/操作

    def loginpage_loginBusiness(self,username="13611849759", passwd="123456", code="1234"):
        '''登录操作'''
        self.openUrl(url)
        self.sendKeys(loginpage_usernameBox, username)
        self.sendKeys(loginpage_passwordeBox, passwd)
        self.sendKeys(loginpage_codeBox, code)
        self.click(loginpage_loginButton)

    def loginpage_verifylogin(self):
        '''验证登录是否成功'''
        try:
            # result = self.is_text_in_element(loginpage_ver_login,login_title)
            result = self.is_element_exsit(loginpage_ver_login)
            print(result)
            return result
        except:
            print('异常了')
            return False

    def loginpage_registerBusigness(self):
        '''前往立即注册链接'''
        self.openUrl(url)
        self.click(loginpage_registerButton)
    def loginpage_verifyregister(self):
        '''验证前往立即注册链接'''
        try:
            result = self.is_element_exsit(loginpage_ver_register)
            return result
        except:
            return False

    def loginpage_forgetpwd(self):
        '''前往忘记密码链接'''
        self.openUrl(url)
        self.click(loginpage_forgetpwdButton)
    def loginpage_verifyforgetpwd(self):
        '''验证前往忘记密码链接'''
        try:
            result = self.is_element_exsit(loginpage_ver_forgetpwd)
            return result
        except:
            return False

    def loginpage_returnmain(self):
        '''前往返回首页链接'''
        self.openUrl(url)
        self.click(loginpage_gomainsButton)
    def loginpage_verifyreturnmain(self):
        '''验证返回首页链接'''
        try:
            result = self.is_links(loginpage_ver_returnmain_title)
            return result
        except:
            return False

    def loginpage_gokjsd(self):
        '''前往独立站收单链接'''
        self.openUrl(url)
        self.click(loginpage_gokjsdButton)
    def loginpage_verifygokjsd(self):
        ''''''
        try:
            result = self.is_links(loginpage_ver_gosd_links)
            print(result)
            return result
        except:
            print('yic')
            return False

    def loginpage_gokjsk(self):
        '''前往收款链接'''
        self.openUrl(url)
        self.click(loginpage_gokjskButton)
    def loginpage_verifygokjsk(self):
        '''验证前往收款链接'''
        try:
            result = self.is_links(loginpage_ver_gosk_links)
            return result
        except:
            return False
    def loginpage_gogylkj(self):
        '''前往供应链科技链接'''
        self.openUrl(url)
        self.click(loginpage_gogylkjButton)
    def loginpage_verifygogylkj(self):
        '''验证前往供应链科技链接'''
        try:
            result = self.is_links(loginpage_ver_gogylkj_links)
            return result
        except:
            return False


    def loginpage_goaboutwe(self):
        '''前往关于我们链接'''
        self.openUrl(url)
        self.click(loginpage_goaboutweButton)
    def loginpage_verifygoaboutwe(self):
        '''验证前往关于我们链接'''
        try:
            result = self.is_links(loginpage_ver_aboutwe_links)
            return result
        except:
            return False

    def loginpage_gotouchwe(self):
        '''前往联系我们链接'''
        self.openUrl(url)
        self.click(loginpage_gotouchweButton)
    def loginpage_verifygotouchwe(self):
        '''验证前往联系我们链接'''
        try:
            result = self.is_links(loginpage_ver_touchwe_links)
            return result
        except BaseException as e:
            print(e)
            return False
if __name__ == '__main__':
    d = webdriver.Chrome()
    lo = LoginPage(d)
    # lo.loginpage_loginBusiness()
    # print(lo.loginpage_verifylogin('yu1@qq.com'))
    # lo.loginpage_registerBusigness()
    # a = lo.loginpage_verifyregister()
    # lo.loginpage_forgetpwd()
    # a = lo.loginpage_verifyforgetpwd()
    lo.loginpage_returnmain()
    a = lo.loginpage_verifyreturnmain()
    # lo.loginpage_gokjsd()
    # a = lo.loginpage_verifygokjsd()
    # lo.loginpage_aboutwe
    # lo.loginpage_returnmain()
    # a = lo.loginpage_verifyreturnmain()
    print(a)
    # assert a==True

