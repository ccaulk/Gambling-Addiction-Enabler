from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

NBACSV = "Fanduel NBA Odds.csv"

#Chrome webdriver for the scrapping program
driver = webdriver.Chrome()
#Fanduel NBA odds website
driver.get("https://sportsbook.fanduel.com/navigation/nba")
#wait 5 seconds for the site to load might be to remove
time.sleep(5)
#this should get all the elements for each game that is listed
divsHoldingGames = driver.find_elements(By.CLASS_NAME, "am.aq.ao.ap.af.id.s.dd.ie.az.h.i.j.ah.ai.m.aj.o.ak.q.al")
with open(NBACSV, 'a') as csvfile:
	writer = csv.writer(csvfile)
	writer.seek(2)
	writer.writerow(["test","test2",1,1,1,1,1,1,1,1,1,1])
for game in divsHoldingGames:
	teams = game.find_element(By.CLASS_NAME, "am.an.bb.ap.ck.ct.af.hx.s.hj.h.i.j.ah.ai.m.aj.o.ak.q.al").text
	print(title)
	print("-------------------------------------------------------------------------------------")
driver.quit()