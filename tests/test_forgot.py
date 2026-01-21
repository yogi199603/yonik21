import pytest
from pages.forgot_page import Forgot

def test_valid_forgot(page):
    forgot= Forgot(page)
    forgot.open()
    forgot.forgot('yogeshly24@gmail.com')
    error_message = page.wait_for_selector("//div[text()='Code sent successfully']").text_content()
    assert "Code sent successfully" == error_message

def test_invalid_email(page):
    forgot= Forgot(page)
    forgot.open()
    forgot.forgot('yog')
    error_message= page.wait_for_selector('//div[text()="Invalid email address"]').text_content()
    assert "Invalid email address" == error_message

def test_non_rig_email(page):
    for_got = Forgot(page)
    for_got.open()
    for_got.forgot('yuihhu@yopmail.com')
    tost_message= page.wait_for_selector('//div[text()="This email is not registered"]').text_content()
    assert "This email is not registered"==tost_message

def test_blank_data(page):
    for_blank = Forgot(page)
    for_blank.open()
    for_blank.forgot("")
    error_message = page.wait_for_selector("//div[text()='Email is required']").text_content()
    assert "Email is required" == error_message