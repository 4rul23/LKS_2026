# 👾 Mission: Protocol Breach // Stellaron Hunter Archive

> **Incoming encrypted transmission...**
> **Sender:** Silver Wolf (Hacker, Stellaron Hunters)
> **Subject:** New Playground Found

---

## 💬 Mission Brief
"Yo, newbie. Kafka told me to drag you along for this one.

We found a dusty old corp called **Trailblazer Corp**. Their security is a joke—literal ancient tech held together by hope and duct tape. Elio's script says there's a **Master Flag** hidden deep inside, but I'm too busy grinding my rank in Aetherium Wars to deal with their lvl 1 ferrets.

So, I'm outsourcing the fun to you. I already scanned their perimeter while you were AFK getting coffee. Here’s the map. Don't mess it up, or I’ll ban your account."

---

## 🧭 Recon Snapshot (Scan by Silver Wolf)

"I ran a quick scan on their local network. Check it out using your sad little terminal."

```bash
# silver_wolf@stellaron:~/recon$ nmap -sC -sV -p- trailblazer.corp

Aether Editing... 100% [==================>]
TARGET: trailblazer.corp (127.0.0.1)

PORT      STATE SERVICE  VERSION & NOTES
8082/tcp  open  http     Flask Portal
2121/tcp  open  ftp      vsftpd 3.0.3
2222/tcp  open  ssh      OpenSSH 8.9p1
5354/tcp  open  domain   BIND 9.18
2525/tcp  open  smtp     Python smtpd
1445/tcp  open  netbios  Samba smbd 4.x

Nmap done: 1 IP address (1 host up) scanned in 1.337 seconds
```

---

## 🎮 Game Guide (Walkthrough)

"Keep getting stuck? Fine, I'll backseat game for a bit. Here’s the combo chain:"

1.  **Level 1: HTTP (Port 8082)**
    *   **Objective:** Find the FTP creds.
    *   **Hint:** The `/docs/` endpoint reads files. Try reading `/app/config.txt`.
    *   **Loot:** First Flag + FTP Creds.

2.  **Level 2: FTP (Port 2121)**
    *   **Objective:** Get the SSH Key.
    *   **Hint:** Login as `anonymous`. Download `ssh_key.pem`. The passphrase is weak—literally written in the file comments.
    *   **Loot:** SSH Private Key.

3.  **Level 3: SSH (Port 2222)**
    *   **Objective:** Breaching the server.
    *   **Hint:** User is `sysadmin`. Use the key you stole.
    *   **Loot:** SSH Flag + Hints about SMTP.

4.  **Level 4: DNS (Port 5354)**
    *   **Objective:** Map the network.
    *   **Hint:** Their DNS is leaking everything. Try a Zone Transfer (`dig AXFR`).
    *   **Loot:** DNS Flag + SMB Server Info.

5.  **Level 5: SMTP (Port 2525)**
    *   **Objective:** Social Engineering via VRFY.
    *   **Hint:** The server verifies users. Ask it about `smbuser`.
    *   **Loot:** SMB Password (leaked in response).

6.  **Boss Room: SMB (Port 1445)**
    *   **Objective:** The Treasure.
    *   **Hint:** Connect to `//localhost/finance_backup` with the credentials you farmed.
    *   **Reward:** **MASTER FLAG**.

---

## 🏆 Achievement List (Flags)

| Challenge | Flag Format | Status |
| :--- | :--- | :--- |
| **HTTP** | `STELKCSC{http_enum_lfi}` | 🔓 Locked |
| **FTP** | `STELKCSC{ftp_anon_brute}` | 🔓 Locked |
| **SSH** | `STELKCSC{ssh_key_reuse}` | 🔓 Locked |
| **DNS** | `STELKCSC{dns_zone_xfer}` | 🔓 Locked |
| **SMTP** | `STELKCSC{smtp_vrfy_relay}` | 🔓 Locked |
| **SMB** | `STELKCSC{smb_null_shares}` | 🔓 Locked |
| **ULTIMATE** | `STELKCSC{protocol_chain_mastery_2025}` | 🔓 Locked |

---

## 🛠️ Setup Instructions (For Noobs)

"Just run this. If it fails, restart your router or something."

```bash
cd protocol-ctf
docker-compose up --build -d
```

**Clean up your mess:**
```bash
docker-compose down -v
```

"Good luck, partner. Don't disappoint me." 
*- Silver Wolf*
