import time
from time import sleep
from selenium import webdriver


browser = webdriver.Chrome(r"C:\Users\Akhilesh\Desktop\html\chromedriver")
browser.implicitly_wait(2)
browser.get('https://www.yelp.com/')
username_input = browser.find_element_by_xpath('//*[@maxlength="64"]')

username_input.send_keys("KFC")

sleep(2)
login_button = browser.find_element_by_xpath('//*[@value="submit"]')
login_button.click()
sleep(5)
follow_button = browser.find_element_by_xpath('//*[@class="css-166la90"]')
follow_button.click()
sleep(5)

sleep(10)

for i in range(5):
        f_button = list(browser.find_elements_by_xpath('//*[@class="fs-block css-m6anxm"]'))
        print(f_button[i+1].text)
        foow_button =list(browser.find_elements_by_xpath('//*[@class="comment__373c0__1M-px css-n6i4z7"]'))
        print(foow_button[i].text)

       
        

       

