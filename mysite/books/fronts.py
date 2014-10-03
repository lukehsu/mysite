__author__ = 'lukehsu'
from pymongo import Connection
from django.shortcuts import render_to_response
from django.template import RequestContext
def product(request):
    conn = Connection('localhost', 27017)
    db = conn.test
    db.authenticate("test", "test")
    dbt = db.test
    #dbt = dbt.find_one().keys()
    dbt = dbt.find().sort("time", -1)
    backpic = []
    backcontent = []
    backprice = []
    backtime = []
    for i in dbt:
        backpic.append(i["pic"])
        backcontent.append(i["content"])
        backprice.append(i["price"])
        backtime.append(i["time"][0:10])
    allinfo = zip(backpic, backcontent,backprice,backtime)
    return render_to_response('front.html', {'allinfo': allinfo },context_instance=RequestContext(request))