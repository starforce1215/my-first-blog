#-*- coding:utf-8 -*-

#http://hurderella.tistory.com/126?category=642057 [Hurderella]

import urllib.request
import shutil
import sys
import imp
from bs4 import BeautifulSoup

if __name__ == "__main__":
    print("Hello World")

    req = urllib.request.Request("http://gall.dcinside.com/board/view/?id=kimsohye&no=630655&page=1");
    data = urllib.request.urlopen(req).read()
    print("data:", data)
    bs = BeautifulSoup(data, 'html.parser')
    print("bs:", bs.prettify())
    li = bs.find_all('li')
    print("li:", li)

    for ele in li:
        val = ele.get('class')
        print("ele")
        if val != None and val[0] == 'icon_pic':
            base_url = ele.a.get("href")
            rp_from = "http://image.dcinside.com/download.php"
            rp_to = "http://dcimg2.dcinside.com/viewimage.php"
            base_url = base_url.replace(rp_from, rp_to);
            print(base_url)
            f = open("./" + ele.a.contents[0], "wb");
            img_req = urllib.request.Request(base_url);
            f.write(urllib.request.urlopen(img_req).read())
            f.close()
            
    print("End")

