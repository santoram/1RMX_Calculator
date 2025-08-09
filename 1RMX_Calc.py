import json
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

print('server listening on port 5004...')

@app.route('/1rm', methods=['GET'])
def get_exercise_info():
    """
    calculates 1 rep max from weight and reps provided
    """
    try:
        weight_request = int(request.args.get('weight'))
        reps_request = int(request.args.get('reps'))
        one_rep_max = int(weight_request /(1.0278 - (0.0278 * reps_request)))
        print(one_rep_max)
        return jsonify({"ORM": one_rep_max})
    except:
        print(f"Error: Unable to calculate")
        return jsonify({"error": "Could not calculate 1 rep max"}),500



if __name__ == '__main__':
    # check to make sure the file path exsists before execution
    # note this is running on port 5004
    app.run(host='127.0.0.1', port=5004, debug=True)