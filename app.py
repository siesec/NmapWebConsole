from bottle import Bottle, request, template, static_file, response
import subprocess
import os
import threading
import re
import json
import warnings

warnings.filterwarnings("ignore", category=ImportWarning)

app = Bottle()

@app.route('/')
def index():
    return template('templates/index')

@app.route('/generate_command', method='POST')
def generate_command():
    ip_address = request.forms.get('ip_address')
    input_file = request.forms.get('input_file')
    result_file = request.forms.get('result_file')
    parallel_jobs = request.forms.get('parallel_jobs')

    script_content = f"""#!/bin/bash
date
cat {input_file} | parallel -j {parallel_jobs} nmap -sT -Pn -p{{}} {ip_address} >> {result_file} 2>&1
date
"""

    script_path = 'run_parallel.sh'
    with open(script_path, 'w') as f:
        f.write(script_content)

    os.chmod(script_path, 0o755)

    download_link_script = f'<a href="/download/{script_path}">Download {script_path}</a>'
    return template('templates/result', download_links=download_link_script)

@app.route('/run_script')
def run_script():
    script_path = os.path.abspath('run_parallel.sh')
    log_file = 'output.log'
    try:
        if not os.path.exists(script_path):
            return template('templates/output', output="Error: Script file not found.")

        os.chmod(script_path, 0o755)

        with open(log_file, 'w') as f:
            pass

        def run_and_log():
            with open(log_file, 'a') as log_f:
                process = subprocess.Popen(['/bin/bash', script_path], stdout=log_f, stderr=subprocess.STDOUT)
                process.wait()

        threading.Thread(target=run_and_log).start()
        return template('templates/progress')
    except Exception as e:
        return template('templates/output', output=f"Error: {e}")

@app.route('/get_log')
def get_log():
    log_file = 'output.log'
    try:
        with open(log_file, 'r') as f:
            log_content = f.read()

        is_complete = False
        if log_content.count('date') >= 2:
            is_complete = True

        # ポートスキャン結果の解析
        port_info = []
        lines = log_content.split('\n')
        for i in range(len(lines)):
            match = re.search(r'(\d+)/(\w+)\s+(\S+)\s+(\S+)', lines[i])
            if match:
                port_info.append({
                    'port': match.group(1),
                    'protocol': match.group(2),
                    'state': match.group(3),
                    'service': match.group(4)
                })

        result = {
            'is_complete': is_complete,
            'port_info': port_info
        }
        response.content_type = 'application/json'
        return json.dumps(result)
    except Exception as e:
        response.status = 500
        return json.dumps({'error': str(e)})

@app.route('/download/<filename>')
def download(filename):
    return static_file(filename, root='./', download=filename)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
