# Nexus Gaming - Checkout Assurance (CTF)

**Difficulty:** Easy  
**Port:** 5006  
**Category:** Web Security / Payment Flow Hardening

---

## Scenario (Bug Bounty / Production-like)

**Program:** Nexus Gaming Enterprise Store (staging, internet-reachable in a real engagement; local in this lab)  
**Surface:** Checkout and payment submission flow  
**Context:** Frontend was recently refactored to speed up flash-sale checkouts. Security asked for a light-touch review to ensure pricing and totals still enforce business rules server-side.

---

### About Nexus Gaming

Nexus Gaming handles premium DLCs and season passes with high traffic during drops. Product and pricing data are rendered client-side for responsiveness; the backend is expected to verify any monetary fields before fulfillment.

### Rules / Scope

- Target: `http://[TARGET_IP]:5006`
- Test the purchase flow for gaps that allow underpayment/zero-cost checkout.
- Stay within the provided host/port. No external services, no auth brute force.
- Out of scope: DoS, social engineering, attacks on third-party processors.

---

## Setup (local lab)

```bash
docker-compose up -d --build
```

Access locally at: `http://localhost:5006`

---

## Skills Useful

- Basic web testing (forms, requests, DevTools/proxy)
- Understanding client vs server trust boundaries for price/total fields
