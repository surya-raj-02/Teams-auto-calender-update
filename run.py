import time
import random
import utils
import argparse
import log
from getpass import getpass

parser = argparse.ArgumentParser(description='Show browser window or not')
parser.add_argument('--show-browser', '-b', action='store_true',
                    help='Show browser window', dest='show_browser')
args = parser.parse_args()
driver = utils.make_driver(args.show_browser)
load = utils.load(driver)
load_all = utils.load_all(driver)

def human_delay(start=1, end=3):
    time.sleep(random.randrange(start, end))

def main():

    username = input("Enter your Teams email-id: ")
    password = getpass()
    driver.get("https://teams.microsoft.com")
    email_form = load("name","loginfmt")
    email_form.send_keys(username)
    human_delay()
    load("id","idSIButton9").click()
    password_form = load("xpath","//input[@class = 'form-control input ext-input text-box ext-text-box']")
    password_form.send_keys(password)
    human_delay()
    load("xpath","//input[@type='submit']").click()
    load("xpath","//input[@class = 'button ext-button secondary ext-secondary']").click()
    log.info('Logged you in.')
    try:
        all_classrooms = len(load_all("class","team-card"))
        log.info('Found all your teams. YAY.')
    except Exception as e:
        log.error('Something went wrong; Probably that your teams are in some weird messed up way.')
        exit()
    for classroom_id in range(all_classrooms):
        classrooms = load_all("class","team-card")
        classrooms[classroom_id].click()
        human_delay()
        
        try:
            all_classes = load_all("xpath","//div[@title = 'Click to see details of this meeting']")
            class_number = len(all_classes)
            if class_number > 1:
                for class_id in range(class_number):
                    classes = load_all("xpath","//div[@title = 'Click to see details of this meeting']")
                    class_name = classes[class_id].find_element_by_class_name('title-icon').text
                    classes[class_id].click()
                    human_delay()
                    class_time = load('xpath',
                        '//*[@id="page-content-wrapper"]/div[1]/div/div/'
                        'calendar-dialog-bridge/div/div[2]/div[2]/div/div[1]/div/div/'
                        'div/div[1]/div/div/div[1]/label').text
                    try:
                        load("xpath","//button[@data-tid='calv2-sf-add-to-calendar']").click()
                        log.info(f'{class_name} added to calendar.\n'+' '*31+
                                   f'It is scheduled for {class_time}')
                        
                    except:
                        log.warn(f'{class_name} is already in calendar.\n'+' '*31+
                                   f'It is scheduled for {class_time}')
                        log.warn('It might also have been another issue, the code is not perfect yet.')
                    human_delay()
                    driver.back()
            else:
                class_name = all_classes[0].find_element_by_class_name('title-icon').text
                all_classes[0].click()
                human_delay()
                class_time = load('xpath',
                    '//*[@id="page-content-wrapper"]/div[1]/div/div/'
                    'calendar-dialog-bridge/div/div[2]/div[2]/div/div[1]/div/div/'
                    'div/div[1]/div/div/div[1]/label').text
                try:
                    load("xpath","//button[@data-tid='calv2-sf-add-to-calendar']").click()
                    log.info(f'{class_name} added to calendar.\n'+' '*31+
                                f'It is scheduled for {class_time}')
                except:
                    log.warn(f'{class_name} is already in calendar.\n'+' '*31+
                                f'It is scheduled for {class_time}')
                    log.warn('It might also have been another issue, the code is not perfect yet.')
                human_delay()
                driver.back()
        except Exception as e:
            print(f'Exception: {e}')
            log.warn("Looks like you don't have any classes in this classroom, or something else went wrong.")
        try:
            load("xpath","//button[@class = 'school-app-back-button ts-sym app-icons-fill-hover app-icons-fill-focus button-command focus-round-border']").click()
        except:
            load("xpath","//button[@id = 'app-bar-66aeee93-507d-479a-a3ef-8f494af43945']").click()
        human_delay()
    load("xpath","//button[@id = 'app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c']").click()
    human_delay()
    #upcoming = load_all("css","div.node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__eventCard--h5y4X",driver)
    #running = load_all("class","node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__eventCard--h5y4X node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__activeCall--25Ch-",driver)
    #print("upcoming:",len(upcoming))
    #print("running:",len(running))
    #print("Thank you for running the code and giving me all your details.... Just kidding.. the code is open-source it is safe... check for yourself.")
    print('#FREEATTENDANCEFTW')
    driver.quit()


if __name__ == "__main__":
    main()
