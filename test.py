from selenium import webdriver
from lib.pom.Home import Home

browser = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
browser.get('http://www.style-arena.jp/')
assert "東京のストリートファッション最新情報 | スタイルアリーナ" in browser.title

home = Home(browser)
home.get_area_urls()
home.get_city_list()
harajuku = home.open_harajuku_page()
harajuku.get_style_list()

browser.quit()
