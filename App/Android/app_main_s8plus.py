from selenium import webdriver as chrome_driver
from appium import webdriver
from time import sleep
import time
import random
import datetime
import unittest
import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import app_pocket_s8plus
import app_register_login_s8plus

# Freyja
# 關閉【新手教學頁】
def init(self):
    # 新手教學
    for i in range(3):
        self.driver.find_element_by_class_name('android.widget.ImageView').click()
        self.driver.implicitly_wait(3)

    # 立即逛逛btn
    self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/beginner_close_btn').click()
    self.driver.implicitly_wait(3)

# Freyja
# 【會員登入頁】完成Apple ID登入，並檢查有登入成功
def appleIDLogin(self):
    print('(待補)Apple ID登入')

# Freyja
# 【會員註冊頁】/【會員登入頁】完成Facebook登入，並檢查有登入成功
def facebookLogin(self):
    # FB登入
    if self.is_element_exist('com.tvbs.supertastemvppack:id/ivFbRegister') is True:
        self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivFbRegister').click()    #當前在【會員註冊頁】
        print('Click「Facebook快速註冊」button')
    elif self.is_element_exist('com.tvbs.supertastemvppack:id/ivFbLogin') is True:
        self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivFbLogin').click()    #當前在【會員登入頁】
        print('Click「Facebook登入」button')
    WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('android.view.ViewGroup'))  # 若會fail, 是因登入資訊被記住ㄌ
    sleep(3)
    if self.driver.find_elements_by_xpath("//*[@text='手機號碼或電子郵件地址']"):
        print('當前畫面的語系是中文')
    else:
        print('當前畫面的語系不是中文，點一下這個位置，會把FB登入頁切換成中文')
        self.driver.tap([(480, 870)])  # 點一下這個位置，會把FB登入頁切換成中文
    sleep(3)

    self.driver.find_element_by_xpath("//*[@text='手機號碼或電子郵件地址']").send_keys('s23321286@gmail.com')
    self.driver.find_element_by_xpath("//*[@text='密碼']").send_keys('Tvbs2020')
    print("輸入帳號密碼")
    sleep(1)
    self.driver.tap([(480, 1700)])  # click「登入」
    sleep(6)
    self.driver.tap([(480, 1650)])  # click「以xxx的身分繼續」，但如果不是第一次登，就不用此步驟
    # sleep(6)
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Title'))
    print("toast顯示：「完成登入」")

    sleep(3)

    # WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@text='我的']"))  #也未必一定回【我的頁】

    self.driver.find_element_by_xpath("//*[@text='我的']").click()
    print("進入【我的頁】")

    while True:
        if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_Logout') is False:
            self.driver.swipe(900, 1500, 900, 200)
            print("找不到「登出」鈕，滑1次")
        else:
            print('找到「登出」鈕，確定登入成功')
            break

# Freyja
# 【會員登入頁】完成Email登入，並檢查有登入成功
def emailLogin(self):

    if self.driver.find_elements_by_xpath("//*[@text='會員登入']"):

        # 定位帳號欄位
        account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
        # 定位密碼欄位
        password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
        # 輸入正確帳號密碼進行登入
        account_blank.send_keys('freyjachen0002@gmail.com')
        password_blank.send_keys('a123456')
        self.driver.find_element_by_xpath("//*[@text='登入']").click()

        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='首頁']"))
        print("toast顯示：「完成登入」")

        self.driver.find_element_by_xpath("//*[@text='我的']").click()
        print("進入【我的頁】")
    else:
        print("目前為已登入狀態，未開啟【會員登入頁】")

    while True:
        if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_Logout') is False:
            self.driver.swipe(900, 1500, 900, 200)
            print("找不到「登出」鈕，滑1次")
        else:
            print('找到「登出」鈕，確定登入成功')
            break

# Freyja
# 執行登出
def logoutApp(self):
    self.driver.find_element_by_xpath("//*[@text='我的']").click()
    print("進入【我的頁】")

    while True:
        if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_Logout') is False:
            self.driver.swipe(900, 1500, 900, 200)
            print("找不到「登出」鈕，滑1次")
        else:
            print('找到「登出」鈕')
            break

    # 驗證登出相關文字
    self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Logout').click()
    self.driver.implicitly_wait(10)
    dialog_text = self.driver.find_element_by_id('android:id/message').text
    self.assertEqual(dialog_text, '你確定要登出嗎？')
    print('登出跳出dialog : ' + dialog_text)
    confirm_btn_text = self.driver.find_element_by_id('android:id/button1').text
    self.assertEqual(confirm_btn_text, '含淚登出')
    print('確定登出按鈕wording : ' + confirm_btn_text)
    cancel_btn_text = self.driver.find_element_by_id('android:id/button2').text
    self.assertEqual(cancel_btn_text, '再想一下')
    print('取消登出按鈕wording : ' + cancel_btn_text)

    # 驗證登出相關行為
    self.driver.find_element_by_id('android:id/button2').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Logout'))
    print('取消登出按鈕功能正常')
    self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Logout').click()
    self.driver.implicitly_wait(10)
    self.driver.find_element_by_id('android:id/button1').click()
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Login'))
    print('確定登出按鈕功能正常')

# Freyja
# 【性別生日頁】UI檢查
def genderBirthdayPageUICheck(self):
    # 有「性別」項目代表已載入【生日性別頁】
    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='性別']"))
    print('\n開啟【生日性別頁】')

    # 檢查
    dialog_text = self.driver.find_elements_by_class_name('android.widget.TextView')[0].text
    self.assertEqual(dialog_text, '提供您的資料，讓我們可以不定期推送屬於您的內容與優惠喔~')
    print("有文字「提供您的資料，讓我們可以不定期推送屬於您的內容與優惠喔~」")

    dialog_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
    self.assertEqual(dialog_text, '性別')

    self.driver.find_element_by_xpath("//*[@text='性別']")
    print("有文字「性別」")

    # 判斷男性RadioButton預設是否已勾選
    male_radiobtn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rbMale')
    male_radiobtn_checked = male_radiobtn.is_selected()
    self.assertFalse(male_radiobtn_checked, '男性RadioButton預設已經被勾選! ')
    print('有RadioButton：男，預設為未勾選')

    # 判斷女性RadioButton預設是否已勾選
    female_radiobtn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rbFemale')
    female_radiobtn_checked = female_radiobtn.is_selected()
    self.assertFalse(female_radiobtn_checked, '女性RadioButton預設已經被勾選! ')  # 判斷女性RadioButton預設是否已勾選
    print('有RadioButton：女，預設為未勾選')

    # 判斷秘密RadioButton預設是否已勾選
    secret_radiobtn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rbSecret')
    secret_radiobtn_checked = secret_radiobtn.is_selected()
    self.assertFalse(secret_radiobtn_checked, '秘密RadioButton預設已經被勾選! ')  # 判斷女性RadioButton預設是否已勾選
    print('有RadioButton：秘密，預設為未勾選')

    self.driver.find_element_by_xpath("//*[@text='生日']")
    birthday_choice = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvBirthday')
    self.assertEqual(birthday_choice.text, '1983/01/01')
    print("有文字「生日」，預設值為1983/01/01")

    self.driver.find_element_by_xpath("//*[@text='不提供生日']")
    no_birthday_checkbox = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbNoBirthday')
    self.assertFalse(no_birthday_checkbox.is_selected(), 'Checkbox預設為已勾選狀態!')
    print("有Checkbox「不提供生日」，預設為未勾選")

    self.driver.find_element_by_xpath("//*[@text='我同意TVBS會員的服務條款及隱私權政策']")
    print("有文字「我同意TVBS會員的服務條款及隱私權政策」")

    next_button = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btNext')
    self.assertEqual(next_button.text, '下一步')
    self.assertTrue(next_button.is_enabled())
    print("有「下一步」button")

    self.driver.find_element_by_xpath("//*[@text='小提醒：']")
    print("有文字「小提醒：」")

    self.driver.find_element_by_xpath("//*[@text='＊如有填寫資料，送出後即無法更改']")
    print("有文字「＊如有填寫資料，送出後即無法更改」")

    self.driver.find_element_by_xpath("//*[@text='＊如未填寫資料，可於會員中心補填']")
    print("有文字「＊如未填寫資料，可於會員中心補填」")

    self.driver.find_element_by_xpath("//*[@text='＊填寫生日才能享有生日驚喜']")
    print("有文字「＊填寫生日才能享有生日驚喜」")

    # [0].text = 提供您的資料，讓我們可以不定期推送屬於您的內容與優惠喔~
    # [1].text = 性別
    # [2].text = 生日
    # [3].text = 1983/01/01
    # [4].text = 不提供生日
    # [5].text = 我同意TVBS會員的服務條款及隱私權政策
    # [6].text = 小提醒：
    # [7].text = ＊如有填寫資料，送出後即無法更改
    # [8].text = ＊如未填寫資料，可於會員中心補填
    # [9].text = ＊填寫生日才能享有生日驚喜

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
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'ce031713bc2694670d',  # S8+(8.0) : ce031713bc2694670d, HTC(9.0) NE9CF1S01374
            'appPackage': 'com.tvbs.supertastemvppack',
            'appActivity': 'com.tvbs.supertaste.ui.activity.SplashActivity',
            'autoGrantPermissions': True
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 連接Appium
        self.driver.implicitly_wait(8)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 底部tab檢查
    def test_bottomTabCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 檢查tab名稱
            index_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_featured')
            self.assertEqual(index_tab.get_attribute('content-desc'), '首頁')
            store_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_store')
            self.assertEqual(store_tab.get_attribute('content-desc'), '購物')
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            self.assertEqual(pocket_tab.get_attribute('content-desc'), '口袋')
            search_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_search')
            self.assertEqual(search_tab.get_attribute('content-desc'), '熱搜')
            member_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_member')
            self.assertEqual(member_tab.get_attribute('content-desc'), '我的')
            print('底部tab有「首頁」、「購物」、「口袋」、「熱搜」、「我的」')

            # # 檢查tab selected狀態
            # index_tab_selected = index_tab.is_selected()
            # self.assertTrue(index_tab_selected, '首頁icon經點選後未被填滿')  # 判斷首頁icon經點選後有無填滿
            # store_tab.click()
            # self.driver.implicitly_wait(3)
            # store_tab_selected = store_tab.is_selected()
            # self.assertTrue(store_tab_selected, '購物icon經點選後未被填滿')  # 判斷購物icon經點選後有無填滿
            # search_tab.click()
            # self.driver.implicitly_wait(3)
            # search_tab_selected = search_tab.is_selected()
            # self.assertTrue(search_tab_selected, '熱搜icon經點選後未被填滿')  # 判斷熱搜icon經點選後有無填滿
            # member_tab.click()
            # self.driver.implicitly_wait(3)
            # member_tab_selected = member_tab.is_selected()
            # self.assertTrue(member_tab_selected, '我的icon經點選後未被填滿')  # 判斷我的icon經點選後有無填滿
            # print('Tab Bar icon經點選後有被填滿')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【首頁】搖一搖
    def test_indexShake(self):
        # # 網頁自動化設定
        # chrome_path = 'C:/workspace/selenium_driver_chrome/chromedriver.exe'
        # self.chrome_driver = chrome_driver.Chrome(chrome_path)
        # self.chrome_driver.maximize_window()
        #
        # # 後台 - 頭條管理
        # self.chrome_driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
        # self.chrome_driver.maximize_window()
        # self.chrome_driver.implicitly_wait(6)
        # login_adm_name = self.chrome_driver.find_element_by_id('login_adm_name')
        # login_adm_pw = self.chrome_driver.find_element_by_id('login_adm_pw')
        # login_adm_name.send_keys('jacktsao')
        # login_adm_pw.send_keys('TVBS2020')
        # self.chrome_driver.find_element_by_xpath("//input[@value='登入']").click()
        # self.chrome_driver.implicitly_wait(6)
        #
        # # 新開一個視窗，通過執行js來新開一個視窗
        # js = 'window.open("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_app_activities");'
        # self.chrome_driver.execute_script(js)
        #
        # # 獲取當前視窗控制代碼集合（列表型別）
        # handles = self.chrome_driver.window_handles
        # self.chrome_driver.switch_to.window(handles[-1])
        # time.sleep(2)
        #
        # add_page_btn = self.chrome_driver.find_element_by_id('add_page')
        # add_page_btn.click()
        #
        # title = self.chrome_driver.find_element_by_id('title')
        # url = self.chrome_driver.find_element_by_id('url')
        # link = self.chrome_driver.find_element_by_id('link')
        # released = self.chrome_driver.find_element_by_id('released')
        # end = self.chrome_driver.find_element_by_id('end')
        # save = self.chrome_driver.find_element_by_id('save')
        #
        # now = datetime.datetime.now()
        # delta = datetime.timedelta(seconds=10)
        # new_time = (now + delta).strftime('%Y/%m/%d %H:%M:%S')
        # title.send_keys('Automation ' + new_time)
        # url.send_keys('https://supertaste.tvbs.com.tw/')
        # link.send_keys('/program_piwigo/piwigo/upload/2020/05/22/20200522214613-422e6a1d.jpg')
        # released.clear()
        # released.send_keys(new_time)
        # end.clear()
        # end.send_keys('2020/12/31 12:00:00')
        # save.click()
        # self.chrome_driver.switch_to.alert.accept()

        # 新手教學
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            print('350')
            # 關掉【新手教學頁】
            init(self)
            print('353')
            # 搖一搖
            print('\n=======搖一搖=======')
            shake_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_shake')
            shake_btn.click()
            print('358')
            # # 定位帳號欄位
            # account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            # # 定位密碼欄位
            # password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            # # 帳號欄位傳值
            # account_blank.send_keys('s0932748681@gmail.com')
            # # 密碼欄位傳值
            # password_blank.send_keys('s23321286')
            # self.driver.find_element_by_xpath("//*[@text='登入']").click()

            # 【會員登入頁】完成Email登入，並檢查有登入成功
            emailLogin(self)
            print('371')
            self.driver.find_element_by_xpath("//*[@text='首頁']").click()
            print('373')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/iv_shake'))
            shake_btn.click()
            print('372')
            if self.is_element_exist('android:id/message') is True:
                print('搖一搖目前沒活動')
                self.driver.find_element_by_id('android:id/button1').click()
            else:
                print('377')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Shake_Background'))
                print('379')
                self.driver.shake() #這裡會error(2021.04.20)
                # 網頁自動化設定
                chrome_path = 'C:/workspace/selenium_driver_chrome/chromedriver.exe'
                self.chrome_driver = chrome_driver.Chrome(chrome_path)

                # 後台 - 頭條管理
                self.chrome_driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
                self.chrome_driver.implicitly_wait(6)
                login_adm_name = self.chrome_driver.find_element_by_id('login_adm_name')
                login_adm_pw = self.chrome_driver.find_element_by_id('login_adm_pw')
                login_adm_name.send_keys('jacktsao')
                login_adm_pw.send_keys('TVBS2020')
                self.chrome_driver.find_element_by_xpath("//input[@value='登入']").click()
                self.chrome_driver.implicitly_wait(6)

                # 新開一個視窗，通過執行js來新開一個視窗
                js = 'window.open("http://2017back-pre.tvbs.com.tw/index.php/program_supertaste/supertaste_shake");'
                self.chrome_driver.execute_script(js)

                # 獲取當前視窗控制代碼集合（列表型別）
                handles = self.chrome_driver.window_handles
                self.chrome_driver.switch_to.window(handles[-1])
                web_shake_title = self.chrome_driver.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[3]').text
                web_shake_content = self.chrome_driver.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[4]').text
                print('搖一搖目前有活動')
                shake_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Title').text
                shake_content = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Content').text
                self.assertEqual(web_shake_title, shake_title)
                print('後台設定與前台顯示標題一樣為 : ' + shake_title)
                self.assertEqual(web_shake_content, shake_content)
                print('後台設定與前台顯示內文一樣為 : ' + shake_content)
                self.driver.back()

            # 輪播圖
            banner = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')
            banner.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))
            self.driver.back()
            print('\n=======Banner=======')
            print('跳轉Banner正常')

            # 節目即時看
            print('\n=======節目即時看=======')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title')[3])
            channel_watch = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[3]
            channel_watch_text = channel_watch.text
            print('節目即時看文章標題為 :' + channel_watch_text)
            channel_watch.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))
            direct_channel_watch_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            print('節目即時看跳轉文章標題為 :' + direct_channel_watch_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))
            channel_watch_pic = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            channel_watch_pic.click()
            print('點選圖片可跳轉' + direct_channel_watch_text)
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))

            # 來討論
            print('\n=======來討論=======')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/llMessage').click()
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_class_name(
                'android.widget.EditText'))
            print('來討論跳轉正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivBack').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/llMessage'))

            # 去分享
            print('\n=======去分享=======')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/llShare').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/title'))
            print('去分享跳轉正常')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/llMessage'))

            # 藏口袋
            print('\n=======藏口袋=======')
            # 點選收藏
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').text
            self.assertEqual(collect_btn_text, '藏口袋')
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 判斷愛心有無填滿
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
            print('收藏文章後愛心有填滿')

            # 判斷收藏按鈕文字變化
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            collected_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            self.assertEqual(collected_btn.text, '已收藏')
            print('收藏按鈕文字變化正確 ')

            # 取消收藏
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
            print('取消收藏文章後愛心沒有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 再次收藏
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            article_title = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/smallLabel'))

            # 返回收藏頁面
            self.driver.find_element_by_xpath("//*[@text='口袋']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))
            news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            news_tab.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more_article'))
            collected_article_title = self.driver.find_elements_by_class_name('android.widget.TextView')[4].text
            self.assertEqual(article_title, collected_article_title)
            print('已收藏的標題為 : ' + collected_article_title)
            print('確認為剛剛收藏的文章標題，收藏文章功能正常。')

            # 刪除收藏
            action = TouchAction(self.driver)  # 創建TouchAction物件
            action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
            action.perform()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
            self.driver.find_element_by_id('android:id/button1').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 節目即時看下方店家資訊
            print('\n=======節目即時看下方店家資訊=======')
            self.driver.swipe(900, 730, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collect_store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 判斷愛心有無填滿
            collect_store_checked = bool(collect_store.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            print('收藏下方店家後愛心有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 取消收藏
            collect_store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collect_store_checked = bool(collect_store.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "取消收藏後愛心仍有填滿!")
            print('取消收藏下方店家後愛心沒有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 節目即時看下方店家跳轉
            store_title = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            print('節目即時看下方店家: ' + store_title)
            store = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            direct_store_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.assertEqual(store_title, direct_store_title)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            print('節目即時看下方店家跳轉正常')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_more'))

            # # More
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_more').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            # self.assertTrue(channel_tab.is_selected(), '未跳轉至節目頁')  # 判斷More按鈕
            # print('More按鈕功能正常')
            #
            # # 資訊卡
            # print('\n=======資訊卡=======')
            # index_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[0]
            # index_tab.click()
            # sleep(5)
            # self.driver.swipe(900, 1400, 900, 300)
            # info_card = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            # info_card.click()
            # print('資訊卡跳轉功能正常')
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # sleep(5)
            #
            # # 推薦商品
            # print('\n=======推薦商品=======')
            # self.driver.swipe(900, 1200, 900, 300)
            # item = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')
            # item.click()
            # WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))  # 未來要改
            # self.driver.back()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # print('推薦商品跳轉功能正常')
            #
            # # 節目
            # print('\n=======分頁跳轉=======')
            # channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            # channel_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(channel_tab.is_selected(), '未跳轉至節目頁')
            # print('跳轉至節目頁正常')
            #
            # # 好喝
            # drink_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[2]
            # drink_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(drink_tab.is_selected(), '未跳轉至好喝頁')
            # print('跳轉至好喝頁正常')
            #
            # # 熱門
            # hot_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[3]
            # hot_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(hot_tab.is_selected(), '未跳轉至熱門頁')
            # print('跳轉至熱門頁正常')
            #
            # # 美食
            # foods_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[3]
            # foods_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(foods_tab.is_selected(), '未跳轉至美食頁')
            # print('跳轉至美食頁正常')
            #
            # # 旅行
            # travel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[4]
            # travel_tab.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.assertTrue(travel_tab.is_selected(), '未跳轉至旅行頁')

        except:
            flag = False
            if flag is False or Exception or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/index_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

        # com.tvbs.supertastemvppack: id / iv_more
        # # 後台新增美食資訊卡
        # self.chrome_driver.get('http://2017back-pre.tvbs.com.tw/index.php/admission_list')
        # self.chrome_driver.maximize_window()
        # self.chrome_driver.implicitly_wait(6)
        # login_adm_name = self.chrome_driver.find_element_by_id('login_adm_name')
        # login_adm_pw = self.chrome_driver.find_element_by_id('login_adm_pw')
        # login_adm_name.send_keys('jacktsao')
        # login_adm_pw.send_keys('TVBS2020')
        # self.chrome_driver.find_element_by_xpath("//input[@value='登入']").click()
        # sleep(3)
        # js = "var action=document.documentElement.scrollTop=10000"
        # self.chrome_driver.execute_script(js)
        # self.chrome_driver.implicitly_wait(3)
        # self.chrome_driver.find_element_by_xpath('/html/body/div/div/div/ul/li[17]/span').click()
        # self.chrome_driver.implicitly_wait(3)
        # self.chrome_driver.find_element_by_link_text('景點管理').click()
        # sleep(3)

    def test_hotRecommend(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 節目
            print('\n=======熱門推薦=======')
            channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            channel_tab.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.assertTrue(channel_tab.is_selected(), '未跳轉至節目頁')
            print('跳轉至節目頁正常')

            # 文章
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel').click()
            sleep(3)
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_tip') is False:
                    self.driver.swipe(900, 1300, 900, 300)
                else:
                    self.driver.swipe(900, 1300, 900, 300)
                    break
            date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
            datetime.datetime.strptime(date_time, '%Y/%m/%d')
            print('文章時間格式正確')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel').click()
            print('熱門推薦文章跳轉正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/hotRecommend_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_relatedNews(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 資訊卡
            self.driver.swipe(900, 1400, 900, 600)
            info_card = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/iv_channel')[1]
            info_card.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            self.driver.swipe(900, 1400, 900, 600)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
            datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
            print('\n=======相關報導=======')
            print('文章縮圖時間格式正確')
            related_news = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            related_news.click()
            print('相關報導跳轉正常')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_author').text
            datetime.datetime.strptime(date_time, '%Y/%m/%d %H:%M')
            print('文章時間格式正確')

            # 藏口袋
            # 點選收藏
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').text
            self.assertEqual(collect_btn_text, '藏口袋')
            collect_article.click()
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))

            # 判斷愛心有無填滿
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
            print('收藏文章後愛心有填滿')

            # 判斷收藏按鈕文字變化
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            collected_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            self.assertEqual(collected_btn.text, '已收藏')
            print('收藏按鈕文字變化正確 ')

            # 取消收藏
            collect_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent')
            collect_article_checked = bool(collect_article.get_attribute("checked"))
            self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
            print('取消收藏文章後愛心沒有填滿')
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # # 返回收藏頁面
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/smallLabel'))
            # self.driver.find_element_by_xpath("//*[@text='口袋']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
            #     'com.tvbs.supertastemvppack:id/btn_more'))
            # news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            # news_tab.click()

            # # 確認無收藏
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/relatedNews_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_collectSearch(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            sleep(2)

            # 節目即時看下方店家資訊
            print('\n=======收藏驗證=======')
            self.driver.swipe(900, 730, 900, 200)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collect_store.click()
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            collect_store.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            # 判斷愛心有無填滿
            collect_store_checked = bool(collect_store.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))

            #  搜尋節目即時看下方店家名稱
            store_name = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            self.driver.find_element_by_xpath("//*[@text='熱搜']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/icon_search'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '已收藏')
            print('搜尋已收藏的節目即時看下方店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '藏口袋')
            print('搜尋未收藏的節目即時看下方店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='首頁']").click()
            sleep(3)

            # 搜尋資訊卡店家名稱
            self.driver.swipe(900, 1400, 900, 300)
            info_card = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            info_card.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            store_name = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='熱搜']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/icon_search'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '已收藏')
            print('搜尋已收藏的資訊卡店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(store_name)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            self.assertEqual(collect_btn_text, '藏口袋')
            print('搜尋未收藏的資訊卡店家收藏按鈕文字 : ' + collect_btn_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='首頁']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))

            # 文章底部功能列
            channel_tab = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1]
            channel_tab.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            article_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollectionContent').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_xpath("//*[@text='熱搜']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/icon_search'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(article_title[0:4])
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                'android.support.v7.app.ActionBar$Tab'))
            self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1].click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            status = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            status_checked = bool(status.get_attribute("checked"))
            self.assertTrue(status_checked, '收藏後仍未填滿')
            print('搜尋已收藏的文章收藏按鈕有填滿')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').send_keys(article_title[0:4])
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name(
                'android.support.v7.app.ActionBar$Tab'))
            self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[1].click()
            self.assertFalse(status.is_selected(), '取消收藏後仍填滿')
            print('搜尋未收藏的文章收藏按鈕未填滿')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/collectSearch_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 改成註冊頁面欄位檢查
    def test_memberCenterRegisterPageCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            self.driver.find_element_by_xpath("//*[@text='我還沒有TVBS帳號，註冊去']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))
            # 註冊帳號欄位
            register_account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            register_account_blank_text = register_account_blank.text
            # 註冊密碼欄位
            register_password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            register_password_blank_text = register_password_blank.text
            # 確認密碼欄位
            password_confirm_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWordCheck')
            password_confirm_blank_text = password_confirm_blank.text
            # # checkbox
            # notification_checkbox = self.driver.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/cbNotification')
            # notification_checkbox_checked = bool(notification_checkbox.get_attribute("checked"))
            #
            # # 註冊欄位驗證
            # self.assertEqual(register_account_blank_text, '請輸入註冊Email')  # 判斷欄位placeholder
            # print('\n註冊帳號欄位placeholder為 : ' + register_password_blank_text)
            # self.assertEqual(register_password_blank_text, '請設定密碼(6~12個英數字)')  # 判斷欄位placeholder
            # print('註冊密碼欄位placeholder為 : ' + register_password_blank_text)
            # self.assertEqual(password_confirm_blank_text, '請再次輸入密碼')  # 判斷欄位placeholder
            # print('註冊密碼欄位placeholder為 : ' + password_confirm_blank_text)
            # self.assertTrue(notification_checkbox_checked, 'Checkbox預設並未勾選! ')  # 判斷Checkbox預設是否已勾選
            # print('Checkbox預設為已勾選')
            #
            # # 判斷Checkbox預設是否已勾選
            # notification_checkbox = self.driver.find_element_by_class_name('android.widget.CheckBox')
            # notification_checkbox.click()
            # self.assertFalse(notification_checkbox.is_selected(), 'Checkbox點擊後仍為勾選狀態!')
            # print('Checkbox點擊後可取消勾選狀態')
            # self.driver.implicitly_wait(3)
            #
            # # 不輸入Email、密碼、確認密碼註冊
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入Email、密碼、確認密碼')
            # print('不輸入Email、密碼、確認密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            #
            # # 不輸入密碼、確認密碼註冊
            # register_account_blank.send_keys('tvbstest')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入密碼、確認密碼')
            # print('不輸入密碼、確認密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            #
            # # 不輸入Email、密碼註冊
            # password_confirm_blank.send_keys('tvbstest')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入Email、密碼')
            # print('不輸入Email、密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # password_confirm_blank.clear()
            #
            # # 不輸入Email、確認密碼註冊
            # register_password_blank.send_keys('tvbstest')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入Email、確認密碼')
            # print('不輸入Email、確認密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_password_blank.clear()
            #
            # # 不輸入確認密碼註冊
            # register_account_blank.send_keys('tvbstest')
            # register_password_blank.send_keys('tvbstest')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入確認密碼')
            # print('不輸入確認密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            # register_password_blank.clear()
            #
            # # 不輸入Email註冊
            # register_password_blank.send_keys('tvbstest')
            # password_confirm_blank.send_keys('tvbstest')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入Email')
            # print('不輸入Email註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_password_blank.clear()
            # password_confirm_blank.clear()
            #
            # # 不輸入密碼註冊
            # register_account_blank.send_keys('tvbstest')
            # password_confirm_blank.send_keys('tvbstest')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '請輸入密碼')
            # print('不輸入密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_password_blank.clear()
            # password_confirm_blank.clear()
            #
            # # 輸入不一樣密碼、確認密碼註冊
            # register_account_blank.send_keys('tvbstest@gmail.com')
            # register_password_blank.send_keys('tvbstest1')
            # password_confirm_blank.send_keys('tvbstest2')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '密碼與確認密碼不符，請重新確認！')
            # print('輸入不一樣密碼、確認密碼註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            # register_password_blank.clear()
            # password_confirm_blank.clear()
            #
            # # 輸入不符合密碼、確認密碼規則註冊
            # register_account_blank.send_keys('tvbstest@gmail.com')
            # register_password_blank.send_keys('tvbstvbs')
            # password_confirm_blank.send_keys('tvbstvbs')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '密碼建議為 6~12 位數，必須是英文數字混合！')
            # print('輸入不符合密碼、確認密碼規則註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            # register_password_blank.clear()
            # password_confirm_blank.clear()
            #
            # # 輸入已註冊為TVBS會員的帳號註冊
            # register_account_blank.send_keys('s0932748681@gmail.com')
            # register_password_blank.send_keys('tvbstvbs123')
            # password_confirm_blank.send_keys('tvbstvbs123')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '此帳號已透過 Email 註冊為會員！')
            # print('輸入已註冊為TVBS會員的帳號註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            # register_password_blank.clear()
            # password_confirm_blank.clear()
            #
            # # 輸入已註冊為FB會員的帳號註冊
            # register_account_blank.send_keys('s23321286@gmail.com')
            # register_password_blank.send_keys('tvbstvbs123')
            # password_confirm_blank.send_keys('tvbstvbs123')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '此帳號已透過 FB 註冊為會員！')
            # print('輸入已註冊為FB會員的帳號註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            # register_password_blank.clear()
            # password_confirm_blank.clear()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterRegisterPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_hotSearch(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 熱搜
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_search').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_keyword'))
            search_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search')
            search_blank_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/edit_search').text
            self.assertEqual(search_blank_text, '請搜尋你感興趣的內容')  # 判斷欄位placeholder
            print('\n=======元件判斷=======')
            print('搜尋欄位placeholder為 : ' + search_blank_text)

            # 判斷搜尋無結果
            search_blank.send_keys('qaz')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            sleep(3)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_searcherror'))
            no_result_text = self.driver.find_elements_by_class_name('android.widget.TextView')[4].text
            self.assertEqual(no_result_text, '查無相關內容，換個關鍵字試試吧！')
            print('搜尋無結果顯示wording為 :', no_result_text)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/search_cancel'))
            search_cancel = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/search_cancel')
            search_cancel.click()

            # 自定義搜尋
            search_blank.send_keys('早午')
            search_cancel.click()
            search_blank.send_keys('早午')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            sleep(3)
            search_keyword = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            self.assertEqual(search_keyword, '早午')  # Title：顯示搜尋關鍵字名稱
            print('Title有顯示搜尋關鍵字名稱')

            # Tab bar驗證
            store_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
            item_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[3].text
            self.assertEqual(store_tab[0:3], '找店家')
            self.assertEqual(news_tab[0:3], '看報導')
            self.assertEqual(item_tab[0:3], '買東西')
            print('搜尋Tab文字為 : ' + store_tab[0:3] + '、' + news_tab[0:3] + '、' + item_tab[0:3])
            print('搜尋Tab文字正確')
            print('=======找店家=======')

            # 搜尋 - 判斷打電話btn
            phone_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_phone')
            if phone_btn.is_enabled() is True:
                phone_btn.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.asus.contacts:id/dialButton'))
                self.driver.back()
                print('該店家有電話且可撥打')
            else:
                print('該店家沒電話且按鈕反灰')

            # 搜尋 - 判斷看路線btn
            map_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_map')
            if map_btn.is_enabled() is True:
                map_btn.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.google.android.apps.maps:id/search_omnibox_menu_button'))
                self.driver.back()
                print('該店家有地址且可導航')
            else:
                print('該店家沒地址且按鈕反灰')

            # 自定義搜尋 - 收藏店家
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collection_btn.click()
            self.driver.implicitly_wait(3)
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            click_collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            self.assertEqual(click_collection_btn.text, '已收藏')
            print('收藏店家後按鈕文字變為 : ' + collection_btn.text)
            collect_store_checked = bool(collection_btn.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            print('搜尋店家收藏功能正常')
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))

            # 自定義搜尋 - 找店家跳轉
            article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            article_text = article.text
            print('自定義搜尋店家為 : ' + article_text)
            article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/cbCollectionContent'))
            direct_article = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            direct_article_text = direct_article.text
            print('自定義搜尋跳轉店家為 : ' + direct_article_text)
            self.assertEqual(article_text, direct_article_text)
            print('自定義搜尋店家功能正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))

            # 自定義搜尋 - 看報導
            print('=======看報導=======')
            search_news_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            search_news_tab.click()
            # 顯示：主圖、標題、日期、收藏
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title')[1])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))
            print('看報導主圖、標題、日期、收藏有正常顯示')

            # 自定義搜尋 - 收藏報導
            collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            collection_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            collection_btn.click()
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_date'))
            collect_store_checked = bool(collection_btn.get_attribute("checked"))
            self.assertTrue(collect_store_checked, "收藏後愛心未填滿!")
            print('搜尋報導收藏功能正常')
            collection_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/cbCollection'))

            # 自定義搜尋 - 看報導跳轉
            search_news_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            search_news_article_text = search_news_article.text
            print('自定義搜尋報導為 : ' + search_news_article_text)
            search_news_article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('android.widget.TextView'))
            direct_search_news_article = self.driver.find_elements_by_class_name('android.widget.TextView')[1]
            direct_search_news_article_text = direct_search_news_article.text
            print('自定義搜尋跳轉報導為 : ' + direct_search_news_article_text)
            self.assertEqual(search_news_article_text, direct_search_news_article_text)
            print('自定義搜尋報導功能正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/navigation_search'))

            # 自定義搜尋 - 買東西跳轉
            print('=======買東西=======')
            search_blank.send_keys('芒果')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            sleep(3)
            search_item_tab = self.driver.find_elements_by_class_name('android.widget.TextView')[3]
            search_item_tab.click()
            item_keyword = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            print('此次搜尋 : ' + item_keyword)
            search_item = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            search_item_text = search_item.text
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title')[1])
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_discount'))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_price'))
            print('買東西主圖、標題、原價、特價有正常顯示')
            print('自定義搜尋商品為 : ' + search_item_text)
            search_item.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='購物首頁']"))
            print('搜尋商品進入EC頁面成功')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/search_cancel'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/search_cancel').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_keyword'))
            # direct_search_item = self.driver.find_elements_by_id('store_title')[1]
            # direct_search_item_text = direct_search_item.text
            # print('自定義搜尋跳轉商品為 : ' + direct_search_item_text)
            # self.assertEqual(search_item_text, direct_search_item_text)
            # print('自定義搜尋商品功能正常')
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/action_icon'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/navigation_search'))

            # # 推薦搜尋
            # search_autocomplete = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_list_autocom')
            # search_autocomplete.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/cbCollection'))
            # article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            # article_text = article.text
            # print('推薦搜尋文章標題為 : ' + article_text)
            # article.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # direct_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')
            # direct_article_text = direct_article.text
            # print('推薦搜尋跳轉文章標題為 : ' + article_text)
            # self.assertEqual(article_text, direct_article_text)
            # print('推薦搜尋功能正常')
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/action_icon'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/navigation_search'))
            # search_cancel.click()

            # 熱門搜尋
            print('=======熱門搜尋=======')
            keyword_search = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_keyword')
            keyword_search_text = keyword_search.text[1:]
            print('熱門搜尋文章標籤為 : ' + keyword_search_text)
            keyword_search.click()
            keyword_search_title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            print('跳轉搜尋文章標籤為 : ' + keyword_search_title)
            self.assertEqual(keyword_search_text, keyword_search_title)
            print('熱門搜尋引導正確')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/recyclerView_history'))

            # 歷史搜尋
            print('=======歷史搜尋=======')
            self.driver.find_element_by_xpath("//*[@text='#早午']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            article_text = article.text
            print('歷史搜尋文章標題為 : ' + article_text)
            article.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            direct_article = self.driver.find_elements_by_class_name('android.widget.TextView')[2]
            direct_article_text = direct_article.text
            print('歷史搜尋跳轉標題為 : ' + article_text)
            self.assertEqual(article_text, direct_article_text)
            print('歷史搜尋功能正常')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/navigation_search'))

            # 刪除歷史紀錄
            delete_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_delete')
            delete_btn.click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/recyclerView_history'))  # 判斷歷史紀錄消失
            print('刪除歷史紀錄功能正常')

            # 自定義搜尋關閉網路
            print('=======網路狀態=======')
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            search_blank.send_keys('早午')
            search_blank.click()
            self.driver.press_keycode(66)  # 鍵盤ENTER
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('自定義搜尋關閉網路功能正常')

            # 自定義搜尋開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('自定義搜尋開啟網路功能正常')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/search_cancel'))
            search_cancel.click()

            # # 推薦搜尋關閉網路
            # search_blank.send_keys('早午')
            # self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            # search_autocomplete.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/btn_retry'))
            # print('推薦搜尋關閉網路功能正常')
            #
            # # 推薦搜尋開啟網路
            # self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            # sleep(3)
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_title'))
            # print('推薦搜尋開啟網路功能正常')
            # self.driver.back()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/search_cancel'))
            # search_cancel.click()

            # 熱門搜尋關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            keyword_search.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('熱門搜尋關閉網路功能正常')

            # 熱門搜尋開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('熱門搜尋開啟網路功能正常')
            self.driver.back()

            # 歷史搜尋關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            self.driver.find_element_by_xpath("//*[@text='#早午']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('歷史搜尋關閉網路功能正常')

            # 歷史搜尋開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('歷史搜尋開啟網路功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/hotSearch_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_profileEdit(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 個人資料
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            profile = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member')
            profile.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount'))

            # 登入TVBS
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('s0932748681@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_member'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/rl_modifyPhoto'))

            # 大頭貼
            # photo = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyPhoto')
            # photo.click()

            # # 拍照
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/b_takePic').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.asus.camera:id/button_capture'))
            # self.driver.tap([(540, 1800)])
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.asus.camera:id/button_used'))
            # self.driver.find_element_by_id('com.asus.camera:id/button_used').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/btn_confirm'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_confirm').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/rl_modifyPhoto'))
            #
            # # 相簿
            # photo.click()
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/b_choosePic').click()
            # 490 320
            # 修改基本資料
            modify_data = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyData')
            modify_data.click()
            nickname = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyData')
            nickname.click()
            random_nickname = random.choice('abcdefg') + str(random.randint(0, 9999))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyPhoto').send_keys(random_nickname)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_save').click()
            # # 修改密碼
            # modify_password = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_modifyPassWord')
            # modify_password.click()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/profileEdit_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_myCollection(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 我的收藏
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_my_collection').click()
            self.driver.implicitly_wait(3)

            # 登入TVBS
            # 定位帳號欄位
            account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            # 定位密碼欄位
            password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            # 帳號欄位傳值
            account_blank.send_keys('mybooktest0604@gmail.com')
            # 密碼欄位傳值
            password_blank.send_keys('s23321286')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tv_Title'))

            # 收藏頁面
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_my_collection').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))

            # 關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_retry'))
            print('\n=======網路狀態=======')
            print('我的收藏關閉網路功能正常')

            # 開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(4)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()
            # 判斷有無推薦店家
            if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_channel') is False:
                print('我的收藏開啟網路功能正常')
                print('=======找店家=======')
                print('當前無推薦店家')
                self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[2])
            # 點選收藏
            else:
                print('我的收藏開啟網路功能正常')
                print('=======找店家=======')
                title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
                self.assertEqual(title_text, '更多店家推薦')
                store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
                collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
                self.assertEqual(collect_btn_text, "藏口袋")  # 判斷未收藏按鈕文字
                print('收藏店家為 : ' + store_text)
                collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                collect_article.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collected_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
                self.assertEqual(collected_btn_text, "已收藏")  # 判斷已收藏按鈕文字
                print('收藏按鈕文字變化正確 : ' + collect_btn_text + '->' + collected_btn_text)
                collect_people_count = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_count').text
                collect_people_desc = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_desc').text
                print(collect_people_count + collect_people_desc)

                # 判斷愛心有無填滿
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
                print('收藏後愛心有填滿')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                collect_article.click()  # 取消收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))

                collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
                print('取消收藏後愛心沒有填滿')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article.click()  # 再次收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                self.driver.back()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))

                # 返回收藏頁面
                collected_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
                self.assertEqual(store_text.replace(" ", ""), collected_store_text.replace(" ", ""))
                print('已收藏的店家為 : ' + collected_store_text)
                print('確認為剛剛收藏的店家，收藏功能正常。')

                # # 更多文章收藏
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
                # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
                # more_article.click()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/action_icon'))
                # sleep(3)
                # for i in range(3):
                #     self.driver.swipe(900, 1500, 900, 300)
                #     sleep(1)
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/cbCollection'))
                # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article.click()  # 收藏推薦文章的第二篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                # sleep(3)
                # print('更多文章收藏功能正常')

                # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article[3].click()  # 收藏推薦文章的第四篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.back()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # print('更多文章收藏功能正常')

                # 收藏店家跳轉
                collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
                collect_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
                print('要跳轉的店家為 : ' + collect_store_text)
                collect_store.click()

                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                      'com.tvbs.supertastemvppack:id/iv_img'))
                direct_store_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
                self.assertEqual(collect_store_text.replace(" ", ""), direct_store_text.replace(" ", ""))  # 去除空白
                print('跳轉後的店家為 : ' + direct_store_text)
                self.driver.back()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))
                print('收藏店家跳轉功能正常')

                # 判斷已收藏數量正不正確
                store_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
                self.assertEqual(store_amount, '找店家 1')
                print('店家收藏數量正確')

                # 刪除收藏
                action = TouchAction(self.driver)  # 創建TouchAction物件
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                dialog_text = self.driver.find_element_by_id('android:id/message').text
                self.assertEqual(dialog_text, '確認刪除?')
                print('長按收藏店家可跳出刪除訊息')

                # 取消刪除收藏
                self.driver.find_element_by_id('android:id/button2').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))
                print('取消刪除收藏店家功能正常')

                # 確定刪除收藏
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                self.driver.find_element_by_id('android:id/button1').click()
                # 判斷刪除後數量是否有減少
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='找店家 0']"))
                print('確定刪除收藏功能正常')

                # 空收藏
                # action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                # action.perform()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                # self.driver.find_element_by_id('android:id/button1').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/btn_more'))
                print('確定刪除所有收藏店家後會顯示"錯過那些必踩點?"按鈕')

            # 看報導
            print('=======看報導=======')
            self.driver.find_elements_by_class_name('android.widget.TextView')[2].click()
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/cl_main') is True:
                    action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                    action.perform()
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                    self.driver.find_element_by_id('android:id/button1').click()
                else:
                    break
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/action_icon'))
            title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
            self.assertEqual(title_text, '更多報導推薦')
            # 判斷有無推薦報導
            if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_date') is False:
                print('當前無推薦報導')
                self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name(
                    'android.support.v7.app.ActionBar$Tab')[2])
            else:
                date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
                datetime.datetime.strptime(date_time, '%Y/%m/%d')
                print('文章時間格式正確')
                article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
                print('收藏的報導標題為 : ' + article_text)

                # 點選收藏
                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
                collect_article.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))

                # 判斷愛心有無填滿
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
                print('收藏後愛心有填滿')
                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
                collect_article.click()  # 取消收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/cbCollection'))

                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
                collect_article_checked = bool(collect_article.get_attribute("checked"))
                self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
                print('取消收藏後愛心沒有填滿')
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article.click()  # 再次收藏
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                collect_article2 = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[3]
                collect_article2.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                self.driver.back()

                # 返回收藏頁面
                collected_article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
                self.assertEqual(article_text, collected_article_text)
                print('已收藏的報導為 : ' + collected_article_text)
                print('確認為剛剛收藏的報導，收藏功能正常。')

                # # 更多文章收藏
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
                # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
                # more_article.click()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/action_icon'))
                # sleep(3)
                # for i in range(3):
                #     self.driver.swipe(900, 1500, 900, 300)
                #     sleep(1)
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/cbCollection'))
                # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article.click()  # 收藏推薦文章的第二篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
                # sleep(3)
                # print('更多文章收藏功能正常')

                # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
                # collect_article[3].click()  # 收藏推薦文章的第四篇文章
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # self.driver.back()
                # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                #     'com.tvbs.supertastemvppack:id/tv_title'))
                # print('更多文章收藏功能正常')

                # 收藏報導跳轉
                collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
                collect_article_text = collect_article.text
                print('要跳轉的報導為 : ' + collect_article_text)
                collect_article.click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                direct_article_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
                self.assertEqual(collect_article_text, direct_article_text)
                print('跳轉後的報導為 : ' + direct_article_text)
                self.driver.back()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/iv_channel'))
                print('收藏報導跳轉功能正常')

                # 判斷已收藏數量正不正確
                article_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
                self.assertEqual(article_amount, '看報導 2')
                print('報導收藏數量正確')

                # 刪除收藏
                action = TouchAction(self.driver)  # 創建TouchAction物件
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cl_main')[0])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                dialog_text = self.driver.find_element_by_id('android:id/message').text
                self.assertEqual(dialog_text, '確認刪除?')
                print('長按收藏報導可跳出刪除訊息')

                # 取消刪除收藏
                self.driver.find_element_by_id('android:id/button2').click()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/tv_title'))
                print('取消刪除報導收藏功能正常')

                # 確定刪除收藏
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                self.driver.find_element_by_id('android:id/button1').click()
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_xpath("//*[@text='看報導 1']"))  # 判斷刪除後數量是否有減少

                # 空收藏
                action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
                action.perform()
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
                self.driver.find_element_by_id('android:id/button1').click()
                WebDriverWait(self.driver, 20).until(
                    lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))  # 判斷刪除後數量是否有減少
                WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                    'com.tvbs.supertastemvppack:id/btn_more'))
                print('確定刪除所有收藏店家後會顯示"大家在夯什麼?"按鈕')

            # 買東西
            print('=======買東西=======')
            self.driver.find_elements_by_class_name('android.widget.TextView')[3].click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btn_more'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_channel'))
            title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
            self.assertEqual(title_text, '更多商品推薦')
            item = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            print('收藏的商品為 :' + item.text)
            item.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='購物首頁']"))
            print('進入EC商城')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/myCollection_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_myNotification(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 我的通知 - 文章
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_my_notifications').click()
            self.driver.implicitly_wait(3)
            notification = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
            notification_text = notification.text

            # 判斷日期排序
            first_date = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_date')[0].text
            second_date = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_date')[1].text
            if first_date >= second_date:
                print('\n' + first_date + ' 大於等於 ' + second_date + ' : 文章日期排序正確')
            else:
                print(first_date + ' 小於 ' + second_date + ' : 文章日期排序錯誤')
                assert False

            # 關閉網路
            self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            notification.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/button1'))
            print('\n我的通知關閉網路功能正常')

            # 開啟網路
            self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
            sleep(4)
            self.driver.find_element_by_id('android:id/button1').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_id(
                'com.tvbs.supertastemvppack:id/tv_title'))
            print('我的通知開啟網路功能正常')

            # 判斷通知文章標題
            print('我的通知文章標題為 : ' + notification_text)
            direct_article_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            self.assertEqual(notification_text, direct_article_text)
            print('跳轉通知文章標題為 : ' + direct_article_text)
            print('跳轉通知文章標題正確')
            print('我的通知功能正常')
            self.driver.back()
            self.driver.implicitly_wait(3)
            # 會員專屬

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/myNotification_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_officialAccount(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # FB官方帳號
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_FaceBook').click()
            WebDriverWait(self.driver, 20).until_not(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_FaceBook'))
            print('\n可正確跳轉FB官方帳號')
            self.driver.back()

            # YouTube官方帳號
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_YouTube').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='食尚玩家']"))
            print('可正確跳轉YouTube官方帳號')
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.google.android.youtube:id/subtitle'))
            self.driver.back()

            # LINE官方帳號
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/iv_Line').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='食尚玩家']"))
            print('可正確跳轉LINE官方帳號')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/OfficialAccount_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_otherSettings(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)
            # 新手教學
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)

            # 立即逛逛btn
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)

            # 推播通知
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/rl_Setting').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='Pack 食尚玩家']"))
            print('\n可正確跳轉通知設定')
            self.driver.back()
            self.driver.implicitly_wait(3)

            # 分享APP

            # 評分APP

            # 新手教學
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Teching').click()
            self.driver.implicitly_wait(3)
            for i in range(3):
                self.driver.find_element_by_class_name('android.widget.ImageView').click()
                self.driver.implicitly_wait(3)
            self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/beginner_close_btn').click()
            self.driver.implicitly_wait(3)
            print('新手教學功能正常')
            self.driver.swipe(900, 1500, 900, 200)
            self.driver.implicitly_wait(3)

            # 購物須知
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Buy_News').click()
            sleep(2)
            self.driver.swipe(900, 1600, 900, 700)
            sleep(2)
            self.driver.tap([(960, 1800)])  # ^按鈕
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('可正確跳轉購物須知')

            # 常見問題
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Question').click()
            sleep(2)
            self.driver.swipe(900, 1600, 900, 700)
            self.driver.implicitly_wait(3)
            self.driver.tap([(960, 1800)])  # ^按鈕
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('可正確跳轉常見問題')

            # 聯絡我們
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Contact_Us').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.google.android.gm:id/subject'))
            self.driver.find_element_by_id('com.google.android.gm:id/subject').send_keys('Automation_' + current_time)
            self.driver.implicitly_wait(3)
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.google.android.gm:id/subject'))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('進入聯絡我們功能正常')

            # 隱私權政策
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Privacy').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS個資與隱私權聲明']"))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('進入隱私權政策功能正常')

            # 會員服務條款
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rl_Service').click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS會員服務條款']"))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='推播通知']"))
            print('進入服務條款功能正常')

            # 使用版本
            version = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_Version')
            print('APP當前版本為 : ' + version.text)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/otherSettings_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 這個方法不好
    def call_app_register_login_s8plus(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 這種方式呼叫的是class外的function，但這樣無法各別算出pass/fail，前一個case已登入的資訊也沒被登出...
            # app_register_login_s8plus.test_memberCenterRegisterPageUICheck(self)    #pass
            # app_register_login_s8plus.test_memberCenterRegisterPageFacebookRegister(self)    #pass
            # app_register_login_s8plus.test_memberCenterRegisterPageFacebookLogin(self)
            # app_register_login_s8plus.test_memberCenterRegisterPageEmailRegisterErrorCheck(self)
            # app_register_login_s8plus.test_memberCenterRegisterEmailRegister(self)
            # app_register_login_s8plus.test_memberCenterLoginPageUICheck(self)
            # app_register_login_s8plus.test_memberCenterLoginPageFacebookLogin(self)
            # app_register_login_s8plus.test_memberCenterLoginPageEmailLoginErrorCheck(self)
            # app_register_login_s8plus.test_memberCenterLoginPageEmailLogin(self)
            # app_register_login_s8plus.test_checkFBName(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/pocket_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def call_app_pocket_s8plus(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 口袋(Freyja)
            app_register_login_s8plus.pocket_list(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/pocket_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_Register(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 口袋(Freyja)
            app_register_login_s8plus.pocket_list(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/pocket_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def test_test(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 開啟登入頁
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            # 登入email
            emailLogin(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/pocket_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../../../report/supertasteAppReport/supertaste_App_Report_{}.html'.format(current_time))
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(SuperTaste('test_bottomTabCheck'))  # 【首頁】底部Tab檢查　#2021.04.01 Pass
    # suite.addTest(SuperTaste('test_indexShake'))  # 【首頁】搖一搖 #2021.04.23 Fail android不支援driver.shake() https://appium.io/docs/en/commands/device/interactions/shake/
    # 【首頁】上方購物車  #無code
    # suite.addTest(SuperTaste('test_indexTopTab'))  # 【首頁】上方Tab跳轉  #無code
    # suite.addTest(SuperTaste('test_indexBanner))  # 【首頁】banner  #無code
    # suite.addTest(SuperTaste('test_indexProgramIV'))  # 【首頁】節目即時看  #無code
    # suite.addTest(SuperTaste('test_index'))  # 【首頁】十大熱門排行榜  #無code
    # suite.addTest(SuperTaste('test_index'))  # 【首頁】最新文章  #無code
    # suite.addTest(SuperTaste('test_hotRecommend'))  # 熱門推薦  #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_relatedNews'))  # 相關報導   #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_collectSearch'))  # 收藏後、取消收藏後搜尋  #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_hotSearch'))  # 熱搜   #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_profileEdit'))  # 個人資料編輯(施工中)
    suite.addTest(SuperTaste('test_myCollection'))  # 口袋    #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_myNotification'))  # 我的通知    #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_officialAccount'))  # 官方帳號   #2020.12.01 Fail
    # suite.addTest(SuperTaste('test_otherSettings'))  # 其他設定 #2020.12.01 Fail
    # suite.addTest(SuperTaste('call_app_register_login_s8plus'))  # 呼叫另一隻python檔(會員註冊/會員登入頁)
    # suite.addTest(SuperTaste('call_app_pocket_s8plus'))  # 呼叫另一隻python檔(收藏/口袋頁)
    # suite.addTest(SuperTaste('test_Register'))  # 呼叫另一隻python檔(會員註冊/會員登入頁)的口袋功能
    # suite.addTest(SuperTaste('test_test'))  #各種測試

    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste App Test Report')
    runner.run(suite)

