import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_css_selector(".form-control")
input1.send_keys(y)
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option1 = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("window.scrollBy(0, 700);")
option1.click()
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 700);", button)
button.click()

