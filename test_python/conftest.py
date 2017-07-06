__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from test_python.fixture.application import Application


@pytest.fixture
def app():
    fixture = Application(browser="chrome", base_url="https://mail.ru/")
    return fixture
