from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class SubstancePolicy(BasePage):
    __download_PDF = (By.LINK_TEXT, "Download Full PDF")
    __policy_button = (By.NAME, "option.key")
    __continue_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//button[.=' Continue ']")
    __view_resource = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container[@class='block router-container']/div[@class='h-full w-full']//a[@href='https://d117755cb8dh4.cloudfront.net/macaw/denied/Alternative-Resources.pdf']/span[.=' View Resources ']")

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def agree_substance_policy(self):
        super()._click(self.__policy_button)
        super()._click(self.__continue_button)

    def download_pdf(self):
        super._click(self.__download_PDF)
    
    def click_view_resources(self):
        super()._click(self.__view_resource)
