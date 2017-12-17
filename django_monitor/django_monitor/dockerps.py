#coding=utf8

import docker
import re
c=docker.from_env()
dockerps=c.containers(all=1)
for i in c.containers(all=1):
    ret=i[u'Image']
    re.findall('(/..*)',ret)
