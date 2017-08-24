from lib.util.Logger import get_module_logger


class Home:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_top_area_wrap(self):
        return self.driver.find_element_by_id('top_area_wrap')

    def get_city_list(self):
        elems = self.get_top_area_wrap().find_elements_by_class_name('cms_list')
        for elm in elems:
            self.logger.debug(elm.get_attribute('data-published'))

    def get_area_urls(self):
        urls = []
        elements = self.driver.find_elements_by_xpath("//h2[@class='title_parts01 title_type02']")
        self.logger.debug(len(elements))
        for elm in elements:
            a_elem = elm.find_element_by_tag_name('a')
            url = a_elem.get_attribute('href')
            if 'tokyo-streetstyle' in url:
                urls.append(url)

        self.logger.debug(urls)
        return urls

    def get_harajuku_url(self):
        elem = self.driver.find_element_by_xpath("//*[@id='top_area_wrap']/div/div/ul/li[1]/div/div/h2/a")
        self.logger.debug(elem.get_attribute('href'))
        return elem.get_attribute('href')

    def open_harajuku_page(self):
        self.driver.get(self.get_harajuku_url())
        from lib.pom.Harajuku import Harajuku
        return Harajuku(self.driver)
