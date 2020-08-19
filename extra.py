from selenium.webdriver import Chrome
from time import sleep as delay
from selenium.webdriver.support.ui import WebDriverWait

def wait(option, name, driver, time = 10):
    if option == "name":
        return WebDriverWait(driver,time).until(lambda d : d.find_element_by_name(name))
    elif option == "id":
        return WebDriverWait(driver,time).until(lambda d : d.find_element_by_id(name))
    elif option == "xpath":
        return WebDriverWait(driver,time).until(lambda d : d.find_element_by_xpath(name))

def waitall(option, name, driver, time = 10):
    if option == "class":
        return WebDriverWait(driver,time).until(lambda d : d.find_elements_by_class_name(name))
    elif option == "xpath":
        return WebDriverWait(driver,time).until(lambda d : d.find_elements_by_xpath(name))