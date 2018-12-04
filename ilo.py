#!/bin/python
import redfish

REST_OBJ = redfish.redfish_client(base_url="https://uls-ep-swtools-04-m1.wdc.com",username="it-ops-adm",
                             password="$vc@!t0p$", default_prefix='/rest/v1')
REST_OBJ.login(auth="session")
#response = REST_OBJ.get("/rest/v1/systems/1", None)
response = REST_OBJ.post("/Systems/1",{"Action":"Reset","ResetType":"On"})
print response

REST_OBJ.logout()
