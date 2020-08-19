from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep as delay
from selenium.webdriver.support.ui import WebDriverWait
import random
from extra import wait, waitall
import sys

def main():

    mail = input("Enter teams username:")
    passw = input("Enter teams password:")

    try:
        x = sys.argv[1]
        if x == "-o" or "--show-output":
            driver = Chrome()
        else:
            chromeOptions = Options()
            chromeOptions.add_argument('headless')
            driver = Chrome(options=chromeOptions)
    except:
        chromeOptions = Options()
        chromeOptions.add_argument('headless')
        driver = Chrome(options=chromeOptions)

    driver.get("https://teams.microsoft.com")
    email = wait("name","loginfmt",driver)
    email.send_keys(mail)
    delay(random.randint(1,3))
    wait("id","idSIButton9",driver).click()
    print("Sent mail id to teams")
    delay(random.randint(1,3))
    password = wait("xpath","//input[@class = 'form-control input ext-input text-box ext-text-box']",driver)
    password.send_keys(passw)
    delay(random.randint(1,3))
    wait("xpath","//input[@type='submit']",driver).click()
    print("Sent password to teams")
    try:
        delay(random.randint(1,3))
        wait("xpath","//input[@class = 'button ext-button secondary ext-secondary']",driver).click()
        delay(random.randint(1,3))
        print("Just sit back and relax")
    except:
        print("Just sit back and relax")
    try:
        teams = waitall("class","team-card",driver,20)
        print("Got all ur the teams ;)")
    except:
        print("Ur teams are not organized according to this code... usually code is supposed to handle this... but this code was made for a very small set of people... if you want the feature included... let me know")
        exit()
    delay(random.randint(1,3))
    i = 0
    while teams:
        teams1 = waitall("class","team-card",driver,20)
        teams1[i].click()
        delay(random.randint(1,3))
        try:
            meets = waitall("xpath","//div[@title = 'Click to see details of this meeting']",driver)
            if len(meets) > 1:
                print("Too many meetings to handle... but lemme give it a try")
                x = 0
                while meets:
                    meets1 = waitall("xpath","//div[@title = 'Click to see details of this meeting']",driver)
                    meets1[x].click()
                    delay(random.randint(1,3))
                    wait("xpath","//button[@data-tid='calv2-sf-add-to-calendar']",driver).click()
                    x+=1
                    meets.pop(0)
                    delay(random.randint(1,3))
                    driver.back()
            else:
                meets[0].click()
                delay(random.randint(1,3))
                try:
                    wait("xpath","//button[@data-tid='calv2-sf-add-to-calendar']",driver).click()
                    print("Meeting added to calender")
                except:
                    print("Meeting already in Calender.")
                    print("Could also be other issue... code is still in beta\n")
                delay(random.randint(1,3))
                driver.back()
        except:
            print("Looks like you dont have any meetings...")
        delay(random.randint(1,3))
        wait("xpath","//button[@class = 'school-app-back-button ts-sym app-icons-fill-hover app-icons-fill-focus button-command focus-round-border']",driver).click()
        delay(random.randint(1,3))
        i+=1
        teams.pop(0)
    print("Thank you for running the code and giving me all ur details.... Just kidding.. the code is open-source it is safe... check for yourself.")
    delay(5)
    driver.quit()


if __name__ == "__main__":
    main()