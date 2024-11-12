from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class HearAboutUs(BasePage):
    __options = {
        "SocialMedia": (By.NAME, "SocialMedia"),
        "WebSearch": (By.NAME, "WebSearch"),
        "FlyerOrBrochure": (By.NAME, "FlyerOrBrochure"),
        "CurrentOrPreviousPatientReferred": (By.NAME, "CurrentOrPreviousPatientReferred"),
        "DoctorReferredMe": (By.NAME, "DoctorReferredMe"),
        "TherapistReferredMe": (By.NAME, "TherapistReferredMe"),
        "CollegeOrUniversityReferredMe": (By.NAME, "CollegeOrUniversityReferredMe"),
        "Other": (By.NAME, "other"),
    }
    __continue_button = (By.XPATH, "/html//section[@id='docmentSignature']/app-falcon/app-container//button[.=' Continue ']")
    __save_exit_button = (By.LINK_TEXT, "Save & Exit")


    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def select_option(self, option_name: str):
        """
        根據選項名稱點擊對應的選項
        :param option_name: 選項的名稱，如 'SocialMedia', 'WebSearch' 等
        """
        if option_name in self.__options:
            option_locator = self.__options[option_name]
            self.click(option_locator)
        else:
            raise ValueError(f"未知的選項: {option_name}")

    def click_continue(self):
        super()._click(self.__continue_button)

    def click_save_exit(self):
        super()._click(self.__save_exit_button)
