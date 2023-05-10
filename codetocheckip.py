import network

ssid = ''  # replace with your network SSID
password = ''  # replace with your network password

wlan = network.WLAN(network.STA_IF)  # create a station interface object
wlan.active(True)  # activate the interface

if not wlan.isconnected():  # check if the interface is already connected
    print('Connecting to network...')
    wlan.connect(ssid, password)  # connect to the network

    while not wlan.isconnected():  # wait for the connection to succeed
        pass

print('Network connected!')
print('IP address:', wlan.ifconfig()[0])
