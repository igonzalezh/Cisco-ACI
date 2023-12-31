import requests
import json
import conf

def get_token():
    requests.packages.urllib3.disable_warnings()

    url="https://10.10.20.14/api/aaaLogin.json"
    data = {
          "aaaUser":{
                "attributes":{
                      "name":conf.user,
                      "pwd": conf.password
                }
          }
    }
    header={"content-type": "application/json"}

    ##LA DATA SE DEBE PASAR A LA ESTRUCTURA JSON CON JSON DUMPS##
    ##LA VARIABLE RESPUESTA SE CARGA CON EL CONTENIDO QUE RESPONDE EL CISCO APIC##

    respuesta=requests.post(url, json.dumps(data), headers=header, verify=False)

    ##LO ANTERIOR REGRESA COMO TEXTO, LE DAMOS EL FORTMATO DE JSON.() ##
    respuesta_json=respuesta.json()

    ## LA RESPUESTA ESTA EN JSON - DICCIONARIO (2 ELEMENTOS) EL 2ª CON UNA LISTA ##
    ## SI QUEREMOS SACAR EL VALOR DEL TOKEN DEBEMOS INVOCAR LA VARIABLE "imdata"##
    API_TOKEN=respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return API_TOKEN

API_TOKEN = get_token()
print("\nAPI_TOKEN: "+API_TOKEN)



