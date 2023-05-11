finalcopyof the code

import network
import socket
from time import sleep
import machine
from machine import Pin
import ujson
import time

# Define a rate limiter function that takes a maximum number of requests and time interval
def rate_limiter(max_requests, interval):
    # Initialize a request counter and timestamp
    counter = 0
    timestamp = time.time()

    # Define a decorator that wraps around the API function
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the current time
            now = time.time()

            # If the time interval has passed, reset the counter and timestamp
            if now - timestamp > interval:
                counter = 0
                timestamp = now

            # If the maximum number of requests has been reached, return an error response
            if counter >= max_requests:
                return "Rate limit exceeded"

            # Increment the request counter and call the API function
            counter += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


 # Yes, these could be in another file. But on the Pico! So no more secure. :)
ssid = 'iPad'
password = '12345678900'

# Define pins to pin motors!
led_A = Pin(0, Pin.OUT)
led_B = Pin(1, Pin.OUT)
led_C = Pin(2, Pin.OUT)
led_D = Pin(3, Pin.OUT)
led_E = Pin(4, Pin.OUT)
led_F = Pin(5, Pin.OUT)
led_G = Pin(6, Pin.OUT)
led_H = Pin(7, Pin.OUT)

def move_forward():
    led_A.value(1)
    
def move_backward():
    led_B.value(1)

def move_stop():
     led_A.value(0)
     led_B.value(0)
     led_C.value(0)
     led_D.value(0)
     led_E.value(0)
     led_F.value(0)
     led_G.value(0)
     led_H.value(0)
def move_left():
     led_C.value(1)

def move_right():
     led_D.value(1)
     
def move_up():
     led_E.value(1)

def move_down():
     led_F.value(1)
def move_rleft():
     led_G.value(1)
def move_rright():
     led_H.value(1)     
#Stop the robot as soon as possible
move_stop()
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def my_endpoint(req, resp):
    # Check for the Authorization header
    auth_header = req.headers.get('Authorization')
    if not auth_header:
        resp.status = 401
        resp.headers['WWW-Authenticate'] = 'Basic realm="My API"'
        resp.body = "Unauthorized"
        return

    # Extract the username and password from the Authorization header
    encoded_credentials = auth_header.split(' ')[1]
    decoded_credentials = b64decode(encoded_credentials).decode('utf-8')
    username, password = decoded_credentials.split(':', 1)

    # Verify the username and password
    if username != 'myuser' or password != 'mypassword':
        resp.status = 401
        resp.headers['WWW-Authenticate'] = 'Basic realm="My API"'
        resp.body = "Unauthorized"
        return

def webpage():
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>3 Axis Robot Control</title>
            </head>
            <form action="./stop">
            <input type="submit" value="Stop" style="height:120px; width:120px" />
            </form>
            <center><b><table><tr>
            <form action="./up">
            <input type="submit" value="Up" style="height:120px; width:120px" />
            </form>
            
            <td><form action="./left">
            <input type="submit" value="Left" style="height:120px; width:120px" />
            </form></td>
            <td><form action="./back">
            <input type="submit" value="Backward" style="height:120px; width:120px" />
            </form></td>
            <td><form action="./right">
            <input type="submit" value="Right" style="height:120px; width:120px" />
            </form></td>
            
            <form action="./down">
            <input type="submit" value="Down" style="height:120px; width:120px" />
            </form>
            <form action="./forward">
            <input type="submit" value="Forward" style="height:120px; width:120px" />
            </form>
            <form action="./rotateleft">
            <input type="submit" value="R Left" style="height:120px; width:120px" />
            </form>
            <form action="./rotateright">
            <input type="submit" value="R Right" style="height:120px; width:120px" />
            </form></tr></table>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    #Start web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/forward?':
            move_forward()
        elif request =='/left?':
            move_left()
        elif request =='/stop?':
            move_stop()
        elif request =='/right?':
            move_right()
        elif request =='/back?':
            move_backward()
        elif request =='/up?':
            move_up()
        elif request =='/down?':
            move_down()
        elif request =='/rotateleft?':
            move_rleft()
        elif request =='/rotateright?':
            move_rright()    
        html = webpage()
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()    

    # Process the request
    resp.body = "Hello, world!"


#Define a rate limiter function that takes a maximum number of requests and time interval
def rate_limiter(max_requests, interval):
    # Initialize a request counter and timestamp
    counter = 0
    timestamp = time.time()

    # Define a decorator that wraps around the API function
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the current time
            now = time.time()

            # If the time interval has passed, reset the counter and timestamp
            if now - timestamp > interval:
                counter = 0
                timestamp = now

            # If the maximum number of requests has been reached, return an error response
            if counter >= max_requests:
                return "Rate limit exceeded"

            # Increment the request counter and call the API function
            counter += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator



