import json
import urllib.request
from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

from django.conf import settings


def search(request):
    items = dict(request.GET)

    key = "?key=%s" % settings.FOOD2FORK_KEY

    if len(items.get('ingredient', [])) > 0:
        params = key + "&q=" + ",".join(items["ingredient"])

    url = "http://food2fork.com/api/search%s" % params 

    req = urllib.request.Request(url=url,data=b'None',headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})

    f = urllib.request.urlopen(req)
    data = json.loads(f.read())

    return JsonResponse(data)


@login_required
def save_recipe(request):
    pass
