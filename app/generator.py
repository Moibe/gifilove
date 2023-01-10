from selenium import webdriver
from selenium.webdriver.common.by import By    
from selenium.common.exceptions import NoSuchElementException  
import time
import imageio

def construyeGIF(frames, url, username, special_tag):
    print("Hola, soy una función generadora de animaciones.")

    #Configuración y generación de Driver. 
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--window-size=1920,1080");
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    #Dale click en aceptar los términos.
    #//*[@id="close_entrance_terms"]
    acepto = driver.find_element(By.ID, "close_entrance_terms").click()
    time.sleep(1)

    #Dale click a la pantalla si esta no está en play: 
    pantalla = driver.find_element(By.ID, "vjs_video_3_html5_api")
    time.sleep(1)

    #En éste arreglo se recibirán las imagenes.
    images = []
    
    try:
        time.sleep(2)
        for i in range(frames):
            try:
                pantalla.screenshot('fotograma.png')
                images.append(imageio.imread('fotograma.png'))
                print(i)
                print(time.time())
                #Controlador de velocidad...
                #time.sleep(1)
            except Exception as e: 
                print(e)    
                time.sleep(3)
                #Escribe los archivos.
                resultado = writeFiles(images, username, special_tag)
                print("Éste es el nuevo resultado...")
                #Termina la operación y entrega el resultado.
                driver.close()
                return resultado
        #Escribe los archivos.
        resultado = writeFiles(images, username, special_tag)
        print("Éste es el nuevo resultado...")
        #Termina la operación y entrega el resultado.
        driver.close()
        return resultado

    except Exception as e: 
        print(e)   
        print("User stopped streaming, video will be recorded up to there...")
        time.sleep(10)
        resultado = writeFiles(images, username, special_tag)
        print("Éste es el nuevo resultado...")
        #Termina la operación y entrega el resultado.
        driver.close()
        return resultado

def writeFiles(images, username, retrieveID):
    
    archivo_gif = username + retrieveID + '.gif'
    archivo_apng = username + retrieveID + '.apng'
    #archivo_mp4 = username + retrieveID + '.mp4'

    #fps=55 o duration = 0.5
    kargs = { 'macro_block_size': 1 }
    print("Printing gif...")
    imageio.v3.imwrite(archivo_gif, images, duration=10)
    print("Printing apng...")
    imageio.v3.imwrite(archivo_apng, images, duration=10)
    #Por la nueva versión se cambio de fps=10 a duration = 10, usando la fórmula sugerida: 
    #The keyword 'fps' is no longer supported. Use 'duration' (in ms) instead, e.g. 'fps=50' == 'duration=20' (1000 * 1/50)
    #En mi caso 'fps=10' y tengo 100 frames, entonces (100*1/10)== 'duration=10'.
    #print("Printing mp4")
    #imageio.v3.imwrite(archivo_mp4, images, fps=10, **kargs)

    return archivo_gif, archivo_apng #, archivo_mp4
