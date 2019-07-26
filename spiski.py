from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#num1")
x = x_element.text
y_element = browser.find_element_by_css_selector("#num2")
y = y_element.text
z = str(int(x)+int(y))

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z) # ищем элемент с текстом "Python"
button = browser.find_element_by_css_selector("[type='submit']")
button.click()
