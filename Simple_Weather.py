import json, requests

print(f"Simple Weather Program\n")

#This function calls makes the request to api and displays the temp for the given city
def weather():
    base_url="https://api.openweathermap.org/data/2.5/weather"
    appid="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"    #Enter your API key here
    city=input("Enter a city or zip code: ")

    url=f"{base_url}?q={city}&units=imperial&APPID={appid}"
    #print(url)

    response=requests.get(url)
    unformated_data=response.json()
    #print(unformated_data)

    name = unformated_data["name"]
    temp = unformated_data["main"]["temp"]
    feels_like = unformated_data["main"]["feels_like"]
    temp_min = unformated_data["main"]["temp_min"]
    temp_max = unformated_data["main"]["temp_max"]

    # Prints weahter informaion for user input and displays "name" json value insted of user input
    print(f"Weather information for {name}: ")
    print(f"Temperature:                {temp} farenheit")
    print(f"Feels-like temperature:     {feels_like} farenheit")
    print(f"Minimum temperature:        {temp_min} farenheit")
    print(f"Maximum temperature:        {temp_max} farenheit")


#While loop for try-except block
while True:
    try:
        #While loop for user input
        while True:
            weather()
            choice = input("\nEnter another city? Y/N ")
            choice = choice.upper()
            print()
            if choice == "Y":
                continue
            elif choice == "N":
                print(f"Exiting...")
                break
            break
    except:
        print(f"Invalid entry...\n")
    else:
        break
print(f"\nThank you for using my program!")
