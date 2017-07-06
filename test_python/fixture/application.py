__author__ = 'NovikovII'

from selenium import webdriver


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognixed brouser %s" % browser)
        self.base_url = base_url


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("Login").click()
        wd.find_element_by_name("Login").clear()
        wd.find_element_by_name("Login").send_keys(username)
        wd.find_element_by_name("Password").click()
        wd.find_element_by_name("Password").clear()
        wd.find_element_by_name("Password").send_keys(password)
        wd.find_element_by_id("mailbox__auth__button").click()

    def logout(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("выход").click()

    def send_mail(self, to_mail, text):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("Написать письмо").click()
        wd.find_element_by_css_selector("textarea.js-input.compose__labels__input").send_keys(to_mail)
        wd.find_element_by_link_text("Убрать оформление").click()
        wd.find_element_by_name("Body").send_keys(text)
        wd.find_element_by_xpath("//div[@id='b-toolbar__right']//span[.='Отправить']").click()

    def destroy(self):
        self.wd.quit()