import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        n = 10
        num1 = 0
        num2 = 1
        next_number = num2  
        count = 1
 
        while count <= n:
            self.response.write(next_number)
            count += 1
            num1, num2 = num2, next_number
            next_number = num1 + num2
            self.response.write(" ")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)