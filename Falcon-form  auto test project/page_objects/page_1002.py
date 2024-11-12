from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class ChooseAddress(BasePage):
    __first_address = (By.NAME, "West Greenville, SC")
    __second_address = (By.NAME, "East Greenville, SC")
    __third_address = (By.NAME, "Seneca, SC")
    __fourth_address = (By.NAME, "Spartanburg, SC")
    __policy_button = (By.NAME, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//app-preference-location//input[@type='checkbox']")
    __continue_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//button[.=' Continue ']")
    __view_resource = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//a[@href='https://d117755cb8dh4.cloudfront.net/macaw/denied/Alternative-Resources.pdf']/span[.=' View Resources ']")


    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def first_address(self):
        super()._click(self.__first_address)
        super()._click(self.__policy_button)
        super()._click(self.__continue_button)

    def second_address(self):
        super()._click(self.__second_address)
        super()._click(self.__policy_button)
        super()._click(self.__continue_button)

    def third_address(self):
        super()._click(self.__third_address)
        super()._click(self.__policy_button)
        super()._click(self.__continue_button)
    
    def fourth_address(self):
        super()._click(self.__fourth_address)
        super()._click(self.__policy_button)
        super()._click(self.__continue_button)
    
    def click_view_resources(self):
        super()._click(self.__view_resource)