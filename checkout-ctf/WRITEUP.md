# 🎮 Nexus Gaming - Writeup

## Challenge Overview
**Name:** The Checkout  
**Category:** Client-Side Validation Bypass  
**Difficulty:** Easy  
**Flag:** `STELKCSC{cl13nt_s1d3_pr1c3_m4n1pul4t10n}`

## Vulnerability

The checkout form uses a **hidden input field** to store the product price:

```html
<input type="hidden" name="price" value="999999">
```

The server trusts this client-provided value without verifying it against the database.

## Solution

### Method 1: DevTools (Elements Tab)
1. Browse to any product → Click "Buy Now"
2. Open DevTools (F12) → Elements tab
3. Find: `<input type="hidden" name="price" value="999999">`
4. Change `value="999999"` to `value="0"`
5. Click "Complete Purchase"
6. Flag appears!

### Method 2: Burp Suite
1. Intercept the POST request to `/purchase`
2. Modify `price=999999` to `price=0`
3. Forward the request
4. Flag in response

### Method 3: cURL
```bash
curl -X POST http://localhost:5006/purchase \
  -d "product_id=legendary-key&price=0"
```

## Flag
```
STELKCSC{cl13nt_s1d3_pr1c3_m4n1pul4t10n}
```

## Key Takeaways
1. **Never trust client input** - especially for sensitive data like prices
2. **Hidden fields are NOT secure** - they can be easily modified
3. **Server-side validation is mandatory** - price should be fetched from database
