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

class PicasaDisp:
  def __init__(self,email,password,albumname):
	self.email=email
	self.password=password
	self.albumname=albumname
  def runDisp(self):
	#----------------------------------------------------------------------------------
	gd_client = gdata.photos.service.PhotosService()
	gd_client.email = self.email
	gd_client.password = self.password
	gd_client.source = 'exampleCo-exampleApp-1'
	gd_client.ProgrammaticLogin()
	
	username=self.email
	
	albumid = ""
	albums = gd_client.GetUserFeed(user=username)
	for album in albums.entry:
	  if album.title.text == self.albumname:
	    albumid = album.gphoto_id.text
	
	photos = gd_client.GetFeed(
	  '/data/feed/api/user/%s/albumid/%s?kind=photo' % (
	    username, albumid))
	
	
	print "<h2>Album -- %s</h2>" % (self.albumname)
	
	for photo in  photos.entry:
	  print '<table align="center">'
	  print '<tr><td><a href="%s" rel="lightbox"><img src="%s"/></a></td>' % (photo.content.src, photo.media.thumbnail[2].url)
#	  print '<tr><td><a href="%s"><img src="%s"/></a></td>' % (photo.content.src, photo.media.thumbnail[2].url)
	  print '<td><table width="450">'
	  print '<tr><td>%s\n</td></tr>' % (photo.summary.text)
	  camera="unknown"
	  exposure="unknown"
	  flash="unknown"
	  focallength="unknown"
	  fstop="unknown"
	  iso="unknown"
	  make="unknown"
	  model="unknown"
	  time="unknown"
	  if photo.exif.make:
	    camera = '%s %s' % (photo.exif.make.text, photo.exif.model.text)
	  if photo.exif.exposure:
	    exposure = '%s' % (photo.exif.exposure.text)
	  if photo.exif.flash:
	    flash = '%s' % (photo.exif.flash.text)
	  if photo.exif.focallength:
	    focallength = '%s' % (photo.exif.focallength.text)
	  if photo.exif.fstop:
	    fstop = '%s' % (photo.exif.fstop.text)
	  if photo.exif.iso:
	    iso = '%s' % (photo.exif.iso.text)
	  if photo.exif.make:
	    make = '%s' % (photo.exif.make.text)
	  if photo.exif.model:
	    model = '%s' % (photo.exif.model.text)
	  if photo.exif.time:
	    time = '%s' % datetime.date.fromtimestamp(int(photo.exif.time.text)/1000)
	
	  print '<tr><td class="aa">camera:<td>%s\n</td></td></tr>' % (camera)
	  print '<tr><td class="aa">メーカ(make):<td>%s\n</td></td></tr>' % (make)
	  print '<tr><td class="aa">モデル(model):<td>%s\n</td></td></tr>' % (model)
	  print '<tr><td class="aa">ISO:<td>%s\n</td></td></tr>' % (iso)
	  print '<tr><td class="aa">絞り(fstop):<td>%s\n</td></td></tr>' % (fstop)
	  print '<tr><td class="aa">露出(exposure):<td>%s\n</td></td></tr>' % (exposure)
	  print '<tr><td class="aa">レンズ焦点距離(focallength):<td>%s\n</td></td></tr>' % (focallength)
	  print '<tr><td class="aa">フラッシュ(flash):<td>%s\n</td></td></tr>' % (flash)
	  print '<tr><td class="aa">日時(time):<td>%s\n</td></td></tr>' % (time)
	  print '</table></td>'
	  print '</tr>'
	  print '</table>'
	print '</table>'	
#---------------------------------------------------------------------------------------------

