# 🎮 Challenge: Nexus Gaming - The Checkout

**Difficulty:** Easy  
**Port:** 5006  
**Category:** Web Security / Client-Side Validation

---

## 📝 Scenario

**BUG BOUNTY PROGRAM**  
**Target:** Nexus Gaming Digital Store  
**Scope:** Payment processing flow

---

### About Nexus Gaming

Nexus Gaming is a popular digital gaming store that sells premium content, season passes, and exclusive DLC keys. Their platform processes thousands of transactions daily.

### Scope

The development team has recently launched a new checkout system. Your task is to test the payment flow for any security issues that could allow unauthorized transactions.

**Target:** `http://[TARGET_IP]:5006`

### Out of Scope

- Denial of Service attacks
- Social engineering
- Attacks on third-party services

---

## 🛠️ Setup

```bash
docker-compose up -d --build
```

Access at: `http://localhost:5006`

---

## 📚 Skills Required

- Web application fundamentals
- HTML form understanding
- Browser developer tools
