from lib.util.Logger import get_module_logger


class Home:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_harajuku_url(self):
        elem = self.driver.find_element_by_xpath("//*[@id='top_area_wrap']/div/div/ul/li[1]/div/div/h2/a")
        self.logger.debug(elem.get_attribute('href'))
        return elem.get_attribute('href')
