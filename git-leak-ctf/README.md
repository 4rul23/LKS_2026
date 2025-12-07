# 🔐 Challenge: DevFolio - The Git Leak

**Difficulty:** Medium  
**Port:** 5007  
**Category:** Web Security / Information Disclosure

---

## 📝 Scenario

**BUG BOUNTY REPORT**  
**Target:** DevFolio - Developer Portfolio Template  
**Scope:** Information Disclosure Assessment

---

### Background

DevFolio is a popular open-source portfolio template used by developers worldwide. A security researcher reported that some deployments may be leaking sensitive information through misconfigured web servers.

### Your Task

Investigate the target deployment for any exposed sensitive files or directories that shouldn't be publicly accessible.

**Target:** `http://[TARGET_IP]:5007`

---

## 🛠️ Setup

```bash
docker-compose up -d --build
```

Access at: `http://localhost:5007`

---

## 📚 Skills Required

- Web enumeration techniques
- Version control system understanding
- Git forensics basics
