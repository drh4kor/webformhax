# webformhax
bang bang on the admin login webpage
----------------
Part 1: recon
https://digital-watchdog.com/productdetail/VMAX
admin
Password blank (default)
Use the login.html form as the template for a local apache server on kali

Put the page on /var/www/html/
In kali FireFox open localhost/login.html

The page needs to render, even if there is no CCS. we just want to test the automation part.
If more parts are needed, we’ll need to add those too. Resources like JavaScript and other files that are referenced.  

We want to use this to refine the script that will bang on the actual page.
Target uri: 10.0.0.x (box)
Test uri:   localhost  (kali)

We basically want to know what the page does after it logs in successfully and what DOM object to look for after the login has failed. 

--------------------------------------
Part 2: Testing
Using a framework to automate FireFox called Selenium
This will open a page, enter a sequence of numbers, press a button and wait for the next page to load. If the same page is presented, move on to the next sequence, if the page is not the same on the url bar..winner winner chicken dinner.
The script to run can be from shell script (hard) or preferably python (easy).
The script will log the successful pin.

We need names of the DOM items to manipulate. The names and IDs will help.
HTML IDs and/or HTML names:
Form is actually a set of nested <table> objects :-\
Name: login_id type:input
Name:login_pwd type:input
Button ID:btn_login type:div <dummy object>
Actual DOM object to simulate click: <a onfocus="blur()" onclick="auto_submit()" 






Python examples on using Selenium:
https://selenium-python.readthedocs.io/locating-elements.html

Example: var inputElement = driver.find_element_by_id("login_id")
Example: inputElement.send_keys(Keys.ENTER)
Example: inputElement_link.send_keys(var);
Example: driver.findElement(By.xpath("//a[@href='/docs/configuration']")).click();
Example: getting the link to click on for submission with find_element_by_xpath
Firefox - Inspect Element - Copy - XPATH ;-)


Setup Kali  box
https://selenium-python.readthedocs.io/installation.html
Literature
http://lifeofpentester.blogspot.com/2018/03/selenium-with-python-using-geckodriver.html?m=1
http://lifeofpentester.blogspot.com/2013/10/web-applications-authentication-brute.html?m=1

Running the tests 
place vendor files in /var/www/html
--vmax.html
--dashboard.html
These are modified version for test the framework only. Simulate the real server locally.
After the target URL is added to the .py script, the real vmax.html will be used.

-----------------------------------------
Part 3: Security ByPass
If the box has security measure that prevent the brute force attack, we’ll need to re-write the script to wait or use a proxy chain to modify mac and ip address so the box thinks its a new machine and network.




We won't know most of this until we try our code against the target.

---------------------------
Part 4: Bang Bang!
The fun part is running the script until the page locks or denies access and the next pin can be retired. The kali box will need to loop with local access to the target box.
Update the .py script and change the 'loginURL' variable to the target box.

Possible logins
admin
alma
IT

Things we know:
It has to be 4 numeric values per embedded js
“alert("Password must be a combination of numbers.");”
admin (default) account is immutable



GDrive has prototype .py scripts.

Once it runs on our Kali boxes it's ready for use against target






