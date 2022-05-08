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

# 之後再整理
def pocket_list(self):
    flag = True
    # noinspection PyBroadException
    try:
        self.driver.implicitly_wait(6)

        # 關掉【新手教學頁】
        init(self)

        print('77')
        # self.driver.implicitly_wait(1)
        # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/navigation_pocket'))  # 等待底部功能列的「口袋」出現
        # self.driver.implicitly_wait(1)
        # pocket_tab = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/navigation_pocket')
        # self.driver.implicitly_wait(2)
        #
        # # 大頭貼btn
        # self.driver.find_element_by_xpath("//*[@text='我的']").click()
        # self.driver.implicitly_wait(3)
        # self.driver.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/iv_member').click()
        # self.driver.implicitly_wait(3)
        #
        # self.driver.find_element_by_xpath("//*[@text='我還沒有TVBS帳號，註冊去']").click()
        # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/etAccount'))
        # # 註冊帳號欄位
        # register_account_blank = self.driver.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/etAccount')
        # register_account_blank_text = register_account_blank.text
        # # 註冊密碼欄位
        # register_password_blank = self.driver.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/etPassWord')
        # register_password_blank_text = register_password_blank.text
        # # 確認密碼欄位
        # password_confirm_blank = self.driver.find_element_by_id(
        #     'com.tvbs.supertastemvppack:id/etPassWordCheck')
        # password_confirm_blank_text = password_confirm_blank.text
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
            self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
            self.assertTrue(flag, 'Execute Fail.')

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

    #  【會員註冊頁】UI檢查
    def test_memberCenterRegisterPageUICheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            print('\nClick頭像')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='會員登入']"))
            print('\n開啟【會員登入頁】')

            # 有「我還沒有TVBS帳號，註冊去」文字
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister'))
            print('有「我還沒有TVBS帳號，註冊去」文字')

            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister').click()
            print('Click「我還沒有TVBS帳號，註冊去」button')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='註冊']"))
            print('\n開啟【會員註冊頁】')

            # 有「＜」icon
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/ivBack'))
            print('有「＜」icon')

            title_text = self.driver.find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(title_text, '註冊')
            print('Title = 註冊')
            # [0].text = 註冊
            # [1].text = 或
            # [2].text = 我願意收到TVBS發出的相關通知
            # [3].text = Email將用於登入認證與優惠聯繫，建議為方便收信的個人Email，保護您的權益
            # [4].text = 想先瀏覽看看

            # 檢查「Facebook快速註冊」按鈕
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivFbRegister')
            print('有「Facebook快速註冊」按鈕')

            # 檢查email帳號欄位提示文字
            email_register_account_hint_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount').text
            self.assertTrue(email_register_account_hint_text, '請輸入註冊Email')
            print('email帳號欄位有提示文字:「請輸入註冊Email」')

            # 檢查email密碼欄位1提示文字
            email_register_password_hint_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWord').text
            self.assertTrue(email_register_password_hint_text, '請設定密碼(6~12個英數字)')
            print('email密碼欄位有提示文字:「請設定密碼(6~12個英數字)」')

            # 檢查email密碼欄位2提示文字
            email_register_password_confirm_hint_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etPassWordCheck').text
            self.assertTrue(email_register_password_confirm_hint_text, '請再次輸入密碼')
            print('email密碼欄位有提示文字:「請再次輸入密碼」')

            # 檢查有CheckBox
            checkbox = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbNotification')
            # 判斷Checkbox預設是否已勾選
            checkbox_checked = bool(checkbox.get_attribute("checked"))
            self.assertTrue(checkbox_checked, 'Checkbox預設為已勾選! ')  # 判斷Checkbox預設是否已勾選
            print('有CheckBox，預設為已勾選')
            checkbox.click()
            self.assertFalse(checkbox.is_selected(), 'Checkbox點擊後為未勾選狀態')
            print('Checkbox點擊後可取消勾選狀態')

            # 檢查CheckBox提示文字
            email_login_password_hint_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/tvNotification').text
            self.assertTrue(email_login_password_hint_text, '我願意收到TVBS發出的相關通知')
            print('有文字:「我願意收到TVBS發出的相關通知」')

            # 檢查「登入」按鈕文字
            register_button_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btSend').text
            self.assertTrue(register_button_text, '送出')
            print('有「送出」按鈕')

            alert_text = self.driver.find_elements_by_class_name('android.widget.TextView')[3].text
            self.assertEqual(alert_text, 'Email將用於登入認證與優惠聯繫，建議為方便收信的個人Email，保護您的權益')
            print('有提示文字『Email將用於登入認證與優惠聯繫，建議為方便收信的個人Email，保護您的權益』')

            look_around_text = self.driver.find_elements_by_class_name('android.widget.TextView')[4].text
            self.assertEqual(look_around_text, '想先瀏覽看看')
            print('有提示文字『想先瀏覽看看』')

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員註冊頁】Facebook註冊（在測試環境沒那麼多註冊過FB developer的帳號，難以執行自動化）
    # 【前置作業】FB APP登出 → 移除所有登過的帳號資訊
    def test_memberCenterRegisterPageFacebookRegister(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')

            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister').click()
            print('Click「我還沒有TVBS帳號，註冊去」button')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='註冊']"))
            print('\n開啟【會員註冊頁】')

            print('在測試環境沒那麼多註冊過FB developer的帳號，難以執行自動化')

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

            # # FB快速註冊
            # fb_register_account_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivFbRegister')
            # fb_register_account_btn.click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/rl_my_collection'))
            # sleep(3)
            #
            # # 驗證FB會員名字
            # fb_member_name = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tv_member_name')
            # fb_member_name_text = fb_member_name.text
            # self.assertEqual(fb_member_name_text, 'Jack Tsao')
            # print('\nFB會員快速註冊成功，此次註冊用戶名稱為 : ' + fb_member_name_text)
            # self.driver.swipe(900, 1500, 900, 200)
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Logout'))
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_Logout').click()
            # print('FB會員快速註冊成功且順利登出')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員註冊頁】Facebook登入，並檢查有登入成功
    # 【前置作業】FB APP登出 → 移除所有登過的帳號資訊
    def test_memberCenterRegisterPageFacebookLogin(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')

            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister').click()
            print('Click「我還沒有TVBS帳號，註冊去」button')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='註冊']"))
            print('\n開啟【會員註冊頁】')

            # 【會員登入頁】完成Facebook登入，並檢查有登入成功
            facebookLogin(self)

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員註冊頁】Email註冊欄位錯誤檢查
    def test_memberCenterRegisterPageEmailRegisterErrorCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister').click()
            print('Click「我還沒有TVBS帳號，註冊去」button')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='註冊']"))
            print('\n開啟【會員註冊頁】')

            register_account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            register_password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            password_confirm_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWordCheck')

            # 不輸入Email、密碼、確認密碼註冊
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、密碼、確認密碼')
            print('不輸入Email、密碼、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))

            # 不輸入密碼、確認密碼註冊
            register_account_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入密碼、確認密碼')
            print('不輸入密碼、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()

            # 不輸入Email、確認密碼註冊
            register_password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、確認密碼')
            print('不輸入Email、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_password_blank.clear()

            # 不輸入Email、密碼註冊
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、密碼')
            print('不輸入Email、密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            password_confirm_blank.clear()

            # 不輸入確認密碼註冊
            register_account_blank.send_keys('tvbstest')
            register_password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入確認密碼')
            print('不輸入確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()

            # 不輸入密碼註冊
            register_account_blank.send_keys('tvbstest')
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入密碼')
            print('不輸入密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            password_confirm_blank.clear()

            # 不輸入Email註冊
            register_password_blank.send_keys('tvbstest')
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email')
            print('不輸入Email註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入非Email格式帳號進行登入
            register_account_blank.send_keys('tvbstest')
            register_password_blank.send_keys('tvbstest')
            password_confirm_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '帳號格式錯誤，請填寫完整Email！')
            print('輸入非Email格式帳號登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入不符合密碼、確認密碼規則註冊
            register_account_blank.send_keys('tvbstest@gmail.com')
            register_password_blank.send_keys('tvbstvbs')
            password_confirm_blank.send_keys('tvbstvbs')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '密碼建議為 6~12 位數，必須是英文數字混合！')
            print('輸入不符合密碼、確認密碼規則註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入不一樣密碼、確認密碼註冊
            register_account_blank.send_keys('tvbstest@gmail.com')
            register_password_blank.send_keys('tvbstest1')
            password_confirm_blank.send_keys('tvbstest2')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '密碼與確認密碼不符，請重新確認！')
            print('輸入不一樣密碼、確認密碼註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入停用帳號進行登入
            register_account_blank.send_keys('freyjachen0206@gmail.com')
            register_password_blank.send_keys('a123456')
            password_confirm_blank.send_keys('a123456')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            sleep(5)  # 等待API回傳可能會出現「載入中」的訊息
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))  # 等待API回傳訊息
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '此帳號被禁用! 任何疑問請與客服(service@tvbs.com.tw)聯絡')
            print('輸入被禁用帳號 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入已註冊為TVBS會員的帳號註冊
            register_account_blank.send_keys('s0932748681@gmail.com')
            register_password_blank.send_keys('tvbstvbs123')
            password_confirm_blank.send_keys('tvbstvbs123')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '此帳號已透過 Email 註冊為會員！')
            print('輸入已註冊為TVBS會員的帳號註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 輸入已註冊為FB會員的帳號註冊
            register_account_blank.send_keys('s23321286@gmail.com')
            register_password_blank.send_keys('tvbstvbs123')
            password_confirm_blank.send_keys('tvbstvbs123')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '此帳號已透過 FB 註冊為會員！')
            print('輸入已註冊為FB會員的帳號註冊跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            register_account_blank.clear()
            register_password_blank.clear()
            password_confirm_blank.clear()

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

            # 輸入已註冊為Apple ID會員的帳號註冊（android不用測）
            # register_account_blank.send_keys('freyja070301@gmail.com')
            # register_password_blank.send_keys('a123456')
            # password_confirm_blank.send_keys('a123456')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '此帳號已透過 Apple ID 註冊為會員！')
            # print('輸入已註冊為FB會員的帳號註冊跳出wording : ' + dialog_text)
            # self.driver.find_element_by_xpath("//*[@text='確定']").click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            # register_account_blank.clear()
            # register_password_blank.clear()
            # password_confirm_blank.clear()

            # # 註冊欄位傳值
            # random_account = random.choice('abcdefg') + str(random.randint(0, 9999))
            # print('此次註冊帳號為 : ' + random_account + '@gmail.com')
            # register_account = random_account + '@gmail.com'
            # register_account_blank.send_keys(register_account)
            # print('')
            # self.driver.implicitly_wait(3)
            # register_password_blank.send_keys('a00000')
            # password_confirm_blank.send_keys('a00000')
            # print('此次註冊密碼為 : a00000')
            # self.driver.find_element_by_xpath("//*[@text='送出']").click()

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterRegisterTVBS_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員註冊頁】Email註冊（但還無法到信箱點擊認證信）
    def test_memberCenterRegisterEmailRegister(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')

            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister').click()
            print('Click「我還沒有TVBS帳號，註冊去」button')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='註冊']"))
            print('\n開啟【會員註冊頁】')

            register_account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            register_password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            password_confirm_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWordCheck')

            # 註冊欄位傳值
            random_account = random.choice('abcdefg') + str(random.randint(0, 9999))
            print('\n此次註冊帳號為 : ' + random_account + '@gmail.com')
            register_account = random_account + '@gmail.com'
            register_account_blank.send_keys(register_account)
            self.driver.implicitly_wait(3)
            register_password_blank.send_keys('a00000')
            password_confirm_blank.send_keys('a00000')
            print('此次註冊密碼為 : a00000')
            self.driver.find_element_by_xpath("//*[@text='送出']").click()
            print('Click「送出」button')

            # 【性別生日頁】UI檢查
            genderBirthdayPageUICheck(self)

            # 判斷服務條款、隱私權政策功能
            self.driver.tap([(824, 1338)])  # 服務條款
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS會員服務條款']"))
            self.driver.back()
            print('進入【服務條款頁】功能正常')
            self.driver.tap([(1144, 1344)])  # 隱私權政策
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='TVBS個資與隱私權聲明']"))
            self.driver.back()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_class_name('android.widget.CheckBox'))
            print('進入【隱私權政策頁】功能正常')

            # 未勾選性別+未勾選「我同意」
            next_btn = self.driver.find_element_by_xpath("//*[@text='下一步']")  # 下一步btn
            next_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入性別')
            print('未勾選性別，Click「下一步」，跳出wording : 『請輸入性別』')
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='性別']"))

            # Click 「秘密」RadioButton
            secret_radiobtn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/rbSecret')
            secret_radiobtn.click()
            secret_radiobtn_checked = bool(secret_radiobtn.get_attribute("checked"))
            self.assertTrue(secret_radiobtn_checked, '「秘密」RadioButton點擊後仍為未勾選狀態!')
            print('Click 「秘密」RadioButton')
            self.driver.implicitly_wait(3)

            # 目前無法做到選擇超過(含)當天日期
            # 生日功能驗證
            # birthday_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivBirthday')
            # birthday_btn.click()
            # birthday_btn_alert_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/alertTitle').text
            # self.assertEqual(birthday_btn_alert_text, '選擇生日')
            # print('進入選擇生日頁面正常')
            # self.driver.find_element_by_id('android:id/button2').click()
            # print('離開選擇生日頁面正常')
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/ivBirthday'))
            # birthday_btn.click()
            # self.driver.implicitly_wait(3)
            # self.driver.find_element_by_xpath("//*[@text='1982']").click()
            # self.driver.find_element_by_xpath("//*[@text='2']").click()
            # self.driver.find_element_by_xpath("//*[@text='31']").click()
            # self.driver.find_element_by_id('android:id/button1').click()
            # print('選擇生日功能正常')

            # 未勾選「我同意」
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbNoBirthday').click()
            print('勾選「不提供生日」')
            next_btn = self.driver.find_element_by_xpath("//*[@text='下一步']")  # 下一步btn
            next_btn.click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('android:id/message'))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請同意 TVBS 會員中心的服務條款及隱私權政策。')
            print('未勾選「我同意」，Click「下一步」，跳出wording : 『請同意 TVBS 會員中心的服務條款及隱私權政策。』')
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='性別']"))

            # 已勾選同意
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/cbPrivacy').click()
            next_btn.click()
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/tvWording1'))
            success_dialog_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvWording1').text
            print('註冊成功，' + success_dialog_text)

            # 與我們聯絡
            self.driver.tap([(716, 910)])  # 我們聯絡btn
            self.driver.find_element_by_xpath("//*[@text='service@tvbs.com.tw']")
            print('Click「與我們聯絡」，進入【email撰寫】')

            self.driver.find_element_by_id('com.google.android.gm:id/subject').send_keys('Automation_' + current_time)
            print('於「主旨」欄位輸入Automation_' + current_time)
            self.driver.find_element_by_id('com.google.android.gm:id/send').click()
            print('Click　寄信')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
                'com.tvbs.supertastemvppack:id/btLogin'))  # com.tvbs.supertastemvppack:id/btLogin
            print('回到【註冊驗證信已寄出】頁')

            # 到信箱點擊認證信

            register_account_blank.send_keys(register_account)
            register_password_blank.send_keys('a00000')
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btLogin').click()
            print('Click「登入」button')

            sleep(3)

            if self.is_element_exist('android:id/message') is True:
                print('出現提示訊息：『'+self.driver.find_element_by_id('android:id/message').text+'』')
                self.driver.find_element_by_id('android:id/button1').click()

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/open_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員登入頁】UI檢查
    def test_memberCenterLoginPageUICheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            print('\nClick頭像')

            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//*[@text='會員登入']"))
            print('開啟【會員登入頁】')

            # 有「X」icon
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/ivCancel'))
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivCancel')
            print('有「X」icon')

            # 檢查Title
            dialog_text = self.driver.find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(dialog_text, '會員登入')
            print('Title = 會員登入')
            # [0].text = 會員登入
            # [1].text = 或
            # [2].text = 忘記密碼
            # [3].text = 想先瀏覽看看

            # 檢查「Facebook登入」按鈕
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/ivFbLogin')
            print('有「Facebook登入」按鈕')

            # 檢查email帳號欄位提示文字
            email_login_account_hint_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount').text
            self.assertTrue(email_login_account_hint_text, '請輸入註冊Email')
            print('email帳號欄位有提示文字:「請輸入註冊Email」')

            # 檢查email密碼欄位提示文字
            email_login_password_hint_text = self.driver.find_element_by_id(
                'com.tvbs.supertastemvppack:id/etAccount').text
            self.assertTrue(email_login_password_hint_text, '請輸入密碼')
            print('email密碼欄位有提示文字:「請輸入密碼」')

            # 檢查「登入」按鈕文字
            login_button_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btLogin').text
            self.assertTrue(login_button_text, '登入')
            print('有「登入」按鈕')

            # 有「忘記密碼」文字
            forget_password_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvForgetPassWord').text
            self.assertTrue(forget_password_text, '忘記密碼')
            print('有「忘記密碼」文字')

            # 有「我還沒有TVBS帳號，註冊去」文字
            go_register_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btRegister').text
            self.assertTrue(go_register_text, '我還沒有TVBS帳號，註冊去')
            print('有「我還沒有TVBS帳號，註冊去」文字')

            # 有「想先瀏覽看看」文字
            look_around_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvPass').text
            self.assertTrue(look_around_text, '想先瀏覽看看')
            print('有「想先瀏覽看看」文字')

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

            # # 想先瀏覽看看
            # self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvPass').click()
            # self.driver.implicitly_wait(3)
            # print('想先瀏覽看看功能正常')
            #
            # # 判斷頁面是否有大頭貼btn且可點選
            # profile_assert = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').is_enabled()
            # # 判斷頁面是否有點擊登入文字且可點選
            # login_text_assert = self.driver.find_element_by_xpath("//*[@text='點擊登入']").is_enabled()
            # self.assertTrue(profile_assert)
            # print('點選想先瀏覽看看功能正常 - 偵測頁面是否有大頭貼按鈕且enable')
            # self.assertTrue(login_text_assert)
            # print('點選想先瀏覽看看功能正常 - 偵測頁面是否有點擊登入按鈕且enable')
            # self.driver.swipe(900, 1500, 900, 200)
            # sleep(2)
            # self.driver.tap([(500, 1700)])  # 登入btn
            # print('點選底部登入按鈕功能正常')
            # self.driver.implicitly_wait(3)

        except:
            flag = False
            profile_assert = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/loginFeature_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員登入頁】Facebook登入，並檢查有登入成功
    # 【前置作業】FB APP登出 → 移除所有登過的帳號資訊
    def test_memberCenterLoginPageFacebookLogin(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')

            # 【會員登入頁】完成Facebook登入，並檢查有登入成功
            facebookLogin(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/memberCenterLoginFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員登入頁】Email登入欄位錯誤檢查
    def test_memberCenterLoginPageEmailLoginErrorCheck(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')

            # [會員登入頁]UI檢查 > 'test_memberCenterLoginPageUICheck'

            # [會員登入頁][FB登入]錯誤檢查 > X

            # [會員登入頁][Apple ID登入]錯誤檢查 > X

            # [會員登入頁][Email登入]錯誤檢查
            # 不輸入帳號、密碼登入
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email、密碼')
            print('不輸入帳號密碼登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))

            # 不輸入帳號登入
            password_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etPassWord')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入Email')
            print('不輸入帳號登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            password_blank.clear()

            # 不輸入密碼登入
            account_blank = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount')
            account_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '請輸入密碼')
            print('不輸入密碼登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()

            # 輸入非Email格式帳號進行登入
            account_blank.send_keys('tvbstest')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '帳號格式錯誤，請填寫完整Email！')
            print('輸入非Email格式帳號登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()
            password_blank.clear()

            # 輸入不存在帳號進行登入
            account_blank.send_keys('tvbstest@gmail.com')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '查無此帳號！')
            print('輸入不存在帳號登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()
            password_blank.clear()

            # 輸入錯誤密碼進行登入
            account_blank.send_keys('freyjachen0206@gmail.com')
            password_blank.send_keys('tvbstest')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '帳號或密碼錯誤，請重新輸入！')
            print('輸入錯誤密碼登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()
            password_blank.clear()

            # 輸入停用帳號進行登入
            account_blank.send_keys('freyjachen0206@gmail.com')
            password_blank.send_keys('a123456')
            self.driver.find_element_by_xpath("//*[@text='登入']").click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@text='確定']"))
            dialog_text = self.driver.find_element_by_id('android:id/message').text
            self.assertEqual(dialog_text, '此帳號被禁用! 任何疑問請與客服(service@tvbs.com.tw)聯絡')
            print('輸入錯誤密碼登入 > 跳出wording : ' + dialog_text)
            self.driver.find_element_by_xpath("//*[@text='確定']").click()
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_id('com.tvbs.supertastemvppack:id/etAccount'))
            account_blank.clear()
            password_blank.clear()

            # 為了搭配下一項測試，回到【我的頁】頂端
            back_to_my_page_top(self)

            # # 忘記密碼
            # forgot_mail = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/tvForgetPassWord')
            # forgot_mail.click()
            # forgot_mail_text = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/etEmail').text
            # self.assertEqual(forgot_mail_text, '請輸入註冊Email')
            # print('忘記密碼placeholder為 : ' + forgot_mail_text)
            # forgot_mail.send_keys('s23321286')
            # send_btn = self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/btSend')
            # send_btn.click()
            # message = self.driver.find_element_by_id('android:id/message')
            # message_text = message.text
            #
        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterLoginPageCheck_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 【會員登入頁】完成Email登入，並檢查有登入成功
    def test_memberCenterLoginPageEmailLogin(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)
            print('\n由頭像開啟【會員登入頁】')

            # 【會員登入頁】完成Email登入，並檢查有登入成功
            emailLogin(self)

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('../../../screenshot/supertasteAppFail/memberCenterLoginFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    # 檢查FB名稱（暫時不想做這項檢查）
    def test_checkFBName(self):
        flag = True
        # noinspection PyBroadException
        try:
            self.driver.implicitly_wait(6)

            # 關掉【新手教學頁】
            init(self)

            # 大頭貼btn
            self.driver.find_element_by_xpath("//*[@text='我的']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_id('com.tvbs.supertastemvppack:id/iv_member').click()
            self.driver.implicitly_wait(3)

            # 【會員登入頁】完成Facebook登入，並檢查有登入成功
            facebookLogin(self)

            # # 驗證FB會員名字
            # fb_member_name = self.driver.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/tv_member_name')
            # fb_member_name_text = fb_member_name.text
            # self.assertEqual(fb_member_name_text, 'Jack Tsao')
            # print('\nFB會員登入成功且名字正確，此次登入用戶名稱為 : ' + fb_member_name_text)
            # self.driver.implicitly_wait(3)
            # self.driver.swipe(900, 1500, 900, 200)
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/iv_Logout'))
            #
            # # 驗證登出相關文字
            # self.driver.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/iv_Logout').click()
            # self.driver.implicitly_wait(10)
            # dialog_text = self.driver.find_element_by_id('android:id/message').text
            # self.assertEqual(dialog_text, '你確定要登出嗎？')
            # print('登出跳出dialog : ' + dialog_text)
            # confirm_btn_text = self.driver.find_element_by_id('android:id/button1').text
            # self.assertEqual(confirm_btn_text, '含淚登出')
            # print('確定登出按鈕wording : ' + confirm_btn_text)
            # cancel_btn_text = self.driver.find_element_by_id('android:id/button2').text
            # self.assertEqual(cancel_btn_text, '再想一下')
            # print('取消登出按鈕wording : ' + cancel_btn_text)
            #
            # # 驗證登出相關行為
            # self.driver.find_element_by_id('android:id/button2').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/iv_Logout'))
            # print('取消登出按鈕功能正常')
            # self.driver.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/iv_Logout').click()
            # self.driver.implicitly_wait(10)
            # self.driver.find_element_by_id('android:id/button1').click()
            # WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_id(
            #     'com.tvbs.supertastemvppack:id/iv_Login'))
            # print('確定登出按鈕功能正常')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot(
                    '../../../screenshot/supertasteAppFail/memberCenterLoginFB_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = ('../../../report/supertasteAppReport/supertaste_App_Report_{}.html'.format(current_time))
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(SuperTaste('test_memberCenterRegisterPageUICheck'))  # 【會員註冊頁】UI檢查    #2021.03.26 Pass
    # suite.addTest(SuperTaste('test_memberCenterRegisterPageFacebookRegister'))  # 【會員註冊頁】Facebook註冊（在測試環境沒那麼多註冊過FB developer的帳號，難以執行自動化）
    # suite.addTest(SuperTaste('test_memberCenterRegisterPageFacebookLogin'))  # 【會員註冊頁】Facebook登入   #2021.03.26 Pass
    # suite.addTest(SuperTaste('test_memberCenterRegisterPageEmailRegisterErrorCheck'))  # 【會員註冊頁】Email註冊欄位錯誤檢查    #2021.03.29 Pass
    # suite.addTest(SuperTaste('test_memberCenterRegisterEmailRegister'))  # 【會員註冊頁】Email註冊（但還無法到信箱點擊認證信） #2021.03.29 Pass
    # suite.addTest(SuperTaste('test_memberCenterLoginPageUICheck'))  # 【會員登入頁】UI檢查   #2021.03.29 Pass
    # suite.addTest(SuperTaste('test_memberCenterLoginPageFacebookLogin'))  # 【會員登入頁】Facebook登入   #2021.03.29 Pass
    # suite.addTest(SuperTaste('test_memberCenterLoginPageEmailLoginErrorCheck'))  # 【會員登入頁】Email登入欄位錯誤檢查   #2021.03.29 Pass
    # suite.addTest(SuperTaste('test_memberCenterLoginPageEmailLogin'))  # 【會員登入頁】Email登入   #2021.03.29 Pass
    # suite.addTest(SuperTaste('test_checkFBName'))  # 檢查FB名稱（暫時不想做這項檢查）

    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='SuperTaste App Test Report')
    runner.run(suite)
