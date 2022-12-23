from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index (request):

    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Delhi'



    appid='94b7a5f9be5713db1341cb08ac45a003'
    URL='https://api.openweathermap.org/data/2.5/weather'
    PARAMS={'q':city,'appid':appid,'units':'metric'}
    r=requests.get(url=URL,params=PARAMS)
    res=r.json()
    print(res)
    code = res["cod"]
    if code == "404":
        description="Enter Valid City Name"
        icon=""
        temp=""
        day=""
    else:
        description = res["weather"][0]['description']
        icon=res["weather"][0]['icon']
        temp=res['main']['temp']
        day=datetime.date.today()



    return render(request,'weatherapp/index.html',{
        'description':description,'icon':icon,'temp':temp,'day':day,'city':city, 'code':code})