
from flask import Flask, request, render_template, jsonify
from scanner import port_scanner, brute_forcer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan_ports', methods=['POST'])
def scan_ports():
    host = request.form['host']
    ports = list(range(20, 1025))  # demo range
    open_ports = port_scanner.scan_ports(host, ports)
    return jsonify({'open_ports': open_ports})

@app.route('/brute_force', methods=['POST'])
def brute_force():
    username = request.form['username']
    password_list = ["123456", "admin", "password", "admin123", "root"]
    result = brute_forcer.brute_force(username, password_list)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
