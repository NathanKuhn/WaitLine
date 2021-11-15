import requests as req
import lxml.html
import json
import datetime as dt
import time

URL = "https://www.tapingo.com/order/campus/cpsl/pickup/"

REL_DICT = {
    "streats" : "streats-vista-grande-dining-complex",
    "brunch" : "brunch",
    "hearth" : "hearth-cpsl",
    "balance" : "balance-cafe-vista-grande-dining-complex",
    "noodles" : "noodles-california-polytechnic-san-luis-obispo",
    "sweet bar" : "sweet-bar-california-polytechnic-university-cal-poly-slo"
}

def getWaitTime(rel):
    html = req.get(URL)
    doc = lxml.html.fromstring(html.content)
    container = doc.xpath('//tr[@rel="%s"]' % rel)
    waitTimeString = container[0].xpath('.//td/text()')[2]
    return float(waitTimeString)

def logData():
    data = {}
    for key, value in REL_DICT.items():
        data[key] = getWaitTime(value)

    now = str(dt.datetime.now())

    return data

print(logData())