from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
app.secret_key = 'nusantara_gateway_internal_2025'

FLAG = "STELKCSC{http_m3th0ds_m4tt3r_1n_4p1s}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/transactions/export', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def export_transactions():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        response.headers['Allow'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
        return response
    
    if request.method == 'GET':
        return jsonify({
            'error': {
                'code': 'FORBIDDEN',
                'message': 'GET requests are not permitted on this endpoint',
                'documentation_url': '/api/docs'
            }
        }), 403
    
    if request.method == 'POST':
        auth = request.headers.get('Authorization', '')
        if not auth.startswith('Bearer '):
            return jsonify({
                'error': {
                    'code': 'UNAUTHORIZED', 
                    'message': 'Authentication required',
                    'required_header': 'Authorization: Bearer <token>'
                }
            }), 401
        return jsonify({
            'error': {
                'code': 'INVALID_TOKEN',
                'message': 'The provided API key is invalid or expired'
            }
        }), 401
    
    if request.method == 'PUT':
        return jsonify({
            'error': {
                'code': 'METHOD_NOT_ALLOWED',
                'message': 'PUT is not supported for this resource'
            }
        }), 405
    
    if request.method == 'PATCH':
        return jsonify({
            'error': {
                'code': 'METHOD_NOT_ALLOWED', 
                'message': 'PATCH is not supported for this resource'
            }
        }), 405
    
    if request.method == 'DELETE':
        # Misconfigured endpoint - DELETE bypasses auth check
        return jsonify({
            'status': 'success',
            'message': 'Export completed',
            'data': {
                'export_id': 'EXP-2024-00847',
                'generated_at': '2024-12-06T10:30:00Z',
                'record_count': 18492,
                'checksum': FLAG
            }
        }), 200

@app.route('/api/docs')
def api_docs():
    return render_template('docs.html')

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'version': '1.0.3'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
