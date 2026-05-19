<p align="center">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="auto">
    <defs>
      <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#0a0f2a;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#1a1a3e;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#ff4d4d;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#cc0000;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#00c6ff;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#0072ff;stop-opacity:1" />
      </linearGradient>
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur" />
        <feMerge>
          <feMergeNode in="blur" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
    </defs>
    <rect width="800" height="200" fill="url(#bgGrad)" rx="12" ry="12" />
    <circle cx="700" cy="30" r="40" fill="#ffffff" opacity="0.05" />
    <circle cx="100" cy="180" r="60" fill="#ffffff" opacity="0.03" />
    <circle cx="750" cy="170" r="25" fill="#00c6ff" opacity="0.1" />
    <g transform="translate(50, 50)" filter="url(#glow)">
      <path d="M40 0 L80 20 L80 80 C80 120 40 160 40 160 C40 160 0 120 0 80 L0 20 Z" fill="url(#shieldGrad)" stroke="#ff8080" stroke-width="1.5" />
      <text x="40" y="85" font-family="Arial, sans-serif" font-weight="bold" font-size="28" fill="#ffffff" text-anchor="middle">⚔️</text>
    </g>
    <text x="160" y="80" font-family="'Segoe UI', Arial, sans-serif" font-weight="800" font-size="46" fill="url(#accentGrad)" filter="url(#glow)">DNS Fighter</text>
    <text x="160" y="115" font-family="'Segoe UI', Arial, sans-serif" font-weight="500" font-size="18" fill="#b0b0d0">Multi-DNS Resolver &amp; Hosts Updater</text>
    <g transform="translate(160, 135)">
      <rect x="0" y="0" width="14" height="14" rx="3" fill="#00c6ff" />
      <text x="20" y="12" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#c0c0e0">DNS Poisoning Protection</text>
      <rect x="200" y="0" width="14" height="14" rx="3" fill="#ff4d4d" />
      <text x="220" y="12" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#c0c0e0">Multi‑Threaded</text>
      <rect x="340" y="0" width="14" height="14" rx="3" fill="#ffaa00" />
      <text x="360" y="12" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#c0c0e0">Auto‑Update</text>
    </g>
    <g transform="translate(680, 100)">
      <path d="M30 40 L45 20 L60 40 L45 60 Z" fill="#ff4d4d" opacity="0.8" />
      <path d="M45 10 L50 20 L40 20 Z" fill="#ffaa00" />
      <line x1="45" y1="20" x2="45" y2="60" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="4 2" opacity="0.6" />
      <text x="45" y="80" font-family="Arial" font-size="12" fill="#00c6ff" text-anchor="middle">FAST</text>
    </g>
    <line x1="160" y1="160" x2="750" y2="160" stroke="url(#accentGrad)" stroke-width="2" opacity="0.5" />
  </svg>
</p>

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
| 📁 **Domain Categorization** | Organise your domains in a structured [`domains.txt`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/domains.txt) file (Fonts, CDNs, Trackers, etc.). New domains go into `User Custom`. |
| 🎮 **Interactive & Non‑Interactive Modes** | Use it manually or integrate it into scripts and Task Scheduler with command‑line arguments. |
| 💰 **Free & Open Source** | Released under the **MIT License** (see [`LICENSE`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/LICENSE)). No strings attached, but your support keeps the project alive. |

---

## ❤️ Support the Developer

If DNS Fighter makes your browsing safer and faster, please consider giving this project a **⭐ Star on GitHub** – it helps others discover it. You can also support me via cryptocurrencies:

```
**USDT (TRC20)**: TQWRW7Zo35WyqZSBYGp4uEycNu7P8bBYDs
**USDT (BEP20)**: 0x6a0f997D86B2A32AE973947C73800e6688F4e5d2
**USDT (TON)**:   UQBi75cUao86m8EIxCYWSLUqo4mP28DX3ZcBqvQZGvnfrGPI
```

> Every star and donation encourages further development. Thank you! 🙏

---

## 📦 Requirements

- **Windows** 7 / 8 / 10 / 11  
- **Python** 3.6 or higher  
- **Administrator rights** (to modify `C:\Windows\System32\drivers\etc\hosts`)  

---

## 🛠️ Installation

### Step 1: Install Python (if not already installed)

1. Download the latest Python version from [python.org](https://www.python.org/downloads/).  
2. Run the installer – **IMPORTANT**: Check ✅ **"Add Python to PATH"** at the bottom of the installer window.  
3. Click **Install Now** and wait for the installation to finish.  
4. To verify Python is installed correctly, open **Command Prompt (CMD)** and type:
   ```cmd
   python --version
   ```
   You should see something like `Python 3.12.x`.

> 📖 **Need a visual guide?**  
> Watch this 2‑minute tutorial: [How to install Python on Windows and add to PATH](https://www.youtube.com/watch?v=Kn1HF3o0G_U) (YouTube).

### Step 2: Install the required dependency (`dnspython`)

#### 🚀 **Automatic method (recommended)**

Simply double‑click the file **`install_dependencies.bat`** that is already inside the repository folder.  
It will automatically install the library using a fast Iranian mirror (or fall back to the default PyPI if needed).  
A command window will open, run the installation, and then wait for you to press any key – after that you are ready to use DNS Fighter.

#### 🔧 **Manual method (if the automatic method fails or is blocked)**

Open **Command Prompt (CMD) as Administrator** and run one of the following commands:

- **Using Iranian mirror (recommended inside Iran):**
  ```cmd
  pip install dnspython -i https://mirror-pypi.runflare.com/simple/ --trusted-host mirror-pypi.runflare.com
  ```

- **Direct installation (if the mirror is blocked):**
  ```cmd
  pip install dnspython
  ```

- **If you are behind a proxy or have other network issues:**
  ```cmd
  pip install dnspython --proxy http://your-proxy-address:port
  ```

> ✅ The dependency is very small (< 200 KB) and installs in a few seconds.

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
- Enter **`c`** to use the **consensus** (the IP that appears most often across all selected DNS servers) per domain.  
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
| [`dns_fighter.py`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/dns_fighter.py) | Main script. |
| [`domains.txt`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/domains.txt) | Categorized domain list (editable). |
| [`admin_run.bat`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/admin_run.bat) | Batch file to auto‑elevate privileges. |
| [`install_dependencies.bat`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/install_dependencies.bat) | Automatically installs the required library. |
| `last_resolver.txt` | Stores your last resolver choice (created automatically). |
| [`LICENSE`](https://github.com/ahmadpromax/Dns_Fighter/blob/main/LICENSE) | MIT License. |

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
| `No module named 'dns'` | Install `dnspython` using `install_dependencies.bat` or the manual commands above. |
| `File "domains.txt" gets messed up` | Delete it and let the script recreate a fresh one, or use the provided template. The latest version fully protects category headers. |
| `Advanced test says "No valid IPs"` | Make sure the resolver you selected actually returned some IPs (check the main table). |
| `pip install fails (connection issues)` | Use the mirror or try again with a VPN. You can also download `dnspython` manually from [PyPI](https://pypi.org/project/dnspython/) and install using `pip install dnspython-*.whl`. |

---

## 📄 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it. However, **please give credit** to the original author (`Ahmadpromax` on GitHub) and consider supporting the project with a ⭐ star or a donation.

---

**Enjoy a faster, more secure internet!**  
**Ahmadpromax – 2026**
