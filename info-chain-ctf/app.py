from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

FLAG = "STELKCSC{ch41n3d_1nf0_d1scl0sur3_m4st3r}"

# ============================================
# CHAIN 1: .env file exposed (classic mistake)
# ============================================

@app.route('/.env')
def env_file():
    return """# Strapi CMS Configuration
HOST=0.0.0.0
PORT=1337
APP_KEYS=xM3pL7qR9sT2vW5yA8bC0dE4fG6hJ
API_TOKEN_SALT=kL2mN4pQ6rS8tU0vW2xY4zA6bC8d
ADMIN_JWT_SECRET=eE3fG5hJ7kL9mN1pQ3rS5tU7vW9x

# Database (PostgreSQL)
DATABASE_CLIENT=postgres
DATABASE_HOST=db.strapi.internal
DATABASE_PORT=5432
DATABASE_NAME=strapi_prod
DATABASE_USERNAME=strapi_admin
DATABASE_PASSWORD=Str4p1_Pr0d_2024!

# AWS S3 Upload
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=ap-southeast-1
AWS_BUCKET=strapi-uploads-prod

# Internal API
INTERNAL_API_URL=http://localhost:1337/api/internal
INTERNAL_API_KEY=sk_live_51N3xK2LmNoPqRsTuVwXyZ

# See /strapi/config/server.js for more settings
""", 200, {'Content-Type': 'text/plain'}

# ============================================
# CHAIN 2: Exposed Strapi config file
# ============================================

@app.route('/strapi/config/server.js')
def strapi_config():
    return """'use strict';

module.exports = ({ env }) => ({
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  app: {
    keys: env.array('APP_KEYS'),
  },
  // Admin panel config - see /strapi/config/admin.js
  // API docs: /documentation/v1.0.0
});
""", 200, {'Content-Type': 'application/javascript'}

# ============================================
# CHAIN 3: Swagger/OpenAPI docs exposed
# ============================================

@app.route('/documentation/v1.0.0')
def api_docs():
    return jsonify({
        "openapi": "3.0.0",
        "info": {
            "title": "Strapi Internal API",
            "version": "1.0.0"
        },
        "paths": {
            "/api/users": {"get": {"summary": "List users", "security": [{"bearerAuth": []}]}},
            "/api/articles": {"get": {"summary": "List articles"}},
            "/api/internal/health": {"get": {"summary": "Health check (no auth)"}},
            "/api/internal/debug": {"get": {"summary": "Debug info", "description": "Requires X-Internal-Key header"}}
        },
        "components": {
            "securitySchemes": {
                "bearerAuth": {"type": "http", "scheme": "bearer"}
            }
        }
    })

# ============================================
# CHAIN 4: Debug endpoint leaks more info
# ============================================

@app.route('/api/internal/debug')
def internal_debug():
    api_key = request.headers.get('X-Internal-Key', '')
    
    if api_key != 'sk_live_51N3xK2LmNoPqRsTuVwXyZ':
        return jsonify({"error": "Unauthorized", "required": "X-Internal-Key header"}), 401
    
    return jsonify({
        "status": "debug_active",
        "environment": "production",
        "strapi_version": "4.15.0",
        "node_version": "18.17.0",
        "database": {
            "type": "postgres",
            "connected": True
        },
        "secrets": {
            "admin_panel": "/strapi/admin",
            "super_admin_token": "sa_prod_eyJhbGciOiJIUzI1NiJ9.YWRtaW4",
            "note": "Use this token for /api/internal/admin-status"
        }
    })

# ============================================
# CHAIN 5: Final endpoint with FLAG
# ============================================

@app.route('/api/internal/admin-status')
def admin_status():
    auth = request.headers.get('Authorization', '')
    
    if auth != 'Bearer sa_prod_eyJhbGciOiJIUzI1NiJ9.YWRtaW4':
        return jsonify({"error": "Invalid super admin token"}), 403
    
    return jsonify({
        "admin_status": "active",
        "permissions": ["all"],
        "system_flag": FLAG,
        "message": "You have gained super admin access through chained information disclosure."
    })

@app.route('/api/internal/health')
def health():
    return jsonify({"status": "healthy", "uptime": "45d 12h 33m"})

# ============================================
# Main Website
# ============================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5009)
