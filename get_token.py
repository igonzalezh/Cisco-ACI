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

TOKEN_FUNCION = get_token()
#print("\nTOKEN_FUNCION: "+TOKEN_FUNCION)

##OBTENER FIRMWARE DEL APIC##
url="https://10.10.20.14/api/class/firmwareCtrlrFwStatusCont.json"
header={"content-type": "application/json"}
cookie={"APIC-cookie":TOKEN_FUNCION}
respuesta=requests.get(url, headers=header, cookies=cookie, verify=False)
respuesta_json=respuesta.json()
#print(respuesta_json)

##CREACIÒN DE TENANT##

tenant_name="Tenant_cliente1"

url="https://10.10.20.14/api/mo/uni.json"
payload={
      "fvTenant": {
         "attributes": {
            "name": tenant_name
         }
      }
   }
header={"content-type": "application/json"}
cookie={"APIC-cookie":TOKEN_FUNCION}

respuesta=requests.post(url,data=json.dumps(payload), headers=header, cookies=cookie, verify=False)
print(respuesta)


