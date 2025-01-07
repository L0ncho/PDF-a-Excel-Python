
#from utilis import descarga, crear_archivo "asi tambien puede ser cuando vienen del mismo utils"
from utils import descarga
from utils import crear_archivo
from utils import ordenar_csv

url= "https://concesiones.mop.gob.cl/peajesporticos/Documents/2024/URBANAS/"
archivos = ["COSTANERA%20NORTE.pdf","AUTOPISTA%20CENTRAL.pdf"]

for archivo in archivos:
    input = archivo
    url1 = url + input 
    input_csv= input
    print(url1)
    
    try:
        descarga(url1, input)
        crear_archivo(input.replace(".pdf", ""))
        ordenar_csv(input_csv)
    except Exception as e:
         print(f"Hubo un error al procesar el archivo {input}: {e}")
