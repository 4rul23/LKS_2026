# 🗳️ Challenge: Employee Excellence Awards

**Difficulty:** Medium  
**Port:** 5008  
**Category:** Web Security / Parameter Manipulation

---

## 📝 Scenario

**INTERNAL APPLICATION TESTING**  
**System:** Employee Excellence Awards Portal  
**Scope:** Vote Processing Security

---

### Background

PT Maju Bersama is running their quarterly Employee Excellence Awards. Staff members can vote for their outstanding colleagues through the internal HR portal.

Each employee has a unique ID, and votes from Director-level accounts carry additional weight in the final tally.

### Your Assignment

You are logged in as **Budi Santoso (E001)**, a Staff member. Your task is to test the voting system's security controls.

**Target:** `http://[TARGET_IP]:5008`

---

## 🛠️ Setup

```bash
docker-compose up -d --build
```

Access at: `http://localhost:5008`

---

## 📚 Skills Required

- HTTP request analysis
- Parameter handling understanding
- Web security testing methodology
