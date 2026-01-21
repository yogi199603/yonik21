from pages.signup_page import Signup

def test_valid_data(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("Yogi", "pal", "yojaai@yopmail.com", "Test@123")
    page.select_option('//select[@id="gender"]',label='Male')
    error_message= page.wait_for_selector("//div[contains(text(),'Please check your email for the verification link')]").text_content()
    assert "Please check your email for the verification link" == error_message

def test_already_registered(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("Yogi", "pal", "yoji@yopmail.com", "Test@123")
    page.select_option('//select[@id="gender"]',label='Male')
    error_message= page.wait_for_selector("//div[text()='Account already exits with this email.']").text_content()
    assert "Account already exits with this email." == error_message

#check validation in all fields

def test_name_validation(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("","pal","yonik@yopmail.com","test@123")
    page.select_option('//select[@id="gender"]', label="Male")
    error_message = page.wait_for_selector('//div[text()="First name is required"]').text_content()
    assert "First name is required" == error_message

def test_last_validation(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("yogi","","yonik@yopmail.com","test@123")
    page.select_option('//select[@id="gender"]', label="Male")
    error_message = page.wait_for_selector('//div[text()="Last name is required"]').text_content()
    assert "Last name is required" == error_message

def test_email_validation(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("yogi","","","test@123")
    page.select_option('//select[@id="gender"]', label="Male")
    error_message = page.wait_for_selector('//div[text()="Email is required"]').text_content()
    assert "Email is required" == error_message

def test_password_validation(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("yogi","pal","yonik@yopmail.com","")
    page.select_option('//select[@id="gender"]', label="Male")
    error_message = page.wait_for_selector('//div[text()="Password is required"]').text_content()
    assert "Password is required" == error_message

def test_dob_validation(page):
    sign_up= Signup(page)
    sign_up.open()
    sign_up.signup("yogi","pal","yonik@yopmail.com","Test@123")
    page.select_option('//select[@id="gender"]', label="Male")
    sign_up.set_dob("02/05/1996")
    page.wait_for_timeout(2000)

















