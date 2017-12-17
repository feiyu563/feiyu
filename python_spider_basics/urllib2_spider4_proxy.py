#coding=utf8
'''
urllib2库构建proxy
'''
import urllib2

enable_proxy =True
proxy_handler =urllib2.ProxyHandler({'http':'http://some-proxy.com:8080'}) #ProxyHandler({'代理类型':'代理地址'})
null_proxy_handler=urllib2.ProxyHandler({})
if enable_proxy:
    opener=urllib2.build_opener(proxy_handler)
else:
    opener=urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
