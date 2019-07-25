from selenium import webdriver
import time

browser = webdriver.Chrome()


browser.get("http://the-internet.herokuapp.com/")


formAuthLink= browser.find_elements_by_xpath('//a[text()="Form Authentication"]')[0]
formAuthLink.click()


formAuthentication = browser.find_elements_by_xpath('//*[@id="content"]')[0]


emailInput = browser.find_elements_by_xpath('//input[@type="text"]')[0]
emailInput.send_keys('tomsmith')


passwordInput = browser.find_elements_by_xpath('//input[@type="password"]')[0]
passwordInput.send_keys('SuperSecretPassword!')


submitButton = browser.find_elements_by_xpath('//button[@type="submit"]')[0]
submitButton.submit()
time.sleep(3)

logoutButton = browser.find_elements_by_css_selector('a[href^="/logout"]')[0]
logoutButton.click()
time.sleep(4)

browser.close()
