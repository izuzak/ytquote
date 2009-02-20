import cgi
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class YtQuote(webapp.RequestHandler):
  def get(self):
    vid = self.request.get('vid')
    txt = self.request.get('txt')
    
    template_values = {
      'video': vid,
      'quote': txt,
    }

    # cgi.escape()
      
    path = os.path.join(os.path.dirname(__file__), 'ytquote.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/.*', YtQuote)], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()