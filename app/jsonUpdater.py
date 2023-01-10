import json
import time

#Así se abre un json:
with open('app\works.json') as fp:
    js_param = json.load(fp)

print("Esto es el type...")
print(type(js_param))
time.sleep(5)

# convert into JSON:
que_es = json.dumps(js_param)
print("Esto es el type...")
print(type(que_es))

  
""" 
# python object to be appended
y = {"pin":110096}
 
# parsing JSON string:
z = json.loads(js_param)
  
# appending the data
z.update(y)
 
# the result is a JSON string:
print(json.dumps(z)) """