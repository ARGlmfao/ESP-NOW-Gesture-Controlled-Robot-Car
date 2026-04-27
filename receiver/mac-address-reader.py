import network

sta = network.WLAN(network.STA_IF)
sta.active(True)

mac = sta.config('mac')

print("MAC bytes:")
print(mac)

print("For ESP-NOW peer:")
print("peer = b'" + ''.join("\\x%02X" % b for b in mac) + "'")
