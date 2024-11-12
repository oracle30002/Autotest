from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base_page import BasePage

#繼承BasePage的所有function，利用super()來存取父類別的function
class GetStart(BasePage):
    # 在class中，私有的變數宣告是使用__
    __url = "https://d1b940qs9sadm5.cloudfront.net/referralForm/falcon#/referralForm/falcon"
    # 使用tuple來儲存locator(tuple用來存放單個變量但是有多個項目，且為unchangable)
    __get_start_button = (By.XPATH, "/html/body/app-root/app-referral-form/section/app-falcon/app-landing-page/app-container/div/div/div/div/div[2]/div[2]/button")

    # base page object 需要driver變數，故需要使用父類別的init功能，而非創建local的driver變數
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_get_start(self):
        super()._click(self.__get_start_button)

