from lib.util.Logger import get_module_logger


class Harajuku:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_streat_arena_main(self):
        return self.driver.find_element_by_class_name('street_area_main')

    def get_style_list(self):
        elements = self.driver.find_elements_by_xpath("//figure[@class='first_img img_loaded']")
        for elm in elements:
            self.logger.debug(elm.get_attribute('data-image'))
