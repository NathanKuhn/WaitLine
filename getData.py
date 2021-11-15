import requests as req
import lxml.html
import json
import datetime as dt
import time
from food import FoodType

URL = "https://www.tapingo.com/order/campus/cpsl/pickup/"

REL_DICT = {
    FoodType.BURGER : "streats-vista-grande-dining-complex",
    FoodType.BURRITO : "brunch",
    FoodType.PIZZA : "hearth-cpsl",
    FoodType.LEAF : "balance-cafe-vista-grande-dining-complex",
    FoodType.NOODLES : "noodles-california-polytechnic-san-luis-obispo",
    FoodType.ICE_CREAM : "sweet-bar-california-polytechnic-university-cal-poly-slo"
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