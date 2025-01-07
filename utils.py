import requests as rq
import aspose.pdf as ap
import pandas 

def descarga(url,output):
    try:
        respuesta = rq.get(url)

        if respuesta.status_code ==200:

            with open(output, "wb") as f:
                f.write(respuesta.content)
            print (f"el arrchivo se descargo correctamente")

        else:
            print(f"el archivo no pudo descarse correctamente ")
    except Exception as e:
        print(f"Error al descargar el archivo {output}: {e}")

def crear_archivo(input):

  
    
    input_pdf = input+".pdf"
    output_csv = input+".csv"

    try:
        documento = ap.Document(input_pdf)
        opciones_guardado = ap.ExcelSaveOptions()
        opciones_guardado.format = ap.ExcelSaveOptions.ExcelFormat.CSV
        documento.save(output_csv, opciones_guardado)
        ordenar_csv(output_csv)

    except Exception as e:
        print(f"error al guardar archivo: {e}")
   

def ordenar_csv(input_csv):

    try:
        df = pandas.read_csv(input_csv, encoding="latin1", quotechar='"',lineterminator='\n',on_bad_lines="skip",na_values=["-"], dtype=str)
        print("columnas encontradas", df.columns)
    
        if "Pórtico" in df.columns:
            df_sorted = df.sort_values(by="Pórtico", ascending=False)
            df_sorted.to_csv(input_csv, index=False, encoding="latin1")
            print(f"El archivo CSV se ha ordenado correctamente.")

        else:
            print("La columna 'Pórtico' no se encuentra en el archivo CSV.")
    except Exception as e:
        print (f"Error al guardar el archivo {e}")


        