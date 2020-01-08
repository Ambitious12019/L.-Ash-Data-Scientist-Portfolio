

import requests


def weather_data(query):  #Request weather infor by url/API Key
    try:
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=11fc6351b6bd9417a007e3b1d3583c4c&units=imperial');
        return res.json();
    except:
      print("Error while connecting") #Display error connecting to user
        
def print_weather(result,city): #print weather info
	print("{}'s temperature: {}°F ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
    

def main(): # obtain user city selection
    city=input('Enter the city or 9 to stop:')
    print()
   
        
    try:
            
         query='q='+city;     #weather information is queried based on city selection
         w_data=weather_data(query);
         print_weather(w_data, city)
         print()     
                
         if city == city: 
                 input("Enter the city of 9 to stop:") 
            
         while city == '9':
             'break'
             
                
    except:
           print("Error, Restart, or Goodbye!")
            
    
    
if __name__=='__main__':
    main()
    
    
        
