#!/usr/bin/env python
# -*- python -*-

import HTMLParser
import urllib
import re

import linkdown.convert

class HeadlineParser(HTMLParser.HTMLParser):

    def __init__(self):
        """
        
        Arguments:
        - `self`:
        """
        HTMLParser.HTMLParser.__init__(self)
        self.is_h1 = False
        self.is_h2 = False
        self.is_h3 = False
        self.h1 = None
        self.headlines = list()
        self.attr_id = None
        
    def handle_starttag(self, tag, attrs):
        self.is_h1 = False
        self.is_h2 = False
        self.is_h3 = False

        if tag == 'h1':
            self.is_h1 = True
        if tag == 'h2':
            self.is_h2 = True
        if tag == 'h3':
            self.is_h3 = True

        for a, v in attrs:
            if a == 'id':
                self.attr_id = v
        
    def handle_endtag(self, tag):
        self.is_h1 = False
        self.is_h2 = False
        self.is_h3 = False

    def handle_data(self, data):
        if self.is_h1 and not self.h1:
            self.h1 = data

        if self.is_h1:
            self.headlines.append(('h1', data, self.attr_id))
        elif self.is_h2:
            self.headlines.append(('h2', data, self.attr_id))
        elif self.is_h3:
            self.headlines.append(('h3', data, self.attr_id))
    
    def get_h1(self):
        return self.h1

    def get_headlines(self):
        """
        
        Arguments:
        - `self`:
        """

        return self.headlines


def get_h1(html):
    """
    
    Arguments:
    - `html`:
    """
    h1 = HeadlineParser()
    h1.feed(html)
    return h1.get_h1()

_whitespace = re.compile(r'\s+')

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
        self._content += _whitespace.sub(" ", data)
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
