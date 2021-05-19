import time

# Check if any stories available for the user.
def any_stories(driver):
    div_before = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div")
    ariadisabled = (div_before.get_attribute("aria-disabled"))
    tabindex = (div_before.get_attribute("tabindex"))
    div_before.click()
    if tabindex == -1 and ariadisabled:
        return False
    return True


# Check for the url link redirect available
def story_check(driver, url):
    time.sleep(1)
    # print("YAHA AAYA THA")
    story_img = driver.find_element_by_xpath(
        "/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/div/div/div[2]/div[2]/div")
    story_img.click()
    see_post = driver.find_element_by_xpath(
        "/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/div/div/div[2]/div[3]/div[1]/div[1]")
    see_post.click()
    was_current = driver.current_url
    driver.back()
    return was_current == url


# open the stories and navigate among them
def open_stories(driver, url, instaHandle):
    time.sleep(2)
    base = "https://www.instagram.com/" + instaHandle + "/"
    while driver.current_url != base:
        if story_check(url):
            return True
        # print("RUKO NEXT STORY PE JAA RAHE HAI")
        time.sleep(1)
        # next_story = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/button/div")
        # next_story.click()
    return False
