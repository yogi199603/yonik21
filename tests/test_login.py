import pytest
from pages.login_page import Loginpage

def test_valid_data(page):
    login_page= Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com","Test@123")
    toast_locator = page.wait_for_selector('//div[text()="Login successful."]')
    toast_text = toast_locator.text_content()
    assert 'Login successful.'in toast_text


def test_invalid_data(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("binserwerller@yopmail.com", "Test@ewre123")
    toast_locator = page.wait_for_selector('//div[text()="User not found."]')
    toast_text=toast_locator.text_content()
    assert 'User not found.' in toast_text

def test_blank_email(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("   ", "   ")
    error_message = page.wait_for_selector('//div[text()="Email is required"]').text_content()
    assert 'Email is required' == error_message

def test_blank_password(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogesh25@gmail.com", "")
    error_message = page.wait_for_selector('//div[text()="Password is required"]').text_content()
    assert 'Password is required' == error_message

def test_password_validation_upper(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com", "as")
    error_message = page.wait_for_selector('//div[text()="Password must contain at least one uppercase letter"]').text_content()
    assert 'Password must contain at least one uppercase letter' == error_message

def test_password_validation_lower(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com", "AS")
    error_message = page.wait_for_selector('//div[text()="Password must contain at least one lowercase letter"]').text_content()
    assert 'Password must contain at least one lowercase letter' == error_message

def test_password_validation_number(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com", "As@")
    error_message = page.wait_for_selector('//div[text()="Password must contain at least one number"]').text_content()
    assert 'Password must contain at least one number' == error_message

def test_password_validation_special_char(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com", "As7")
    error_message = page.wait_for_selector('//div[text()="Password must contain at least one special character"]').text_content()
    assert 'Password must contain at least one special character' == error_message

def test_password_length(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com", "As7@")
    error_message = page.wait_for_selector('//div[text()="Password must be at least 8 characters"]').text_content()
    assert 'Password must be at least 8 characters' == error_message

