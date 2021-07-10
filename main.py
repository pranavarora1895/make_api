# pip install flask
# Flask Minimal App
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/is_armstrong/<int:n>') # It takes the input value from url
def is_armstrong(n):
    n_copy = n
    summation = 0
    while n != 0:
        remainder = n % 10
        summation = summation + remainder**3
        n //=10
    if summation == n_copy:
        # Makes up the dictionary
        result = {
            "number": n_copy,
            "is_armstrong": True,
            "server IP": 'localhost'
        }
    else:
        result = {
            "number": n_copy,
            "is_armstrong": False,
            "server IP": 'localhost'
        }
    return jsonify(result) # converts the dictionary to JSON

if __name__ == '__main__':
    app.run(debug=True)
    
