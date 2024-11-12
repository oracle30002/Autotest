from os import times_result
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException

'''
1.在Base Page中將創建幾個Methods代表和頁面的基本操作，如find element、click element、type element等
2.且這些Method只能被其他Page物件存取，無法被test所存取(要使其為Protected)
3.Protect的 Method使用單底線_。
4.網頁測試的所有基本操作:
  a.找尋某個元素(find) b.輸入文字(type) c.等待某個元素出現(wait_until) d.點擊(Click)
  e.查看某元素是否有顯示在螢幕上 f.打開網頁 g.獲得網頁某段文字(get_text)
'''


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator) #利用*可以將tuple解壓縮

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)
    
    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):  #wait的預設值是10秒，即若未指定時間，則將等待至多十秒鐘
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click() 

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)    
        self._find(locator).clear()

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
     
    def _open_url(self, url: str):   
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

