#!/usr/bin/env python
# encoding=utf-8

import urllib
import urllib2
from gzip import GzipFile
from StringIO import StringIO
DEBUG_LEVEL = 0


class SunusAddrinfo(urllib.addinfourl):

    def __init__(self, resp):
        for k, v in resp.__dict__.items():
            self.__dict__[k] = v

    @staticmethod
    def try_decompress(data):
        try:
            gf = GzipFile(fileobj=StringIO(data), mode="r")
            decompressed_data = gf.read()
        except:
            decompressed_data = gf.extrabuf
        return decompressed_data

    def read_data(self, *args, **kwargs):
        d = self.read(self, *args, **kwargs)
        content_encoding = self.headers.get('content-encoding')
        if content_encoding:
            if content_encoding == 'gzip':
                return self.try_decompress(d)
            else:
                raise ValueError(
                    "Unsupported compression type: %s" % content_encoding)
        else:
            return d


class SunusBroswer(urllib2.OpenerDirector):

    def __init__(self):
        urllib2.OpenerDirector.__init__(self)
        self.add_handler(urllib2.HTTPHandler(debuglevel=DEBUG_LEVEL))
        self.add_handler(urllib2.HTTPRedirectHandler())
        self.add_handler(urllib2.HTTPDefaultErrorHandler())
        self.add_handler(urllib2.HTTPSHandler(debuglevel=DEBUG_LEVEL))
        self.add_handler(urllib2.HTTPErrorProcessor())
        self.add_handler(urllib2.FTPHandler())
        self.add_handler(urllib2.FileHandler())
        self.add_handler(urllib2.UnknownHandler())
        self.addheaders = [
            ('User-agent', 'Mozilla/5.0 Gecko/20100101 Firefox/20.0'),
            ('Accept-Encoding', 'gzip'),
            ('Connection',  'keep-alive'),
        ]

        def open_wrapper(func_open):
            """SunusAddrinfo is the return object of Openeropen.open"""
            def wrapper(*args, **kwargs):
                return SunusAddrinfo(func_open(*args, **kwargs))
            return wrapper
        self.open = open_wrapper(self.open)


if __name__ == '__main__':
    broswer = SunusBroswer()
    resp = broswer.open('http://www.baidu.com')
    print resp
    print resp.read_data()
