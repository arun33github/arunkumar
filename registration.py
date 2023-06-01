import json_utlis
def register_business(cname,contact,address):
    data=json_utlis.Business("data/business.json")
    business_json={
        "sno":len(data["Business"])+1,
        "business_name":cname,
        "contact":contact,
        "add":address
    }

    data["Business"].append(business_json) 
    json_utlis.write_json("data/business.json",data)


    
        