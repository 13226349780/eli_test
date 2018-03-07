import HTMLTestRunner
import os
import unittest
from time import sleep, time

from appium import webdriver



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
        # desired_caps.setCapability("noReset", true)
        # 把输入法关掉
        desired_caps['unicodeKeyboard'] = True
        #每次是否重新安装
        #desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    #直接登录
    def test_1_login_login(self):
        self.driver.wait_activity('.LoginActivity',10,1)
        UserName = self.driver.find_element_by_id('cn.eliteu.android:id/email_et')
        UserName.clear()
        UserName.send_keys('13226349780')
        PassWord = self.driver.find_element_by_id('cn.eliteu.android:id/password_et')
        PassWord.clear()
        PassWord.send_keys('19940919')
        sleep(2)
        confirm = self.driver.find_element_by_id('cn.eliteu.android:id/login_button_layout')
        confirm.click()
        sleep(3)

        #判断是否登录成功
        #self.driver.wait_activity('.MyCoursesListActivity',10,0.5)
        ac = self.driver.current_activity
        acq = ac.split('.')
        print(acq[-1])
        assert (acq[-1] == 'MyCoursesListActivity')

    #跳过后再登录
    def test_2_login_tiaoguo(self):
        self.driver.wait_activity('.LoginActivity',10,1)
        skip = self.driver.find_element_by_id('cn.eliteu.android:id/actionbar_skip_btn')
        skip.click()
        self.driver.wait_activity('.MyCoursesListActivity',10,1)
        nav = self.driver.find_element_by_class_name('android.widget.ImageButton')
        nav.click()
        login_btn = self.driver.find_element_by_id('cn.eliteu.android:id/navigation_login_button')
        login_btn.click()
        self.driver.wait_activity('.LoginActivity',10,1)
        ac = self.driver.current_activity
        acq = ac.split('.')
        print(acq[-1])
        assert (acq[-1] == 'LoginActivity')

    #跳过后到课程页登录
    def test_3_login_skip(self):
        self.driver.wait_activity('.LoginActivity',10,1)
        skip = self.driver.find_element_by_id('cn.eliteu.android:id/actionbar_skip_btn')
        skip.click()
        self.driver.wait_activity('.MyCoursesListActivity',10,1)
        select = self.driver.find_element_by_id('cn.eliteu.android:id/course_btn')
        select.click()
        sleep(5)
        course = self.driver.find_elements_by_class_name('android.widget.RelativeLayout')
        #print(course[1].text)
        course[1].click()
        self.driver.wait_activity('EliteuCourseDetailActivity',10,1)
        self.driver.swipe(579,1500,579,800,2000)
        join = self.driver.find_element_by_id('cn.eliteu.android:id/button_enroll_now')
        join.click()
        ac = self.driver.current_activity
        acq = ac.split('.')
        print(acq[-1])
        assert (acq[-1] == 'LoginActivity')

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
