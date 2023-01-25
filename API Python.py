from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/pythagorean', methods=['GET'])
def pythagorean():
    leg1 = request.args.get('leg1')
    leg2 = request.args.get('leg2')
    hypotenuse = math.sqrt(float(leg1)**2 + float(leg2)**2)
    return jsonify(hypotenuse=hypotenuse)

if __name__ == '__main__':
    app.run(debug=True)

