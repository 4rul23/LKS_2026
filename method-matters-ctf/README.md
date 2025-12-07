# 🏛️ NusantaraGateway - Internal API Documentation

**Project:** Core Payment Infrastructure (ID-Region)  
**Version:** v2.4.0-stable  
**Maintainer:** PT Nusantara Digital Solusi

---

## � Developer Internal Note (From: Chief Architect, Budi)

**Subject:** API Export Endpoint Security Update

Selamat Pagi Team,

We have successfully migrated the legacy payment gateway to the new **NusantaraGateway** infrastructure. The new system is designed to handle high-throughput IDR processing for our UMKM partners.

However, we are still auditing the **Data Export** module (`/api/v1/transactions/export`). The frontend team previously reported CORS issues, so we had to tweak the allowed HTTP methods configuration.

**Important Security Notice:** 
To comply with **UU PDP (Personal Data Protection Law)**, we have **DISABLED standard GET requests** on the export endpoint. This is to prevent sensitive transaction data from being cached in browser history or proxy logs.

Please perform your integration tests using the updated specifications. The endpoint should be strictly authenticated. If you encounter issues, check if the legacy HTTP methods (POST, etc.) are behaving as expected compared to the new security rules.

---

## 🔗 Endpoint Specifications

**Base URL:** `http://localhost:5005`

### Transaction Data Export
> **Warning:** This endpoint handles strict PII. All access is logged and audited.

- **Route:** `/api/v1/transactions/export`
- **Access Control:** Level 4 (Finance Director)
- **Supported Methods:** (Please check `OPTIONS`)

---

## � Environment Setup

To start the local development server:

```bash
docker-compose up -d --build
```

Access the dashboard at: `http://localhost:5005`

---

*© 2025 PT Nusantara Digital Solusi. All Rights Reserved. Confidential.*
