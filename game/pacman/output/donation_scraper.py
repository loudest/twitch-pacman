from bs4  import BeautifulSoup
from urllib2 import urlopen
from urllib2 import Request
import time

print "Contribution Scraper..."

headers = {'User-Agent' : 'Mozilla 5.10'}

#Pacman Funding Platform
PM_url = "https://www.crowdtilt.com/campaigns/twitch-is-pacman"
pm_request = Request(PM_url,None,headers)

#Blinky Funding Platfom
B_url = "https://www.crowdtilt.com/campaigns/twitch-is-blinky"
b_request = Request(B_url,None,headers)

count = 0

while count<10000:
    #Pacman File Write
    pm_response = urlopen(pm_request)
    pm_html = pm_response.read()
    pm_response.close()
    pm_soup = BeautifulSoup(pm_html, "lxml")
    pm_cur_con = pm_soup.find("div", "current-contributions")
    pm_cur_con = str(pm_cur_con)
    pm_cur_con = pm_cur_con.rstrip('</div>')
    pm_cur_con = pm_cur_con.lstrip('''<div class="current-contributions">''')
    pm_cur_con = pm_cur_con.replace( ",", "")
    pm_cur_con = pm_cur_con.replace( "$", "")
    pm_cur_con = float(pm_cur_con)
    pm_cur_con = ("$" + str('%.2f' % pm_cur_con))
    print ("Pacman:" + pm_cur_con)
    pm_f = open('pacman_current_contributions.txt','w')
    pm_f.write(pm_cur_con)
    pm_f.close()

    #Blinky File Write
    b_response = urlopen(b_request)
    b_html = b_response.read()
    b_response.close()
    b_soup = BeautifulSoup(b_html, "lxml")
    b_cur_con = b_soup.find("div", "current-contributions")
    b_cur_con = str(b_cur_con)
    b_cur_con = b_cur_con.rstrip('</div>')
    b_cur_con = b_cur_con.lstrip('''<div class="current-contributions">''')
    b_cur_con = b_cur_con.replace( ",", "")
    b_cur_con = b_cur_con.replace( "$", "")
    b_cur_con = float(b_cur_con)
    b_cur_con = ("$" + str('%.2f' % b_cur_con))
    print ("Blinky:" + b_cur_con)
    b_f = open('blinky_current_contributions.txt','w')
    b_f.write(b_cur_con)
    b_f.close()

    #Time Delay
    count = count + 1
    time.sleep(60)



