# Python Assignment: Caesar Cipher & Login System

## Part 1 — Caesar Cipher

The Caesar cipher is one of the oldest known encryption techniques, named after Julius Caesar who reportedly used it for secret military communications. The cipher works by shifting each letter in the message by a fixed number of positions in the alphabet. For example, with a shift of 3, `'A'` becomes `'D'`, `'B'` becomes `'E'`, and so on.

---

### Program Requirements

The program should create an interactive experience where users can repeatedly encode or decode messages until they choose to stop. Each interaction should follow this exact sequence:

1. Prompt user to choose between `'encode'` or `'decode'`
2. Get message input from user
3. Get shift number from user
4. Display encoded/decoded result
5. Ask if user wants to repeat (`y/n`)
6. Exit with a "goodbye" message if user chooses `'n'`

**Expected interaction:**

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
Hello Hult LSN!

Type the shift number:
5

Here's the encoded result: Mjqqt Mzqy QUR!

do you want to repeat? (y/n)
y

Type 'encode' to encrypt, type 'decode' to decrypt:
decode

Type your message:
Mjqqt Mzqy QUR!

Type the shift number:
5

Here's the decoded result: Hello Hult LSN!

do you want to repeat? (y/n)
n
OK byee!!
```

---

### Technical Implementation Details

#### Character Case Handling
- The program must preserve the original case: uppercase stays uppercase, lowercase stays lowercase
- Example: with shift 5, `'H'` (position 8) moves to `'M'` (position 13), so `"Hello"` becomes `"Mjqqt"`, not `"mjqqt"`

#### Special Character Preservation
- Numbers, spaces, and punctuation marks should pass through unchanged
- Example: in `"Hello LSN!"`, only `H`, `e`, `l`, `l`, `o`, `L`, `S`, `N` are shifted — the space and `!` remain in place

#### Alphabet Wrapping
- When shifting near the end of the alphabet, wrap around to the beginning
- Example with shift 5: `'z'` → `'e'`
- Example when decoding: `'a'` with shift 5 wraps backward to `'v'`

#### Encoding vs Decoding
- **Encoding** shifts forward in the alphabet by the shift number
- **Decoding** shifts backward in the alphabet by the shift number
- They are opposite operations: encoding `"hello"` with shift 5 gives `"mjqqt"`, decoding `"mjqqt"` with shift 5 gives back `"hello"`

---

### Edge Cases

The program should handle the following gracefully:
- Empty messages
- Messages with only special characters
- Different shift numbers
- Repeated operations without issues

---

### Test Cases

| # | Input | Shift | Operation | Expected Output |
|---|-------|-------|-----------|-----------------|
| 1 | `"hello LSN!"` | 5 | encode | `"mjqqt QXS!"` |
| 2 | `"mjqqt QXS!"` | 5 | decode | `"hello LSN!"` |

---

## Part 2 — Login System

In this part, you will build a simple user authentication system using Python where users can sign up, log in, and have their passwords stored securely using **salting & hashing**.

You will use Python's built-in `hashlib` and `os` modules.

---

### Tasks

#### User Sign-Up
1. Ask the user to create a username
2. Ask them to create a password
3. Generate a random salt
4. Hash the password using SHA-256 combined with the salt
5. Store the username, salt, and hashed password in a dictionary

#### User Login
1. Ask the user to enter their username and password
2. Retrieve the stored salt and hashed password from the dictionary
3. Hash the entered password with the same salt
4. Compare the new hash with the stored hash
5. Print `✅ Login successful!` if they match, otherwise print `❌ Incorrect password.`

---

### Expected Interaction

```
1️⃣ Sign Up  |  2️⃣ Log In  |  3️⃣ Exit
Choose an option (1/2/3): 1
Choose a username: alice
Create a password: mysecurepassword
✅ Account created successfully!


1️⃣ Sign Up  |  2️⃣ Log In  |  3️⃣ Exit
Choose an option (1/2/3): 2
Enter your username: alice
Enter your password: mysecurepassword
✅ Login successful!


1️⃣ Sign Up  |  2️⃣ Log In  |  3️⃣ Exit
Choose an option (1/2/3): 2
Enter your username: alice
Enter your password: wrongpassword
❌ Incorrect password. Try again.


1️⃣ Sign Up  |  2️⃣ Log In  |  3️⃣ Exit
Choose an option (1/2/3): 3
Goodbye! 👋
```

---

### Requirements

- Use a dictionary (`user_database`) to store users' credentials
- Generate a random salt for each user
- Store **only** the hashed password and salt — never the original password
- Verify passwords correctly during login
- Allow multiple users to sign up and log in
- Use `input()` for user interaction
- Use only built-in modules: `hashlib` and `os`

---

### Hints

```python
# Generate a random salt
salt = os.urandom(16)

# Hash a password with the salt
hashed = hashlib.sha256(salt + password.encode()).hexdigest()

# Store the salt as a hex string
stored_salt = salt.hex()

# Convert hex back to bytes when verifying
salt_bytes = bytes.fromhex(stored_salt)
```

---

## Submission

Submit the following via **Canvas**:

1. `caesar.py` — right-click the file name and download from Codespaces
2. A comment (~50–100 words) describing the most challenging part of coding the Caesar cipher
3. `login.py`
4. A comment (~50–100 words) describing the most challenging part of the login system

> ⚠️ **Do not email submissions.** Email submissions will not be accepted.