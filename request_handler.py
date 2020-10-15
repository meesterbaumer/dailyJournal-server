from http.server import BaseHTTPRequestHandler, HTTPServer
from instructors.request import get_all_instructors, get_single_instructor
from entries import get_all_entries, get_single_entry, delete_entry
from moods import get_all_moods, get_single_mood


# Here's a class. It inherits from another class.
class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.end_headers()

    def parse_url(self, path):
      path_params = path.split("/")
      resource = path_params[1]
      id = None
      try:
          id = int(path_params[2])
      except IndexError:
          pass
      except ValueError:
          pass

      return (resource, id)

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}

        (resource, id) = self.parse_url(self.path)

        # It's an if..else statement
        if resource == "entries":
            if id is not None:
                response = f"{get_single_entry(id)}"
            else:
                response = f"{get_all_entries()}"

        elif resource == "instructors":
            if id is not None:
                response = f"{get_single_instructor(id)}"
            else:
                response = f"{get_all_instructors()}"

        elif resource == "moods":
            if id is not None:
                response = f"{get_single_mood(id)}"
            else:
                response = f"{get_all_moods()}"

        # This weird code sends a response back to the client
        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request:<br>{post_body}"
        self.wfile.write(response.encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    def do_PUT(self):
        self.do_POST()

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "entries":
            delete_entry(id)
        
        # Encode the new animal and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()