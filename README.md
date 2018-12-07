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
  Run by typing : ``` python -mrun Grab_that_article_on_Medium.py ```
* Choose whichever article you want by typing in the number as given in options listed.
* Choose the file format of the output, either PDF or Text.
* Wait a few minutes. You'll be notified by a beep sound when the program finsihes running.
* Check the output.txt file in the same directory to get the list of articles along with their links. If you've chosen PDF, Click on the link of the PDF to directly open it in a browser.

Now Browse through them and read whichever interests you.

#### For Linux/Unix


* Download and paste everything under the same roof.
* Put your password in pass.txt and your Email/Phone Number in the space provided in the code.
* Install Selenium python package and firefox webdriver for suitable version of Linux from [here](https://github.com/mozilla/geckodriver/releases). Mention it's path in the code or place it in the same directory.
* Open Terminal in the directory of the repository.
  Run by typing : ``` python Grab_that_article_on_Medium.py ```
* Choose whichever article you want by typing in the number as given in options listed.
![Example of execution](/images/run.png)
* Choose the file format of the output, either PDF or Text.
* Wait a few minutes. You'll be notified by a beep sound when the program finsihes running.
* Check the output.txt file in the same directory to get the list of articles along with their links. If you've chosen PDF, Click on the link of the PDF to directly open it in a browser.
![Example of output](/images/output.png)

The links inside the pdf will be displayed as shown below: 

![Example of output](/images/output_pdf.PNG)


Happy Coding. :sparkles:  :)
