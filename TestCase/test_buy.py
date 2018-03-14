import unittest

import os
from time import sleep

from appium import webdriver

from Utils.getyaml import yl
from Utils.toast import is_toast_exist

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


class test_course(unittest.TestCase):
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
        # desired_caps['automationName']='Uiautomator2'
        # desired_caps.setCapability("noReset",true)
        # 把输入法关掉
        desired_caps['automationName'] =  'Uiautomator2'
        desired_caps['unicodeKeyboard'] = True
        # 每次是否重新安装
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.quit()

    def test_buy(self):
        self.driver.wait_activity(yl['test_buy']['wa'],10,0.5)
        find_course = self.driver.find_element_by_id(yl['test_buy']['find_course'])
        find_course.click()
        self.driver.wait_activity(yl['test_buy']['course_ac'],10,0.5)
        find_content = self.driver.find_elements_by_class_name(yl['test_buy']['find_content'])
        #print('------------------------------------')
        #print(find_content)
        #print(find_content[1])
        find_content[0].click()
        self.driver.wait_activity(yl['test_buy']['select_buy'],10,0.5)
        self.driver.swipe(579, 1500, 579, 800, 2000)
        pay = self.driver.find_element_by_id(yl['test_buy']['join_buy'])
        pay.click()
        self.driver.wait_activity(yl['test_buy']['select_buy'],10,0.5)
        select = self.driver.find_element_by_id(yl['test_buy']['select_course'])
        select.click()
        #commit = self.driver.find_element_by_class_name(yl['test_buy']['commit'])
        commit1 = self.driver.find_element_by_id(yl['test_buy']['commit'])
        commit1.click()
        print(is_toast_exist(self.driver,"您未选中任何课程"))







if __name__ == '__main__':
    suitcase = unittest.TestLoader().loadTestsFromTestCase(test_course)
    unittest.TextTestRunner(verbosity=2).run(suitcase)