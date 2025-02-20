from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Nikitha Yangala"

    system_user = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %f')

    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <pre>
    Name: {full_name}
    User: {system_user}
    Server Time (IST): {server_time}

    Top output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)