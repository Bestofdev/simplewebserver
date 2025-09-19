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