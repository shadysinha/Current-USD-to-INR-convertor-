import requests
from bs4 import BeautifulSoup
from datetime import datetime 

url = "https://www.google.com/finance/quote/USD-INR?sa=X&sqi=2&ved=2ahUKEwiap4ehmPiNAxUEyzgGHbpNIScQmY0JegQIChAv"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

response = requests.get(url,headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')
price_element = soup.find('div', class_='YMlKec fxKbKc')
if price_element:
    print("price",price_element.text.strip())
    current_value = price_element.text.strip() #here the price is collected from website 
    print("Current Value :", current_value)
    user_val = int(input("enter the currency in dollars: ")) #value from user 
    Main_val = user_val*(float(current_value)) #multiplying current price with the user input  
    print("The value in is INR =",Main_val) 
    now = datetime.now()
    print("Today's Date and Time: ", now.strftime("%Y-%m-%d %H:%M:%S"))

else:
    print("Element not found")

