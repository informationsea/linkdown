#!/usr/bin/env python
# -*- python -*-

import HTMLParser


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

if __name__ == '__main__':
    import sys
    sys.exit('Cannot run this module')
