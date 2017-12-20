from selenium import webdriver
import time
import pyperclip
import pdfkit
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from collections import OrderedDict
from itertools import repeat
import winsound

driver = webdriver.Firefox()
driver.get("https://medium.com/")
driver.implicitly_wait(10)
#action = webdriver.ActionChains(driver)
time.sleep(2)

login = driver.find_element_by_link_text('Sign in').click()

try:
    login_google = driver.find_element_by_xpath('/html/body/div[4]/div/div/section/div[1]/div/button[1]').click()
except TimeoutException:
    pass

# You can log-in using google only
print(" Logging in to Medium by using Google ")
time.sleep(3)

user = driver.find_element_by_xpath('//*[@id="identifierId"]')
# Enter your email or phone number as registered in Medium
user.send_keys('EMAIL/PHONE NUMBER') # Provide your email or registered phone number here

nextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
nextButton.click()
time.sleep(2)

user = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

# Place just your password in the pass.txt file
with open('pass.txt', 'r') as f:
    Password = f.read().replace('\n', '')
user.send_keys(Password)

LOG = driver.find_element_by_xpath('//*[@id="passwordNext"]/content').click()
print('LOGIN SUCCESSFUL \n')

topics = {
    0: 'Home',
    1: 'Technology',
    2: 'Culture',
    3: 'Entrepreneurship',
    4: 'Creativity',
    5: 'Self',
    6: 'Productivity',
    7: 'Design',
    8: 'Popular'
}
print('  Where would you like to dive in?  ')
print(  """            0--> HOME\ \n
            1-->TECHNOLOGY\ \n
            2-->CULTURE \ \n
            3-->ENTREPRENEURSHIP\ \n
            4-->CREATIVITY\ \n
            5-->SELF\ \n
            6-->PRODUCTIVITY\ \n
            7-->DESIGN \n
            8-->POPULAR  """ )
try:
    topic = int(input())
    output = 'You Chose ' + topics[topic]
    print(output)
except:
    print('Select a valid topic')

if topic == 0:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[1]/a').click()
elif topic == 1:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[2]/a').click()
elif topic == 2:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[3]/a').click()
elif topic == 3:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[4]/a').click()
elif topic == 4:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[5]/a').click()
elif topic == 5:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[6]/a').click()
elif topic == 6:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[9]/a').click()
elif topic == 7:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[10]/a').click()
elif topic == 8:
    t = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/nav/ul/div/div[2]/div/li[11]/a').click()
else:
    print('Please select a correct topic.')

print('The list of articles under this topic are saved as output.txt text file : ')
# print('Just scan through the file and open the link whichever you want to read    :)  \n')
print('The program is crawling down the webpage to gather links of around past 50 atricles. This may take around a minute or two.')

# To Scroll to the bottom/ a portion of page
last_height = 50000
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height >= last_height:
        break

tag = driver.find_elements_by_tag_name('h3')
tag_len = len(tag)

links = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//a[@data-action-source]")]
unique_list = list(OrderedDict(zip(links, repeat(None)))) # To remove duplicates from list

f= open("output.txt","a+") # Stores ouput in output.txt in the same file directory
if tag_len > 0:
    for i,l in zip(range(tag_len), unique_list):
        f.write(time.strftime("%Y-%m-%d %H:%M") + '\n')
        f.write(tag[i].text)
        f.write('\nLink is -->   ' + str(l)  + '\n\n')

print('FINISHED! Please check the output.txt file for the links. Happy reading. :) ')

duration = 2500  # millisecond
freq = 440  # Hz
winsound.Beep(freq, duration)
