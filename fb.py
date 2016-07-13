#!/usr/bin/python

import facebook
import sys

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "page_id",
    "access_token" : "access_token"
    }
  api = get_api(cfg)
  msg = "Photo upload"
  for img in sys.argv[1:]:
    print 'Uploading image ' + img
    status = api.put_photo(image=open(img, 'rb'), message=msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  print "Uploading to Facebook page"
  main()
