# VoIPCrack – VoIP Call Interception and Analysis Tool


## 🔐 Project Overview

**VoIPCrack** is a powerful Python-based penetration testing tool designed for analyzing and exploiting VoIP (Voice over IP) networks. It focuses on VoIP call interception, analysis, and manipulation through protocols like **SIP** and **RTP**, and is built using **Scapy** for low-level packet manipulation.

> ⚠️ **Educational Use Only**: This tool is intended strictly for research, educational, and authorized penetration testing purposes.

---

## 🚀 Features

- 📞 **SIP Call Interception**
- 🎭 **SIP Registration Spoofing / Hijacking**
- 🎙️ **RTP Stream Capture and Audio Playback**
- 🗣️ **RTP Injection (Fake Audio Stream)**
- 📊 **Packet Analysis and Logging**
- 🧪 Compatible with softphones like Linphone, Zoiper, X-Lite, and more

---

## 🧠 How It Works

1. **SIP Interception**: Sniffs SIP traffic on the network to identify VoIP call attempts.
2. **SIP Spoofing**: Hijacks SIP registration to impersonate a user and take over the call.
3. **RTP Capture**: Extracts RTP packets and reconstructs the audio stream.
4. **RTP Injection** *(in progress)*: Allows injecting fake audio during active calls.

---

## 🛠 Requirements

- Python 3.6+
- [Scapy](https://scapy.net/)
- ffmpeg (for audio conversion)
- Wireshark (packets capturing)
- maxmind geoip database
- ip2location
- google maps

Capture all nesscessary packets and credentials using the wireshark to perform the actions
also connect to a public/industry network to get nesscessary packets to be captured 
