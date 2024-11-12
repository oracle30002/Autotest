from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class ComplexityStatement(BasePage):
    __policy_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']//app-checkbox-page/app-checkbox/div[@class='my-3']//input[@name='option.key']")
    __continue_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//button[.=' Continue ']")
    __view_resource = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//a[@href='https://d117755cb8dh4.cloudfront.net/macaw/denied/Alternative-Resources.pdf']/span[.=' View Resources ']")

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def agree_complexity_statement(self):
        super()._click(self.__policy_button)
        super()._click(self.__continue_button)

    def click_view_resources(self):
        super()._click(self.__view_resource)