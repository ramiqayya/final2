import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from dotenv import load_dotenv
from .models import User
# Create your views here.

# This example uses Python 2.7 and the python-request library.
load_dotenv()
print(os.getenv("API_KEY"))


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv("API_KEY"),
}

session = Session()
session.headers.update(headers)


@login_required(login_url='/login')
def index(request):

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
    # btcp = lookup('BTC')['data']['BTC'][0]['quote']['USD']['price']
    # ethp = lookup('ETH')['data']['ETH'][0]['quote']['USD']['price']
    # usdt = lookup('USDT')['data']['USDT'][0]['quote']['USD']['price']

    return render(request, "myapp/index.html", {
        "all": data['data'][1],
        "1stname": data['data'][0]['name'],
        "1stsymbol": data['data'][0]['symbol'],
        "1stprice": data['data'][0]['quote']['USD']['price'],
        "1stpchange1h": data['data'][0]['quote']['USD']['percent_change_1h'],
        "1stpchange24h": data['data'][0]['quote']['USD']['percent_change_24h'],
        "1stpchange7d": data['data'][0]['quote']['USD']['percent_change_7d'],
        "1stmcap": data['data'][0]['quote']['USD']['market_cap'],
        "2ndname": data['data'][1]['name'],
        "2ndsymbol": data['data'][1]['symbol'],
        "2ndprice": data['data'][1]['quote']['USD']['price'],
        "2ndpchange1h": data['data'][1]['quote']['USD']['percent_change_1h'],
        "2ndpchange24h": data['data'][1]['quote']['USD']['percent_change_24h'],
        "2ndpchange7d": data['data'][1]['quote']['USD']['percent_change_7d'],
        "2ndmcap": data['data'][1]['quote']['USD']['market_cap'],
        "3rdname": data['data'][2]['name'],
        "3rdsymbol": data['data'][2]['symbol'],
        "3rdprice": data['data'][2]['quote']['USD']['price'],
        "3rdpchange1h": data['data'][2]['quote']['USD']['percent_change_1h'],
        "3rdpchange24h": data['data'][2]['quote']['USD']['percent_change_24h'],
        "3rdpchange7d": data['data'][2]['quote']['USD']['percent_change_7d'],
        "3rdmcap": data['data'][2]['quote']['USD']['market_cap'],
        "4thname": data['data'][3]['name'],
        "4thsymbol": data['data'][3]['symbol'],
        "4thprice": data['data'][3]['quote']['USD']['price'],
        "4thpchange1h": data['data'][3]['quote']['USD']['percent_change_1h'],
        "4thpchange24h": data['data'][3]['quote']['USD']['percent_change_24h'],
        "4thpchange7d": data['data'][3]['quote']['USD']['percent_change_7d'],
        "4thmcap": data['data'][3]['quote']['USD']['market_cap'],
        "5thname": data['data'][4]['name'],
        "5thsymbol": data['data'][4]['symbol'],
        "5thprice": data['data'][4]['quote']['USD']['price'],
        "5thpchange1h": data['data'][4]['quote']['USD']['percent_change_1h'],
        "5thpchange24h": data['data'][4]['quote']['USD']['percent_change_24h'],
        "5thpchange7d": data['data'][4]['quote']['USD']['percent_change_7d'],
        "5thmcap": data['data'][4]['quote']['USD']['market_cap'],
        "6thname": data['data'][5]['name'],
        "6thsymbol": data['data'][5]['symbol'],
        "6thprice": data['data'][5]['quote']['USD']['price'],
        "6thpchange1h": data['data'][5]['quote']['USD']['percent_change_1h'],
        "6thpchange24h": data['data'][5]['quote']['USD']['percent_change_24h'],
        "6thpchange7d": data['data'][5]['quote']['USD']['percent_change_7d'],
        "6thmcap": data['data'][5]['quote']['USD']['market_cap'],
        "7thname": data['data'][6]['name'],
        "7thsymbol": data['data'][6]['symbol'],
        "7thprice": data['data'][6]['quote']['USD']['price'],
        "7thpchange1h": data['data'][6]['quote']['USD']['percent_change_1h'],
        "7thpchange24h": data['data'][6]['quote']['USD']['percent_change_24h'],
        "7thpchange7d": data['data'][6]['quote']['USD']['percent_change_7d'],
        "7thmcap": data['data'][6]['quote']['USD']['market_cap'],
        "8thname": data['data'][7]['name'],
        "8thsymbol": data['data'][7]['symbol'],
        "8thprice": data['data'][7]['quote']['USD']['price'],
        "8thpchange1h": data['data'][7]['quote']['USD']['percent_change_1h'],
        "8thpchange24h": data['data'][7]['quote']['USD']['percent_change_24h'],
        "8thpchange7d": data['data'][7]['quote']['USD']['percent_change_7d'],
        "8thmcap": data['data'][7]['quote']['USD']['market_cap'],
        "9thname": data['data'][8]['name'],
        "9thsymbol": data['data'][8]['symbol'],
        "9thprice": data['data'][8]['quote']['USD']['price'],
        "9thpchange1h": data['data'][8]['quote']['USD']['percent_change_1h'],
        "9thpchange24h": data['data'][8]['quote']['USD']['percent_change_24h'],
        "9thpchange7d": data['data'][8]['quote']['USD']['percent_change_7d'],
        "9thmcap": data['data'][8]['quote']['USD']['market_cap'],
        "10thname": data['data'][9]['name'],
        "10thsymbol": data['data'][9]['symbol'],
        "10thprice": data['data'][9]['quote']['USD']['price'],
        "10thpchange1h": data['data'][9]['quote']['USD']['percent_change_1h'],
        "10thpchange24h": data['data'][9]['quote']['USD']['percent_change_24h'],
        "10thpchange7d": data['data'][9]['quote']['USD']['percent_change_7d'],
        "10thmcap": data['data'][9]['quote']['USD']['market_cap'],

    }
    )


@login_required(login_url='/login')
def greet(request, name):
    return render(request, "myapp/greet.html", {
        "name": name.title()

    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "myapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "myapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "myapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "myapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "myapp/register.html")


@login_required(login_url='/login')
def profile(request):

    return render(request, "myapp/profile.html")


def lookup(*symbols):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol='
    for symbol in symbols:
        url += f'{symbol},'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'Request failed with status code:', response.status_code
