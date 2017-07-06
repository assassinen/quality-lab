__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from test_python.fixture.application import Application

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture
def app():
    fixture = Application(browser="chrome", base_url="https://mail.ru/")
    return fixture
