# RULES.md

## Overview
This document outlines the rules and validation criteria for inputs and data processing in the Credit Card Statement Generator system. These rules apply to customer data, credit card accounts, transactions, and PDF output formatting.

---

## 1. Customer ID
- **Type:** Integer
- **Required:** Yes
- **Validation:** Must exist in the database
- **Error if:** Not found or non-numeric

---

## 2. Language
- **Type:** String (2-letter language code)
- **Required:** Yes
- **Allowed values:**
  - `en` – English
  - `ta` – Tamil
  - `hi` – Hindi
  - `ar` – Arabic
  - `zh` – Chinese
  - `fr` – French
  - `es` – Spanish
  - `ms` – Malay
  - `ja` – Japanese
  - `de` – German
- **Fallback:** Defaults to `en` (English) if missing or invalid

---

## 3. Card Number
- **Type:** String
- **Length:** 16 digits
- **Format:** `#### #### #### ####`
- **Validation:** Must be unique and assigned to a valid customer

---

## 4. Transaction Data
- **Date:** Must be in `YYYY-MM-DD` format
- **Merchant Name:** Max 100 characters
- **Amount:** Decimal (positive)
- **Transaction Type:** One of `Purchase`, `Payment`, `Cash`, `Refund`

---

## 5. Reward Points
- **Earned & Redeemed:** Must be non-negative integers
- **Available Points:** Calculated as Earned - Redeemed
- **No points data:** Show as `0` in the PDF

---

## 6. Account Summary Fields
| Field              | Type     | Rules                                |
|-------------------|----------|---------------------------------------|
| PreviousBalance   | Decimal  | ≥ 0.00                                |
| TotalPayment      | Decimal  | ≥ 0.00                                |
| NewPurchases      | Decimal  | ≥ 0.00                                |
| Interest          | Decimal  | ≥ 0.00                                |
| MinDue            | Decimal  | ≥ 0.00                                |
| TotalDue          | Decimal  | ≥ 0.00                                |
| DueDate           | Date     | Must be future or today               |
| CreditLimit       | Decimal  | ≥ 0.00                                |
| AvailableCredit   | Decimal  | Between 0 and CreditLimit             |
| CashLimit         | Decimal  | ≥ 0.00                                |
| AvailableCash     | Decimal  | Between 0 and CashLimit               |

---

## 7. PDF Output
- **Must include:**
  - Customer info
  - Card and account details
  - Transaction table (latest 10)
  - Reward points section (if available)
  - Footer with contact info
- **Multi-language:** Labels and headings must reflect selected language
- **RTL support:** Enabled for Arabic (`ar`) language

---

## 8. Error Handling
| Scenario                            | Message                         |
|-------------------------------------|----------------------------------|
| Invalid or missing customer ID      | `Customer ID is required`       |
| Customer not found                  | `Customer not found`            |
| No account linked to customer       | `Account not found`             |
| Backend/server issues               | `Unable to generate statement`  |
| Unsupported language code           | Defaults to English             |

---

## 9. API Endpoint
 - `GET /api/generate-statement/?customer_id=1001&language=en`


---

## Author
Developed by **Saris T S**  
Backend: Django REST | Frontend: React | PDF: WeasyPrint  
