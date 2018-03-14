import os
from appium.webdriver import webdriver

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
def set_devices(self):
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
    desired_caps['unicodeKeyboard'] = True
    # 每次是否重新安装
    desired_caps['noReset'] = True
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
