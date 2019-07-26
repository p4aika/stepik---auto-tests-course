import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
wait = WebDriverWait(browser, 12).until(
EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button = browser.find_element_by_css_selector("#book")
button.click()
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_css_selector(".form-control")
input1.send_keys(y)
button = browser.find_element_by_css_selector("#solve")
button.click()
driver.quit()
