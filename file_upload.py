from selenium import webdriver
import os
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("sample@email.com")
browser.execute_script("window.scrollBy(0, 120);")
element = browser.find_element_by_css_selector('input[type=file]')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element.send_keys(file_path)
button2 = browser.find_element_by_css_selector("button.btn")
button2.click()