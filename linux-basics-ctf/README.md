# 🐧 Linux Basics CTF - The Lost Key

**Difficulty:** Easy  
**Category:** Linux Fundamentals  
**Port:** 2222 (SSH)

## 📝 Scenario

Sysadmin sebelumnya meninggalkan server secara tiba-tiba. Tim IT membutuhkan bantuan Anda untuk menemukan recovery key yang tersimpan di suatu tempat di server ini.

**Credentials:**
- **User:** `ctfuser`
- **Password:** `intership2024`

## 🎯 Objective

Connect via SSH dan temukan flag yang tersembunyi. Ikuti petunjuk yang ada di server.

## 🛠️ Connection

```bash
ssh ctfuser@<SERVER_IP> -p 2222
```

## 💡 Hints

- Baca file yang ada di home directory Anda
- Perhatikan semua informasi yang Anda temukan
- Gunakan command `ls -la` untuk melihat hidden files
- Explore direktori `/home` untuk melihat user lain

## 🔧 Local Setup (Juri Only)

```bash
docker-compose up -d --build
```

Connect locally: `ssh ctfuser@localhost -p 2222`
