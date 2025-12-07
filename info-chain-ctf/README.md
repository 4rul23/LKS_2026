# 🔗 Challenge: NovaTech - The Chain Reaction

**Difficulty:** Medium-Hard  
**Port:** 5009  
**Category:** Information Disclosure / Chained Exploitation

---

## 📝 Scenario

**PENETRATION TEST ENGAGEMENT**  
**Client:** NovaTech Inc.  
**Scope:** External Information Disclosure Assessment

---

### Background

NovaTech is a rapidly growing cloud infrastructure startup. As part of their security program, they've engaged your team to assess their public-facing web application for any information disclosure vulnerabilities.

Your goal is to identify and chain together any exposed sensitive information to gain unauthorized access to internal systems.

### Scope

**Target:** `http://[TARGET_IP]:5009`

All paths and endpoints on the target are in scope. Focus on:
- Sensitive file exposure
- Debug information leakage
- API endpoint security

---

## 🛠️ Setup

```bash
docker-compose up -d --build
```

Access at: `http://localhost:5009`

---

## 📚 Skills Required

- Web enumeration
- Information gathering
- API testing
- Connecting the dots
