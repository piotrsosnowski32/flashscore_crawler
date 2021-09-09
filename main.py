# -*- coding: utf-8 -*-

import time
import codecs
from telegram_bot import send_message
from telegram_bot import today_matches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.flashscore.pl/")
page = driver.page_source
soup = BS(page, 'html.parser')

matches = {}

try:
    accept_cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")
    ))
    accept_cookies.click()
except:
    driver.quit()

signIn = driver.find_element_by_id("signIn")
signIn.click()

time.sleep(2)

data = []
file = open('data.txt', 'r')
for nb, content in enumerate(file):
    data.append(content)


login = driver.find_element_by_id("email")
login.send_keys(data[0])
password = driver.find_element_by_id("passwd")
password.send_keys(data[1])
button = driver.find_element_by_id("login")
button.click()

time.sleep(5)

fav = driver.find_element_by_class_name("menuTop__item")
fav.click()

time.sleep(5)


def get_teams(index):
    teams_home = driver.find_elements_by_xpath("//*[starts-with(@class, 'event__participant event__participant--home')]")
    teams_away = driver.find_elements_by_xpath("//*[starts-with(@class, 'event__participant event__participant--away')]")
    return teams_home[index].text, teams_away[index].text

def get_score(index):
    score_home = driver.find_elements_by_xpath("//*[starts-with(@class, 'event__score event__score--home')]")
    score_away = driver.find_elements_by_xpath("//*[starts-with(@class, 'event__score event__score--away')]")
    return score_home[index].text, score_away[index].text

def get_time(index):
    time = driver.find_element_by_class_name("event__stage--block")
    print(time[index].text)
    return time[index].text

def save_result(index, teams, score):
    matches[f'mecz{index}'] = [teams[0], teams[1], score[0], score[1]]
    return matches[f'mecz{index}']

index = 0
while True:
    try:
        teams = get_teams(index)
        score = get_score(index)
        #time = get_time(index)
        save_result(index, teams, score)
        today_matches(teams)
        index = index + 1
    except IndexError:
        break


while True:
    index = 0
    for i in range(len(matches)):
        teams = get_teams(index)
        score = get_score(index)
        #time = get_time(index)
        if matches[f'mecz{index}'][2] != score[0] or matches[f'mecz{index}'][3] != score[1]:
            result = save_result(index, teams, score)
            send_message(result)

        index = index + 1

    time.sleep(30)






