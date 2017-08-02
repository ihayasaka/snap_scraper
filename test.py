from selenium import webdriver

browser = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')

browser.get('http://www.style-arena.jp/')
assert "東京のストリートファッション最新情報 | スタイルアリーナ" in browser.title

elements = browser.find_elements_by_class_name('cms_list_content')
for elem in elements:
    print(elem)

browser.quit()
