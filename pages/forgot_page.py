class Forgot:

    def __init__(self, page):
        self.page=page

    def open(self):
        self.page.goto('https://suhavi-web-dev.vercel.app/forgotpassword')

    def forgot(self, email):
        self.page.fill('#email', email)
        self.page.click('//button[@type="submit"]')
