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
    respuesta=requests.post(url, json.dumps(data), headers=header, verify=False)

    respuesta_json=respuesta.json()

    API_TOKEN=respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return API_TOKEN

API_TOKEN = get_token()

## ELIMINAR TENANT ##
url = "https://10.10.20.14/api/mo/uni.json"

payload = {
    "fvTenant": {
        "attributes": {
            "name": "Tenant_cliente1",
            "status": "deleted"
        }
    }
}

cookie={"APIC-cookie":API_TOKEN}
header={"content-type": "application/json"}
response = requests.post(url, data=json.dumps(payload), headers=header, cookies=cookie, verify=False)
print(response)