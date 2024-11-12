
from http.client import ImproperConnectionState
from page_objects.page_0000 import GetStart
from page_objects.page_1000 import AboutOurServices
from page_objects.page_1001 import PatientCriterial
from page_objects.page_1002 import ChooseAddress
from page_objects.page_1003 import ComplexityStatement
from page_objects.page_1004 import SubstancePolicy
from page_objects.page_1005 import ContactInformation
from page_objects.page_1005_01 import HearAboutUs

# 利用page factory來將所有page做import，並利用get_page的功能來獲取所需的頁面class
class PageFactory():
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_page(self, page_name):
        if page_name == "0000":
            return GetStart(self.driver)
        elif page_name == "1000":
            return AboutOurServices(self.driver)
        elif page_name == "1001":
            return PatientCriterial(self.driver)
        elif page_name == "1002":
            return ChooseAddress(self.driver)
        elif page_name == "1003":
            return ComplexityStatement(self.driver)
        elif page_name == "1004":
            return SubstancePolicy(self.driver)
        elif page_name == "1005":
            return ContactInformation(self.driver)
        elif page_name == "1005_01":
            return HearAboutUs(self.driver)
        

        else:
            raise ValueError(f"Unknown page: {page_name}")
        