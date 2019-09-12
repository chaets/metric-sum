import time
from flask import Flask, jsonify, request  # import objects from the Flask model
app = Flask(__name__)  # define app using Flask


in_mem_dict = {}
# Funtion to store real time data with time stamps in dictionary
def timestamp_dict(data):
    ts = time.time()

    in_mem_dict[ts] = data

def sum_2hours(): # function to check lastest 2 hours data
    sum1 = 0
    for k, v in in_mem_dict.items():
        print(time.time(), k)
        if 7200 >= (time.time() - k):
            sum1 = sum1 + in_mem_dict[k]

    return int(sum1)


values = []
#function to show if there is any value in metric url
@app.route('/metric/', methods=['GET'])
def returnAlla():
	return jsonify(values)


#function to POST all values using POST request in metric url
@app.route('/metric/', methods=['POST'])
def try_f():
    if request.method == "POST":

        value = {'value': request.json['value']}
        values.append(value)
        timestamp_dict(value['value'])
        return jsonify(values)


#function to show if there is show sum of all latest 2 hours data from metric url to /metric/activeuser/sum'
@app.route('/metric/activeuser/sum', methods=['GET'])
def returnAll():
    if request.method == "GET":
        total = sum_2hours()
    return jsonify({'sum': total})




if __name__ == '__main__':
    app.run(debug=True, port=8080)  # run app on port 8080 in debug mode