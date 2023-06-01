import json 
def Business(file):
    f=open(file)
    data=json.load(f)
    f.close()
    return data

def write_json(file,data):
    f=open(file,"w")
    json.dump(data,f,indent=3)
    f.close()
    