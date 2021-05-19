from selenium import webdriver
import time
from names import members
from credentials import user_name,password
import datetime
from selenium.common.exceptions import NoSuchElementException

def init():
    path = "C:\\webdrivers\\chromedriver.exe"
    driver_var = webdriver.Chrome(path)
    driver_var.maximize_window()
    return driver_var


def login(driver):
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    login_username = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    login_username.send_keys(user_name)
    login_password = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    login_password.send_keys(password)
    login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    login_button.click()
    time.sleep(5)
    not_now = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    not_now.click()
    time.sleep(2)
    disable_noti = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    disable_noti.click()
    print("logged in")
    time.sleep(2)


def open_messages(driver):
   driver.get("https://www.instagram.com/direct/inbox/")
   print("Messages Opened")
   time.sleep(5)

def check_xpath(driver,path):
    try:
        driver.find_element_by_xpath(path)
    except NoSuchElementException:
        return False
    return True

def check(driver):
    count = 1
    while(True):
        base_path = "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div["+str(count)+"]"

        time = driver.find_element_by_xpath(base_path+"/a/div/div[2]/div[2]/div/div/time")
        post_time = time.get_attribute("datetime")
        post_time_mod = datetime.datetime.strptime(post_time , '%Y-%m-%dT%H:%M:%S.%fZ')
        elapsed_time = datetime.datetime.utcnow() - post_time_mod

        members_name = driver.find_element_by_xpath(base_path+"/a/div/div[2]/div[1]/div/div/div/div")
        members_username = members_name.text

        if (members_username in members):
            unread_msg = check_xpath(driver,base_path+"/a/div/div[3]/div")
            visible_msg = driver.find_element_by_xpath(base_path+"/a/div/div[2]/div[2]/div/div/span[1]/span")
            validation(driver,members_name.text,unread_msg,visible_msg.text,base_path)
        count+=1
        if (datetime.timedelta(hours=24)<elapsed_time):
            break

def send_confirmation(driver,base_path):
    dm_page = driver.find_element_by_xpath(base_path+"/a/div").click()
    time.sleep(1)
    textarea = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    textarea.send_keys("[OWASP BOT]: Thank you for sharing our Story\n")
    driver.back()

def validation(driver,username,unread,visible_text,base_path):
    if unread and visible_text == "Mentioned you in their story":
        send_confirmation(base_path)
        print(username)

def main():
    driver = init()
    login(driver)
    open_messages(driver)
    check(driver)

if __name__ == '__main__':
    main()
