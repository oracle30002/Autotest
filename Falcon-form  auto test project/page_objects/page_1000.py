from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class AboutOurServices(BasePage):
    __yes_options = (By.NAME, "yes")
    __no_options = (By.NAME, "no")
    __continue_button = (By.XPATH, "/html/body/app-root/app-referral-form/section/app-falcon/app-container/div/div/div/div/div/button")
    __view_resource = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//a[@href='https://d117755cb8dh4.cloudfront.net/macaw/denied/Alternative-Resources.pdf']/span[.=' View Resources ']")
    

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def select_yes_option(self):
        super()._click(self.__yes_options)
        
    def select_no_option(self):
        super()._click(self.__no_options)

    def click_continue(self):
        super()._click(self.__continue_button)

    def click_view_resources(self):
        super()._click(self.__view_resource)
        