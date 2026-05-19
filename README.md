# ⚔️ DNS Fighter – Stop DNS Poisoning & Speed Up Your Browsing

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)

**DNS Fighter** is a powerful, multi‑threaded command‑line tool for Windows that automatically resolves domain names using multiple DNS servers and writes the obtained IP addresses directly into your **hosts** file.  
By doing so, it completely bypasses the system DNS resolver – which means **no more DNS poisoning attacks, faster web browsing, and full control over which IPs your computer connects to.**

> 💡 **What does this mean for you?**  
> - **Stop hackers** from redirecting you to fake websites (DNS spoofing).  
> - **Speed up page loading** by eliminating DNS lookup delays.  
> - **Compare results** from up to 4 DNS servers at once.  
> - **Test advanced protocols** (ICMP, TCP, UDP, HTTP, HTTPS, TLS) to verify reachability.  
> - **Automatically keep your hosts file up‑to‑date** with the IPs you choose.

---

## 🚀 What can DNS Fighter do?

| Feature | Description |
|---------|-------------|
| 🛡️ **DNS Poisoning Prevention** | Writes resolved IPs into the Windows `hosts` file, bypassing the system DNS resolver. |
| ⚡ **Blazing Fast** | Multi‑threaded resolution (`MAX_WORKERS = 40`) – even with hundreds of domains. |
| 🔍 **Multi‑DNS Comparison** | Choose up to 4 DNS servers (Google, Cloudflare, Shecan, Begzar, etc.) and compare their responses side by side in a clean table. |
| 📈 **Advanced Reachability Test** | Test **7 different protocols** (ICMP, TCP/80, TCP/443, UDP/53, HTTP GET, HTTPS GET, TLS handshake) on the IPs obtained from any resolver. |
| 🔄 **Auto‑Update** | After you pick a resolver, DNS Fighter remembers your choice and automatically updates the `hosts` file at any interval you set (e.g., every 2 hours). |
| 📁 **Domain Categorization** | Organise your domains in a structured `domains.txt` file (Fonts, CDNs, Trackers, etc.). New domains go into `User Custom`. |
| 🎮 **Interactive & Non‑Interactive Modes** | Use it manually or integrate it into scripts and Task Scheduler with command‑line arguments. |
| 💰 **Free & Open Source** | Released under the **MIT License**. No strings attached, but your support keeps the project alive. |

---

## ❤️ Support the Developer

If DNS Fighter makes your browsing safer and faster, please consider giving this project a **⭐ Star on GitHub** – it helps others discover it. You can also support me via cryptocurrencies:
USDT (TRC20): TQWRW7Zo35WyqZSBYGp4uEycNu7P8bBYDs
USDT (BEP20): 0x6a0f997D86B2A32AE973947C73800e6688F4e5d2
USDT (TON):   UQBi75cUao86m8EIxCYWSLUqo4mP28DX3ZcBqvQZGvnfrGPI
```

> Every star and donation encourages further development. Thank you! 🙏

---

## 📦 Requirements

- **Windows** 7 / 8 / 10 / 11  
- **Python** 3.6 or higher  
- **Administrator rights** (to modify `C:\Windows\System32\drivers\etc\hosts`)  

---

## 🛠️ Installation

1. **Clone or download** this repository.  
2. **Install the required library** (use an Iranian mirror if needed):

   ```cmd
   pip install dnspython -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com
   ```

   (If the mirror fails, just use `pip install dnspython`.)

---

## 🎮 How to Use

### 1️⃣ Interactive Mode (default)

Run as Administrator – you can double‑click `admin_run.bat` or open CMD as Administrator and type:

```cmd
python dns_fighter.py
```

Then follow the prompts:

- Choose domain source (use existing categories or add new domains manually).
- Pick up to 4 DNS resolvers.
- Set timeout (1‑5 seconds, default 2).
- Enable/disable ping check and Auto‑Update.

After the main comparison table appears, you can:

- Enter a **number** to use that resolver’s results for **all** domains.  
- Enter **`p`** to pick per domain individually.  
- Enter **`c`** to use the consensus (most frequent IP) per domain.  
- Enter **`a`** to run the **advanced reachability test** (protocol checks) on a specific resolver.

### 2️⃣ Advanced Reachability Test

Once you select `a` and choose a resolver, DNS Fighter will:

- Test each resolved IP against 7 protocols.  
- Show a separate table with ✓ / ✗.  
- Ask you which protocols must succeed.  
- **Only keep domains that pass all selected protocols** – then save them.

### 3️⃣ Auto‑Update Mode

When you enable Auto‑Update, the script:

- Runs interactively once to let you choose a resolver (or consensus).  
- Saves your choice into `last_resolver.txt`.  
- Then **enters an infinite loop** and updates the hosts file every X hours **without asking any further questions** – exactly repeating your previous selection.

### 4️⃣ Non‑Interactive Mode (for automation)

```cmd
python dns_fighter.py --non-interactive --domains-file domains.txt --dns-list 1,4 --ping --timeout 3
```

| Argument | Description |
|----------|-------------|
| `--auto-update` | Run continuously. |
| `--interval` | Interval in seconds (for auto‑update). |
| `--domains-file` | Plain text file with domains (one per line, no categories). |
| `--dns-list` | Comma‑separated DNS keys (e.g., `1,3,5` or `local`). |
| `--non-interactive` | No user prompts – auto‑approve. |
| `--use-resolver` | Force resolver number N (1‑based) for all domains. |
| `--ping` | Enable ping checks. |
| `--timeout` | DNS resolution timeout (1‑5 seconds, default 2). |

---

## 📂 File Structure

| File | Purpose |
|------|---------|
| `dns_fighter.py` | Main script. |
| `domains.txt` | Categorized domain list (editable). |
| `admin_run.bat` | Batch file to auto‑elevate privileges. |
| `last_resolver.txt` | Stores your last resolver choice (created automatically). |
| `LICENSE` | MIT License. |

---

## 🔧 Example `domains.txt` (simplified)

```text
# ==================== Fonts ====================
fonts.googleapis.com
fonts.gstatic.com

# ==================== General CDNs ====================
cdn.jsdelivr.net
ajax.googleapis.com

# ==================== User Custom ====================
# Your manually added domains go here
```

> The script **preserves category order** and will never mess up your structure.

---

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| `Administrator privileges required` | Run CMD or the batch file as Administrator. |
| `No module named 'dns'` | Install `dnspython`: `pip install dnspython`. |
| `File "domains.txt" gets messed up` | Delete it and let the script recreate a fresh one, or use the provided template. The latest version fully protects category headers. |
| `Advanced test says "No valid IPs"` | Make sure the resolver you selected actually returned some IPs (check the main table). |

---

## 📄 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it. However, **please give credit** to the original author (`Ahmadpromax` on GitHub) and consider supporting the project with a ⭐ star or a donation.

---

**Enjoy a faster, more secure internet!**  
**Ahmadpromax – 2026**
