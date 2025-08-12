
import json 
# Sample JSON data


with open('/Users/ritikpal/Desktop/Python/Funtions/Built_in_fn/ritik.json','r') as file:
    data = json.load(file)
# Using map to extract names from the JSON data
def get_name(x):
    return x['name']
names = map(get_name, data) 
# Convert map object to list
names_list = list(names)
print("Names:", names_list)  # Output: ['Alice', 'Bob', 'Charlie']
names = list(map(lambda person: person['name'], data))
print("Names:", names)  # Output: ['Alice', 'Bob', 'Charlie']
# Using filter to extract people older than 30

# print complete json 
print("Complete JSON Data:", data)


