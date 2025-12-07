# 🕹️ NEON ARCADE - Writeup

## Challenge Overview
- **Name:** User-Agent Gatekeeper
- **Category:** Web / HTTP Fundamentals
- **Difficulty:** Easy
- **Flag:** `   `

## Reconnaissance

1. **Visit the website** at `http://localhost:5003`
2. You'll see an "ACCESS DENIED" message
3. Notice that your current User-Agent is displayed on the page
4. Click the "NEED A HINT?" button for guidance

## Finding the Clues

### Clue 1: Hint Page
The `/hint` page reveals:
- The arcade only allows browsers from its network
- The official browser is called: `NeonArcade/1.0`

### Clue 2: Browser Console
Open DevTools (F12) → Console tab. You'll see:
```
🎮 NEON ARCADE 🎮
Hint: Check your User-Agent header...
The arcade only accepts: NeonArcade/1.0
```

## Solution

### Method 1: Using curl
```bash
curl -A "NeonArcade/1.0" http://localhost:5003
```

### Method 2: Using Browser DevTools
1. Open DevTools (F12)
2. Go to Network tab
3. Right-click on the request → "Edit and Resend"
4. Modify the `User-Agent` header to `NeonArcade/1.0`
5. Send the request

### Method 3: Browser Extension
1. Install "User-Agent Switcher" extension
2. Set custom User-Agent to `NeonArcade/1.0`
3. Refresh the page

### Method 4: Burp Suite
1. Intercept the request
2. Modify `User-Agent: NeonArcade/1.0`
3. Forward the request

## Flag
```
STELKCSC{us3r_4g3nt_sp00f1ng_m4st3r}
```

## Key Takeaways
1. **User-Agent is client-controlled** - Never trust it for security decisions
2. **HTTP headers can be easily modified** - Any client-side header can be spoofed
3. **DevTools is powerful** - Learn to use Network tab for web security testing
4. **curl is your friend** - Quick way to test HTTP requests with custom headers
