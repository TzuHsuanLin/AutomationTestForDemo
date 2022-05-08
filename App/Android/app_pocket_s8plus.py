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
import app_main_s8plus
import app_register_login_s8plus

# 為了搭配下一項測試，回到【我的頁】頂端
def back_to_my_page_top(self):
    print('>>>>>back_to_my_page_top<<<<<')
    if self.is_element_exist('com.tvbs.supertastemvppack:id/ivBack') is True:
        self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivBack').click()
        print('Click『＜』')
    else:
        print('畫面中沒有『＜』')

    if self.is_element_exist('com.tvbs.supertastemvppack:id/navigation_member') is True:
        self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_member').click()
        print('Click『我的』')
    else:
        print('畫面中沒有『我的』')

    if self.is_element_exist('com.tvbs.supertastemvppack:id/tvPass') is True:
        self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvPass').click()
        print('Click『想先瀏覽看看』')
    else:
        print('畫面中沒有『想先瀏覽看看』')

    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_member'))

    while True:
        if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_member') is False:
            self.driver.swipe(900, 300, 900, 1500)
            print("找不到「頭像」，滑1次")
        else:
            print('找到「頭像」')
            break

# 關閉【新手教學頁】
def init(self):
    if self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/beginner_viewpager'):
        print('\n開啟【新手教學頁】')
        # 新手教學
        for i in range(3):
            self.driver.find_element_by_class_name('android.widget.ImageView').click()
            self.driver.implicitly_wait(3)

        # 立即逛逛btn
        self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/beginner_close_btn').click()
        self.driver.implicitly_wait(3)
    else:
        print('未出現新手教學頁')

# 【會員登入頁】完成Apple ID登入，並檢查有登入成功
def appleIDLogin(self):
    print('(待補)Apple ID登入')

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
    print("\n進入【我的頁】")

    while True:
        if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_Logout') is False:
            self.driver.swipe(900, 1500, 900, 200)
            print("找不到「登出」鈕，滑1次")
        else:
            print('找到「登出」鈕，確定登入成功')
            break

    # 為了搭配下一項測試，回到【我的頁】頂端
    back_to_my_page_top(self)

# 【會員登入頁】完成Email登入，並檢查有登入成功
def emailLogin(self):
    print("進行Email登入流程")
    # 定位帳號欄位
    account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
    account_blank_text = account_blank.text
    # 定位密碼欄位
    password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
    password_blank_text = password_blank.text

    # 輸入正確帳號密碼進行登入
    account_blank.send_keys('freyjachen0002@gmail.com')
    password_blank.send_keys('a123456')
    self.driver.find_element_by_xpath("//*[@text='登入']").click()

    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_featured'))
    print("完成登入 freyjachen0002@gmail.com")

    self.driver.find_element_by_xpath("//*[@text='我的']").click()
    print("進入【我的頁】")

    while True:
        if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_Logout') is False:
            self.driver.swipe(900, 1500, 900, 200)
            print("找不到「登出」鈕，滑1次")
        else:
            print('找到「登出」鈕，確定登入成功')
            break

    # 為了搭配下一項測試，回到【我的頁】頂端
    back_to_my_page_top(self)

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

    # 為了搭配下一項測試，回到【我的頁】頂端
    back_to_my_page_top(self)

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

# 之後再整理
def find_specific_str(self, className, specificStr):
    content_desc = className.get_attribute('content-desc')
    # 【找關鍵字】【方法一】
    print('\t要搜尋的字串為：『' + content_desc + '』')  # 96 找店家 0
    if specificStr in content_desc:  # 使用in運算子檢查
        print('\t字串中有\'' + specificStr + '\'')
    else:
        print('\t字串中沒有\'' + specificStr + '\'')
        self.assertFalse(specificStr, '找不到指定字串')
    # 【找關鍵字】【方法二】
    # pos = content_desc.find(specificStr)
    # if pos >= 0:  # 有找到
    #     print('字串中有\'' + specificStr + '\'')
    # else:  # 沒有找到
    #     print('字串中沒有\'' + specificStr + '\'')
    #     self.assertFalse(specificStr, '找不到指定字串')

    print("\t字串長度有 "+str(len(content_desc)))  # 5
    print("\t收藏數是 "+content_desc[4:len(content_desc)])  # 0

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

    #  【口袋清單頁】UI檢查
    def test_pocketListPageUICheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            self.driver.implicitly_wait(1)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            self.driver.implicitly_wait(1)
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            self.driver.implicitly_wait(2)
            pocket_tab.click()  # Click「口袋」button

            # 執行Email登入
            emailLogin(self)

            sleep(6)
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            pocket_tab.click()  # Click「口袋」button
            sleep(6)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='口袋清單']"))  # 等待【口袋清單】頁出現
            print('\n開【口袋清單頁】')

            back = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon')  # ＜返回鍵
            title = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title')  # title
            self.driver.implicitly_wait(1)
            self.assertEqual(title.text, '口袋清單')
            print('\t左：＜返回鍵')
            print('\tTitle：顯示『口袋清單』')

            tab1 = self.driver.find_elements_by_class_name('androidx.appcompat.app.a$c')[0]  # 搶優惠 %d
            tab2 = self.driver.find_elements_by_class_name('androidx.appcompat.app.a$c')[1]  # 找店家 %d
            tab3 = self.driver.find_elements_by_class_name('androidx.appcompat.app.a$c')[2]  # 看報導 %d
            tab4 = self.driver.find_elements_by_class_name('androidx.appcompat.app.a$c')[3]  # 買東西 %d
            # 尋找指定字串『找店家』、『看報導』、『看報導』是否存在
            find_specific_str(self, tab1, '搶優惠')
            find_specific_str(self, tab2, '找店家')
            find_specific_str(self, tab3, '看報導')
            find_specific_str(self, tab4, '買東西')

            tab1_is_selected = bool(tab1.is_selected())
            self.assertTrue(tab1_is_selected, "畫面沒有預設在「搶優惠」Tab")
            print('\t畫面預設在「搶優惠」Tab')

            more_discount = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_discount')   #沒辦法找到文字『更多優惠推薦』

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    #  【口袋清單頁】【搶優惠】刪除所有收藏
    def test_pocketListDiscountDeleteCollection(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            self.driver.implicitly_wait(1)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            self.driver.implicitly_wait(1)
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            self.driver.implicitly_wait(2)
            pocket_tab.click()  # Click「口袋」button

            # 執行Email登入
            emailLogin(self)

            sleep(6)
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            pocket_tab.click()  # Click「口袋」button
            sleep(6)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='口袋清單']"))  # 等待【口袋清單】頁出現
            print('\n開【口袋清單頁】')

            # 刪除所有[搶優惠]收藏
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_store') is True: #用店家名稱來判斷還有沒有收藏
                    action = TouchAction(self.driver)  # 創建TouchAction物件
                    # 從[1]開始起算第一筆資料，因為外層還有一個大ViewGroup
                    # 長按第一筆收藏
                    action.long_press(self.driver.find_elements_by_class_name('android.view.ViewGroup')[1])
                    action.perform()
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))  #訊息：『確認刪除？』
                    self.driver.find_element_by_id('android:id/button1').click()  # button1=刪除 button2=取消
                    sleep(2)    #刪完後等一下畫面load完再繼續
                    print("刪除了一筆收藏")
                else:
                    print('已無收藏可刪除')
                    break

            if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_none') is True:
                print('出現圖片『按裝滿小資必備優惠　眾多好康　不再錯過』，但由於這是圖片，無法識別文字')

            if self.is_element_exist('com.tvbs.supertastemvppack:id/btn_more') is True:
                print('出現按鈕『建立省錢清單』，但由於這是圖片，無法識別文字')

            # # 判斷有無推薦店家
            # if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_channel') is False:  # 店家的圖片
            #     print('我的收藏開啟網路功能正常')
            #     print('=======找店家=======')
            #     print('當前無推薦店家')
            #     self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            #     WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[2])
            #     # 點選收藏
            #     else:
            #         print('我的收藏開啟網路功能正常')
            #         print('=======找店家=======')
            #         title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
            #         self.assertEqual(title_text, '更多店家推薦')
            #         store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            #         collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            #         self.assertEqual(collect_btn_text, "藏口袋")  # 判斷未收藏按鈕文字
            #         print('收藏店家為 : ' + store_text)
            #         collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         collect_article.click()
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         collected_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            #         self.assertEqual(collected_btn_text, "已收藏")  # 判斷已收藏按鈕文字
            #         print('收藏按鈕文字變化正確 : ' + collect_btn_text + '->' + collected_btn_text)
            #         collect_people_count = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_count').text
            #         collect_people_desc = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_desc').text
            #         print(collect_people_count + collect_people_desc)
            #
            #         # 判斷愛心有無填滿
            #         collect_article_checked = bool(collect_article.get_attribute("checked"))
            #         self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
            #         print('收藏後愛心有填滿')
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         collect_article.click()  # 取消收藏
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #
            #         collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         collect_article_checked = bool(collect_article.get_attribute("checked"))
            #         self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
            #         print('取消收藏後愛心沒有填滿')
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         collect_article.click()  # 再次收藏
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         self.driver.back()
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/iv_channel'))
            #
            #         # 返回收藏頁面
            #         collected_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            #         self.assertEqual(store_text.replace(" ", ""), collected_store_text.replace(" ", ""))
            #         print('已收藏的店家為 : ' + collected_store_text)
            #         print('確認為剛剛收藏的店家，收藏功能正常。')
            #
            #         # # 更多文章收藏
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
            #         # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
            #         # more_article.click()
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/action_icon'))
            #         # sleep(3)
            #         # for i in range(3):
            #         #     self.driver.swipe(900, 1500, 900, 300)
            #         #     sleep(1)
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/cbCollection'))
            #         # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         # collect_article.click()  # 收藏推薦文章的第二篇文章
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/tv_title'))
            #         # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            #         # sleep(3)
            #         # print('更多文章收藏功能正常')
            #
            #         # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         # collect_article[3].click()  # 收藏推薦文章的第四篇文章
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/tv_title'))
            #         # self.driver.back()
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/tv_title'))
            #         # print('更多文章收藏功能正常')
            #
            #         # 收藏店家跳轉
            #         collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            #         collect_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            #         print('要跳轉的店家為 : ' + collect_store_text)
            #         collect_store.click()
            #
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/iv_img'))
            #         direct_store_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            #         self.assertEqual(collect_store_text.replace(" ", ""), direct_store_text.replace(" ", ""))  # 去除空白
            #         print('跳轉後的店家為 : ' + direct_store_text)
            #         self.driver.back()
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/iv_channel'))
            #         print('收藏店家跳轉功能正常')
            #
            #         # 判斷已收藏數量正不正確
            #         store_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            #         self.assertEqual(store_amount, '找店家 1')
            #         print('店家收藏數量正確')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    #  【口袋清單頁】【找店家】刪除所有收藏
    def test_pocketListDiscountDeleteStore(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            self.driver.implicitly_wait(1)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            self.driver.implicitly_wait(1)
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            self.driver.implicitly_wait(2)
            pocket_tab.click()  # Click「口袋」button

            # 執行Email登入
            emailLogin(self)

            sleep(6)
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            pocket_tab.click()  # Click「口袋」button
            sleep(6)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='口袋清單']"))  # 等待【口袋清單】頁出現
            print('\n開【口袋清單頁】')

            self.driver.find_elements_by_class_name('androidx.appcompat.app.a$c')[1].click()  # 找店家 %d
            print('Click「找店家」')

            # 刪除所有[找店家]收藏
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_channel') is True: #用店家圖片來判斷還有沒有收藏
                    action = TouchAction(self.driver)  # 創建TouchAction物件
                    # 從[1]開始起算第一筆資料，因為外層還有一個大ViewGroup
                    # 長按第一筆收藏
                    action.long_press(self.driver.find_elements_by_class_name('android.view.ViewGroup')[1])
                    action.perform()
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))  #訊息：『確認刪除？』
                    self.driver.find_element_by_id('android:id/button1').click()  # button1=刪除 button2=取消
                    sleep(2)    #刪完後等一下畫面load完再繼續
                    print("刪除了一筆收藏")
                else:
                    print('已無收藏可刪除')
                    break

            if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_none') is True:
                print('出現圖片『點♡建立你的踩點地圖 跟著玩家　吃喝玩樂』，但由於這是圖片，無法識別文字')

            if self.is_element_exist('com.tvbs.supertastemvppack:id/btn_more') is True:
                print('出現按鈕『錯過哪些必踩點？』，但由於這是圖片，無法識別文字')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    #  【口袋清單頁】【看報導】刪除所有收藏
    def test_pocketListDiscountDeleteArticle(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            self.driver.implicitly_wait(1)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            self.driver.implicitly_wait(1)
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            self.driver.implicitly_wait(2)
            pocket_tab.click()  # Click「口袋」button

            # 執行Email登入
            emailLogin(self)

            sleep(6)
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
            pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
            pocket_tab.click()  # Click「口袋」button
            sleep(6)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='口袋清單']"))  # 等待【口袋清單】頁出現
            print('\n開【口袋清單頁】')

            self.driver.find_elements_by_class_name('androidx.appcompat.app.a$c')[2].click()  # 找店家 %d
            print('Click「看報導」')

            # 刪除所有[看報導]收藏
            while True:
                if self.is_element_exist('com.tvbs.supertastemvppack:id/cl_main') is True:  # 用整筆資料來判斷還有沒有收藏
                    action = TouchAction(self.driver)  # 創建TouchAction物件
                    # 從[1]開始起算第一筆資料，因為外層還有一個大ViewGroup
                    # 長按第一筆收藏
                    action.long_press(self.driver.find_elements_by_class_name('android.view.ViewGroup')[1])
                    action.perform()
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))  # 訊息：『確認刪除？』
                    self.driver.find_element_by_id('android:id/button1').click()  # button1=刪除 button2=取消
                    sleep(2)  # 刪完後等一下畫面load完再繼續
                    print("刪除了一筆收藏")
                else:
                    print('已無收藏可刪除')
                    break

            if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_none') is True:
                print('出現圖片『點♡收納流行"食"尚 優惠好康 話題一把抓』，但由於這是圖片，無法識別文字')

            if self.is_element_exist('com.tvbs.supertastemvppack:id/btn_more') is True:
                print('出現按鈕『大家在夯什麼？』，但由於這是圖片，無法識別文字')

            # # 判斷有無推薦店家
            # if self.is_element_exist('com.tvbs.supertastemvppack:id/iv_channel') is False:  # 店家的圖片
            #     print('我的收藏開啟網路功能正常')
            #     print('=======找店家=======')
            #     print('當前無推薦店家')
            #     self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            #     WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')[2])
            #     # 點選收藏
            #     else:
            #         print('我的收藏開啟網路功能正常')
            #         print('=======找店家=======')
            #         title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
            #         self.assertEqual(title_text, '更多店家推薦')
            #         store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            #         collect_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            #         self.assertEqual(collect_btn_text, "藏口袋")  # 判斷未收藏按鈕文字
            #         print('收藏店家為 : ' + store_text)
            #         collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         collect_article.click()
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         collected_btn_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection').text
            #         self.assertEqual(collected_btn_text, "已收藏")  # 判斷已收藏按鈕文字
            #         print('收藏按鈕文字變化正確 : ' + collect_btn_text + '->' + collected_btn_text)
            #         collect_people_count = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_count').text
            #         collect_people_desc = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_people_desc').text
            #         print(collect_people_count + collect_people_desc)
            #
            #         # 判斷愛心有無填滿
            #         collect_article_checked = bool(collect_article.get_attribute("checked"))
            #         self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
            #         print('收藏後愛心有填滿')
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         collect_article.click()  # 取消收藏
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #
            #         collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         collect_article_checked = bool(collect_article.get_attribute("checked"))
            #         self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
            #         print('取消收藏後愛心沒有填滿')
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         collect_article.click()  # 再次收藏
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/tv_title'))
            #         self.driver.back()
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/iv_channel'))
            #
            #         # 返回收藏頁面
            #         collected_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            #         self.assertEqual(store_text.replace(" ", ""), collected_store_text.replace(" ", ""))
            #         print('已收藏的店家為 : ' + collected_store_text)
            #         print('確認為剛剛收藏的店家，收藏功能正常。')
            #
            #         # # 更多文章收藏
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
            #         # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
            #         # more_article.click()
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/action_icon'))
            #         # sleep(3)
            #         # for i in range(3):
            #         #     self.driver.swipe(900, 1500, 900, 300)
            #         #     sleep(1)
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/cbCollection'))
            #         # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         # collect_article.click()  # 收藏推薦文章的第二篇文章
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/tv_title'))
            #         # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
            #         # sleep(3)
            #         # print('更多文章收藏功能正常')
            #
            #         # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
            #         # collect_article[3].click()  # 收藏推薦文章的第四篇文章
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/tv_title'))
            #         # self.driver.back()
            #         # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #         #     'com.tvbs.supertastemvppack:id/tv_title'))
            #         # print('更多文章收藏功能正常')
            #
            #         # 收藏店家跳轉
            #         collect_store = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_channel')
            #         collect_store_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1].text
            #         print('要跳轉的店家為 : ' + collect_store_text)
            #         collect_store.click()
            #
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/iv_img'))
            #         direct_store_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_title').text
            #         self.assertEqual(collect_store_text.replace(" ", ""), direct_store_text.replace(" ", ""))  # 去除空白
            #         print('跳轉後的店家為 : ' + direct_store_text)
            #         self.driver.back()
            #         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #             'com.tvbs.supertastemvppack:id/iv_channel'))
            #         print('收藏店家跳轉功能正常')
            #
            #         # 判斷已收藏數量正不正確
            #         store_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
            #         self.assertEqual(store_amount, '找店家 1')
            #         print('店家收藏數量正確')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../../../report/supertasteAppReport/supertaste_App_Report_{}.html'.format(current_time))
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()

    # suite.addTest(SuperTaste('test_pocketListPageUICheck'))   # 【口袋清單頁】UI檢查    #2021.04.26 Pass
    # suite.addTest(SuperTaste('test_pocketListDiscountDeleteCollection')) # 【口袋清單頁】【搶優惠】刪除所有收藏    #2021.05.04 Pass
    # suite.addTest(SuperTaste('test_pocketListDiscountDeleteStore'))  # 【口袋清單頁】【找店家】刪除所有收藏    #2021.05.12 Pass
    suite.addTest(SuperTaste('test_pocketListDiscountDeleteArticle'))  # 【口袋清單頁】【看報導】刪除所有收藏    #2021.05.12 Pass

    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste App Test Report')
    runner.run(suite)

# def test_myCollection(self):
#
#         # 我的收藏
#         self.driver.find_element_by_xpath("//*[@text='我的']").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/iv_my_collection').click()
#         self.driver.implicitly_wait(3)
#
#         # 登入TVBS
#         # 定位帳號欄位
#         account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
#         # 定位密碼欄位
#         password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
#         # 帳號欄位傳值
#         account_blank.send_keys('mybooktest0604@gmail.com')
#         # 密碼欄位傳值
#         password_blank.send_keys('s23321286')
#         self.driver.find_element_by_xpath("//*[@text='登入']").click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/tv_Title'))
#
#         # 收藏頁面
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_my_collection').click()
#         WebDriverWait(self.drivpacker, 20).until(lambda x: x.find_element_by_id(
# #             'com.tvbs.supertastemvp:id/btn_more'))
#
#         # 關閉網路
#         self.driver.set_network_connection(0)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
#         self.driver.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_retry'))
#         print('\n=======網路狀態=======')
#         print('我的收藏關閉網路功能正常')
#
#         # 開啟網路
#         self.driver.set_network_connection(2)  # NO_CONNECTION = 0,　WIFI_ONLY = 2
#         sleep(4)
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_retry').click()


#
#             # 刪除收藏
#             action = TouchAction(self.driver)  # 創建TouchAction物件
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             dialog_text = self.driver.find_element_by_id('android:id/message').text
#             self.assertEqual(dialog_text, '確認刪除?')
#             print('長按收藏店家可跳出刪除訊息')
#
#             # 取消刪除收藏
#             self.driver.find_element_by_id('android:id/button2').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_channel'))
#             print('取消刪除收藏店家功能正常')
#
#             # 確定刪除收藏
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             self.driver.find_element_by_id('android:id/button1').click()
#             # 判斷刪除後數量是否有減少
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='找店家 0']"))
#             print('確定刪除收藏功能正常')
#
#             # 空收藏
#             # action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             # action.perform()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             # self.driver.find_element_by_id('android:id/button1').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/btn_more'))
#             print('確定刪除所有收藏店家後會顯示"錯過那些必踩點?"按鈕')
#
#         # 看報導
#         print('=======看報導=======')
#         self.driver.find_elements_by_class_name('android.widget.TextView')[2].click()
#         while True:
#             if self.is_element_exist('com.tvbs.supertastemvppack:id/cl_main') is True:
#                 action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#                 action.perform()
#                 WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#                 self.driver.find_element_by_id('android:id/button1').click()
#             else:
#                 break
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more'))
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/action_icon'))
#         title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
#         self.assertEqual(title_text, '更多報導推薦')
#         # 判斷有無推薦報導
#         if self.is_element_exist('com.tvbs.supertastemvppack:id/tv_date') is False:
#             print('當前無推薦報導')
#             self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_class_name(
#                 'android.support.v7.app.ActionBar$Tab')[2])
#         else:
#             date_time = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_date').text
#             datetime.datetime.strptime(date_time, '%Y/%m/%d')
#             print('文章時間格式正確')
#             article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
#             print('收藏的報導標題為 : ' + article_text)
#
#             # 點選收藏
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
#             collect_article.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#
#             # 判斷愛心有無填滿
#             collect_article_checked = bool(collect_article.get_attribute("checked"))
#             self.assertTrue(collect_article_checked, "收藏後愛心未填滿!")
#             print('收藏後愛心有填滿')
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
#             collect_article.click()  # 取消收藏
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/cbCollection'))
#
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[1]
#             collect_article_checked = bool(collect_article.get_attribute("checked"))
#             self.assertTrue(collect_article_checked, "取消收藏後愛心仍有填滿!")
#             print('取消收藏後愛心沒有填滿')
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collect_article.click()  # 再次收藏
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             collect_article2 = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')[3]
#             collect_article2.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             self.driver.back()
#
#             # 返回收藏頁面
#             collected_article_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[2].text
#             self.assertEqual(article_text, collected_article_text)
#             print('已收藏的報導為 : ' + collected_article_text)
#             print('確認為剛剛收藏的報導，收藏功能正常。')
#
#             # # 更多文章收藏
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/btn_more_infocard'))
#             # more_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more_infocard')
#             # more_article.click()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/action_icon'))
#             # sleep(3)
#             # for i in range(3):
#             #     self.driver.swipe(900, 1500, 900, 300)
#             #     sleep(1)
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/cbCollection'))
#             # collect_article = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             # collect_article.click()  # 收藏推薦文章的第二篇文章
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/action_icon').click()
#             # sleep(3)
#             # print('更多文章收藏功能正常')
#
#             # collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cbCollection')
#             # collect_article[3].click()  # 收藏推薦文章的第四篇文章
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # self.driver.back()
#             # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             #     'com.tvbs.supertastemvppack:id/tv_title'))
#             # print('更多文章收藏功能正常')
#
#             # 收藏報導跳轉
#             collect_article = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
#             collect_article_text = collect_article.text
#             print('要跳轉的報導為 : ' + collect_article_text)
#             collect_article.click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             direct_article_text = self.driver.find_elements_by_class_name('android.widget.TextView')[1].text
#             self.assertEqual(collect_article_text, direct_article_text)
#             print('跳轉後的報導為 : ' + direct_article_text)
#             self.driver.back()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/iv_channel'))
#             print('收藏報導跳轉功能正常')
#
#             # 判斷已收藏數量正不正確
#             article_amount = self.driver.find_elements_by_class_name('android.widget.TextView')[2].text
#             self.assertEqual(article_amount, '看報導 2')
#             print('報導收藏數量正確')
#
#             # 刪除收藏
#             action = TouchAction(self.driver)  # 創建TouchAction物件
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/cl_main')[0])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             dialog_text = self.driver.find_element_by_id('android:id/message').text
#             self.assertEqual(dialog_text, '確認刪除?')
#             print('長按收藏報導可跳出刪除訊息')
#
#             # 取消刪除收藏
#             self.driver.find_element_by_id('android:id/button2').click()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/tv_title'))
#             print('取消刪除報導收藏功能正常')
#
#             # 確定刪除收藏
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             self.driver.find_element_by_id('android:id/button1').click()
#             WebDriverWait(self.driver, 20).until(
#                 lambda x: x.find_element_by_xpath("//*[@text='看報導 1']"))  # 判斷刪除後數量是否有減少
#
#             # 空收藏
#             action.long_press(self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1])
#             action.perform()
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
#             self.driver.find_element_by_id('android:id/button1').click()
#             WebDriverWait(self.driver, 20).until(
#                 lambda x: x.find_element_by_xpath("//*[@text='看報導 0']"))  # 判斷刪除後數量是否有減少
#             WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#                 'com.tvbs.supertastemvppack:id/btn_more'))
#             print('確定刪除所有收藏店家後會顯示"大家在夯什麼?"按鈕')
#
#         # 買東西
#         print('=======買東西=======')
#         self.driver.find_elements_by_class_name('android.widget.TextView')[3].click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/btn_more'))
#         self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btn_more').click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
#             'com.tvbs.supertastemvppack:id/iv_channel'))
#         title_text = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[0].text
#         self.assertEqual(title_text, '更多商品推薦')
#         item = self.driver.find_elements_by_id('com.tvbs.supertastemvppack:id/tv_title')[1]
#         print('收藏的商品為 :' + item.text)
#         item.click()
#         WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='購物首頁']"))
#         print('進入EC商城')
#
#     except:
#         flag = False
#         if flag is False or Exception:
#             self.driver.save_screenshot(
#                 '../../screenshot/supertasteAppFail/myCollection_Fail_{}.png'.format(current_time))
#             self.assertTrue(flag, 'Execute Fail.')