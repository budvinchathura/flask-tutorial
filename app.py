from flask import Flask,jsonify,request

app = Flask(__name__)


stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My item',
                'price': 788
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hellosf   sdf world!!!!"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for s in stores:
        if s['name'] == name:
            return jsonify(s)
    return jsonify({'message':'store not found'})
    


@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name':request_data['name'],
        'price':request_data['price']
    }
    for s in stores:
        if s['name']== name:
            s['items'].append(new_item)    
        return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for s in stores:
        if s['name'] == name:
            return jsonify({'items':s['items']})
    return jsonify({'message':'store not found'})
    


app.run(port=4000, debug=True)
