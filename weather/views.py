from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        res= urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633')
        json_data=json.load(res)
        data={
            "country_code": str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon']) + ' '+
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data={}
        
    return render(request,'index.html',{'city':city},{"data":data},{'res':res})