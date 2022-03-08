from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "s3xytempest@gmail.com"
PASSWORD = "aman@2000"

CHROME_WEBDRIVER = "D:\Selenium\chromedriver"

driver = webdriver.Chrome(CHROME_WEBDRIVER)
driver.get("https://tinder.com/")
time.sleep(2)

login_button = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(3)

more_option = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div[1]/div/div[3]/span/button')
more_option.click()
time.sleep(2)

fb = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb.click()
time.sleep(5)

tinder_site = driver.window_handles[0]
fb_page = driver.window_handles[1]
driver.switch_to.window(fb_page)

email = driver.find_element_by_id("email")
email.send_keys(EMAIL)

password = driver.find_element_by_id("pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(tinder_site)

time.sleep(10)
location = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]/span')
location.click()

time.sleep(1)

notification = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[2]')
notification.click()

time.sleep(4)

maybe_later = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div[3]/button[2]/span')
maybe_later.click()

dislike = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')
dislike.click()
time.sleep(3)

while True:
    dislike = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button/span/span')
    dislike.click()
    time.sleep(3)
