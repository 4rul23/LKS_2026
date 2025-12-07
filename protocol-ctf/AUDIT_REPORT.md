# 📋 Audit Report: Protocol Chain CTF
**Date:** 2024-12-07  
**Auditor:** AntiGravity AI  
**Subject:** Structural Integrity & Real-World Relevance Assessment for LKS Competition

---

## Executive Summary
The **Protocol Chain CTF** has been audited for its suitability in the *Lomba Kompetensi Siswa (LKS)*. The challenge creates a highly realistic simulation of an **Internal Infrastructure Penetration Test**. Unlike abstract CTFs that rely on guessing or cryptography, this scenario simulates a chain of **misconfigurations**, which is the #1 cause of data breaches in the real world.

**Verdict:** ✅ **HIGHLY RECOMMENDED** for Pre-OWASP/Network Security Stage.

---

## 🔗 Chain Logic Analysis (Real-World Mapping)

The attack path follows a logical linear progression: `Recon -> Initial Access -> Credential Harvesting -> Lateral Movement`.

### 1. HTTP Local File Inclusion (LFI)
*   **Scenario:** A legacy "Intranet Portal" uses a simple parameter (`?doc=`) to load files.
*   **Real-World Parallel:** Common in legacy PHP/Python web apps or simple internal dashboards that lack input sanitization.
*   **MITRE ATT&CK:** [T1190] Exploit Public-Facing Application.
*   **Skill Check:** Ability to recognize dangerous URL parameters and understand file system paths (`/app/config.txt`).

### 2. FTP Anonymous Access
*   **Scenario:** An FTP server allows `anonymous` login and contains sensitive keys.
*   **Real-World Parallel:** Developers often enable anonymous FTP for convenient file sharing within an internal LAN and forget to disable it. Critical files (`.pem` keys) are accidentally left in "public" folders.
*   **MITRE ATT&CK:** [T1078] Valid Accounts (Default).
*   **Skill Check:** Standard service enumeration (checking if 'anonymous' works).

### 3. SSH Pivot (Credential Reuse)
*   **Scenario:** The stolen SSH key is protected by a passphrase found in the key's comment (`trailblazer2025`).
*   **Real-World Parallel:** **Credential Reuse** and **Hardcoded Secrets** are pandemic. Admins often put passwords in comments, descriptions, or sticky notes to help teammates.
*   **MITRE ATT&CK:** [T1552] Unsecured Credentials in Files.
*   **Skill Check:** Key handling (`chmod 600`) and recognizing metadata/comments in files.

### 4. DNS Zone Transfer (AXFR)
*   **Scenario:** The internal DNS server allows anyone to request a full copy of the `trailblazer.corp` zone.
*   **Real-World Parallel:** Internal DNS servers (BIND/Windows DNS) are often configured with `allow-transfer { any; };` for ease of replication between servers, assuming "trust" within the LAN.
*   **MITRE ATT&CK:** [T1590] Gather Victim Network Information: DNS.
*   **Skill Check:** Understanding that DNS is not just for pinging, but contains network topology.

### 5. SMTP User Enumeration (VRFY)
*   **Scenario:** The Mail Server allows the `VRFY` command to confirm user existence and returns debug info (the password).
*   **Real-World Parallel:** Legacy mail servers or "Development Mode" mail relays often leave debug commands (`VRFY`, `EXPN`) enabled. Attackers use this to build valid user lists for phishing/brute-force.
*   **MITRE ATT&CK:** [T1087] Account Discovery.
*   **Skill Check:** Interacting with raw protocols via `netcat`/`telnet`.

### 6. SMB Share Access
*   **Scenario:** Accessing a restricted Finance share using credentials harvested from the previous step.
*   **Real-World Parallel:** SMB Shares are the gold mine of internal networks. Once credentials are obtained, attackers immediately hunt for "Backup", "Finance", or "HR" shares.
*   **MITRE ATT&CK:** [T1021] Remote Services: SMB/Windows Admin Shares.
*   **Skill Check:** Using `smbclient` with specific authentication.

---

## ⚖️ Competitive Balance (LKS Context)

| Aspek | Penilaian | Catatan |
| :--- | :--- | :--- |
| **Kejelasan Alur** | ⭐⭐⭐⭐⭐ (5/5) | Siswa tidak akan "tersesat". Setiap flag memberikan hint eksplisit untuk port berikutnya. |
| **Tingkat Kesulitan** | ⭐⭐⭐⭐ (4/5) | Pas untuk SMK. Tidak terlalu mudah (script kiddie), tapi tidak mustahil (expert). |
| **Variasi Tools** | ⭐⭐⭐⭐⭐ (5/5) | Memaksa penggunaan CLI (`curl`, `ssh`, `dig`, `nc`, `smbclient`) daripada tool GUI otomatis. |
| **Edukasi** | ⭐⭐⭐⭐⭐ (5/5) | Mengajarkan bahwa *hacking* adalah tentang memahami cara kerja protokol, bukan magic. |

## 🛠️ Rekomendasi Final

1.  **Network Segregation**: Pastikan saat lomba, setiap peserta mendapatkan instance Docker sendiri (Isolated Network) untuk mencegah *flag sharing* atau *interference*.
2.  **Scoring Weight**: Berikan bobot lebih besar pada **SMB (Final Flag)** karena itu membuktikan siswa berhasil merangkai seluruh serangan.

**Conclusion:** Struktur challenge ini sudah **World-Class** untuk kategori Educational CTF. Sangat merefleksikan metodologi *Internal Network Penetration Test*.
