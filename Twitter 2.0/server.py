from flask import Flask, jsonify

app = Flask(__name__)

# Default background color
default_background_color = '#ffffff'

# Endpoint for GET and POST requests to reset background
@app.route('/reset-background', methods=['GET', 'POST'])
def reset_background():
    return jsonify({'result': 'Background reset successfully'})

# Endpoint for POST request to change background
@app.route('/change-background', methods=['POST'])
def change_background():
    return jsonify({'result': 'Background changed successfully'})

# Endpoint for HEAD request to get flag
@app.route('/get-flag', methods=['HEAD'])
def get_flag():
    return '', 200, {'flag': 'CTF{your_flag_here}'}

if __name__ == '__main__':
    app.run(debug=True)
