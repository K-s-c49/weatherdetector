from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method =='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9eaac3b0270973148a26ae70c6443059').read()
        json_data = json.loads(res)
        
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            "temp" : str(json_data['main']['temp']),
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
        }
    else:      
        city = ''    
        data = {}
    return render(request ,'index.html',{'city':city,'data':data})