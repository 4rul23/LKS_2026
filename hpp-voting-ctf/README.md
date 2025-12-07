# 🇮🇩 SIREKAP - Sistem Informasi Rekapitulasi (Ver. 2.4.0-BETA)

> **DOKUMEN NEGARA - SANGAT RAHASIA**
> HANYA UNTUK KEPENTINGAN PENGUJIAN INTERNAL KPU

**KEMENTERIAN DALAM NEGERI REPUBLIK INDONESIA**
**KOMISI PEMILIHAN UMUM (KPU)**

---

## 📜 Dasar Hukum
1.  Undang-Undang Nomor 7 Tahun 2017 tentang Pemilihan Umum.
2.  Peraturan KPU Nomor 3 Tahun 2022 tentang Tahapan dan Jadwal Penyelenggaraan Pemilu.
3.  Surat Edaran KPU No. 17/TI.05/2024 tentang Uji Kelayakan Sistem e-Voting.

## 🎯 Tujuan Pengujian
Aplikasi ini adalah **prototipe** SIREKAP v2 yang sedang dalam tahap *Stress Test* dan *Vulnerability Assessment*. 
Anda ditugaskan sebagai **Tenaga Ahli IT Independen** untuk melakukan verifikasi integritas sistem sebelum peluncuran nasional.

**Fokus Pengujian:**
- Memastikan prinsip **One Person One Vote** (OPOV).
- Menguji ketahanan sistem terhadap manipulasi parameter suara.
- Memverifikasi mekanisme validasi NIK Pemilih Tetap (DPT).

---

## 🏗️ Petunjuk Teknis (Juknis)
Untuk menjalankan lingkungan simulasi pemilihan umum:

```bash
docker-compose up -d --build
```

**Akses Sistem:**
- URL: `http://localhost:5008`
- NIK Pemilih Terdaftar: `3174052001950005` (Warga Sipil)

---

## ⚠️ Peringatan Keamanan (Sangat Penting)
Sistem ini dilengkapi dengan **Firewall Aplikasi Web (WAF) Generasi 1** yang memfilter input pengguna.
Logika validasi saat ini:
> *"Sistem memverifikasi parameter `voter_id` pertama yang dikirimkan oleh klien. Jika cocok dengan sesi login, transaksi dilanjutkan."*

**Tugas Anda:**
Sebagai auditor keamanan, buktikan bahwa mekanisme ini **CACAT** dan temukan cara untuk memasukkan suara atas nama **Ketua KPU Pusat** (Privileged Actor) guna mengakses menu *Super Admin Verification*.

---

*“Bersama KPU, Kita Wujudkan Pemilu LUBER JURDIL”.*
*Pusat Data dan Informasi (PUSDATIN) KPU - Jakarta, Indonesia.*
