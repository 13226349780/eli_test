from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
    try:

        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)

        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))

        return True

    except:

        return False

    