from bs4 import BeautifulSoup
import requests


url = 'stex drvum a en linky ,vor saytic vor ogtvel enq'

response = requests.get(url)

soup = BeautifulSoup(response.txt,'lxml')

x = soup.find('ay ste du petqa ed elementy stanas ira classov,xosqi heto gces listi mej.listic vercnes')


'''
heto petqa ed stacvac tvyaly kces qo bazayin

dra hamar ogtagorcum enq es kody w3school ic

'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

'''


'''