from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)

# Configuration
FTP_USER = "anonymous"
FTP_PASS = "anon123"
FLAG_HTTP = "STELKCSC{http_enum_lfi}"

# Static assets route
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('/app', filename)

@app.route('/')
def index():
    return render_template('index.html', ftp_user=FTP_USER, ftp_pass=FTP_PASS, flag_http=FLAG_HTTP)

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/docs/')
def doc_viewer():
    # Legacy document viewer
    doc = request.args.get('doc', 'welcome.msg')
    base_dir = '/app'
    try:
        # Normalize to an app-local path to simulate a sloppy allowlist
        path = os.path.abspath(doc if doc.startswith('/') else os.path.join(base_dir, doc))

        if path.startswith(base_dir):
            if os.path.exists(path):
                with open(path, 'r') as f:
                    content = f.read()
                return f'<pre>{content}</pre>'
            else:
                return 'Document not found.'
        else:
            return 'Access Denied: You do not have permission to view files outside the document repository.'
    except Exception as e:
        return 'System Error: Unable to retrieve document.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
