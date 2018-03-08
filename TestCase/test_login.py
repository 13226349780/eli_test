import HTMLTestRunner
import os
import unittest
from time import sleep, time

from appium import webdriver

from Utils.Operate import swipe_up
from Utils.getyaml import yl

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


class test_login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../app/cn.eliteu.android_1.2.3_123.apk'
        )
        desired_caps['appPackage'] = 'cn.eliteu.android'
        desired_caps['appActivity'] = 'org.edx.mobile.view.SplashActivity'
        #desired_caps['automationName']='Uiautomator2'
        #desired_caps.setCapability("noReset",true)
        # 把输入法关掉
        desired_caps['unicodeKeyboard'] = True
        #每次是否重新安装
        #desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_l(self):
        sleep(10)
        swipe_up()



"""
  #直接登录
    def test_1_login_login(self):
        self.driver.wait_activity(yl['test_login']['LA'],10,1)
        UserName = self.driver.find_element_by_id(yl['test_login']['username_input'])
        UserName.clear()
        UserName.send_keys(13226349780)
        PassWord = self.driver.find_element_by_id(yl['test_login']['password_input'])
        PassWord.clear()
        PassWord.send_keys(19940919)
        sleep(2)
        confirm = self.driver.find_element_by_id(yl['test_login']['confirm'])
        confirm.click()
        sleep(3)
        #判断是否登录成功
        #self.driver.wait_activity('.MyCoursesListActivity',10,0.5)
        ac = self.driver.current_activity
        acq = ac.split('.')
        print(acq[-1])
        assert (acq[-1] == yl['test_login']['mainye'])



    ##跳过后再登录
    def test_2_ls(self):
        self.driver.wait_activity(yl['test_login']['LA'],10,1)
        skip = self.driver.find_element_by_id(yl['test_ls']['skip'])
        skip.click()
        self.driver.wait_activity(yl['test_ls']['mainye'],10,1)
        nav = self.driver.find_element_by_class_name(yl['test_ls']['nav'])
        nav.click()
        login_btn = self.driver.find_element_by_id(yl['test_ls']['login_btn'])
        login_btn.click()
        self.driver.wait_activity(yl['test_login']['LA'],10,1)
        ac = self.driver.current_activity
        acq = ac.split('.')
        print(acq[-1])
        assert (acq[-1] == yl['test_ls']['LA'])


    #跳过后到课程页登录
    def test_3_login_skip(self):
        self.driver.wait_activity(yl['test_lk']['LA'],10,1)
        skip = self.driver.find_element_by_id(yl['test_lk']['skip'])
        skip.click()
        self.driver.wait_activity(yl['test_lk']['mainye'],10,1)
        select = self.driver.find_element_by_id(yl['test_lk']['select'])
        select.click()
        sleep(5)
        course = self.driver.find_elements_by_class_name(yl['test_lk']['courses'])
        #print(course[1].text)
        course[1].click()
        self.driver.wait_activity(yl['test_lk']['wa'],10,1)
        swipe_up()

        #self.driver.swipe(579,1500,579,800,2000)
        join = self.driver.find_element_by_id(yl['test_lk']['join'])
        join.click()
        ac = self.driver.current_activity
        acq = ac.split('.')
        print(acq[-1])
        assert (acq[-1] == yl['test_lk']['LA'])
"""



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_login)

    filename = 'D:\lqf\eli_test\TestReport\Report.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"TestReport",
        description=u"Result"
    )
    runner.run(suite)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    fp.close()
