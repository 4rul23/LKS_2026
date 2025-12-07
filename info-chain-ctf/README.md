# 🔗 Chain Reaction: The NovaTech Breach

> **CLASSIFIED ASSIGNMENT // RED TEAM OPERATIONS**
> **Codename:** GLASS_HOUSE
> **Target:** NovaTech Infrastructure

---

## 🕵️ Mission Briefing
**Agent**,
NovaTech is a "Unicorn" startup that prides itself on its *cutting-edge* cloud architecture. However, our intel suggests their developers are sloppy with secrets management. They claim their internal API is "impenetrable" because it's behind a firewall... but we believe they've left the keys under the doormat.

Your objective is to prove that **Information Leakage** is just as deadly as Remote Code Execution. You must find the small cracks in their perimeter, chain them together, and compromise their Super Admin account.

**Remember:** One small leak can sink a great ship.

---

## 🎯 Target Scope
- **URL:** `http://localhost:5009`
- **Objective:** Obtain the sensitive "System Flag" from the protected internal API.
- **Rules of Engagement:**
    1.  Enumeration is key. Look for what *shouldn't* be there.
    2.  Read the developers' breadcrumbs (config files, docs).
    3.  Chain your findings. Item A gives access to Item B.

---

## 🧩 Intelligence (Hints)
*   *"Developers love storing secrets in files starting with a dot."*
*   *"If you find a new technology stack, learn its default paths."*
*   *"Internal APIs often trust 'internal' traffic implicitly. Can you fake it?"*
*   *"Documentation is meant for developers, but hackers read it better."*

---

## 🛠️ Deployment
Initialize the target environment:

```bash
cd info-chain-ctf
docker-compose up -d --build
```

**Target Status:** `ONLINE` at `http://localhost:5009`

---

## 🏆 Key Takeaways (Post-Game)
- **Secrets Management:** Never commit `.env` files or keys to production code.
- **API Security:** "Internal" APIs must still require robust authentication, not just static keys.
- **Defense in Depth:** Obscurity (hiding an API) is not Security.

*Good luck, Agent.*
