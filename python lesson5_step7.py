from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html" 
#link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
input1.send_keys("Peter")
input2 = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
input2.send_keys("Bulochkin")
input3 = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
input3.send_keys('PetBull@gmail.com')

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
