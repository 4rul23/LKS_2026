from flask import Flask, request
import os

app = Flask(__name__)

FTP_USER = "anonymous"
FTP_PASS = "anon123"
FLAG_HTTP = "STELKCSC{http_enum_lfi}"

@app.route('/')
def index():
    return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Honkai Star Rail - Trailblazer Console</title>
    <style>
        :root {{
            --bg: #0a0f1c;
            --panel: #111a2c;
            --accent: #7c9bff;
            --accent-2: #9ef5ff;
            --text: #e5ecff;
            --muted: #93a4c2;
        }}
        * {{ box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: radial-gradient(circle at 20% 20%, rgba(124,155,255,0.08), transparent 30%), radial-gradient(circle at 80% 0%, rgba(158,245,255,0.08), transparent 25%), var(--bg); color: var(--text); margin: 0; padding: 0; }}
        header {{ background: linear-gradient(90deg, rgba(124,155,255,0.25), rgba(158,245,255,0.1)); border-bottom: 1px solid rgba(255,255,255,0.06); padding: 22px; }}
        h1 {{ margin: 0; font-size: 22px; letter-spacing: 0.5px; }}
        .nav a {{ color: var(--text); text-decoration: none; margin-right: 14px; font-weight: 600; font-size: 14px; }}
        .container {{ padding: 22px; max-width: 900px; margin: 24px auto; background: var(--panel); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; box-shadow: 0 20px 80px rgba(0,0,0,0.35); }}
        .alert {{ background: rgba(124,155,255,0.08); border: 1px solid rgba(124,155,255,0.25); padding: 12px; border-radius: 8px; color: var(--text); font-size: 14px; }}
        code {{ background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px; color: var(--accent-2); }}
        .footer {{ margin: 32px auto; max-width: 900px; color: var(--muted); font-size: 12px; text-align: center; padding: 12px 0 24px; }}
        a.btn {{ display: inline-block; margin-top: 14px; padding: 10px 14px; border-radius: 8px; background: rgba(124,155,255,0.16); color: var(--text); text-decoration: none; font-weight: 600; border: 1px solid rgba(124,155,255,0.3); }}
    </style>
</head>
<body>
    <header>
        <h1>Trailblazer Console // Astral Express</h1>
        <div class="nav">
            <a href="/">Bridge</a>
            <a href="/policy">Crew Policy</a>
            <a href="/docs/">Star Logs</a>
        </div>
    </header>
    <div class="container">
        <div class="alert">
            <strong>Silver Wolf:</strong> Left some QA comments in the bundle. Check page source for the mirror link and, uh, shiny loot.
        </div>
        <h2 style="margin-top:18px;">Welcome, Trailblazer</h2>
        <p style="color: var(--muted); line-height: 1.6;">Systems are in maintenance mode. Navigation, crew policies, and star logs remain accessible. QA left a mirror for rollback testing.</p>
        <a class="btn" href="/docs/?doc=/app/welcome.msg">Open Star Log</a>
    </div>
    <div class="footer">
        &copy; 2025 Astral Express Ops. Secure the Stellaron.
    </div>

    <script>
        // QA NOTE: FTP mirror left for rollback testing.
        // Access: ftp://{FTP_USER}:{FTP_PASS}@localhost:2121 (use -a to list hidden .releases/)
        // HTTP_FLAG: {FLAG_HTTP}
    </script>
</body>
</html>
'''

@app.route('/policy')
def policy():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Company Policy - Trailblazer Corp</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 0; }
        header { background-color: #0056b3; color: white; padding: 20px; }
        .container { padding: 20px; max-width: 800px; margin: 0 auto; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <header><h1>Trailblazer Corp Policy</h1></header>
    <div class="container">
        <h3>IT Security Policy</h3>
        <p>1. Do not share passwords.</p>
        <p>2. Lock your workstation when leaving.</p>
        <p>3. Report suspicious activity immediately.</p>
        <a href="/">Back to Home</a>
    </div>
</body>
</html>
'''

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
