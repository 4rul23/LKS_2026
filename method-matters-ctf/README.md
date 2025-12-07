# 💳 Challenge: NexusPay - API Security Assessment

**Difficulty:** Easy-Medium  
**Port:** 5005  
**Category:** Web Security / API Testing

---

## 📝 Scenario

**PENETRATION TEST SCOPE DOCUMENT**  
**Client:** NexusPay Inc.  
**Engagement:** API Security Assessment  
**Classification:** Confidential

---

### Background

NexusPay is a payment processing platform that handles millions of transactions daily. Following industry best practices, their security team has implemented strict access controls on all sensitive API endpoints.

### Scope

Your assessment is limited to the following endpoint:

```
Target: http://[TARGET_IP]:5005
Endpoint: /api/v1/transactions/export
```

### Objective

The development team claims this endpoint is "fully secured" and cannot be accessed without proper authentication. Your task is to verify this claim and document any findings.

### Rules of Engagement

- Do not attempt to brute-force credentials
- Do not perform denial of service attacks  
- Focus on access control validation

---

## 🛠️ Setup

```bash
docker-compose up -d --build
```

Access at: `http://localhost:5005`

---

## 📚 Skills Required

- REST API fundamentals
- HTTP protocol understanding
- API testing methodology
