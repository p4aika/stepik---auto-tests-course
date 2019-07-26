import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
