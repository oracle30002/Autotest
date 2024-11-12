from codecs import latin_1_decode
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import random
import string
from selenium.webdriver.support.ui import Select

class ContactInformation(BasePage):
    __first_name = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[1]//input[@placeholder='First name']")
    __last_name = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[2]//input[@placeholder='Last name']")
    __chosen_name = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[3]//input[@placeholder='Chosen name (Optional)']")
    __date_of_birth = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input-calendar[@class='ng-star-inserted']//nz-date-picker//input[@placeholder='Date of birth (ex. 05/01/1990)']")
    __phone_number = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input-phone[@class='ng-star-inserted']//nz-input-group/input[@type='text']")
    __email = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input-email[@class='ng-star-inserted']//nz-input-group/input[@type='text']")
    __address1 = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[4]//input[@placeholder='Address 1']")
    __address2 = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[5]//input[@placeholder='Address 2']")
    __city = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[6]//input[@placeholder='City']")
    __state = (By.XPATH, "//section[@id='docmentSignature']//app-container//app-dynamic-page/app-dropdown-state[@class='ng-star-inserted']//nz-select/nz-select-top-control[@class='ant-select-selector ng-tns-c2869038095-3']/nz-select-search[@class='ant-select-selection-search ng-star-inserted']/input")
    __state_sc = (By.XPATH, "//div[@id='cdk-overlay-1']/nz-option-container//nz-option-item[@title='SC']/div[@class='ant-select-item-option-content']")
    __zip = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container//app-dynamic-page/app-input[7]//input[@placeholder='Zip']")
    __continue_button = (By.XPATH, "//section[@id='docmentSignature']/app-falcon/app-container/div[@class='h-full w-full']//button[.=' Continue ']")


    def __init__(self, driver:WebDriver):
        super().__init__(driver)
    
    def execute_information(self, first_name: str, last_name: str, chosen_name: str, 
                            date_of_birth: str, phone_number: str, email: str,
                            address1: str, address2: str, city: str, zip1: str):
        super()._type(self.__first_name, first_name)
        super()._type(self.__last_name, last_name)
        super()._type(self.__date_of_birth, date_of_birth)
        super()._type(self.__phone_number, phone_number)
        super()._type(self.__email, email)
        super()._type(self.__address1, address1)
        super()._type(self.__city, city)
        super()._click(self.__state)
        super()._click(self.__state_sc)
        super()._type(self.__zip, zip1)
        super()._click(self.__continue_button)
    