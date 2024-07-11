from pywifi import PyWiFi, const, Profile
import time

def scan():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)  # Allow time for the scan to complete
    results = iface.scan_results()
    for network in results:
        print(f"SSID: {network.ssid}, Signal: {network.signal}")

scan()
