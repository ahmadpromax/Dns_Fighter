<div align="center">
  <img src="banner.svg" alt="DNS Fighter Banner" width="100%">
</div>

# ⚔️ DNS Fighter – Stop DNS Poisoning & Speed Up Your Browsing

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)

> **English** | [فارسی](README.fa.md)

---

## 🚀 What is DNS Fighter?

**DNS Fighter** is a fast, multi‑threaded Windows tool that automatically resolves domain names using multiple DNS servers and writes the IP addresses directly into your **hosts** file. By doing this, it completely bypasses your system DNS resolver.

**Benefits:**

- 🛡️ **Blocks DNS poisoning** – No more fake websites
- ⚡ **Faster browsing** – Eliminates DNS lookup delays (0 ms!)
- 🔍 **Compare up to 4 DNS servers** side‑by‑side
- 📈 **Advanced protocol tests** – ICMP, TCP, UDP, HTTP, HTTPS, TLS
- 🔄 **Auto‑update** – Set it and forget it

---

## 🧠 How It Works (Simple)

| Normal (Without DNS Fighter) | ✅ With DNS Fighter |
|:---|:---|
| 🌐 1- Browser sends a **DNS request** over the network. | 🌐 1- Browser reads IP directly from the **hosts file**. |
| ⚠️2- **DPI can intercept** and send a fake (spoofed) IP. | 🛡️ 2- **No DNS request** is sent – DPI sees nothing. |
| 🎭 3- You are redirected to a **fake website** (phishing / blocked). | ✅ 3- You go directly to the **real website**. |
| 🐢 4- 20‑100 ms delay, 🔓 high poisoning risk, 👁️ low privacy. | ⚡ 4- **0 ms delay**, 🔒 **zero risk**, 👁️ **perfect privacy**. |

---

## 🔥 Key Features

| Feature | Description |
|---------|-------------|
| 🛡️ **DNS Poisoning Prevention** | Stores resolved IPs in the Windows `hosts` file, bypassing system DNS. |
| ⚡ **Blazing Fast** | Multi‑threaded (`MAX_WORKERS = 40`) – even with hundreds of domains. |
| 🔍 **Multi‑DNS Comparison** | Compare up to 4 DNS servers (Google, Cloudflare, Shecan, Begzar, etc.). |
| 📈 **Advanced Reachability Test** | Tests 7 protocols (ICMP, TCP, UDP, HTTP, HTTPS, TLS). |
| 🔄 **Auto‑Update** | Remembers your choice and updates the `hosts` file automatically. |
| 📁 **Domain Categorization** | Organised `domains.txt` file – new domains go to `User Custom`. |
| 🎮 **Interactive & Non‑Interactive Modes** | Use manually or integrate into scripts / Task Scheduler. |
| 💰 **Free & Open Source** | MIT License. |

---

## 📂 Why These Domains?

The included `domains.txt` has **300+ carefully selected domains** to boost speed and privacy.

| Category | Benefit |
|----------|---------|
| **Fonts** | Instant font loading on every website |
| **General CDNs** | Caches common JS/CSS libraries (jQuery, Bootstrap) |
| **Trackers & Analytics** | Reduces tracking, improves privacy |
| **Ad Networks** | Blocks ad‑related delays |
| **Video Streaming** | Reduces buffering (YouTube, Netflix, etc.) |
| **Captcha Services** | Faster CAPTCHA verification |
| **Microsoft Updates** | Faster Windows / Office updates |
| **WordPress Resources** | Quicker plugin / theme downloads |
| **Iranian CDNs & Tools** | Much faster for users inside Iran |
| **User Custom** | Add your own domains |

> 💡 **How to use it:** Run DNS Fighter, select **"Use existing categories"**, and it resolves and stores all these domains for you. You can edit `domains.txt` anytime – the script preserves the structure.

---

## ❤️ Support the Developer

If DNS Fighter makes your internet safer and faster, please ⭐ **Star** this repository. You can also donate via cryptocurrency:

```
USDT (TRC20): TQWRW7Zo35WyqZSBYGp4uEycNu7P8bBYDs
USDT (BEP20): 0x6a0f997D86B2A32AE973947C73800e6688F4e5d2
USDT (TON):   UQBi75cUao86m8EIxCYWSLUqo4mP28DX3ZcBqvQZGvnfrGPI
```

---

## 📦 Requirements

- Windows 7 / 8 / 10 / 11
- Python 3.6 or higher
- Administrator rights (to modify `C:\Windows\System32\drivers\etc\hosts`)

---

## 🛠️ Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/).
2. Run the installer – **check ✅ "Add Python to PATH"**.
3. Verify installation:
   ```cmd
   python --version
   ```

### Step 2: Install Dependency

**Automatic (recommended):** Double‑click `install_dependencies.bat` inside the repository.
or


**Manual (if automatic fails):**
```cmd
pip install dnspython -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com
```
Or simply:
```cmd
pip install dnspython
```

---

## 🎮 How to Use

### 1️⃣ Interactive Mode (default)

**Automatic (recommended):** Double‑click `admin_run.bat` inside the repository.
or


**Manual:** open CMD as Administrator:

```cmd
python dns_fighter.py
```

Then follow the prompts:

- Choose domain source (existing categories or manual entry)
- Pick up to 4 DNS resolvers
- Set timeout (1‑5 seconds, default 2)
- Enable/disable ping check and Auto‑Update

After the comparison table appears:

- Enter a **number** to use that resolver for **all** domains
- Enter **`p`** to pick per domain individually
- Enter **`c`** to use consensus (most frequent IP)
- Enter **`a`** to run **advanced reachability test**

### 2️⃣ Advanced Reachability Test

Select `a`, choose a resolver, and DNS Fighter will:

- Test each IP against 7 protocols
- Show a table with ✓ / ✗
- Ask which protocols must succeed
- **Only keep domains that pass all selected protocols** – then save them

### 3️⃣ Auto‑Update Mode

When you enable Auto‑Update:

- Runs once interactively to let you choose a resolver (or consensus)
- Saves your choice to `last_resolver.txt`
- Then updates the hosts file every X hours **without further questions**

### 4️⃣ Non‑Interactive Mode (for automation)

```cmd
python dns_fighter.py --non-interactive --domains-file domains.txt --dns-list 1,4 --ping --timeout 3
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `--auto-update` | Run continuously |
| `--interval` | Interval in seconds (for auto‑update) |
| `--domains-file` | Plain text file with domains (one per line) |
| `--dns-list` | Comma‑separated DNS keys (e.g., `1,3,5` or `local`) |
| `--non-interactive` | No user prompts – auto‑approve |
| `--use-resolver` | Force resolver number N (1‑based) for all domains |
| `--ping` | Enable ping checks |
| `--timeout` | DNS resolution timeout (1‑5 seconds, default 2) |

---

## 📂 File Structure

| File | Purpose |
|------|---------|
| `dns_fighter.py` | Main script |
| `banner.svg` | Banner image for README |
| `architecture.svg` | architecture image for README |
| `domains.txt` | Categorised domain list (editable) |
| `admin_run.bat` | Batch file to auto‑elevate privileges |
| `install_dependencies.bat` | Automatically installs the library |
| `last_resolver.txt` | Stores your last resolver choice (auto‑created) |
| `LICENSE` | MIT License |

---

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| `Administrator privileges required` | Run CMD or the batch file as Administrator |
| `No module named 'dns'` | Install `dnspython` using `install_dependencies.bat` |
| `File "domains.txt" gets messed up` | Delete it and let the script recreate a fresh one |
| `Advanced test says "No valid IPs"` | Make sure the selected resolver actually returned some IPs |
| `pip install fails` | Try the Iranian mirror, a VPN, or download `dnspython` manually from [PyPI](https://pypi.org/project/dnspython/) |

---

## 📄 License

This project is licensed under the **MIT License**. Please give credit to the original author (`Ahmadpromax` on GitHub) and consider ⭐ starring the repository.

---

**Enjoy a faster, more secure internet!**  
**Ahmadpromax – 2026**
