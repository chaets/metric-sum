import requests
import time
from flask import Flask, jsonify, request  # import objects from the Flask model
app = Flask(__name__)  # define app using Flask

# in_memory = dict()
in_mem_dict= {}

# # def add(val, data):
#     curr = time.localtime()
#     data[curr] = val
#     print(data)
#
#
# def parse_data (data):
#     curr = time.localtime()
#     total = 0
#     print('test: ', list(data.values())[0]['value'])
#     # new_data = dict()
#     for key in data:
#         # key = int(keys)
#         if (key.tm_year == curr.tm_year and key.tm_mon == curr.tm_mon and key.tm_mday == curr.tm_mday):
#             if ((curr.tm_hour - key.tm_hour) < 1 and curr.tm_min - key.tm_min < 1 and (curr.tm_sec - key.tm_sec) < 20):
#                 total = total + list(data.values())[0]['value']
#     return total


def timestamp_dict(data):
    ts = time.time()
    # in_mem_dict.update(ts = data )
    in_mem_dict[ts] = data

def sum_2hours():
    sum1 = 0
    # values = [v for k,v in in_mem_dict.items() if k >= (time.localtime().tm_hour- 2)]
    for k, v in in_mem_dict.items():
        if k >= (time.localtime().tm_hour - 2):
            sum1 = sum1 + int(in_mem_dict[k])
    print(sum1)
    return sum1


values = [{'value': 5}, {'value': 6}, {'value': 7}]



@app.route('/metric/', methods=['GET'])
def returnAlla():
	return jsonify({'values' : values})



@app.route('/metric/', methods=['POST'])
def try_f():
    if request.method == "POST":

        value = {'value': request.json['value']}
        values.append(value)
        timestamp_dict(value)
        # add(value, in_memory)
        return jsonify({'value': values})



@app.route('/metric/activeuser/sum', methods=['GET'])
def returnAll():
    # sum = 0
    if request.method == "GET":
        # sum = parse_data(in_memory)
        total = sum_2hours()

    return jsonify({'sum': total})




if __name__ == '__main__':
    app.run(debug=True, port=8080)  # run app on port 8080 in debug mode