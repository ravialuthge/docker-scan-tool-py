###conf dockerfile#

#import os
import tmp.imagename
from sdk.images_list import *

class officialimage(imageslist,tmp.imagename.IMAGENAME):
    """Check Docker Official Image"""
    def __init__(test):
       from tmp.filepath import FILEPATH
       #from tmp.imagename import IMAGENAME
       test.p = FILEPATH
       #test._o = IMAGENAME
       test.a_h=[]
     
    def officialimagescan(test):
         try:
            f = open(test.p, "r")
            mystring  = f.read()

            for item in mystring.split("\n"):
               if "FROM" in item:
                  d =  item.strip()
                  _s = d.split()
                  img = _s[1]
                  s = img.split(':')
                  o = s[0]
                  
                  test._o = o
                  #cmd = "docker search --format '{{.IsOfficial}}' --filter is-official=true " + o
                  #cmdout = os.popen(cmd).read()
                  #cmdout_a = cmdout.rstrip()
                  images = test.__images_off_ch
                  wo = " 'is_official':"
                  for im in images:
                   if wo in im:
                     test.a_h.append(im)
                  __h = test.a_h[0]
                  _h = __h.split(":")
                  _install_version  = _h[1]
                  bbc =  _install_version.replace(" ",'')
                  #install_version = bbc.replace("'",'')
                  #print (_install_version)
                  
                  if bbc == 'True':
                     print (o +" is Docker Official Image")
                  else:
                     print (o +" not Docker Official Images")
         except FileNotFoundError:
            print ("I did not find the Dockerfile at, "+str(test.p))
