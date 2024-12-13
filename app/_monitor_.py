import pyshark
import logging
from app.ml_model import predict_traffic
from app.response import block_ip

# Configure logging
logging.basicConfig(
    filename="logs/traffic_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def start_monitor(interface="eth0"):
    """
    Starts real-time network monitoring on the specified interface.
    Captures packets, analyzes them, and logs suspicious activity.
    """
    print(f"[*] Monitoring network traffic on interface: {interface}")
    try:
        capture = pyshark.LiveCapture(interface=interface)

        for packet in capture.sniff_continuously():
            try:
                # Extract relevant fields from the packet
                src_ip = packet.ip.src if hasattr(packet, 'ip') else "Unknown"
                dst_ip = packet.ip.dst if hasattr(packet, 'ip') else "Unknown"
                protocol = packet.transport_layer if hasattr(packet, 'transport_layer') else "Unknown"
                length = packet.length

                # Log the captured packet
                logging.info(f"Packet: {src_ip} -> {dst_ip} | Protocol: {protocol} | Length: {length}")

                # Analyze the packet using the ML model
                prediction = predict_traffic(protocol, length)
                if prediction == "malicious":
                    logging.warning(f"Threat detected: {src_ip} -> {dst_ip} | Protocol: {protocol}")
                    print(f"[!] Threat detected: {src_ip} -> {dst_ip}")
                    block_ip(src_ip)

            except Exception as e:
                logging.error(f"Error processing packet: {e}")

    except KeyboardInterrupt:
        print("[*] Stopping monitoring.")
    except Exception as e:
        logging.error(f"Error starting monitor: {e}")
