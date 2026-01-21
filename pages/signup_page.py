from utils.date_utils import convert_ddmmyyyy_to_iso

class Signup:


    def __init__(self, page):
        self.page= page
        self.first= '//input[@id="firstname"]'
        self.last= "//input[@id='lastname']"
        self.email= "//input[@id='email']"
        self.password= '//input[@id="password"]'
        self.submit= "//button[@type='submit']"

    def open(self):
        self.page.goto("https://suhavi-web-dev.vercel.app/signup")

    def signup(self, first, last, email, password ):
        self.page.fill(self.first, first)
        self.page.fill(self.last, last)
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.click(self.submit)

    # def set_dob(self, dob_ddmmyyyy):
    #     iso_dob = convert_ddmmyyyy_to_iso(dob_ddmmyyyy)
    #     self.page.fill("#dob", iso_dob)

