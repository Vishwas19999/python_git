# import json
# with open('data.json')as f:
#     data=json.load(f)
#
#     print(data)

#json to dict
# import json
# employee='{"name":"Vishu","age":22,"location":"Bangalore"}'
# employee_dict=json.loads(employee)
# print(employee_dict)

#dict to json
# import json
# employee_dict={'name':'Vishu','age':22,'location':'Bangalore'}
# employee_json=json.dumps(employee_dict)
# print(employee_json)

#write json to file
# import json
# employee_json={"name":"Vishu","age":22,"languages":["Kannada","English","Hindi"]}
# with open('employee.txt','w')as file:
#     json.dump(employee_json,file)

#pretty print json
# import json
# employee_string='{"name":"Vishu","age":22,"location":"Bangalore"}'
# employee_dict=json.loads(employee_string)
# print(json.dumps(employee_dict,indent=5))

#update json
# import json
# x='{"name":"abc","age":22,"clg":"vpc"}'
# y={"location":"Vijayapura"}
# z=json.loads(x)
# z.update(y)
# print(json.dumps(z))

# import json
# def new(file_data,filname='data.json'):
#     with open('data.json','r+')as file:
#         file_data=json.load(file)
#         file_data['employee'].append(file_data)
#         file.seek(0)
#         json.dump(file_data,file,indent=4)
#
# y={
#     "id":22,
#     "name":"Vishu",
#     "department":"ECE"
#     }
# new(y)

#
# import json
# # function to add to JSON
# def write_json(new_data, filename='data.json'):
#     with open(filename, 'r+') as file:
#         # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data["employee"].append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent=4, sort_keys=True)
#
# # python object to be appended
# y = {
#          "id": "04",
#          "name": "JKTE",
#          "department": "HR"
#       }
#
# write_json(y)


#writing to json file using json.dump
# import json
# employee={
#     "details":{
#         "name":"aba",
#         "age":22,
#         "place":"USA"
#     }
# }
# with open('datafile.json','w')as write:
#     json.dump(employee,write)

#pyhton object into json string
import json
data={
    "std":{
        "class":12,
        "sub":"PCMB",
    }
}
res=json.dumps(data)
print(res)




