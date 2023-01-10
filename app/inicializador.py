from selenium import webdriver
from selenium.webdriver.common.by import By    
from selenium.common.exceptions import NoSuchElementException  
import generator
import paramikosender
import calendar
import time

def doit(username, retrieveID):
    
    frames = 100
    domain = 'https://chaturbate.com/'
    url = domain + username
    print(url)

    resultado = generator.construyeGIF(frames, url, username, retrieveID)
    print("Ésto es el resultado...")
    print(resultado)

    paramikosender.upload_result(resultado)

    print("Regresamos al punto final del inicializador...")