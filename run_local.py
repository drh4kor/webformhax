from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#load
loginURL='http://localhost/login.html'

binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get(loginURL)

inputElement_id = driver.find_element_by_name('login_id')
inputElement_psw = driver.find_element_by_name('login_pwd')
pathToLink = '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr/td/a'
inputElement_link = driver.find_element_by_xpath(pathToLink)

counter = 0
psw_value=0000
max_value = 10000
print driver.current_url
for x in range(1, max_value):
    print "Loop count %d" % (x)
    inputElement_id.send_keys('admin')
    inputElement_psw.send_keys(x)
    inputElement_link.click()
    newURL = driver.current_url;
    if newURL != current: 
	      #log the current loop value as psw to psw
        break;	
driver.close()
