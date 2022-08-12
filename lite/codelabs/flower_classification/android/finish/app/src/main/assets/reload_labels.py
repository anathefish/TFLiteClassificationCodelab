import json

# Opening JSON file
f = open('index_to_name_dict.json')
wf = open('labels.txt', 'w')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    wf.write(str(data[i]))
    wf.write('\n')


# Closing file
f.close()
wf.close()
