from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class PatientCriterial(BasePage):
    __age_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-checkbox-page/app-checkbox/div[1]//input[@name='option.key']")
    __policy_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-checkbox-page/app-checkbox/div[2]//input[@name='option.key']")
    __continue_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container/div[@class='h-full w-full']//button[.=' Continue ']")
    __view_resource = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container/div[@class='h-full w-full']//a[@href='https://d117755cb8dh4.cloudfront.net/macaw/denied/Alternative-Resources.pdf']/span[@class='ng-star-inserted']")


    def __init__(self, driver:WebDriver):
        super().__init__(driver)
    
    def select_age_button(self):
        super()._click(self.__age_button)
    
    def select_policy(self):
        super()._click(self.__policy_button)
    
    def click_continue(self):
        super()._click(self.__continue_button)

    def click_view_resources(self):
        super()._click(self.__view_resource)
        