import pytest
from page_objects.page_factory import PageFactory
import random
import string
from selenium.webdriver.support.ui import Select

class TestPositiveScenarios:

    @pytest.positive
    def page_factory(driver):
        return PageFactory(driver)
    
    def test_positive_register(page_factory): #成功完成預約
        #為了要使用page object，需要先創建該page class的instance，故page_0000為GetStart這個類別的實例
        page_0000 = page_factory.get_page("0000")
        page_0000.open()
        page_0000.execute_get_start()

        #page_1000
        page_1000 = page_factory.get_page("1000")
        page_1000.select_yes_option()
        page_1000.click_continue()
    
        #page_1001
        page_1001 = page_factory.get_page("1001")
        page_1001.select_age_button()
        page_1001.select_policy()
        page_1001.click_continue()

        #page_1002(挑選第一個地址)
        page_1002 = page_factory.get_page("1002")
        page_1002.first_address()

        #page_1003
        page_1003 = page_factory.get_page("1003")
        page_1003.agree_complexity_statement()

        #page_1004
        page_1004 = page_factory.get_page("1004")
        page_1004.agree_substance_policy()

        #page_1005
        page_1005 = page_factory.get_page("1005")
        date_of_birth = "08/08/1998"
        address1, city = "test"
        zip1 = "12345"

        def generate_random_name():
            first_name = 'test_' + "".join(random.choices(string.ascii_letters, k=5))
            last_name = 'test_' + "".join(random.choices(string.ascii_letters, k=5))
            return first_name, last_name

        def generate_random_phone_number():
            return ''.join(random.choices(string.digits, k=10))

        def generate_random_email():
            email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@gmail.com'
            return email

        first_name, last_name =generate_random_name()
        phone_numer = generate_random_phone_number()
        email = generate_random_email()
        page_1005.execute_information(first_name, last_name, date_of_birth, phone_numer,
                                      email, address1, city, zip1)

        #page_1005_01
        page_1005_01 = page_factory.get_page("1005_01")
        page_1005_01.select_option("SocialMedia")
        page_1005_01.click_continue()