from selenium import webdriver
from lib.pom.Home import Home

browser = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
browser.get('http://www.style-arena.jp/')
assert "東京のストリートファッション最新情報 | スタイルアリーナ" in browser.title

home = Home(browser)
browser.get(home.get_harajuku_url())

browser.quit()
