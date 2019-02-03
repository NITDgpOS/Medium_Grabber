from selenium import webdriver
import time
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from collections import OrderedDict
from itertools import repeat
from fpdf import FPDF
from cred import username,password
import platform
if platform.system()=='Windows':
    import winsound

while True:
    print( """Choose the browser you want to use:(Enter the appropriate number)\n
                1---> firefox \n
                2---> chrome \n 
                0--->exit""")
    choice = int(input())

    if choice==1:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        break
    elif choice==2:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)
        break
    elif choice==0:
        quit()
    else:
        print("Please enter a valid choice")

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
assert "Sign in – Google accounts" in driver.title
user = driver.find_element_by_xpath('//*[@id="identifierId"]')
# Enter your email or phone number as registered in Medium
user.send_keys(username) # Provide your email or registered phone number here

nextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
nextButton.click()
time.sleep(2)

user = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

# Place just your password in the pass.txt file
user.send_keys(password)

LOG = driver.find_element_by_xpath('//*[@id="passwordNext"]/content').click()
try:
    time.sleep(5)                 
    driver.find_element_by_xpath('//*[@id="headingText"]/content/text()').text
    # detects If 2 step verification is active
    if text== '2-Step Verification':
        print("You are using 2 step verification. Please turn it off before running the code")
        exit()
except :
    pass
finally:
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
        t = driver.get("https://medium.com/");
    elif topic<9:
        t = driver.get("https://medium.com/topic/"+topics[topic]);
    else:
        print('Please select a correct topic.')

    print('The list of articles under this topic are saved as output.txt text file : ')
    # print('Just scan through the file and open the link whichever you want to read    :)  \n')
    print('The program is crawling down the webpage to gather links of around past 50 atricles. This may take around a minute or two.')

    # To Scroll to the bottom/ a portion of page
    last_height = 1000
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height >= last_height:
            break

    tag = driver.find_elements_by_tag_name('h3')
    tag_len = len(tag)
    links = [i.get_attribute('href') for i in driver.find_elements_by_xpath("//a[@data-action-source]")]
    unique_list = list(OrderedDict(zip(links, repeat(None)))) # To remove duplicates from list


    print("\n\nChoose between PDF or txt format:")
    txt_pdf = int(input("Enter 1--->PDF\n      2--->Text\n"))

    if txt_pdf == 1:
        title = 'Medium Grabber'
        pdf = FPDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_title(title)
        pdf.set_font('Times', 'B', 24)
        pdf.cell(0, 10, 'Medium Grabber Links: ', 0, 1)
        pdf.set_font('Times', '', 12)
        if topic==0:               # Different structure of Home and other topic pages.
            if tag_len > 0:
                for i,l in zip(range(tag_len), unique_list):
                    pdf.set_text_color(r=0, g=0, b=0)
                    pdf.cell(0, 6, str(time.strftime("%Y-%m-%d %H:%M")), 0, 1)
                    text = tag[i].text.encode('latin-1', 'ignore')
                    text = text.decode('latin-1')
                    pdf.cell(0, 6, text , 0, 1)
                    pdf.set_text_color(r=0, g=0, b=250)
                    pdf.multi_cell(0, 6, str(l), 0)
                    pdf.cell(0, 6, ' ', 0, 1)
        else:
            for i in range(tag_len):
                pdf.set_text_color(r=0, g=0, b=0)
                pdf.cell(0, 6, time.strftime("%Y-%m-%d %H:%M"), 0, 1)
                text = tag[i].text.encode('latin-1', 'ignore')
                text = text.decode('latin-1')
                pdf.cell(0, 6,text, 0, 1)
                l = tag[i].find_element_by_css_selector('a').get_attribute('href')
                pdf.set_text_color(r=0, g=0, b=250)
                pdf.multi_cell(0, 6, str(l), 0)
                pdf.cell(0, 6, ' ', 0, 1)
        pdf.output('output.pdf', 'F')
        print('FINISHED! Please check the output.pdf file for the links. Happy reading. :) ')

    elif txt_pdf == 2:
        f= open("output.txt","a+", encoding='utf8') # Stores ouput in output.txt in the same file directory
        if topic==0:               # Different structure of Home and other topic pages.
            if tag_len > 0:
                for i,l in zip(range(tag_len), unique_list):
                    f.write(time.strftime("%Y-%m-%d %H:%M") + '\n')
                    f.write(tag[i].text)
                    f.write('\nLink is -->   ' + str(l)  + '\n\n')
            else:
                for i in range(tag_len):
                    f.write(time.strftime("%Y-%m-%d %H:%M") + '\n')
                    f.write(tag[i].text)
                    l = tag[i].find_element_by_css_selector('a').get_attribute('href');
                    f.write('\nLink is -->   ' + str(l)  + '\n\n')

        f.close()
        print('FINISHED! Please check the output.txt file for the links. Happy reading. :) ')

    else:
        print('Invalid input.')


    driver.close()
    duration = 2500  # millisecond
    freq = 440  # Hz
    if platform.system()=='Windows':
        winsound.Beep(freq, duration)