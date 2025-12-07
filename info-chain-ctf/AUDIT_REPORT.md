# 📋 Audit Report: NovaTech Info Chain CTF
**Date:** 2024-12-07  
**Auditor:** AntiGravity AI  
**Subject:** Structural Integrity & Real-World Relevance Assessment

---

## Executive Summary
The **NovaTech Info Chain CTF** has been audited for its suitability in educational and competitive environments. The challenge focuses on **Information Disclosure Chaining**, a critical skill set where attackers combine multiple minor leaks to achieve a critical compromise. It perfectly illustrates the concept of *"Death by a thousand cuts"*.

**Verdict:** ✅ **EXCELLENT EXAMPLE OF MODERN WEB RECONNAISSANCE**.

---

## 🔗 Chain Logic Analysis (Real-World Mapping)

The attack path is a classic "OSINT to Admin" flow: `Recon -> Discovery -> Credential Extraction -> Privilege Escalation`.

### 1. The .env Leak (`/.env`)
*   **Scenario:** The web server serves the sensitive `.env` configuration file to the public.
*   **Real-World Parallel:** This is one of the most common critical vulnerabilities in modern web apps (Laravel, Node.js, Django). Misconfigured Webpack, Nginx, or Docker deployments often expose this file.
*   **OWASP Category:** A05:2021 – Security Misconfiguration.
*   **Lesson:** "Dotfiles" must be explicitly denied in web server config.

### 2. Config File & Code Exposure (`/strapi/config/server.js`)
*   **Scenario:** The `.env` file hints at other config files, which are also readable.
*   **Real-World Parallel:** Once an attacker knows the tech stack (Strapi), they can guess standard file paths. If directory traversal or simple file serving is enabled, source code is leaked.
*   **Lesson:** Knowledge of the target's architecture (Tech Stack Fingerprinting) accelerates exploitation.

### 3. API Documentation Discovery (`/documentation/v1.0.0`)
*   **Scenario:** Finding unlisted API endpoints via exposed Swagger/OpenAPI specs.
*   **Real-World Parallel:** Developers often leave Swagger UIs (`/swagger`, `/docs`, `/api-docs`) enabled in production for convenience, inadvertently mapping the entire attack surface for the attacker.
*   **MITRE ATT&CK:** [T1592] Gather Victim Host Information.

### 4. Weak Internal Authentication (`X-Internal-Key`)
*   **Scenario:** Using a static API Key found in `.env` to access a "Debug" endpoint.
*   **Real-World Parallel:** Many "Internal" APIs rely on a single shared secret (API Key) rather than robust user authentication. If that key leaks (e.g. in `.env` or GitHub), the internal API is compromised.
*   **OWASP Category:** A07:2021 – Identification and Authentication Failures.

### 5. Critical Data Leakage (`super_admin_token`)
*   **Scenario:** The debug endpoint returns sensitive runtime data, including a Super Admin JWT.
*   **Real-World Parallel:** Debug endpoints (`/health`, `/metrics`, `/debug`) are notorious for over-sharing information (ENV vars, memory dumps, active tokens) which can lead to full account takeover.
*   **Impact:** Complete System Compromise (RCE or Full Admin Access).

---

## ⚖️ Competitive Balance

| Aspek | Penilaian | Catatan |
| :--- | :--- | :--- |
| **Alur Logika** | ⭐⭐⭐⭐⭐ (5/5) | Sangat linear. `Leak A` memberikan `Key B` untuk membuka `Pintu C`. Tidak ada tebak-tebakan. |
| **Realisme** | ⭐⭐⭐⭐⭐ (5/5) | Skenario ini (Env Leak -> API Key -> Admin) terjadi setiap hari di dunia Bug Bounty. |
| **Edukasi** | ⭐⭐⭐⭐ (4/5) | Mengajarkan pentingnya **Secrets Management** dan **API Security**. |

---

## 🛠️ Rekomendasi
*   **Hinting**: Jika siswa buntu di awal, berikan hint untuk memeriksa "file konfigurasi standar" atau "common dotfiles".
*   **Post-Exploitation**: Saat ini challenge berhenti di mendapatkan Flag. Untuk tingkat lanjut, bisa ditambahkan step untuk *menggunakan* Admin Token tersebut untuk melakukan aksi write (misal: defacement palsu), tapi untuk level LKS/CTF standar, current state sudah cukup.

**Kesimpulan:** Challenge ini sangat rapi dan mencerminkan kesalahan konfigurasi modern pada aplikasi Cloud-Native/Microservices.
