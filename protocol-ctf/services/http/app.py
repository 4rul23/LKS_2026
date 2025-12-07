from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Trailblazer Corp - Internal Portal</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 0; }
        header { background-color: #0056b3; color: white; padding: 20px; }
        .container { padding: 20px; max-width: 800px; margin: 0 auto; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: 20px; border-radius: 5px; }
        h1 { margin: 0; font-size: 24px; }
        .nav { margin-top: 10px; }
        .nav a { color: white; text-decoration: none; margin-right: 15px; font-weight: bold; }
        .content { margin-top: 20px; line-height: 1.6; }
        .footer { margin-top: 40px; font-size: 12px; color: #666; text-align: center; border-top: 1px solid #eee; padding-top: 10px; }
        .alert { background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 4px; margin-bottom: 15px; border: 1px solid #ffeeba; }
    </style>
</head>
<body>
    <header>
        <h1>Trailblazer Corp</h1>
        <div class="nav">
            <a href="/">Home</a>
            <a href="/policy">Company Policy</a>
            <a href="/docs/">Document Viewer</a>
        </div>
    </header>
    <div class="container">
        <div class="alert">
            <strong>Notice:</strong> System maintenance scheduled for this weekend.
        </div>
        <h2>Welcome to the Employee Portal</h2>
        <p>Access internal resources, view company policies, and manage your profile.</p>
        <p>For IT support, please contact the helpdesk at extension 5555.</p>
    </div>
    <div class="footer">
        &copy; 2025 Trailblazer Corp. Authorized Personnel Only.
    </div>
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
    try:
        # Simulate a document storage path
        # In a real app this might be /var/www/docs, here we just use absolute path for the CTF logic
        # The vulnerability is that we allow absolute paths if they start with /app or contain /flags (simulating a misconfigured allowlist)
        
        path = os.path.abspath(doc)
        
        # Realistic-looking logic: "Allow docs in app dir OR special flag dir for audit"
        if '/flags' in path or path.startswith('/app'):
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
