#!/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

#url = 'https://www.dytt8.net/html/gndy/dyzz/20210114/60972.html'
# page = requests.get(url).content.decode('gbk')

page = '''
      <td colspan="2" align="center" valign="top"><div id="Zoom">
<!--Content Start--><span style="FONT-SIZE: 12px"><td>
<img style="MAX-WIDTH: 400px" border="0" alt="" src="https://img9.doubanio.com/view/photo/l_ratio_poster/public/p2630386833.jpg" /><br /><br />◎译　　名　快克年代：可卡因、贪腐与阴谋<br />◎片　　名　Crack: Cocaine, Corruption &amp; Conspiracy<br />◎年　　代　2021<br />◎产　　地　美国<br />◎类　　别　纪录片<br />◎语　　言　英语<br />◎字　　幕　中英双字幕<br />◎上映日期　2021-01-11(美国)<br />◎IMDb评分&nbsp;&nbsp;6.7/10 from 246 users<br />◎文件格式　x264 + aac<br />◎视频尺寸　1920 x 1080<br />◎片　　长　89分钟<br /><br />◎标　　签　纪录片 | 八十年代 | 美国 | 电影 | 2021<br /><br />◎简　　介<br /><br />　　20 世纪 80 年代初，霹雳可卡因泛滥成灾，像海啸一样席卷了美国的市中心贫民区，所到之处满目疮痍。几十年之后，人们仍然能够深切地感受到这场灾难对人民生活、家庭和社区造成的破坏性影响。《快克年代：可卡因、贪腐与阴谋》不仅审视了毒品对个人造成的破坏，还探讨了这场危机的神秘起源，以及由此导致的黑人和棕色人种不断被边缘化的问题，他们深受美国监狱和医保系统所困。<br /><br /><br /><strong><font color="#ff0000"><font size="4">【下载地址】</font></font></strong> <br /><br /><br /><a href="magnet:?xt=urn:btih:12d680508fee63a889e05d004be2f880c3fdfd8a&amp;dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1www.ygdy8.com.%e5%bf%ab%e5%85%8b%e5%b9%b4%e4%bb%a3%ef%bc%9a%e5%8f%af%e5%8d%a1%e5%9b%a0%e3%80%81%e8%b4%aa%e8%85%90%e4%b8%8e%e9%98%b4%e8%b0%8b.BD.1080p.%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%e5%b9%95.mkv&amp;tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&amp;tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&amp;tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce" target="_blank"><strong><font style="BACKGROUND-COLOR: #ff9966"><font color="#0000ff"><font size="4">磁力链点击 快克年代：可卡因、贪腐与阴谋.BD.1080p.中英双字幕.mkv</font></font></font></strong></a> <br><center></center>




</td>
'''


# obj = re.compile(r'<div id="Zoom".*?◎译　　名(?P<film_name>.*?)<br />.*?◎主　　演(?P<actors>.*?)<br /><br />.*?<a href="(?P<download_url>.*?)"', re.S)
obj = re.compile(r'<div id="Zoom".*?◎译　　名(?P<film_name>.*?)<br />.*?◎主　　演(?P<actors>.*?)<br /><br />', re.S)
# print(page)
detail_data = obj.finditer(page)
for i in detail_data:
    print(i.group('film_name'))
    print(i.group('actors'))

