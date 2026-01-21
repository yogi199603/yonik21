def test_password_len(page):
    login_page = Loginpage(page)
    login_page.open()
    login_page.login("yogeshly24@gmail.com", "As7@")
    error_message = page.wait_for_selector('//div[text()="Password must be at least 8 characters"]').text_content()
    assert 'Password must be at least 8 characters' == error_message