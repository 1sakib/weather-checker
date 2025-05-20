import requests

API_KEY = ""  # ENTER YOUR WEATHER API KEY

def apicall(key, city):
    return f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=yes"

def getTime(time):
    hour, minute = map(int, time.split(':'))
    period = 'AM' if hour < 12 else 'PM'
    hour = hour % 12
    if hour == 0:
        hour = 12
    return f"{hour}:{minute:02d} {period}"

def getdata(key, city):
    response = requests.get(apicall(key, city))
    if response.status_code == 400:
        print("\nPlease enter a valid city name!")
        return False
    return response.json()

def main():
    city = ""
    data = None

    while not data:
        city = input("Please enter a city: ")
        data = getdata(API_KEY, city)

    print("")
    print(f"{data['location']['name']}, {data['location']['country']} Weather Data:")
    print(f"Temperature : {data['current']['temp_c']}°C")
    print(f"Condition   : {data['current']['condition']['text']}")
    print(f"Date        : {data['location']['localtime'][:10]}")
    print(f"Time        : {getTime(data['location']['localtime'][11:])}")

main()
