#!/usr/bin/env python
# -*- python -*-

import HTMLParser
import re

class H1Parser(HTMLParser.HTMLParser):
    is_h1 = False
    h1 = None
    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.is_h1 = True
        else:
            self.is_h1 = False
    def handle_endtag(self, tag):
        self.is_h1 = False
    def handle_data(self, data):
        if self.is_h1:
            self.h1 = data
    
    def get_h1(self):
        return self.h1

def get_h1(html):
    """
    
    Arguments:
    - `html`:
    """
    h1 = H1Parser()
    h1.feed(html)
    return h1.get_h1()

class CompressHTML(HTMLParser.HTMLParser):
    _content = ''
    def handle_starttag(self, tag, attrs):
        if attrs:
            self._content += '<{tag} {attr}>'.format(tag=tag, attr=' '.join(['{0}="{1}"'.format(k, v) for k, v in attrs]))
        else:
            self._content += '<{tag}>'.format(tag=tag)
    def handle_endtag(self, tag):
        self._content += '</{0}>'.format(tag)
    def handle_data(self, data):
        self._content += data.strip()
    def get_html(self):
        """
        
        Arguments:
        - `self`:
        """
        return self._content


def compress_html(html):
    """
    
    Arguments:
    - `html`:
    """
    ch = CompressHTML()
    ch.feed(html)
    return ch.get_html()

if __name__ == '__main__':
    import sys
    sys.exit('Cannot run this module')
