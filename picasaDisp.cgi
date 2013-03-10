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
import urllib


print u"Content-type: text/html;charset=utf-8".encode('utf-8')

#フォームからデータを取得
formG1 = cgi.FieldStorage()

email=formG1.getvalue('email', '')
password=formG1.getvalue('password', '')
albumname=formG1.getvalue('albumname', '')
dispType=formG1.getvalue('dispType')


##---------------------------------------------------
## 古典的暗号     
##---------------------------------------------------
##ROT13単換字式暗号（シーザー暗号）ー暗号ーユーザ名
#ur13=ur.encode('utf8').encode('base64_codec').encode('rot_13')
#cookie["ur_save"]=ur13

#クエリ文字列用のデコード
email=urllib.unquote_plus(email)
##ROT13単換字式暗号（シーザー暗号）ー複合ーユーザ名
email=email.decode('rot_13').decode('base64_codec').decode('utf8')
##---------------------------------------------------
##ROT13単換字式暗号（シーザー暗号）ー暗号ーパスワード
#pw13=pw.encode('utf8').encode('base64_codec').encode('rot_13')
#cookie["pw_save"]=pw13

#クエリ文字列用のデコード
password=urllib.unquote_plus(password)
##ROT13単換字式暗号（シーザー暗号）ー複合ーパスワード
password=password.decode('rot_13').decode('base64_codec').decode('utf8')
##---------------------------------------------------
print """
<body bgcolor='#EFECED' text='#5E584E'></body>
"""
#----------------------------------------------------------------------------------
gd_client = gdata.photos.service.PhotosService()
gd_client.email = email
gd_client.password = password
gd_client.source = 'exampleCo-exampleApp-1'
gd_client.ProgrammaticLogin()

username=email

albumid = ""
albums = gd_client.GetUserFeed(user=username)
for album in albums.entry:
  if album.title.text == albumname:
    albumid = album.gphoto_id.text

photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (username, albumid))


print "<h2>Album -- %s</h2>" % (albumname)

if dispType == "list":
  for photo in  photos.entry:
    camera="unknown"
    exposure="unknown"
    flash="unknown"
    focallength="unknown"
    fstop="unknown"
    iso="unknown"
    make="unknown"
    model="unknown"
    time="unknown"
    geo="unknown"
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
    
    shosaiStr="<table width=310>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>メーカ:</td><td class='sss'>" + make + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>モデル:</td><td class='sss'>" + model + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>ISO:</td><td class='sss'>" + iso + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>絞り:</td><td class='sss'>" + fstop + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>露出:</td><td class='sss'>" + exposure + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>レンズ焦点距離:</td><td class='sss'>" + focallength + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>フラッシュ:</td><td class='sss'>" + flash + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>日時:</td><td class='sss'>" + time + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "</table>"
    shosaiStr=shosaiStr + "ファイル:" + photo.content.src

    print '<table align="center">'
    print '<tr><td><a href="%s" rel="lightbox" title="%s"><img src="%s"/></a></td>' % (photo.content.src,shosaiStr, photo.media.thumbnail[2].url)
    print '<td><table width="450">'
    print '<tr><td>%s\n</td></tr>' % (photo.summary.text)
#   print '<tr><td class="aa">camera:<td>%s\n</td></td></tr>' % (camera)
    print '<tr><td class="aa">メーカ(make):<td>%s\n</td></td></tr>' % (make)
    print '<tr><td class="aa">モデル(model):<td>%s\n</td></td></tr>' % (model)
    print '<tr><td class="aa">ISO:<td>%s\n</td></td></tr>' % (iso)
    print '<tr><td class="aa">絞り(fstop):<td>%s\n</td></td></tr>' % (fstop)
    print '<tr><td class="aa">露出(exposure):<td>%s\n</td></td></tr>' % (exposure)
    print '<tr><td class="aa">レンズ焦点距離(focallength):<td>%s\n</td></td></tr>' % (focallength)
    print '<tr><td class="aa">フラッシュ(flash):<td>%s\n</td></td></tr>' % (flash)
    print '<tr><td class="aa">日時(time):<td>%s\n</td></td></tr>' % (time)
#   print '<tr><td class="aa">GEO:<td>%s\n</td></td></tr>' % (geo)
    print '</table></td>'
    print '</tr>'
    print '</table>'

elif dispType == "view":
  for photo in  photos.entry:
    camera="unknown"
    exposure="unknown"
    flash="unknown"
    focallength="unknown"
    fstop="unknown"
    iso="unknown"
    make="unknown"
    model="unknown"
    time="unknown"
    geo="unknown"
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
    
    shosaiStr="<table width=310>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>メーカ:</td><td class='sss'>" + make + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>モデル:</td><td class='sss'>" + model + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>ISO:</td><td class='sss'>" + iso + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>絞り:</td><td class='sss'>" + fstop + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>露出:</td><td class='sss'>" + exposure + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>レンズ焦点距離:</td><td class='sss'>" + focallength + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "<tr>"
    shosaiStr=shosaiStr + "<td class='ss'>フラッシュ:</td><td class='sss'>" + flash + "</td>"
    shosaiStr=shosaiStr + "<td class='ss'>日時:</td><td class='sss'>" + time + "</td>"
    shosaiStr=shosaiStr + "</tr>"
    shosaiStr=shosaiStr + "</table>"
    shosaiStr=shosaiStr + "ファイル:" + photo.content.src

    print '<a href="%s" rel="lightbox" title="%s" ><img src="%s"/></a>' % (photo.content.src, shosaiStr,photo.media.thumbnail[1].url)

print '</table>'
#---------------------------------------------------------------------------------------------

