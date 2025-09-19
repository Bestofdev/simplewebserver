# EX01 Developing a Simple Webserver
## Date:5/9/25

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Devesh</title>
    </head>    
    <body align="center">
        <header> My Device :25011036 </header>
        <table border="3" align="center" cellspacing="3" cellpadding="3" bgcolor="yellow" >
            <tr bgcolor="cyan">
            <th>S.no.</th>
            <th>Device specification</th>
            <th>Details</th>
            </tr>
            <tr align="center">
                <td>1</td>
                <td>device name</td>
                <td>dev</td>
            </tr>
            <tr align="center">
                <td>2</td>
                <td>processor</td>
                <td>Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)</td>
            </tr>
            <tr align="center">
                <td>3</td>
                <td>Ram</td>
                <td>16 GB</td>

            </tr>
            <tr align="center">
                <td>4</td>
                <td>storage</td>
                <td>1 TB</td>
            </tr>
            <tr align="center">
                <td>5</td>
                <td>OS</td>
                <td>Windows 11</td>
            </tr>
        </table>

    </body>


</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot (14).png>)
![alt text](<Screenshot (15).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
