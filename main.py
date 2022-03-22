
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from internet_speed_complainer import InternetSpeedTwitterBot

PROMISED_DOWN = 50
PROMISED_UP = 10

TWITTER_EMAIL = "xxxxx@gmail.com"
TWITTER_PASSWORD = "xxxxxxxxxxxx"

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
URL = "https://www.speedtest.net/"


my_bot = InternetSpeedTwitterBot(Service(CHROME_DRIVER_PATH))
speeds = my_bot.get_internet_speed(URL)
# print(my_bot.up)
# print(my_bot.down)
my_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)


