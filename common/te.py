from common.new_res import API
import json

# a = API().api_method('post','http://api.hd.shall-buy.top/staff/index/staff/login',{"grant_type":"password","client_id":2,"client_secret":"gjcLsvKaAwgR7blX2SV03oE1HOd0SKUx5SN3tVrJ","scope":"*","username":"admin","password":"aa123456"})
# print(a)


a= {"grant_type":"password","client_id":2,"client_secret":"gjcLsvKaAwgR7blX2SV03oE1HOd0SKUx5SN3tVrJ","scope":"*","username":"admin","password":"aa123456"}
print(type(a))