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

**DNS Fighter** is a powerful, multi‑threaded command‑line tool for Windows that automatically resolves domain names using multiple DNS servers and writes the obtained IP addresses directly into your **hosts** file. By doing so, it completely bypasses the system DNS resolver – which means **no more DNS poisoning attacks, faster web browsing, and full control over which IPs your computer connects to.**

> 💡 **What does this mean for you?**  
> - **Stop hackers** from redirecting you to fake websites (DNS spoofing).  
> - **Speed up page loading** by eliminating DNS lookup delays.  
> - **Compare results** from up to 4 DNS servers at once.  
> - **Test advanced protocols** (ICMP, TCP, UDP, HTTP, HTTPS, TLS) to verify reachability.  
> - **Automatically keep your hosts file up‑to‑date** with the IPs you choose.

---

## 🧠 Architecture & How It Works (Graphical)

<div style="background: linear-gradient(135deg, #0a0f2a 0%, #1a1a3e 100%); border-radius: 24px; padding: 30px 20px; margin: 40px 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">
  <h2 style="text-align: center; color: #ffffff; margin-bottom: 30px;">🧠 Normal Connection vs DNS Fighter</h2>
  
  <div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center;">
    
    <div style="flex: 1; min-width: 280px; background: rgba(0,0,0,0.4); border-radius: 20px; padding: 20px; border-left: 4px solid #ff4d4d;">
      <div style="color: #ff4d4d; font-weight: bold; text-align: center; font-size: 1.2em; margin-bottom: 15px;">❌ Without DNS Fighter</div>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <span style="background: #2d2d5a; padding: 6px 12px; border-radius: 20px;">🌐 Browser</span>
          <span style="font-size: 20px;">→</span>
          <span style="background: #2d2d5a; padding: 6px 12px; border-radius: 20px;">📡 DNS Request</span>
        </div>
        <div style="text-align: center; background: #3a1a1a; border-radius: 12px; padding: 10px; border: 1px dashed #ff4d4d;">
          <div style="color: #ffaa00;">⚠️ DPI (Deep Packet Inspection)</div>
          <div style="font-size: 12px;">Intercepts request → sends fake IP</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <span style="background: #2d2d5a; padding: 6px 12px; border-radius: 20px;">🎭 Fake Website</span>
          <span style="font-size: 14px;">(Phishing / Blocked)</span>
        </div>
      </div>
      <div style="margin-top: 18px; background: #1a1a2e; border-radius: 12px; padding: 12px;">
        <div style="font-size: 13px; margin-bottom: 4px;">⏱️ <strong>DNS lookup delay</strong> → 20‑100 ms</div>
        <div style="font-size: 13px; margin-bottom: 4px;">🔓 <strong>DNS poisoning risk</strong> → High</div>
        <div style="font-size: 13px;">👁️ <strong>Privacy</strong> → Queries visible</div>
      </div>
    </div>

    <!-- AFTER -->
    <div style="flex: 1; min-width: 280px; background: rgba(0,0,0,0.4); border-radius: 20px; padding: 20px; border-left: 4px solid #00c6ff;">
      <div style="color: #00c6ff; font-weight: bold; text-align: center; font-size: 1.2em; margin-bottom: 15px;">✅ With DNS Fighter</div>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <span style="background: #2d2d5a; padding: 6px 12px; border-radius: 20px;">🌐 Browser</span>
          <span style="font-size: 20px;">→</span>
          <span style="background: #2d2d5a; padding: 6px 12px; border-radius: 20px;">📁 hosts file</span>
        </div>
        <div style="text-align: center; background: #1a3a2a; border-radius: 12px; padding: 10px; border: 1px solid #00c6ff;">
          <div style="color: #00c6ff;">🛡️ DPI cannot see the DNS request</div>
          <div style="font-size: 12px;">No spoofing → direct connection</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <span style="background: #2d2d5a; padding: 6px 12px; border-radius: 20px;">✅ Real Website</span>
        </div>
      </div>
      <div style="margin-top: 18px; background: #1a1a2e; border-radius: 12px; padding: 12px;">
        <div style="font-size: 13px; margin-bottom: 4px;">⚡ <strong>DNS lookup delay</strong> → <span style="color: #00c6ff;">0 ms</span></div>
        <div style="font-size: 13px; margin-bottom: 4px;">🔒 <strong>DNS poisoning risk</strong> → <span style="color: #00c6ff;">None</span></div>
        <div style="font-size: 13px;">👁️ <strong>Privacy</strong> → No queries → more private</div>
      </div>
    </div>
  </div>
  
  <div style="text-align: center; margin-top: 30px; font-size: 14px; color: #b0b0d0;">
    💡 DNS Fighter stores resolved IPs directly into your <code>hosts</code> file, eliminating DNS lookups and blocking DPI‑based spoofing.
  </div>
</div>

---

## 🔥 Key Features

| Feature | Description |
|---------|-------------|
| 🛡️ **DNS Poisoning Prevention** | Writes resolved IPs into the Windows `hosts` file, bypassing the system DNS resolver. |
| ⚡ **Blazing Fast** | Multi‑threaded resolution (`MAX_WORKERS = 40`) – even with hundreds of domains. |
| 🔍 **Multi‑DNS Comparison** | Choose up to 4 DNS servers (Google, Cloudflare, Shecan, Begzar, etc.) and compare their responses side by side in a clean table. |
| 📈 **Advanced Reachability Test** | Test **7 different protocols** (ICMP, TCP/80, TCP/443, UDP/53, HTTP GET, HTTPS GET, TLS handshake) on the IPs obtained from any resolver. |
| 🔄 **Auto‑Update** | After you pick a resolver, DNS Fighter remembers your choice and automatically updates the `hosts` file at any interval you set (e.g., every 2 hours). |
| 📁 **Domain Categorization** | Organise your domains in a structured [`domains.txt`](domains.txt) file (Fonts, CDNs, Trackers, etc.). New domains go into `User Custom`. |
| 🎮 **Interactive & Non‑Interactive Modes** | Use it manually or integrate it into scripts and Task Scheduler with command‑line arguments. |
| 💰 **Free & Open Source** | Released under the **MIT License**. No strings attached, but your support keeps the project alive. |

---

## 📂 Why These Domains in `domains.txt`?

The included `domains.txt` contains **300+ carefully selected domains** organized into categories that bring immediate benefit to speed and privacy. Here is why each category was chosen:

| Category | Example Domains | Benefit |
|----------|----------------|---------|
| **Fonts** | `fonts.googleapis.com`, `fonts.gstatic.com` | Used by almost every modern website. Caching their IPs makes fonts load instantly, eliminating font‑loading delays. |
| **General CDNs** | `cdn.jsdelivr.net`, `ajax.googleapis.com`, `cdn.bootstrapcdn.com` | These serve common JavaScript/CSS libraries (jQuery, Bootstrap, etc.). Storing their IPs speeds up page rendering across thousands of sites. |
| **Trackers & Analytics** | `google-analytics.com`, `connect.facebook.net`, `bat.bing.com` | Blocking or bypassing these reduces third‑party tracking, improves privacy, and often shortens page load time. |
| **Ad Networks** | `doubleclick.net`, `criteo.com`, `adnxs.com` | Ads are a major source of delay. Resolving these domains (or even blocking them via `hosts`) can dramatically improve browsing speed. |
| **Video Streaming** | `*.googlevideo.com`, `*.nflxvideo.net`, `*.vimeo.com` | Video platforms use separate CDNs for video chunks. Caching their IPs reduces buffering and improves streaming quality. |
| **Captcha Services** | `recaptcha.net`, `api.hcaptcha.com` | CAPTCHA checks often delay form submissions. A faster connection to these services makes the user experience smoother. |
| **Microsoft Updates** | `*.update.microsoft.com`, `*.dl.delivery.mp.microsoft.com` | Windows and Office updates become faster when DNS lookup is skipped. |
| **WordPress Resources** | `api.wordpress.org`, `downloads.wordpress.org` | For WordPress users, plugin/theme updates and downloads are noticeably quicker. |
| **Iranian CDNs & Tools** | `*.arvancloud.ir`, `*.parspack.com`, `iranhtml5.ir` | Local CDNs are much faster for users inside Iran. Including them resolves connection delays caused by international routes. |
| **TradingView & Financial** | `*.tradingview.com`, `*.binance.com` (optional) | Traders and investors benefit from sub‑second resolution for real‑time market data. |
| **User Custom** | (your own domains) | You can add any domain you frequently visit. The script will keep it in a separate category and never touch its IP unless you change it. |

> 💡 **How to use it?** Simply run DNS Fighter, select **"Use existing categories"**, and the tool will resolve and store all these domains’ IPs into your `hosts` file. You can edit `domains.txt` anytime – the script preserves the category structure.

---

## ❤️ Support the Developer

If DNS Fighter makes your browsing safer and faster, please consider giving this project a **⭐ Star on GitHub** – it helps others discover it. You can also support me via cryptocurrencies:

```
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

Simply double‑click the file **`install_dependencies.bat`** that is already inside the repository folder. It will automatically install the library using a fast Iranian mirror (or fall back to the default PyPI if needed). A command window will open, run the installation, and then wait for you to press any key – after that you are ready to use DNS Fighter.

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
| [`dns_fighter.py`](dns_fighter.py) | Main script. |
| [`banner.svg`](banner.svg) | Banner image for README. |
| [`domains.txt`](domains.txt) | Categorized domain list (editable). |
| [`admin_run.bat`](admin_run.bat) | Batch file to auto‑elevate privileges. |
| [`install_dependencies.bat`](install_dependencies.bat) | Automatically installs the required library. |
| `last_resolver.txt` | Stores your last resolver choice (created automatically). |
| [`LICENSE`](LICENSE) | MIT License. |

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
