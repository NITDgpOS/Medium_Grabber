# Medium_Grabber 
[![Join the chat at https://gitter.im/Medium_Grabber/Lobby](https://badges.gitter.im/Medium_Grabber/Lobby.svg)](https://gitter.im/Medium_Grabber/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

WHAT THE HECK IS [MEDIUM](https://medium.com/) ?


**"Medium"** is a place to read, write, and interact with the stories that matter most to you. Every day, thousands of voices read, write, and share important stories on Medium.

### WHAT DOES THIS PROGRAM BRINGS YOU? :


This is an automated program that lets you grab the link of any article in medium under any topic just by logging into your Google-linked-medium account.


* Provides you with all the articles(of medium) and their links in the same text file(output.txt)
* Filters the articles and let's you chose what's most important to you.


### Requirements :


* Selenium (``` pip install selenium ```)
* Web-driver to interface with the chosen browser
* FPDF (`pip install fpdf`)

To run this,

#### For Windows

* Download and paste everything under the same roof.
* Put your password in pass.txt and your Email/Phone Number in the user.txt file.
* Install Selenium python package and firefox/chrome webdriver. Mention it's path or place it in the same directory.
* Put your password in pass.txt and your Email/Phone Number in the space provided in the code.
* Install Selenium python package and firefox webdriver for Windows from [here](https://github.com/mozilla/geckodriver/releases). Mention it's path in the code or place it in the same directory.
* Windows: Open command prompt and cd to the directory.
  Run by typing : ``` python -mrun web_app.py ```
* If prompted in the terminal, enter your credentials and choose whether to save credentials or not.
* Open your browser and go to "http://127.0.0.1:1234/".
* Choose the topic of articles you want as given in the drop-down list.
* Choose the file format of the output, either PDF or Text.
* Click on 'Submit' button.
* Wait a few minutes. You'll be notified by a beep sound when the program finsihes running.

Now browse through the articles and read whichever interests you.

#### For Linux/Unix


* Download and paste everything under the same roof.
* Put your password in pass.txt and your Email/Phone Number in the space provided in the code.
* Install Selenium python package and firefox webdriver for suitable version of Linux from [here](https://github.com/mozilla/geckodriver/releases). Mention it's path in the code or place it in the same directory.
* Open Terminal in the directory of the repository.
  Run by typing : ``` python web_app.py ```
* If prompted in the terminal, enter your credentials and choose whether to save credentials or not.
* Open your browser and go to "http://127.0.0.1:1234/".
* Choose the topic of articles you want as given in the drop-down list.
* Choose the file format of the output, either PDF or Text.
* Click on 'Submit' button.
* Wait a few minutes.

#### NOTE (For Windows and Linux/Unix)


* In order to remove your saved credentials, remove "creds.ge.enc" file. 

![Animation](/animation.gif)

Now browse through the articles and read whichever interests you.
Happy Coding. :sparkles:  :)

