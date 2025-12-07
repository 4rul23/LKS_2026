# 🕹️ Challenge: NEON ARCADE - Access Terminal

**Difficulty:** Easy  
**Port:** 5003  
**Category:** Web Fundamentals

---

## 📝 Scenario

**INTERNAL MEMO**  
**From:** IT Security Team  
**To:** Red Team Operators  
**Subject:** Perimeter Assessment - NEON ARCADE Gaming Portal

---

Our client, NEON ARCADE Corp, has deployed a new gaming portal for their VIP members. They claim their access control system is "unhackable" because it uses a proprietary client verification system.

During our initial reconnaissance, we discovered that their portal rejects all standard browsers. Their developers mentioned something about "only allowing traffic from official NEON ARCADE client software" during a casual conversation at the coffee machine.

The security team couldn't find any public documentation about this client software, but we suspect the verification mechanism might be simpler than they think.

**Your mission:** Gain access to the VIP portal and retrieve the secret key.

**Target:** `http://[TARGET_IP]:5003`

---

## 🎯 Objective

Bypass the client verification and access the restricted area.

## 🛠️ Setup

```bash
docker-compose up -d --build
```

Access at: `http://localhost:5003`

---

## 📚 Skills Required

- HTTP fundamentals
- Web traffic analysis
- Client-server communication understanding

## 💡 Real-World Relevance

This challenge simulates a common security misconception: trusting client-provided data for access control decisions. Many legacy systems still rely on easily spoofable identifiers for "security" checks.
