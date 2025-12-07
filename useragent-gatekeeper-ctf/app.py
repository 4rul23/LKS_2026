from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'neon_arcade_secret_2024'

# The secret User-Agent that grants access
SECRET_USER_AGENT = "NeonArcade/1.0"
FLAG = "STELKCSC{us3r_4g3nt_sp00f1ng_m4st3r}"

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent', '')
    
    # Check if the User-Agent matches our secret
    # Check if the User-Agent matches our secret (allow 1.0 or 2.0 based on footer hint)
    ua_lower = user_agent.lower()
    if "neonarcade/1.0" in ua_lower or "neonarcade/2.0" in ua_lower:
        return render_template('success.html', flag=FLAG)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
