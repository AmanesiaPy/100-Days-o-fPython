from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InterSpeedTwitterBot:

    def __init__(self, driver):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        driver = webdriver.Chrome(self.driver)
        driver.get("https://www.speedtest.net/")
        go = driver.find_element_by_class_name("start-text")
        go.click()
        time.sleep(60)
        result = driver.find_elements_by_class_name("result-data-value")
        self.down = float(result[1].text)
        self.down = float(result[2].text)

    def tweet_at_provide(self, user_name, password, message):
        driver = webdriver.Chrome(self.driver)
        driver.get("https://twitter.com/login")
        time.sleep(3)
        email = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(user_name)
        pas = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pas.send_keys(password)
        pas.send_keys(Keys.ENTER)
        time.sleep(3)
        tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        tweet.send_keys(message)
        send = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        print(send.text)



from internetspeedtwitterbot import InterSpeedTwitterBot

UP_SPEED = 30
DOWN_SPEED = 30
CHROME_DRIVER_PATH = "D:\Selenium\chromedriver"
TWITTER_ID = "*********"
TWITTER_PASSWORD = "*******"

bot = InterSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()

if bot.down < DOWN_SPEED or bot.up < UP_SPEED:
    message = f"Hey Internet Provider, why my internet speed is {bot.down}down/{bot.up}up when I pay for {DOWN_SPEED}down/{UP_SPEED}up."

    bot.tweet_at_provide(TWITTER_ID, TWITTER_PASSWORD, message)
