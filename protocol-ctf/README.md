# Protocol Pentest Lab - CTF Challenge

## Story
You are a red team operator tasked with infiltrating **Trailblazer Corp**'s perimeter network. The company has exposed several legacy services due to cost-cutting. Your goal: traverse the attack surface using common protocols, chaining exploits to retrieve the **MASTER FLAG** hidden deep in the infrastructure.

This lab introduces **real-world protocol abuse** techniques used in CTFs and pentests:
- **HTTP**: Web enumeration & traversal
- **FTP**: Anonymous access & brute-force
- **SSH**: Credential reuse & key auth
- **DNS**: Zone transfer & cache snooping
- **SMTP**: Open relay & VRFY/EXPN
- **SMB**: Null sessions & share enumeration

**Difficulty**: Beginner-Intermediate | **Time**: 30-60 mins

## Architecture (Realistic Perimeter DMZ)
```
Internet ─┬─ HTTP (80) ── FTP (21) ── SSH (22)
          ├─ DNS (53) ─── SMTP (25) ─ SMB (445)
```
- Services interconnected via Docker network (simulating internal routing).
- Flags chained: Each protocol yields creds/hints for the next.
- Vulns based on **common misconfigs** (no zero-days).

## Quick Start
```bash
cd protocol-ctf
docker-compose up --build -d
```

**Targets** (localhost):
| Protocol | Port | Tool Examples |
|----------|------|---------------|
| HTTP     | 8082 | curl, browser |
| FTP      | 2121 | ftp, nmap |
| SSH      | 2222 | ssh, hydra |
| DNS      | 5354 | dig, nslookup |
| SMTP     | 2525 | telnet, swaks |
| SMB      | 1445 | smbclient, enum4linux |

```bash
docker-compose down -v  # Cleanup
```

## Walkthrough (Spoiler-Free Hints)
1. **HTTP**: Enumerate directories. Find FTP creds in `/app/config.txt` via LFI (e.g. `?doc=/app/config.txt`).
2. **FTP**: Login anonymous. Download `ssh_key.pem` & weak pass hint.
3. **SSH**: Use key + pass. `cat /home/user/flag.txt` & grep for SMTP user.
4. **DNS**: `dig AXFR @127.0.0.1 -p 5354 trailblazer.corp`. Get SMB share.

5. **SMTP**: `VRFY smbuser@trailblazer.corp` for pass. Relay test.
6. **SMB**: `smbclient //localhost:1445/share -N` or with creds. MASTER FLAG!

## Flags
- HTTP: `STELKCSC{http_enum_lfi}`
- FTP: `STELKCSC{ftp_anon_brute}`
- SSH: `STELKCSC{ssh_key_reuse}`
- DNS: `STELKCSC{dns_zone_xfer}`
- SMTP: `STELKCSC{smtp_vrfy_relay}`
- SMB: `STELKCSC{smb_null_shares}`
- **MASTER**: `STELKCSC{protocol_chain_mastery_2025}` (combine insights)

## Real-World Relevance
- Mirrors **perimeter hardening failures** (e.g., Equifax breach chaining).
- Tools: nmap, gobuster, hydra, crackmapexec.
- **Safety**: Local-only. No internet exposure.

## Troubleshooting
- Logs: `docker-compose logs service`
- Rebuild: `docker-compose up --build`
- Ports conflict? Edit `ports:` mappings.

**Enjoy the hunt!** 🕵️‍♂️
