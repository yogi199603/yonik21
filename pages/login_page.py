class Loginpage:

    def __init__(self, page):
        self.page=page
        self.email= "//input[@id='email']"
        self.password= "//input[@id='password']"
        self.submit= "//button[@type='submit']"


    def open(self,):
        self.page.goto("https://suhavi-web-dev.vercel.app/login")

    def login(self, email, password):
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.click(self.submit)

    # def get_toast_message(self) -> str:
    #     toast = self.page.locator(self.toast)
    #     toast.wait_for(state="visible", timeout=5000)
    #     return toast.inner_text()


