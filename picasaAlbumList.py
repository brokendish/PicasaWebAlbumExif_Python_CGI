#!/usr/bin/python
# -*- coding: utf-8 -*-

import gdata.photos.service
import gdata.media
import gdata.geo
import getpass
import sys
import datetime
import cgi
import os
import Cookie

class PicasaAlbumListDisp:
  def __init__(self,email,password):
	self.email=email
	self.password=password
  def runDisp(self):
#----------------------------------------------------------------------------------
	gd_client = gdata.photos.service.PhotosService()
	gd_client.email = self.email
	gd_client.password = self.password
	gd_client.source = 'exampleCo-exampleApp-1'
	gd_client.ProgrammaticLogin()
	
	username=self.email
	
	albumid = ""
#---------------------------------------------------------------------------------------------
	albums = gd_client.GetUserFeed(user=username)
	print """
        <table>
          <tr class="cc">
           <th></th><th>Album</th><th>枚数</th>
          </tr>
        """
	for album in albums.entry:
	  print '<tr><td class="cc"></td><td class="bb" width="50"><a href="javascript:void(0);" onclick="execute(getStr(this)); return 	false;">%s</a></td><td>%s</td></tr>' % (album.title.text,
	      album.numphotos.text)
	print '</table>'
#---------------------------------------------------------------------------------------------

