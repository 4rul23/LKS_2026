# 🐧 Challenge: Operation BLACK PENGUIN

> **CLASSIFIED ASSIGNMENT // LINUX RECOVERY**
> **Codename:** FROZEN_SERVER
> **Target:** Legacy Database Server (Linux)

---

## 🕵️ Mission Briefing
**Agent**,
Our monitoring station lost contact with one of our deep-storage legacy servers, codenamed **BLACK PENGUIN**. The previous administrator, "CyberDave", vanished mysteriously last week, leaving behind a chaotic file system and zero documentation.

We need you to SSH into the box, navigate through his messy directories, and recover the **Master Recovery Key** (the Flag). Dave was known for hiding secrets in plain sight and using hidden files.

**Intel:**
- He often left notes for himself.
- He used multiple user accounts to hide his tracks.
- He loved "dotfiles".

---

## 🎯 Target Scope
- **Protocol:** SSH
- **Port:** 2222
- **Objective:** Locate and retrieve the Flag.

**Credentials (Provided by HR):**
- **User:** `ctfuser`
- **Password:** `internship2024`

---

## 🛠️ Deployment
Initialize the target environment:

```bash
cd linux-basics-ctf
docker-compose up -d --build
```

**Access:**
```bash
ssh ctfuser@localhost -p 2222
```

---

## 🧩 Intelligence (Hints)
*   *"If a file starts with a dot, `ls` won't show it unless you ask nicely (`-a`)."*
*   *"Sometimes the treasure isn't in your house, but your neighbor's (`/home`)."*
*   *"Reading is fundamental. check `README` or `.txt` files."*

---

## 🏆 Key Takeaways (Post-Game)
- **Linux Navigation:** Mastery of `ls`, `cd`, `cat`, and permissions.
- **Hidden Files:** Creating and finding files named like `.secret` is a basic obfuscation technique.
- **Permission Model:** Understanding User vs Group vs World permissions.

*Good luck, Agent. Verify your shell.*
