import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#treasure")
value = x_element.get_attribute("valuex")
x = value
y = calc(x)
input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option1 = browser.find_element_by_css_selector("#robotsRule")
option1.click()
button = browser.find_element_by_css_selector("[type='submit']")
button.click()

