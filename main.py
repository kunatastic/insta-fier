import time
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from credentials import user_name,password
from names import members


# initializing selenium
def init():
    path = "C:\\webdrivers\\chromedriver.exe"
    driver_var = webdriver.Chrome(path)
    driver_var.maximize_window()
    return driver_var


# instagram login
def login(driver):
    driver.get("https://www.instagram.com/")

    time.sleep(2)
    # credentials
    try:
        login_username = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        login_username.send_keys(user_name)
        login_password = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        login_password.send_keys(password)
        login_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        login_button.click()
    except :
        print("Either password is wrong or Instagram has IP banned you")


    time.sleep(5)
    # don't save password
    try:
        not_now = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        not_now.click()
    except:
        print("The page has not loaded yet increase the sleep above")


    time.sleep(2)
    # disable notification
    try:
        disable_noti = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        disable_noti.click()
    except:
        print("Clicked button already")


    print("logged in")
    time.sleep(2)


#open the messaging tab
def open_messages(driver):
   driver.get("https://www.instagram.com/direct/inbox/")
   print("Messages Opened")
   time.sleep(5)


# _utility: check if the xpath exists
def check_xpath(driver,path):
    try:
        driver.find_element_by_xpath(path)
    except NoSuchElementException:
        return False
    return True


# brain: checks the previous messages
def check(driver,post_time):
    count = 1
    open_messages(driver)
    file = open("A.txt",'a')
    file.writelines(str(datetime.datetime.now())+"\n")
    # time.sleep(10)
    while(True):
        # base xpath for the images component
        base_path  ="/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div["+str(count)+"]"
        # normal   ="/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[2]/div/div/time"
        # business ="/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[2]/a/div/div[2]/div[2]/div/div/time"

        # Scroll
        I = driver.find_element_by_xpath(base_path)
        a = ActionChains(driver)
        a.move_to_element(I).perform()
        time.sleep(2)

        # print("YAHA GadBadi HAI")
        # time of story uploading
        msg_time = driver.find_element_by_xpath(base_path+"/a/div/div[2]/div[2]/div/div/time")
        story_time = msg_time.get_attribute("datetime")
        story_time_mod = datetime.datetime.strptime(story_time , '%Y-%m-%dT%H:%M:%S.%fZ')
        if (story_time_mod < post_time):
            file.close()
            break
        # print("YAHA BHI")

        # username extraction
        members_name = driver.find_element_by_xpath(base_path+"/a/div/div[2]/div[1]/div/div/div/div")
        members_username = members_name.text
        print("MEMBERS:",members_username)
        # username validation and verification
        if (members_username in members):
            # print("MEMBERS:",members_username)
            unread_msg = check_xpath(driver,base_path+"/a/div/div[3]/div")
            visible_msg = driver.find_element_by_xpath(base_path+"/a/div/div[2]/div[2]/div/div/span[1]/span")
            validation(driver,members_name.text,unread_msg,visible_msg.text,base_path,file)
        count+=1
        time.sleep(2)


# sends the confirmation message
def send_confirmation(driver,base_path):
    dm_page = driver.find_element_by_xpath(base_path+"/a/div").click()
    time.sleep(1)
    textarea = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    textarea.send_keys("[OWASP BOT]: Thank you for sharing our Story.\n")
    driver.back()


# validates the users
def validation(driver,username,unread,visible_text,base_path,file):
    if unread and visible_text == "Mentioned you in their story":
        send_confirmation(driver,base_path)
        print(username)
        file.writelines(username+"\n")


# gets the time of the recent post
def time_of_recent_post(driver,url):
    driver.get(url)
    time.sleep(2)
    post_time = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[2]/a/time")
    recent_post = post_time.get_attribute("datetime")
    recent_post_mod = datetime.datetime.strptime(recent_post, '%Y-%m-%dT%H:%M:%S.%fZ')
    print(recent_post_mod)
    return recent_post_mod


# scroll :STRESSED VOICES ALL OVER
def scroll(driver):
    print("WAITING....")
    prev_person = None
    index = 0
    while(True):
        time.sleep(2)
        print("HELLO!!! I'm Scroller I scroll instagram for you")
        #"/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div"
        parent = driver.find_elements_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article")
        names = []
        for child in parent:
            # "/div"
            names.append(child.find_element_by_xpath("./header/div[2]/div[1]/div/span/a").text)
        print(names)

        if (prev_person == None):
            prev_person = names[0]
            index = 0
        else:
            prev_person_index = names.index(prev_person)
            prev_person = names[prev_person_index]
            index = prev_person_index+1

        base_path = index+1

        i = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article["+str(index+1)+"]")
        tezt = (driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article["+str()+"]/header/div[2]/div[1]/div/span/a"))
        print(tezt.text)
        a = ActionChains(driver)
        a.move_to_element(i).perform()


        time.sleep(0.5)

# SCROLL REAL
# "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[2]"

def block():
    while(True):
        print(1,end="")

# driver
def main():
    url = "https://www.instagram.com/p/CPDpgNtLwVD/"
    driver = init()
    login(driver)
    # post_time = time_of_recent_post(driver,url)
    # check(driver,post_time)
    scroll(driver)
    block()
# "/html/body/div[1]/section/main/section/div/div[2]/div/article[1]"
# "/html/body/div[1]/section/main/section/div/div[2]/div/article[3]"
if __name__ == '__main__':
    main()
