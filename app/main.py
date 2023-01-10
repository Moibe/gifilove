from fastapi import FastAPI
from fastapi import BackgroundTasks, FastAPI
import requests
import inicializador
import time
import calendar 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "MoibeBris"}

@app.get("/validar/{numero}")
def validar_capicua(numero:str):
    respuesta = "Nó es capicúa"

    if numero == numero[::-1]:
        respuesta = "Es capicúa"
    return {
        "numero": numero,
        "validacion": respuesta
    }

@app.get("/obtenEstado")
def obten_estado():

    url = "https://onlinesim.io/api/getState.php"

    querystring = {"apikey":"fjYyvCrMY7947Jc-97mBXv2D-SS1zaVt3-ycq5rw8A-x6fjndCDUuxCd45"}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

           
    return {
        "Esto es una prueba"
    }

@app.get("/createGIF/{username}")
async def send_notification(username: str, background_tasks: BackgroundTasks):
    #Genera el ID de la sesión:
    tiempo = calendar.timegm(time.gmtime())
    retrieveID = str(tiempo)
    background_tasks.add_task(inicializador.doit, username, retrieveID)
    return {"Message": "Recording... Use this ID to retrieve:" + retrieveID}

@app.get("/retrieveGIF/{retrieveID}")
def retrieveGIF(retrieveID: str):
    return {"Éste es tu retrieveID:" + retrieveID}
