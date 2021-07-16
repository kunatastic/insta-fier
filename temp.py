# # # # import datetime
# # # #
# # # # date_time_str = '2021-05-17T18:31:52.565Z'
# # # # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
# # # #
# # # # # print('Date:', date_time_obj.date())
# # # # # print('Time:', date_time_obj.time())
# # # # # print('Date-time:', date_time_obj)
# # # #
# # # # lefttime = (datetime.datetime.utcnow() - date_time_obj)
# # # # file = open("A.txt",'a')
# # # # file.writelines("kunal")
# # # # print(str(datetime.datetime.now())+".txt")
# # #
# # # # import webdriver
# # # from selenium import webdriver
# # #
# # # # import Action chains
# # # from selenium.webdriver.common.action_chains import ActionChains
# # #
# # # # # create webdriver object
# # # # driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")
# # # #
# # # # # get geeksforgeeks.org
# # # # driver.get("https://www.geeksforgeeks.org/")
# # # #
# # # # # create action chain object
# # # # action = ActionChains(driver)
# # # #
# # # # # move the cursor
# # # # action.move_by_offset(200, 200)
# # # #
# # # # # perform the operation
# # # # action.perform()
# # # prev_name = None
# # # index = 0
# # # while(True):
# # #     names = ['hmm_nikhil', 'wowskinscienceindia', 'skrillex', 'enriqueiglesias', 'imzachherron', 'realangelaokorie', 'girltalk_verified', 'hesson_mike', 'kunatastic', 'riyaz.14']
# # #
# # #     if (prev_name != None):
# # #         index = names.index(prev_name)+1
# # #
# # #     print(names[index])
# # #     prev_name = names[index]
# #
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support.expected_conditions import presence_of_element_located
# #
# # wait = WebDriverWait(driver, 10)
# #
# # with webdriver.Firefox() as driver:
# #     driver.get("http://google.com/ncr")
# #     driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
# #
# #     wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>a")))
# #
# #     results = driver.find_elements_by_css_selector("h3>a")
# #     for i, result in results.iteritems():
# #         print("#{}: {} ({})".format(i, result.text, result.get_property("href")))
#
#
# import random
#
# print(random.uniform(1,5))
def fun():
    try:
        raise ValueError('Represents a hidden bug, do not catch this')
        raise Exception('This is the exception you expect to handle')
    except Exception as error:
        print('Caught this error: ' + repr(error))


for i in range(4):
    print(i)
    if (i==3):
        fun()