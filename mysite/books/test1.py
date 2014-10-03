from bs4 import BeautifulSoup
import urllib2
import sys
from django.http import HttpResponse
from mysite.books.models import Analyst,Analyst1,Analyst2
from django.shortcuts import render_to_response
from django.template import RequestContext

def page(request):
    reload(sys)
    sys.setdefaultencoding('utf8')

    url = "http://www.gvm.com.tw/webonly_list_1.html"
    top = urllib2.urlopen(url)
    soup = BeautifulSoup(top.read())
    top1 = soup.findAll("p")
    link1 = ""
    for div in top1:
        link1 = str(div)+link1
        #print link1
    link1 = BeautifulSoup(link1)
    top2 = link1.findAll("span", {"class": "paperMore"})
    link2 = ""
    for div in top2:
        link2 = str(div)+link2
    # print link2
    link2 = BeautifulSoup(link2)
    top3 = link2.findAll("a")
    link3 = []
    http = ""
    for div in top3:
        http = "http://www.gvm.com.tw/" + div["href"]
        link3.append(http)


    url = "http://www.30.com.tw/topic_01.html"
    top = urllib2.urlopen(url)
    soup = BeautifulSoup(top.read())
    top1 = soup.findAll("p")
    link1 = ""
    for div in top1:
        link1 = str(div)+link1
        #print link1
    link1 = BeautifulSoup(link1)
    top2 = link1.findAll("span", {"class": "more"})
    link2 = ""
    for div in top2:
        link2 = str(div)+link2
    # print link2
    link2 = BeautifulSoup(link2)
    top3 = link2.findAll("a")
    link30 = []
    http = ""
    for div in top3:
        http = "http://www.30.com.tw/" + div["href"]
        link30.append(http)



    url = "http://www.gvm.com.tw/webonly_list_2.html"
    top = urllib2.urlopen(url)
    soup = BeautifulSoup(top.read())
    top1 = soup.findAll("p")
    link1 = ""
    for div in top1:
        link1 = str(div)+link1
        #print link1
    link1 = BeautifulSoup(link1)
    top2 = link1.findAll("span", {"class": "paperMore"})
    link2 = ""
    for div in top2:
        link2 = str(div)+link2
    # print link2
    link2 = BeautifulSoup(link2)
    top3 = link2.findAll("a")
    linkha = []
    http = ""
    for div in top3:
        http = "http://www.gvm.com.tw/" + div["href"]
        linkha.append(http)

####################article

    content = urllib2.urlopen('http://www.gvm.com.tw/webonly_list_1.html').read()
    urltemp = Analyst()
    urltemp.feed(content)
    allarticle = []
    # j = ""
    for i in urltemp.name:
        if len(i) > 90 :
            allarticle.append(i.decode('utf-8'))
            #j = j + i.decode('utf-8')

    content = urllib2.urlopen('http://www.30.com.tw/topic_01.html').read()
    urltemp = Analyst1()
    urltemp.feed(content)
    allarticle30 = []
    for i in urltemp.name:
        if len(i) > 90 :
            allarticle30.append(i.decode('utf-8'))

    content = urllib2.urlopen('http://www.gvm.com.tw/webonly_list_2.html').read()
    urltemp = Analyst2()
    urltemp.feed(content)
    allarticleha = []
    for i in urltemp.name:
        if len(i) > 90 :
            allarticleha.append(i.decode('utf-8'))

################pic


    url = "http://www.gvm.com.tw/webonly_list_1.html"
    pages = urllib2.urlopen(url)
    soup = BeautifulSoup(pages.read())
    top1 = soup.findAll("img",{"width": "212"})
    pic = []
    for div in top1:
        if div["src"][:3] != "htt":
            src = "http://www.gvm.com.tw/" + div["src"]
            pic.append(src)
        else:
            pic.append(div["src"])

    url = "http://www.30.com.tw/topic_01.html"
    pages = urllib2.urlopen(url)
    soup = BeautifulSoup(pages.read())
    top1 = soup.findAll("img",{"width": "150"})
    pic30 = []
    for div in top1[1:6]:
        if div["src"][:3] != "htt":
            src = "http://www.30.com.tw/" + div["src"]
            pic30.append(src)
        else:
            pic30.append(div["src"])

    url = "http://www.gvm.com.tw/webonly_list_2.html"
    pages = urllib2.urlopen(url)
    soup = BeautifulSoup(pages.read())
    top1 = soup.findAll("img",{"width": "212"})
    picha = []
    for div in top1:
        if div["src"][:3] != "htt":
            src = "http://www.gvm.com.tw/" + div["src"]
            picha.append(src)
        else:
            picha.append(div["src"])
    count = zip(pic,allarticle,link3,pic30,allarticle30,link30,picha,allarticleha,linkha)
    return render_to_response('grill.html', {'count': count },context_instance=RequestContext(request))