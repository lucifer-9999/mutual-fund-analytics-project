# Data Dictionary

## fact_nav

| Column | Type | Description |
|-------|------|-------------|
| amfi_code | Integer | Mutual Fund Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|-------|------|-------------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |

## fact_performance

| Column | Type | Description |
|-------|------|-------------|
| aum_crore | Float | Assets Under Management |
| expense_ratio_pct | Float | Expense Ratio |
| sharpe_ratio | Float | Sharpe Ratio |
| risk_grade | Text | Risk Category |