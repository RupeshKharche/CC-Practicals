import os
import webapp2
from google.appengine.ext.webapp import template
import urllib
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}

        path = os.path.join(os.path.dirname(__file__), "public", "index.html")
        self.response.write(template.render(path, template_values))

    def post(self):
        # Get the latitude and longitude from the request
        lat = self.request.get("latitude")
        long = self.request.get("longitude")

        # Create the api url
        url = "https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+long+"&hourly=temperature_2m"

        response = urllib.urlopen(url).read()
        response = json.loads(response)

        temp = response['hourly']['temperature_2m'][0]

        template_values = {
            "temperature": temp
        }

        path = os.path.join(os.path.dirname(__file__), "public", "result.html")
        self.response.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    ("/", MainPage)
], debug=True)