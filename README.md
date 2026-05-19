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
