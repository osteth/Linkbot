
# coding: utf-8

# In[ ]:

import time, random, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = 'your linkedin email address'
password = 'your linkedin password'

print("OPENING CHROME")
print("\n")
driver = webdriver.Chrome()
print("Navigating to Login Page")
print('\n')
driver.get("https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in")
time.sleep(5)
account_imput = driver.find_element_by_id("session_key-login")
password_input = driver.find_element_by_id("session_password-login")
print('===============LOGGING IN=================')
print('\n')
time.sleep(5)
account_imput.send_keys(email)
password_input.send_keys(password)
driver.find_element_by_css_selector("#btn-primary").click()
print('Navigation to Netowrk Page')
print('\n')
time.sleep(5)
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)
print('===============================LINKBOT ENGAGED!!!!========================================')
while 1 == 1:
    button_number = str(random.randint(1, 100))
    item = '.'
    print(item, sep=' ', end='', flush=True)
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_css_selector("ul.mn-pymk-list__cards > li:nth-of-type(" + button_number + ") > div.mn-pymk-list__action-container > button.button-secondary-small > span:nth-of-type(1)").click()
    except:
        pass


# In[ ]:




# In[ ]:




# In[ ]:



