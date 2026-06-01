# Problem Set 1 — Solution Guide
**LSN-0104 | Variables, Data Types & Strings**

> This guide walks through each exercise with the complete solution and explanation of key concepts. Read the comments carefully — they explain the *why*, not just the *what*.

---

## Exercise 1 — Hello, Business World! (10 pts)

### Solution

```python
# Get first name, last name, and company from the user
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
company_name = input("What is your company name? ")

# Combine first and last name into full_name
full_name = first_name + " " + last_name

# Convert company to Title Case using .title()
company_name = company_name.title()

# Print the greeting — note: name stays in its original casing here
print(f"Hello, {full_name} from {company_name}! Welcome to Python.")

# Print full name in ALL CAPS using .upper()
print(f"Full name (uppercase): {full_name.upper()}")

# Print company in Title Case
print(f"Company (title case): {company_name}")

# Print the character count of the full name (includes the space)
print(f"Name length: {len(full_name)} characters")
```

### Expected Output
```
Hello, Maria Garcia from Globex Industries! Welcome to Python.
Full name (uppercase): MARIA GARCIA
Company (title case): Globex Industries
Name length: 12 characters
```

### Key Concepts
| Method | What it does |
|---|---|
| `input()` | Pauses the program and waits for user to type something |
| `.upper()` | Returns a new string in ALL CAPS — does not modify the original |
| `.title()` | Capitalizes the first letter of every word |
| `len()` | Returns the number of characters in a string (spaces count!) |

---

## Exercise 2 — Invoice Calculator (20 pts)

### Solution

```python
# Gather inputs — note the type conversions: float for price, int for quantity
product_name = input("What is the product name? ")
unit_price = float(input("What is the unit price? "))
quantity = int(input("How many? (quantity) "))

# Calculations — keep full precision here, round only for display
subtotal = unit_price * quantity
tax = subtotal * 0.08
total = subtotal + tax

# Print the formatted invoice
print("\n===== INVOICE =====")
print(f"Product:    {product_name}")
print(f"Unit Price: ${unit_price:.2f}")   # :.2f displays exactly 2 decimal places
print(f"Quantity:   {quantity}")
print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax (8%):   ${tax:.2f}")
print(f"Total Due:  ${total:.2f}")
print("===================")
```

### Expected Output
```
===== INVOICE =====
Product:    Widget Pro
Unit Price: $24.99
Quantity:   5
Subtotal:   $124.95
Tax (8%):   $9.996
Total Due:  $134.95
===================
```

### Key Concepts
| Concept | Why it matters |
|---|---|
| `float(input(...))` | `input()` always returns a string — you must convert it to a number before doing math |
| `int(input(...))` | Use `int` for whole numbers like quantity, `float` for prices |
| `:.2f` in f-strings | Formats a number for *display* with 2 decimal places — the underlying value is unchanged |

> **Note:** `:.2f` is for display only. The actual value of `tax` is still `9.996`. For real financial systems you would use the `Decimal` module to handle money precisely.

---

## Exercise 3 — Customer Data Cleaner (20 pts)

### Solution

```python
# Hard-coded messy input data
raw_name  = '  jANe  dOe  '
raw_email = '  Jane.Doe@COMPANY.COM  '
raw_phone = '(617) 555-0142'

# Strip leading/trailing whitespace, then apply correct casing
clean_name  = raw_name.strip().title()
clean_email = raw_email.strip().lower()

# Check email domain and classify the contact
if clean_email.endswith("@company.com"):
    status = "Internal employee"
else:
    status = "External contact"

# Extract the area code — index [1:4] skips the '(' and grabs 3 digits
area_code = raw_phone[1:4]

# Print the formatted customer card
print("===== CUSTOMER CARD =====")
print(f"Name:      {clean_name}")
print(f"Email:     {clean_email}")
print(f"Area Code: {area_code}")
print(f"Status:    {status}")
print("=========================")
```

### Expected Output
```
===== CUSTOMER CARD =====
Name:      Jane Doe
Email:     jane.doe@company.com
Area Code: 617
Status:    Internal employee
=========================
```

### Key Concepts
| Concept | Explanation |
|---|---|
| `.strip()` | Removes whitespace from both ends of a string |
| `.title()` | Capitalizes the first letter of each word |
| `.lower()` | Converts the entire string to lowercase |
| `.endswith()` | Returns `True` if the string ends with the given substring — case-sensitive, so lowercase first |
| String slicing `[1:4]` | Extracts characters at index 1, 2, 3 (stops *before* 4) — skips the `(` at index 0 |

> **Tip on slicing:** In `'(617) 555-0142'`, index `0` is `(`, indexes `1–3` are `617`, and index `4` is `)`. So `[1:4]` gives us exactly the area code.

---

## Exercise 4 — Profit Margin Calculator (10 pts)

### Solution

```python
import math

# Get revenue and COGS from the user
revenue = float(input("What is the revenue? "))
cogs = float(input("What is the cost of goods sold? "))

# Calculate gross profit and gross margin percentage
gross_profit = revenue - cogs
gross_margin = (gross_profit / revenue) * 100

# Display results with 2 decimal places and % symbol
print(f"\nGross Profit:  ${gross_profit:.2f}")
print(f"Gross Margin:  {gross_margin:.2f}%")

# math.ceil rounds UP to the nearest whole number
print(f"Margin (ceiling): {math.ceil(gross_margin)}%")

# math.floor rounds DOWN to the nearest whole number
print(f"Margin (floor):   {math.floor(gross_margin)}%")
```

### Expected Output (for revenue: 1,000,000 / COGS: 873,211)
```
Gross Profit:  $126789.00
Gross Margin:  12.68%
Margin (ceiling): 13%
Margin (floor):   12%
```

### Key Concepts
| Function | Behavior | Example |
|---|---|---|
| `math.ceil()` | Always rounds **up** | `ceil(12.1)` → `13` |
| `math.floor()` | Always rounds **down** | `floor(12.9)` → `12` |
| `round()` | Rounds to nearest (banker's rounding) | `round(12.5)` → `12` |

---

## Bonus — `round()` vs `:.2f` in Finance (+5 pts)

```python
# round() changes the actual numeric value stored in memory
rounded_margin = round(gross_margin, 2)
print(f"Using round():  {rounded_margin}")   # e.g. 12.68 — a float

# :.2f only changes how the number is displayed — value is unchanged
print(f"Using :.2f:    {gross_margin:.2f}")  # e.g. "12.68" — a string for display
```

### When rounding vs. display matters in finance

```python
# WRONG: rounding intermediate values causes accumulated errors
prices = [1.005, 2.005, 3.005]
total_wrong = sum(round(p, 2) for p in prices)  # 6.01

# RIGHT: keep full precision through all calculations, round only at the end
total_right = round(sum(prices), 2)              # 6.02
```

> **Rule of thumb:** Use `:.2f` for anything shown on screen. Use `round()` sparingly and only at the *end* of a calculation chain — never in the middle. For regulated financial systems (tax, accounting), use Python's `Decimal` module with an explicit rounding mode.

---

## Quick Reference — String Methods Used in This Problem Set

| Method | Example | Result |
|---|---|---|
| `.upper()` | `"hello".upper()` | `"HELLO"` |
| `.lower()` | `"HELLO".lower()` | `"hello"` |
| `.title()` | `"jane doe".title()` | `"Jane Doe"` |
| `.strip()` | `"  hi  ".strip()` | `"hi"` |
| `.endswith()` | `"a@b.com".endswith(".com")` | `True` |
| `len()` | `len("Maria Garcia")` | `12` |
| Slicing `[i:j]` | `"(617)"[1:4]` | `"617"` |