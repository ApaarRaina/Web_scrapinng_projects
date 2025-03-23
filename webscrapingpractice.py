from bs4 import BeautifulSoup
import requests

response=requests.get('https://sports.ndtv.com/cricket/live-scores')

doc=BeautifulSoup(response.text,"html.parser")
sect=doc.find_all("div",class_="sp-scr_wrp")
section=sect[0]
title=section.find("a")
head=title.find("div",class_="scr_txt-ony")
play=title.find("div",class_="scr_dt-red")
score2=title.find("span",class_="scr_tm-run scr_tm-scr-act")
score1=title.find("span",class_="scr_tm-run")
team1=title.find("div",class_="scr_tm-nm")
teams=title.find_all("div",class_="scr_tm-nm")
status=title.find_all("div",class_="scr_dt-red")
team2=teams[1]
print(" ",head.string)
print("             ",play.string)
print(team1.string,"        ",team2.string)
print(score1.string,"  ",score2.string)
print(status[1].string)