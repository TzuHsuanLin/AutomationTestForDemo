from appium import webdriver
import time
from time import sleep
import unittest
import HTMLTestRunner

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class SuperTaste(unittest.TestCase):

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    # initial setting
    def setUp(self):
        desired_caps = {
            'platformName': 'ios',
            'deviceName': 'iphone 13',
            'platformVersion': '15.0',
            'automationName': 'XCUITest',
            # 'app': 'tw.com.tvbs.supertastemvp.dev',
            'app': 'com.AutoTestActionDemo.DemoForTestAction', # 先用自己寫的小程式測試
            'xcodeOrgId': 'SANBC4ZN9M',
            'xcodeSigningId': 'iPhone Developer',
            'udid': '00008110-001965543C0A801E'
            # 'udid':'00008110-001965543C0A801E',00008030-0004452C0E80802E
            # 'fullReset': True,
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 連接Appium
        self.driver.implicitly_wait(8)


    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print(x, y)
        return (x, y)

    # 螢幕向上滑動
    def swipeUp(self):
        l = self.getSize()
        print(l[0], l[1])
        x1 = int(l[0] * 0.5)  # x座標
        y1 = int(l[1] * 0.75)  # 起始y座標
        y2 = int(l[1] * 0.25)  # 終點y座標
        self.driver.swipe(x1, y1, x1, y2, 1000)
        print(x1, y2, y1)

    def swipeLeft(self):
        screensize = self.getSize()
        x1 = int(screensize[0] * 0.75)
        x2 = int(screensize[0] * 0.25)
        y1 = int(screensize[1] * 0.5)
        self.driver.swipe(x1, y1, x2, y1, 100)
        # self.driver.swipe(x1, y1, x2, y1, 3000)
        print(x1, x2, y1)

    def test_slide(self):
        flag = True
        try:
            self.driver.implicitly_wait(6)
            # TouchAction(self.driver).press(200,100).moveTo(10,100).release()
            # actions = TouchAction(self.driver)
            # actions.press(self,200,100)
            # # actions.release()
            # # actions.perform()
            # actions.tap_and_hold(20, 20)
            # actions.move_to(self,10, 100)
            # actions.perform()

            self.swipeLeft()
            self.swipeLeft()
            print("滑動成功！")


        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail.png')
                self.assertTrue(flag, 'Execute Fail.')


    def tearDown(self):
        pass


if __name__ == '__main__':
    # current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../report/supertasteAppReportIOS/supertaste_App_Report.html')
    # .format(current_time)
    print(filepath)
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(SuperTaste('test_slide'))
    # suite.addTest(SuperTaste('test_bottomTabCheck'))
    # suite.addTest(SuperTaste('test_open'))  # 首頁底部Tab驗證

    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste App Test Report')
    runner.run(suite)
