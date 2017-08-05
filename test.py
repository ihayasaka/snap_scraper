from selenium import webdriver

browser = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
browser.get('http://www.style-arena.jp/')
assert "東京のストリートファッション最新情報 | スタイルアリーナ" in browser.title

elem = browser.find_element_by_xpath("//*[@id='top_area_wrap']/div/div/ul/li[1]/div/div/h2/a")
print(elem.get_attribute('href'))
browser.get(elem.get_attribute('href'))

browser.quit()
