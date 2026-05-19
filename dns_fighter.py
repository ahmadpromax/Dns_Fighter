#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DNS Fighter - Multi-DNS Resolver & Hosts Updater
Prevent DNS poisoning and speed up browsing by resolving domains using multiple DNS servers
and storing results directly into the Windows hosts file (multi-threaded).
Run as Administrator.
"""

import os
import sys
import subprocess
import time
import argparse
from pathlib import Path
from collections import Counter, OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import re
import ctypes
import textwrap
import socket
import ssl
import urllib.request

import dns.resolver

# ==================== SET CONSOLE TITLE ====================
def set_console_title(title):
    if sys.platform == "win32":
        ctypes.windll.kernel32.SetConsoleTitleW(title)

# ==================== LICENSE & COPYRIGHT ====================
LICENSE_SHORT = "MIT License - Copyright (c) 2026 Ahmadpromax"
DONATION_LINKS = """
Support the developer:
  - Bitcoin:  bc1qxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  - Ethereum: 0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  - PayPal:   https://paypal.me/yourusername
  - GitHub:   https://github.com/sponsors/Ahmadpromax
"""

def print_intro():
    print("=" * 80)
    print("DNS Fighter - Multi-DNS Resolver & Hosts Updater")
    print("=" * 80)
    print(LICENSE_SHORT)
    print(DONATION_LINKS)
    print("\nStarting DNS Fighter...\n")

# ==================== CONFIGURATION ====================
HOSTS_PATH = Path(r"C:\Windows\System32\drivers\etc\hosts")
MAX_WORKERS = 40
SELECTION_FILE = Path("last_resolver.txt")

DEFAULT_CATEGORIES = {
    "Fonts": [
        "fonts.googleapis.com", "fonts.gstatic.com", "use.fontawesome.com",
        "cdn.fontawesome.com", "fonts.bunny.net", "fonts.cdnfonts.com", "fonts.geekzu.org"
    ],
    "General CDNs": [
        "cdn.jsdelivr.net", "cdnjs.cloudflare.com", "ajax.googleapis.com", "unpkg.com",
        "cdn.skypack.dev", "pagecdn.io", "code.jquery.com", "cdn.bootstrapcdn.com",
        "stackpath.bootstrapcdn.com", "cdn.datatables.net", "cdn.rawgit.com", "cdn.sstatic.net",
        "ajax.aspnetcdn.com", "cdn.baomitu.com", "lib.baomitu.com", "cdn.staticfile.org",
        "cdn.bootcdn.net", "akamaiedge.net", "akamaitechnologies.com", "akamaized.net",
        "akamaihd.net", "akamai.net", "akamaistaging.net", "cloudfront.net", "cloudflare.com",
        "cdn.cloudflare.net", "cloudflare.net", "fastly.net", "amazonaws.com", "s3.amazonaws.com",
        "googleapis.com", "googleusercontent.com", "gstatic.com", "ggpht.com", "yahooapis.com",
        "yimg.com", "msn.com", "live.com", "windows.net", "azureedge.net", "azurewebsites.net"
    ],
    "Trackers & Analytics": [
        "www.google-analytics.com", "ssl.google-analytics.com", "stats.g.doubleclick.net",
        "www.googletagmanager.com", "connect.facebook.net", "www.facebook.com", "staticxx.facebook.com",
        "platform.twitter.com", "cdn.syndication.twimg.com", "analytics.twitter.com", "bat.bing.com",
        "c.bing.com", "www.clarity.ms", "c.clarity.ms", "www.hotjar.com", "static.hotjar.com",
        "vars.hotjar.com", "script.hotjar.com", "insight.adsrvr.org", "tags.crwdcntrl.net",
        "cdn.segment.com", "cdn.amplitude.com", "api-js.mixpanel.com", "cdn.mxpnl.com",
        "a.klaviyo.com", "static.klaviyo.com", "cdn.optimizely.com", "cdn.rollbar.com",
        "cdn.sentry.io", "browser.sentry-cdn.com", "cdn.heapanalytics.com", "cdn.mouseflow.com",
        "cdn.onesignal.com", "api2.hcaptcha.com", "newassets.hcaptcha.com", "imrworldwide.com",
        "secure.adnxs.com", "ib.adnxs.com", "fls.doubleclick.net", "googleads.g.doubleclick.net",
        "pagead2.googlesyndication.com", "tpc.googlesyndication.com", "partner.googleadservices.com",
        "adservice.google.com", "www.googleadservices.com", "adservice.google.nl", "ad.doubleclick.net",
        "cm.g.doubleclick.net", "pubads.g.doubleclick.net", "adservice.google.ca", "amazon-adsystem.com",
        "s.amazon-adsystem.com", "aax.amazon-adsystem.com", "c.amazon-adsystem.com",
        "aax-eu.amazon-adsystem.com", "image2.pubmatic.com", "ads.pubmatic.com", "showads.pubmatic.com",
        "pixel.adsafeprotected.com", "bs.serving-sys.com", "s0.2mdn.net", "dp.g.doubleclick.net"
    ],
    "Ad Networks": [
        "criteo.com", "cas.criteo.com", "static.criteo.net", "casalemedia.com", "adsrvr.org",
        "lijit.com", "rlcdn.com", "tapad.com", "33across.com", "adnxs.com", "openx.net",
        "adform.net", "contextual.media.net", "ads.yahoo.com", "ads.yimg.com", "advertising.yahoo.com",
        "adserver.yahoo.com", "cdn.taboola.com", "trc.taboola.com", "images.outbrain.com",
        "widgets.outbrain.com", "rubiconproject.com", "ads.rubiconproject.com", "ad.360yield.com",
        "adtech.de", "adserver.adtech.de", "adserver.adtechus.com", "adtechus.com",
        "ads.adaptivemedia.xyz", "adaptivecdn.com"
    ],
    "Video Streaming": [
        "*.googlevideo.com", "*.ytimg.com", "*.ggpht.com", "*.youtube.com", "youtu.be",
        "youtubei.googleapis.com", "*.l.google.com", "*.ytstatic.l.google.com", "yt3.ggpht.com",
        "*.nflxvideo.net", "*.nflxext.com", "*.nflximg.com", "*.nflxso.net", "*.netflix.com",
        "*.vimeo.com", "*.vimeocdn.com", "cdn.livestream.com", "vod-adaptive-ak.vimeocdn.com",
        "*.livestream.com", "*.twitch.tv", "*.ttvnw.net", "*.jtvnw.net", "static.twitchcdn.net",
        "*.ext-twitch.tv", "*.video-edge-*.hls.ttvnw.net", "*.hulu.com", "*.hulustream.com",
        "img.hulu.com", "*.huluad.com", "*.cws-hulu.conviva.com", "*.dailymotion.com",
        "*.dmcdn.net", "statics.dmcdn.net", "vod-progressive.akamaized.net", "*.akafms.net",
        "*.akamaihd.net", "*.bcvp0rtal.com", "*.brightcovecdn.com", "cdn.video-cdn.net",
        "vod.video-cdn.net", "asset-out-cdn.video-cdn.net", "files.brightcove.com",
        "gallery.brightcove.com", "gallery.assets.brightcove.com", "playback.akamaized.net",
        "livestream-f.akamaihd.net", "secure-playlist.livestream.com"
    ],
    "Captcha Services": [
        "www.google.com/recaptcha", "www.recaptcha.net", "recaptcha.google.com",
        "apis.google.com", "www.gstatic.com/recaptcha", "*.google.com/recaptcha",
        "www.googleadservices.com/pagead/conversion.js", "api.hcaptcha.com",
        "assets.hcaptcha.com", "u.hcaptcha.com", "www.hcaptcha.com", "hcaptcha.com",
        "cloudflare.hcaptcha.com", "a2.hcaptcha.com", "cn0.hcaptcha.com", "cn1.hcaptcha.com",
        "challenges.cloudflare.com", "turnstile.arkoselabs.com", "arkoselabs.com",
        "turnstile.metafy.gg", "www.recaptcha.net/recaptcha/api.js",
        "www.recaptcha.net/recaptcha/api2/", "recaptcha.google.com/recaptcha/api/siteverify"
    ],
    "Microsoft Updates": [
        "*.update.microsoft.com", "*.windowsupdate.com", "*.dl.delivery.mp.microsoft.com",
        "*.delivery.mp.microsoft.com", "*.cdn.office.net", "*.officecdn.microsoft.com",
        "*.officecdn.microsoft.com.edgesuite.net", "*.displaycatalog.md.mp.microsoft.com",
        "*.vortex.data.microsoft.com", "*.settings-win.data.microsoft.com",
        "*.telecommand.telemetry.microsoft.com", "*.windowsupdate.microsoft.com",
        "*.update.microsoft.com.delivery.mp.microsoft.com"
    ],
    "WordPress Resources": [
        "api.wordpress.org", "*.wordpress.org", "secure.php.net", "wordpress.org",
        "downloads.wordpress.org", "*.wp.com", "s.w.org", "*.gravatar.com"
    ],
    "Iranian Tools & CDNs": [
        "*.arvancloud.ir", "*.arvancloud.com", "*.arvancdn.ir", "*.parspack.com",
        "*.parspack.net", "*.parspack.co", "*.cdn.parspack.ir", "*.cdn.asia-tech.ir",
        "iranhtml5.ir", "api.soroush-app.ir", "*.soroush-app.ir", "*.soroush.ir",
        "*.bale.ai", "*.balebot.com", "*.bale.ir", "*.gap.im"
    ]
}

USER_CATEGORY = "User Custom"
MISC_CATEGORY = "Misc"

DNS_OPTIONS = {
    '0': ('local', 'System'),
    '1': ('8.8.8.8', 'Google'),
    '2': ('1.1.1.1', 'Cloudflare'),
    '3': ('208.67.222.222', 'OpenDNS'),
    '4': ('178.22.122.100', 'Shecan'),
    '5': ('185.55.225.25', 'Begzar'),
    '6': ('78.157.42.100', 'Electro'),
    '7': ('193.186.32.32', 'Bertina'),
}

# ==================== PROTOCOL TESTS ====================
PROTOCOLS = [
    ("ICMP (ping)", "icmp"),
    ("TCP/80 (HTTP)", "tcp80"),
    ("TCP/443 (HTTPS)", "tcp443"),
    ("UDP/53 (DNS)", "udp53"),
    ("HTTP GET", "http"),
    ("HTTPS GET", "https"),
    ("TLS Handshake", "tls")
]

def test_icmp(ip, timeout=2):
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", str(timeout * 1000), ip],
            capture_output=True, text=True, timeout=timeout+1
        )
        return result.returncode == 0
    except:
        return False

def test_tcp_port(ip, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def test_udp_port(ip, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        if port == 53:
            query = bytes.fromhex("0000010000010000000000000377777706676f6f676c6503636f6d0000010001")
            sock.sendto(query, (ip, port))
            sock.recvfrom(512)
        else:
            sock.sendto(b"test", (ip, port))
            sock.recvfrom(1024)
        sock.close()
        return True
    except:
        return False

def test_http_get(ip, timeout=3):
    try:
        req = urllib.request.Request(f"http://{ip}/", method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status < 400
    except:
        return False

def test_https_get(ip, timeout=3):
    try:
        context = ssl._create_unverified_context()
        req = urllib.request.Request(f"https://{ip}/", method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout, context=context) as resp:
            return resp.status < 400
    except:
        return False

def test_tls_handshake(ip, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, 443))
        context = ssl.create_default_context()
        ssl_sock = context.wrap_socket(sock, server_hostname=ip)
        ssl_sock.close()
        sock.close()
        return True
    except:
        return False

def run_protocol_tests(domain_ip_map, resolver_name):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    test_functions = [
        test_icmp,
        lambda ip: test_tcp_port(ip, 80),
        lambda ip: test_tcp_port(ip, 443),
        lambda ip: test_udp_port(ip, 53),
        test_http_get,
        test_https_get,
        test_tls_handshake
    ]
    results = {}
    total_tests = len(domain_ip_map) * len(PROTOCOLS)
    if total_tests == 0:
        return results

    print(f"\n[*] Running advanced reachability tests using resolver '{resolver_name}'...")
    completed = 0
    lock = threading.Lock()
    max_workers = min(30, total_tests)

    def run_one_test(domain, ip, idx):
        try:
            success = test_functions[idx](ip)
            return domain, PROTOCOLS[idx][0], "✓" if success else "✗"
        except Exception:
            return domain, PROTOCOLS[idx][0], "✗"

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for domain, ip in domain_ip_map.items():
            if not ip:
                continue
            for idx in range(len(PROTOCOLS)):
                futures.append(executor.submit(run_one_test, domain, ip, idx))
        for future in as_completed(futures):
            domain, proto_name, result = future.result()
            with lock:
                if domain not in results:
                    results[domain] = {}
                results[domain][proto_name] = result
                completed += 1
                if completed % 20 == 0 or completed == total_tests:
                    print(f"  Progress: {completed}/{total_tests} tests done", flush=True)
    return results

def display_protocol_table(results, domain_ip_map):
    """Display protocol test results with horizontal lines after each domain."""
    if not results:
        print("[!] No results to display.")
        return
    protocol_list = [p[0] for p in PROTOCOLS]
    col_widths = [30]  # domain column
    for proto in protocol_list:
        max_width = len(proto)
        for domain in results:
            val = results[domain].get(proto, "?")
            if len(val) > max_width:
                max_width = len(val)
        col_widths.append(max_width + 2)
    
    def make_sep():
        parts = ["+" + "-" * col_widths[0] + "+"]
        for w in col_widths[1:]:
            parts.append("-" * w + "+")
        return "".join(parts)
    
    print("\n" + make_sep())
    header_row = f"| {'Domain':<{col_widths[0]-2}} |"
    for i, proto in enumerate(protocol_list):
        header_row += f" {proto:<{col_widths[i+1]-2}} |"
    print(header_row)
    print(make_sep())
    
    for domain, protos in results.items():
        row = f"| {domain:<{col_widths[0]-2}} |"
        for i, proto in enumerate(protocol_list):
            val = protos.get(proto, "?")
            if len(val) > col_widths[i+1] - 2:
                val = val[:col_widths[i+1]-5] + "..."
            row += f" {val:<{col_widths[i+1]-2}} |"
        print(row)
        print(make_sep())   # horizontal line after each domain
    
    print(f"[*] Protocol test complete. {len(results)} domains tested.", flush=True)

def ask_protocol_selection():
    print("\nSelect protocols that must succeed for an IP to be saved:")
    for i, (proto_name, _) in enumerate(PROTOCOLS, start=1):
        print(f"  {i}. {proto_name}")
    while True:
        choice = input("Enter numbers separated by space/comma (e.g., 1,3,5) or 'all' for all: ").strip().lower()
        if choice == 'all':
            return list(range(1, len(PROTOCOLS)+1))
        parts = choice.replace(',', ' ').split()
        selected = []
        for p in parts:
            try:
                idx = int(p)
                if 1 <= idx <= len(PROTOCOLS):
                    selected.append(idx)
                else:
                    print(f"Invalid number {idx}. Please enter numbers 1-{len(PROTOCOLS)}.")
                    break
            except:
                print(f"Invalid input: {p}. Please enter numbers.")
                break
        else:
            if selected:
                return selected
            else:
                print("No valid numbers selected.")

# ==================== UTILITY FUNCTIONS ====================
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def flush_dns():
    subprocess.run(["ipconfig", "/flushdns"], capture_output=True, text=True)

def resolve_domain_with_dns(domain, dns_server, timeout=2, retries=1):
    for attempt in range(retries + 1):
        resolver = dns.resolver.Resolver()
        if dns_server != 'local':
            resolver.nameservers = [dns_server]
        resolver.timeout = timeout
        resolver.lifetime = timeout
        try:
            answers = resolver.resolve(domain, 'A')
            for rdata in answers:
                ip = str(rdata)
                if '.' in ip and ':' not in ip:
                    return ip
            return str(answers[0])
        except Exception:
            if attempt == retries:
                return None
            time.sleep(0.1)
    return None

def ping_check_with_time(ip, timeout=2):
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", str(timeout * 1000), ip],
            capture_output=True, text=True, timeout=timeout + 1
        )
        if result.returncode == 0:
            match = re.search(r'time[=<](\d+(?:\.\d+)?)\s*ms', result.stdout, re.IGNORECASE)
            if match:
                return True, float(match.group(1))
            else:
                return True, 0.0
        else:
            return False, None
    except Exception:
        return False, None

def get_current_hosts_entries(domains):
    if not HOSTS_PATH.exists():
        return {}
    current = {}
    with open(HOSTS_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                ip, domain = parts[0], parts[1]
                if domain in domains:
                    current[domain] = ip
    return current

def update_hosts_file(domain_ip_map):
    if not HOSTS_PATH.exists():
        HOSTS_PATH.touch()
    try:
        with open(HOSTS_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except PermissionError:
        print("[!] Cannot read hosts file. Run as Administrator.")
        return False
    domains_to_update = set(domain_ip_map.keys())
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            parts = stripped.split()
            if len(parts) >= 2 and parts[1] in domains_to_update:
                continue
        new_lines.append(line)
    for domain, ip in domain_ip_map.items():
        if ip:
            new_lines.append(f"{ip} {domain}\n")
            print(f"[+] Updated: {domain} -> {ip}")
    try:
        with open(HOSTS_PATH, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    except PermissionError:
        print("[!] Cannot write to hosts file. Run as Administrator.")
        return False

# ==================== DOMAIN CATEGORY HANDLING ====================
def load_domains_categorized(filepath="domains.txt"):
    if not os.path.exists(filepath):
        return {cat: domains[:] for cat, domains in DEFAULT_CATEGORIES.items()}
    categories = OrderedDict()
    current_cat = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('# =======') and line.endswith('======='):
                parts = line.split('=')
                if len(parts) >= 3:
                    current_cat = parts[2].strip()
                    if current_cat not in categories:
                        categories[current_cat] = []
            elif line.startswith('#'):
                continue
            else:
                if current_cat is not None:
                    categories[current_cat].append(line)
                else:
                    if MISC_CATEGORY not in categories:
                        categories[MISC_CATEGORY] = []
                    categories[MISC_CATEGORY].append(line)
    if not categories:
        return {cat: domains[:] for cat, domains in DEFAULT_CATEGORIES.items()}
    return categories

def save_domains_categorized(categories, filepath="domains.txt"):
    with open(filepath, 'w', encoding='utf-8') as f:
        for cat_name, domains in categories.items():
            if not domains:
                continue
            f.write(f"\n# ==================== {cat_name} ====================\n")
            for domain in sorted(set(domains)):
                f.write(f"{domain}\n")
    print(f"[*] Domains saved to {filepath} (categorized).")

def add_domains_to_custom_category(categories, new_domains):
    if USER_CATEGORY not in categories:
        categories[USER_CATEGORY] = []
    categories[USER_CATEGORY].extend(new_domains)
    return categories

def get_all_domains_from_categories(categories):
    all_domains = []
    for domains in categories.values():
        all_domains.extend(domains)
    return list(set(all_domains))

def get_domains_by_category_selection(categories):
    print("\nSelect categories to include:")
    cat_list = list(categories.keys())
    for i, cat in enumerate(cat_list, start=1):
        print(f"{i}. {cat} ({len(categories[cat])} domains)")
    print("0. All categories")
    choice = input("Enter numbers separated by space/comma (e.g., 1,3) or 0 for all: ").strip()
    if choice == '0':
        return get_all_domains_from_categories(categories)
    parts = choice.replace(',', ' ').split()
    selected_cats = []
    for p in parts:
        try:
            idx = int(p) - 1
            if 0 <= idx < len(cat_list):
                selected_cats.append(cat_list[idx])
        except:
            pass
    if not selected_cats:
        print("[!] No valid categories selected. Using all categories.")
        return get_all_domains_from_categories(categories)
    domains = []
    for cat in selected_cats:
        domains.extend(categories.get(cat, []))
    return list(set(domains))

# ==================== DNS RESOLUTION & SELECTION ====================
def interactive_dns_selection():
    print("\nAvailable DNS resolvers:")
    for key, (ip, name) in DNS_OPTIONS.items():
        display = ip if ip != 'local' else 'System default'
        print(f"{key}. {name} -> {display}")
    print("Select up to 4 (space or comma separated, e.g., 1 3 5)")
    while True:
        choice = input("Enter DNS numbers (0-7): ").strip()
        if not choice:
            print("Please select at least one DNS.")
            continue
        parts = choice.replace(',', ' ').split()
        selected_keys = [p for p in parts if p in DNS_OPTIONS]
        if not selected_keys:
            print("No valid DNS selected.")
            continue
        if len(selected_keys) > 4:
            print("Maximum 4 DNS allowed.")
            continue
        break
    return [DNS_OPTIONS[k] for k in selected_keys]

def interactive_setup(categories):
    print("\n=== DNS Fighter (Multi-DNS Resolver) ===\n")
    print("Domain source:")
    print("1. Use existing categories (load from domains.txt)")
    print("2. Enter new domains manually")
    source_choice = input("Choose [1/2]: ").strip()
    new_categories = dict(categories)
    domains_to_use = []
    if source_choice == '1':
        print("\nWhich categories to resolve?")
        print("1. All categories")
        print("2. Only 'User Custom' (personally added domains)")
        print("3. Custom selection (choose specific categories)")
        cat_choice = input("Choose [1/2/3]: ").strip()
        if cat_choice == '1':
            domains_to_use = get_all_domains_from_categories(categories)
            print(f"[*] Will resolve {len(domains_to_use)} domains from all categories.")
        elif cat_choice == '2':
            if USER_CATEGORY in categories and categories[USER_CATEGORY]:
                domains_to_use = categories[USER_CATEGORY][:]
                print(f"[*] Will resolve {len(domains_to_use)} domains from '{USER_CATEGORY}' category.")
            else:
                print(f"[!] Category '{USER_CATEGORY}' is empty. Falling back to all categories.")
                domains_to_use = get_all_domains_from_categories(categories)
        elif cat_choice == '3':
            domains_to_use = get_domains_by_category_selection(categories)
            print(f"[*] Will resolve {len(domains_to_use)} domains from selected categories.")
        else:
            print("[!] Invalid choice. Using all categories.")
            domains_to_use = get_all_domains_from_categories(categories)
    else:
        print("\nEnter domains (one per line). Type 'done' when finished:")
        new_domains = []
        while True:
            line = input("> ").strip()
            if line.lower() == 'done':
                break
            if line:
                new_domains.append(line)
        if not new_domains:
            print("No domains entered. Exiting.")
            sys.exit(1)
        existing_domains = get_all_domains_from_categories(categories)
        if existing_domains:
            print(f"\nThere are already {len(existing_domains)} domains in the categories.")
            merge = input("Do you want to merge these new domains with the existing ones for resolution? (y/n): ").strip().lower()
            if merge in ['y', 'yes']:
                domains_to_use = list(set(existing_domains + new_domains))
                print(f"[*] Merged: total {len(domains_to_use)} domains will be resolved.")
            else:
                domains_to_use = new_domains
                print(f"[*] Only the {len(new_domains)} newly entered domains will be resolved.")
        else:
            domains_to_use = new_domains
            print(f"[*] Only the {len(new_domains)} newly entered domains will be resolved.")
        new_categories = add_domains_to_custom_category(new_categories, new_domains)

    selected_dns = interactive_dns_selection()
    
    while True:
        try:
            timeout_input = input("\nDNS resolution timeout (seconds, 1-5) [default 2]: ").strip()
            if timeout_input == "":
                timeout = 2
                break
            timeout = int(timeout_input)
            if 1 <= timeout <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid number. Please enter a number between 1 and 5, or press Enter for default (2).")
    
    ping_enabled = input("\nEnable ping reachability check? (y/N): ").strip().lower() in ['y', 'yes']
    auto_update = input("\nEnable Auto-Update mode? (y/N): ").strip().lower() in ['y', 'yes']
    interval_sec = 0
    if auto_update:
        while True:
            try:
                hours_input = input("Check interval (hours) [default 2, Enter to accept]: ").strip()
                hours = float(hours_input) if hours_input else 2.0
                interval_sec = int(hours * 3600)
                if interval_sec < 60:
                    interval_sec = 60
                break
            except:
                print("Invalid number. Use default 2 hours.")
                interval_sec = 7200
                break
    return domains_to_use, selected_dns, interval_sec, auto_update, ping_enabled, new_categories, timeout

# ==================== MULTI-THREADED RESOLUTION ====================
def resolve_multi_dns(domains, dns_list, timeout=2):
    total = len(domains) * len(dns_list)
    if total == 0:
        print("[!] No domains to resolve.")
        return {}
    results = {}
    progress_lock = threading.Lock()
    completed = 0
    bar_width = 50
    print(f"[*] Resolving {len(domains)} domains with {len(dns_list)} DNS servers (timeout={timeout}s) using multi-threading (max_workers={MAX_WORKERS})...")
    tasks = []
    for domain in domains:
        for dns_ip, dns_name in dns_list:
            tasks.append((domain, dns_name, dns_ip))
    max_workers = min(MAX_WORKERS, total)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_task = {executor.submit(resolve_domain_with_dns, domain, dns_ip, timeout): (domain, dns_name) for (domain, dns_name, dns_ip) in tasks}
        for future in as_completed(future_to_task):
            domain, dns_name = future_to_task[future]
            ip = future.result()
            with progress_lock:
                if domain not in results:
                    results[domain] = {}
                results[domain][dns_name] = ip if ip else "FAILED"
                completed += 1
                percent = int(completed * 100 / total)
                filled = int(bar_width * completed / total)
                bar = '[' + '#' * filled + '-' * (bar_width - filled) + ']'
                print(f"\r  {bar} {percent}%", end='', flush=True)
    print(f"\r  [{'#'*bar_width}] 100% Complete\n", flush=True)
    print("[*] Resolution complete. Preparing results table...\n", flush=True)
    return results

# ==================== MULTI-THREADED PING FOR ALL RESOLVERS ====================
def check_pings_for_all_resolvers(domains, resolved_ips, timeout=2):
    ping_results = {domain: {} for domain in domains}
    total = 0
    for domain, resolvers in resolved_ips.items():
        for dns_name, ip in resolvers.items():
            if ip and ip != "FAILED":
                total += 1
    if total == 0:
        return ping_results

    progress_lock = threading.Lock()
    completed = 0
    print("[*] Performing ping checks for each resolver (multi-threaded)...")

    def ping_task(domain, dns_name, ip):
        success, ms = ping_check_with_time(ip, timeout)
        if success:
            return domain, dns_name, ms
        else:
            return domain, dns_name, None

    max_workers = min(MAX_WORKERS, total)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for domain, resolvers in resolved_ips.items():
            for dns_name, ip in resolvers.items():
                if ip and ip != "FAILED":
                    futures.append(executor.submit(ping_task, domain, dns_name, ip))
        for future in as_completed(futures):
            domain, dns_name, ping_ms = future.result()
            with progress_lock:
                ping_results[domain][dns_name] = ping_ms
                completed += 1
                if completed % 10 == 0 or completed == total:
                    print(f"  Ping progress: {completed}/{total}", flush=True)
    return ping_results

# ==================== TABLE DISPLAY (MAIN RESOLUTION) ====================
def display_results_table_grid(combined_results, dns_names):
    domain_width = 30
    col_widths = [domain_width]
    for name in dns_names:
        max_width = len(name)
        for domain, resolvers in combined_results.items():
            val = resolvers.get(name, "FAILED")
            if len(val) > max_width:
                max_width = min(len(val), 35)
        col_widths.append(max_width + 2)
    
    def make_sep():
        parts = ["+" + "-" * col_widths[0] + "+"]
        for w in col_widths[1:]:
            parts.append("-" * w + "+")
        return "".join(parts)
    
    print("\n" + make_sep())
    header_row = f"| {'Domain':<{col_widths[0]-2}} |"
    for i, name in enumerate(dns_names):
        header_row += f" {name:<{col_widths[i+1]-2}} |"
    print(header_row)
    print(make_sep())
    
    for domain, resolvers in combined_results.items():
        cell_width = col_widths[0] - 2
        wrapped_lines = textwrap.wrap(domain, width=cell_width)
        if not wrapped_lines:
            wrapped_lines = [""]
        for i, domain_line in enumerate(wrapped_lines):
            if i == 0:
                row = f"| {domain_line:<{col_widths[0]-2}} |"
                for j, name in enumerate(dns_names):
                    val = resolvers.get(name, "FAILED")
                    if len(val) > col_widths[j+1] - 2:
                        val = val[:col_widths[j+1]-5] + "..."
                    row += f" {val:<{col_widths[j+1]-2}} |"
                print(row)
            else:
                row = f"| {domain_line:<{col_widths[0]-2}} |"
                for j in range(len(dns_names)):
                    empty = " " * (col_widths[j+1] - 2)
                    row += f" {empty:<{col_widths[j+1]-2}} |"
                print(row)
        print(make_sep())
    print(f"[*] Table display complete. {len(combined_results)} rows shown.", flush=True)

# ==================== SELECTION FUNCTIONS ====================
def get_consensus_selection(results):
    selected = {}
    for domain, res in results.items():
        valid_ips = [ip for ip in res.values() if ip != "FAILED"]
        if not valid_ips:
            selected[domain] = None
            continue
        freq = Counter(valid_ips)
        most_common_ip, _ = freq.most_common(1)[0]
        selected[domain] = most_common_ip
    return selected

def get_resolver_selection(results, resolver_index, dns_names):
    selected = {}
    resolver_name = dns_names[resolver_index]
    for domain, res in results.items():
        ip = res.get(resolver_name)
        if ip is None or ip == "FAILED":
            print(f"[!] {domain}: resolver {resolver_name} failed, skipping.")
            selected[domain] = None
        else:
            selected[domain] = ip
    return selected

def ask_user_per_domain(results, dns_names):
    selected = {}
    for domain, res in results.items():
        valid_ips = [ip for ip in res.values() if ip != "FAILED"]
        if not valid_ips:
            print(f"[!] No valid IP for {domain}. Skipping.")
            selected[domain] = None
            continue
        freq = Counter(valid_ips)
        common_ip, common_cnt = freq.most_common(1)[0]
        print(f"\nDomain: {domain}")
        for idx, name in enumerate(dns_names, start=1):
            ip = res[name]
            status = "✓" if ip != "FAILED" else "✗"
            print(f"  {idx}. {name:<12} -> {ip:<16} {status}")
        print(f"  Consensus: {common_ip} (appears {common_cnt} times)")
        while True:
            ans = input(f"Choose (1-{len(dns_names)} / c for consensus): ").strip().lower()
            if ans == 'c':
                selected[domain] = common_ip
                break
            else:
                try:
                    idx = int(ans)
                    if 1 <= idx <= len(dns_names):
                        chosen_ip = res[dns_names[idx - 1]]
                        if chosen_ip == "FAILED":
                            print("That DNS failed. Choose another.")
                            continue
                        selected[domain] = chosen_ip
                        break
                    else:
                        print(f"Invalid number. Choose 1..{len(dns_names)} or 'c'.")
                except ValueError:
                    print("Invalid input.")
    return selected

def ask_user_for_selection(results, dns_names):
    print("\nSelect which resolver's results to apply to ALL domains:")
    for idx, name in enumerate(dns_names, start=1):
        print(f"  {idx}. {name}")
    print("  p. Manual selection per domain (pick IP individually)")
    print("  c. Consensus (most frequent IP per domain)")
    print("  a. Advanced reachability test (check protocols)")
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice == 'p':
            print("\n--- Per-domain selection ---")
            return ask_user_per_domain(results, dns_names), None, None
        elif choice == 'c':
            print("[*] Using consensus IP per domain.")
            return get_consensus_selection(results), None, "consensus"
        elif choice == 'a':
            return None, True, None
        else:
            try:
                idx = int(choice)
                if 1 <= idx <= len(dns_names):
                    print(f"[*] Using resolver '{dns_names[idx - 1]}' for all domains.")
                    return get_resolver_selection(results, idx - 1, dns_names), None, idx - 1
                else:
                    print(f"Invalid number. Please enter 1..{len(dns_names)}, 'p', 'c', or 'a'.")
            except ValueError:
                print("Invalid input. Please enter a number, 'p', 'c', or 'a'.")

def save_selection(selection):
    try:
        with open(SELECTION_FILE, 'w') as f:
            if selection is None:
                f.write("none")
            elif selection == "consensus":
                f.write("consensus")
            else:
                f.write(f"resolver:{selection}")
    except:
        pass

def load_selection():
    if not SELECTION_FILE.exists():
        return None
    try:
        with open(SELECTION_FILE, 'r') as f:
            data = f.read().strip()
            if data == "none":
                return None
            elif data == "consensus":
                return "consensus"
            elif data.startswith("resolver:"):
                return int(data.split(":")[1])
            else:
                return None
    except:
        return None

# ==================== MAIN UPDATE CYCLE ====================
def run_update_cycle(domains, dns_list, ping_enabled, interactive_approval,
                     force_resolver_index=None, timeout=2):
    dns_names = [name for (ip, name) in dns_list]
    print(f"\n[{time.ctime()}] Resolving domains using {len(dns_list)} DNS servers...")
    if ping_enabled and len(domains) > 50:
        print(f"[!] Warning: Ping is enabled for {len(domains)} domains. This will take longer.")
        proceed = input("Continue anyway? (y/N): ").strip().lower()
        if proceed not in ['y', 'yes']:
            print("[!] Exiting. Please run again with ping disabled for large domain lists.")
            return False, None

    resolved_ips = resolve_multi_dns(domains, dns_list, timeout=timeout)
    if not resolved_ips:
        print("[!] No results obtained. Exiting update cycle.")
        return True, None

    ping_times = {}
    if ping_enabled:
        ping_times = check_pings_for_all_resolvers(domains, resolved_ips, timeout=timeout)

    combined_results = {}
    for domain, resolvers in resolved_ips.items():
        combined_results[domain] = {}
        for dns_name, ip in resolvers.items():
            if ip == "FAILED":
                combined_results[domain][dns_name] = "FAILED"
            else:
                ping_val = ping_times.get(domain, {}).get(dns_name)
                if ping_val is None:
                    combined_results[domain][dns_name] = f"{ip} (Timeout)"
                else:
                    combined_results[domain][dns_name] = f"{ip} ({int(ping_val)}ms)"

    display_results_table_grid(combined_results, dns_names)

    def extract_ip(combined_str):
        if combined_str == "FAILED":
            return None
        return combined_str.split()[0]

    pure_ip_map = {}
    for domain, resolvers in combined_results.items():
        pure_ip_map[domain] = {}
        for dns_name, val in resolvers.items():
            pure_ip_map[domain][dns_name] = extract_ip(val)

    selected_map = None
    advanced_requested = False
    chosen_resolver_idx = None
    if force_resolver_index is not None:
        print(f"[*] Using resolver '{dns_names[force_resolver_index]}' for all domains (forced).")
        selected_map = get_resolver_selection(pure_ip_map, force_resolver_index, dns_names)
        chosen_resolver_idx = force_resolver_index
    elif not interactive_approval:
        print("[*] Non‑interactive mode: auto‑selecting consensus IPs.")
        selected_map = get_consensus_selection(pure_ip_map)
        chosen_resolver_idx = "consensus"
    else:
        selected_map, advanced_flag, selection_result = ask_user_for_selection(pure_ip_map, dns_names)
        if advanced_flag:
            advanced_requested = True
        else:
            if selection_result == "consensus":
                chosen_resolver_idx = "consensus"
            elif isinstance(selection_result, int):
                chosen_resolver_idx = selection_result
            save_selection(chosen_resolver_idx)

    if advanced_requested:
        print("\nAdvanced reachability test requires selecting a specific resolver to test.")
        print("Available resolvers:")
        for idx, name in enumerate(dns_names, start=1):
            print(f"  {idx}. {name}")
        while True:
            try:
                choice = input("Select resolver number for testing: ").strip()
                idx = int(choice)
                if 1 <= idx <= len(dns_names):
                    resolver_name = dns_names[idx-1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(dns_names)}.")
            except:
                print("Invalid input.")
        test_ip_map = {}
        for domain, resolvers in pure_ip_map.items():
            ip = resolvers.get(resolver_name)
            if ip:
                test_ip_map[domain] = ip
        if not test_ip_map:
            print("[!] No valid IPs found for the selected resolver. Aborting advanced test.")
            return True, None
        proto_results = run_protocol_tests(test_ip_map, resolver_name)
        display_protocol_table(proto_results, test_ip_map)
        required_protocols = ask_protocol_selection()
        required_protocol_names = [PROTOCOLS[i-1][0] for i in required_protocols]
        print(f"\n[*] Will keep only domains that succeed on: {', '.join(required_protocol_names)}")
        filtered_map = {}
        for domain, ip in test_ip_map.items():
            protos = proto_results.get(domain, {})
            success = all(protos.get(pname) == "✓" for pname in required_protocol_names)
            if success:
                filtered_map[domain] = ip
            else:
                print(f"[!] Domain {domain} (IP {ip}) failed required protocols. Skipping.")
        if not filtered_map:
            print("[!] No domains passed the required protocol tests. Aborting save.")
            return True, None
        selected_map = filtered_map

    if selected_map is None:
        return True, None

    selected_map = {d: ip for d, ip in selected_map.items() if ip is not None}
    if not selected_map:
        print("[!] No valid IPs selected. Exiting cycle.")
        return True, None

    old_map = get_current_hosts_entries(domains)
    changed_count = 0
    unchanged_count = 0
    new_count = 0
    for domain, new_ip in selected_map.items():
        old_ip = old_map.get(domain)
        if old_ip is None:
            new_count += 1
        elif new_ip != old_ip:
            changed_count += 1
        else:
            unchanged_count += 1

    print("\n" + "=" * 60)
    print("Comparison with existing hosts file:")
    print(f"  - Domains with changed IP: {changed_count}")
    print(f"  - New domains (not in hosts): {new_count}")
    print(f"  - Already up-to-date: {unchanged_count}")
    if changed_count == 0 and new_count == 0:
        print("  => All selected entries already exist and are up-to-date. No changes needed.")
        return True, None
    print("=" * 60)

    if changed_count == 0 and new_count == 0:
        return True, None

    print("[*] Changes detected.")
    if interactive_approval and force_resolver_index is None and not advanced_requested:
        print("\nSummary of IPs to be saved:")
        for domain, ip in selected_map.items():
            print(f"  {domain} -> {ip}")
        while True:
            answer = input("Save these entries to hosts file? (y/n): ").strip().lower()
            if answer in ['y', 'yes']:
                break
            elif answer in ['n', 'no']:
                print("[!] User declined.")
                return False, None
            else:
                print("Please answer y or n.")
    else:
        print("[*] Auto‑approving changes (non‑interactive or forced resolver or advanced test).")

    print("[*] Updating hosts file...")
    if update_hosts_file(selected_map):
        flush_dns()
    else:
        print("[!] Failed to update hosts file.")
    return True, chosen_resolver_idx

# ==================== MAIN ENTRY POINT ====================
def main():
    set_console_title("DNS Fighter")
    print_intro()
    parser = argparse.ArgumentParser(description="DNS Fighter - Multi-DNS Resolver & Hosts Updater")
    parser.add_argument("--auto-update", action="store_true", help="Run continuously")
    parser.add_argument("--interval", type=int, help="Interval in seconds for auto-update")
    parser.add_argument("--domains-file", help="Plain text file with domains (one per line, no categories)")
    parser.add_argument("--dns-list", help="Comma-separated DNS keys (e.g., 1,3,5) or 'local'", default=None)
    parser.add_argument("--non-interactive", action="store_true", help="Auto-approve changes and auto-select consensus")
    parser.add_argument("--use-resolver", type=int, help="In non‑interactive mode, use this resolver index (1-based from --dns-list)")
    parser.add_argument("--ping", action="store_true", help="Enable ping reachability check")
    parser.add_argument("--timeout", type=int, default=2, help="DNS resolution timeout in seconds (default 2)")
    args = parser.parse_args()
    if not is_admin():
        print("[!] Administrator privileges required. Please run as Administrator.")
        sys.exit(1)
    interactive_approval = not args.non_interactive
    ping_enabled = args.ping
    timeout = args.timeout
    if not args.domains_file:
        categories = load_domains_categorized("domains.txt")
        domains, selected_dns, interval_sec, auto_update_mode, ping_enabled, new_cats, timeout = interactive_setup(categories)
        save_domains_categorized(new_cats, "domains.txt")
        print(f"\n[*] Starting DNS Fighter")
        print(f"[*] Domains: {len(domains)}")
        print(f"[*] DNS servers: {', '.join([name for (ip, name) in selected_dns])}")
        if auto_update_mode:
            print(f"[*] Mode: AUTO‑UPDATE (interval: {interval_sec // 3600}h / {interval_sec}s)")
        else:
            print(f"[*] Mode: MANUAL (single run)")
        print(f"[*] Ping: {'ON' if ping_enabled else 'OFF'}")
        print(f"[*] Timeout: {timeout} seconds")
        print(f"[*] Max workers: {MAX_WORKERS}")
        print(f"[*] Approval: {'ASK' if interactive_approval else 'AUTO'}\n")
        if auto_update_mode:
            # First run interactive to get selection
            success, chosen_idx = run_update_cycle(domains, selected_dns, ping_enabled, True, timeout=timeout)
            if not success:
                sys.exit(0)
            if chosen_idx is None:
                saved = load_selection()
                if saved == "consensus":
                    chosen_idx = "consensus"
                elif isinstance(saved, int):
                    chosen_idx = saved
                else:
                    chosen_idx = "consensus"
            # Auto-update loop
            while True:
                if chosen_idx == "consensus":
                    success, _ = run_update_cycle(domains, selected_dns, ping_enabled, False, timeout=timeout)
                else:
                    success, _ = run_update_cycle(domains, selected_dns, ping_enabled, False,
                                                   force_resolver_index=chosen_idx, timeout=timeout)
                if not success:
                    sys.exit(0)
                time.sleep(interval_sec)
        else:
            run_update_cycle(domains, selected_dns, ping_enabled, interactive_approval, timeout=timeout)
            print("[*] Manual run completed.")
        return
    # Non‑interactive mode with plain file
    if not args.dns_list:
        print("[!] Non‑interactive mode requires --domains-file and --dns-list.")
        sys.exit(1)
    try:
        with open(args.domains_file, encoding='utf-8') as f:
            domains = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        if not domains:
            print("[!] No domains found in file.")
            sys.exit(1)
        print(f"[*] Loaded {len(domains)} domains from {args.domains_file}")
    except Exception as e:
        print(f"[!] Failed to read domains file: {e}")
        sys.exit(1)
    keys = [k.strip() for k in args.dns_list.replace(',', ' ').split() if k.strip()]
    selected_dns = []
    for k in keys:
        if k in DNS_OPTIONS:
            selected_dns.append(DNS_OPTIONS[k])
        elif k == 'local':
            selected_dns.append(('local', 'System'))
    if not selected_dns:
        print("[!] No valid DNS in --dns-list")
        sys.exit(1)
    if len(selected_dns) > 4:
        print("[!] Maximum 4 DNS allowed.")
        sys.exit(1)
    auto_update_mode = args.auto_update
    interval = args.interval if auto_update_mode else 0
    if auto_update_mode and (interval is None or interval <= 0):
        print("[!] Auto-update requires positive --interval.")
        sys.exit(1)
    force_resolver_index = None
    if args.use_resolver is not None:
        idx = args.use_resolver - 1
        if idx < 0 or idx >= len(selected_dns):
            print(f"[!] Invalid --use-resolver index. Must be 1..{len(selected_dns)}")
            sys.exit(1)
        force_resolver_index = idx
        resolver_name = selected_dns[idx][1]
        print(f"[*] Non‑interactive: forcing resolver '{resolver_name}' for all domains.")
    else:
        print("[*] Non‑interactive: using consensus IP per domain.")
    print(f"\n[*] Starting DNS Fighter (Non‑Interactive)")
    print(f"[*] Domains: {len(domains)}")
    print(f"[*] DNS servers: {', '.join([name for (ip, name) in selected_dns])}")
    if auto_update_mode:
        print(f"[*] Mode: AUTO‑UPDATE (interval: {interval // 3600}h / {interval}s)")
    else:
        print(f"[*] Mode: MANUAL")
    print(f"[*] Ping: {'ON' if ping_enabled else 'OFF'}")
    print(f"[*] Timeout: {timeout} seconds")
    print(f"[*] Max workers: {MAX_WORKERS}")
    print("[*] Approval: AUTO\n")
    if auto_update_mode:
        while True:
            success, _ = run_update_cycle(domains, selected_dns, ping_enabled, False,
                                          force_resolver_index=force_resolver_index, timeout=timeout)
            if not success:
                sys.exit(0)
            time.sleep(interval)
    else:
        run_update_cycle(domains, selected_dns, ping_enabled, False,
                         force_resolver_index=force_resolver_index, timeout=timeout)
        print("[*] Manual run completed.")

if __name__ == "__main__":
    main()