__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def test_mail(app):
    app.login("login", "pass")
    time.sleep(1)
    app.send_mail("vananova@mail.ru", "Хочу работать в quality-lab.ru")
    app.logout()

# def test_mail(driver):
#     driver.get("https://mail.ru/")
#     driver.find_element_by_name("Login").send_keys("vananova")
#     driver.find_element_by_name("Password").send_keys("alena2010")
#     driver.find_element_by_id("mailbox__auth__button").click()
#     time.sleep(1)
#
#
#     driver.find_element_by_link_text("Написать письмо").click()
#     driver.find_element_by_css_selector("textarea.js-input.compose__labels__input").send_keys("assassinen@ya.ru")
#     driver.find_element_by_link_text("Убрать оформление").click()
#
#     driver.find_element_by_name("Body").send_keys("Хочу работать в quality-lab.ru")
#     driver.find_element_by_xpath("//div[@id='b-toolbar__right']//span[.='Отправить']").click()
#
#     time.sleep(10)
#     driver.find_element_by_link_text("выход").click()
