#!/usr/bin/python
# — encoding: utf-8 —
#
# Hayo keciduk kann..
# Sengaja ga gua encrypt, biar bisa kalian pelajari, bukan malah direcode haha!!
# recode ga jadiin lu mastah!!!

import os,sys,time

os.system('clear')

print ("""    _   ___          _____           _       __
   / | / (_)_______ / ___/__________(_)___  / /_
  /  |/ / / ___/ _ \\__ \/ ___/ ___/ / __ \/ __/
 / /|  / / /__/  __/__/ / /__/ /  / / /_/ / /_
/_/ |_/_/\___/\___/____/\___/_/  /_/ .___/\__/
                                  /_/"Version 3.0"
<+> Author : MiSetya
<+> Team   : LightCyberIndonesia
<+> Youtube: https://youtube.com/MiSetya
<+> Github : https://github.com/MiSetya
<!>
<+> Fungsi : Membuat script deface simpel tanpa ribet
<+> Tools Version : 3.0
<!>
<+> Lihat versi sebelumnya di Github saya, tidak kalah keren
<+> dengan tools Version 3.0
<+>""")
title = raw_input("<!> Title/Judul >> ")
logo = raw_input("<!> Link logo/Foto >> ")
musik = raw_input("<!> Link musik >> ")
hek = raw_input("<!> Nick/Nama lu >> ")
tim = raw_input("<!> Team lu >> ")
thanks = raw_input("<!> Terimakasih kepada (contoh: ayah/ibu lu, temen-temen lu, pacar, mantan pacar, terserah) >> ")

# open index
fo = open("NiceV3.html","w")

tod1 = """<!-- Coded By. ./MiSetya -->

<html>
    <head>
        <title>"""
tod2 = title
tod3 = """</title>
<meta property="og:description" content="-=: Created by. NiceScript :=-">
<link rel="icon" href='"""
tod4 = logo
tod5 = """' type="image/x-icon"/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Kelly+Slab" type="text/css"/>
<style
type="text/css">body { background-image:
url(http://1.bp.blogspot.com/-6CsOJUHaxzU/UO7H1jfxWGI/AAAAAAAACHo/Wa2ajy8IgF0/s1600/storm.gif);
background-color:black; }</style>
<style type="text/css">
html {
	background:#000000;
	font-family: "Kelly Slab";
} 
jack {
	color:#000000;
	-webkit-text-stroke: 0.05em #ffffff;
} 
input,select,textarea{
    border: 1px #ffffff solid;
    -moz-border-radius: 5px;
    -webkit-border-radius:5px;
    border-radius:5px;
    
</style>
</head>
<body>
 <div style="position: fixed; top: 75px; left: -225px; width: 600px; padding: 10px; font-size: 24px; text-align: center; color: white; font-family: 'trebuchet ms', verdana, arial, sans-serif;transform: rotate(-45deg);transform-origin: 50% 0px;-o-transform: rotate(-45deg); -o-transform-origin: 50% 0px;-moz-transform: rotate(-45deg); -moz-transform-origin: 50% 0px; -webkit-transform: rotate(-45deg); -webkit-transform-origin: 50% 0px; background-color: Transparent; border: 1px solid rgb(170, 170, 170); z-index: 9999; opacity: 0.5;"><a href="http://www.xnxx.com" style="text-decoration:none;color:white;">Wanna See Me??</a></div>
<style type="text/css">.blink_me{font-size:60px;-webkit-animation-name:blinker;-webkit-animation-duration:2s;-webkit-animation-timing-function:linear;-webkit-animation-iteration-count:infinite;-moz-animation-name:blinker;-moz-animation-duration:2s;-moz-animation-timing-function:linear;-moz-animation-iteration-count:infinite;animation-name:blinker;animation-duration:1s;animation-timing-function:linear;animation-iteration-count:infinite;}@-moz-keyframes blinker{0% {opacity:1.0;}50% {opacity:0.0;}100% {opacity:1.0;}}@-webkit-keyframes blinker{ 0% {opacity:1.0;}50% {opacity:0.0;}100% {opacity:1.0;}}@keyframes blinker{0% {opacity:1.0;}50% {opacity:0.0;}100% {opacity:1.0;}}</style>
<center>
<iframe width="0" height="0" scrolling="no" frameborder="no" allow="autoplay" src='"""
tod6 = musik
tod7 = """' ></iframe>
<img src='"""
tod8 = logo
tod9 = """' height="750px" width="750px"><br>
<br><center><span class="blink_me"><jack><font size="6">Hacked? """
tod10 = hek
tod11 = """</font></jack></span></center><a href="https://lightcyberindonesia.blogspot.com"><h1><center><jack><font size="8"><u>-=: """
tod12 = tim
tod13 = """ :=-</u></jack></h1></a></span>
<center>
<br>
<br>
<font face="Kelly Slab" color="white" size="15px"><marquee scrollamount="95"> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< </marquee></font>
<p align="center">
    <jack><span class="blink_me"><font face="Kelly Slab" size="8" >-= Thanks to =-</font></jack></p>
<p align="center">
    <jack>
<font face="Kelly Slab" size="3" >"""
tod14 = thanks
tod15 = """</font></jack><br></p>
</span>
<font face="Kelly Slab" color="white" size="15px"><marquee scrollamount="95" direction="right"> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> </marquee></font>
<br><center><jack><font size="3"> - Copyleft 2k19 - </font></jack></center><span class="blink_me"><jack><font size="3">./MiSetya</jack></font></span>
<script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju.js" type="text/javascript"> </script> 
</body>
</head>
</html>"""

fo.write(tod1)
fo.write(tod2)
fo.write(tod3)
fo.write(tod4)
fo.write(tod5)
fo.write(tod6)
fo.write(tod7)
fo.write(tod8)
fo.write(tod9)
fo.write(tod10)
fo.write(tod11)
fo.write(tod12)
fo.write(tod13)
fo.write(tod14)
fo.write(tod15)

print "<!>"
print "<+> Script sukses dibuat <+>"
print "<+> Silahkan pindahkan script dengan menulis <+>"
print "<+> mv NiceV3.html /sdcard  <+>"
print "<+> Jangan lupa subscribe YT MiSetya <+>"
print "<+> Dan berikan github MiSetya STAR <+>"

fo.close()
