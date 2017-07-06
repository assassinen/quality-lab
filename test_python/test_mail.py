__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def test_mail(app):
    app.login("login", "pass")
    time.sleep(1)
    app.send_mail("vananova@mail.ru", "Хочу работать в quality-lab.ru")
    app.logout()

