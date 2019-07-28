from selenium import webdriver
link = "http://the-internet.herokuapp.com"
import time
browser = webdriver.Chrome()

browser.get(link)
time.sleep(2)
mainPageRedirectLink= browser.find_elements_by_xpath('//a[text()="Redirect Link"]')[0]
mainPageRedirectLink.click()
time.sleep(2)
redirect = browser.find_element_by_id("redirect")
redirect.click()
time.sleep(2)
#get 301 status code
responseRedirect = browser.find_elements_by_css_selector('a[href*="301"]')[0]
responseRedirect.click()
time.sleep(1)
statusCodesLink = browser.find_elements_by_css_selector('a[href*="status_codes"]')[0]
statusCodesLink.click()
time.sleep(1)
#get 404 status code
responseClientError = browser.find_elements_by_xpath('//a[text()="404"]')[0]
responseClientError.click()
time.sleep(1)
statusCodesLink = browser.find_elements_by_css_selector('a[href*="status_codes"]')[0]
statusCodesLink.click()
time.sleep(1)
#get 500 status code
responseServerError = browser.find_elements_by_xpath('//a[text()="500"]')[0]
responseServerError.click()
time.sleep(1)
statusCodesLink = browser.find_elements_by_css_selector('a[href*="status_codes"]')[0]
statusCodesLink.click()
time.sleep(1)
#get 200 status code
responseOk= browser.find_elements_by_xpath('//a[text()="200"]')[0]
responseOk.click()
time.sleep(2)
browser.quit()