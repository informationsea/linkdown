#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import os
import time
import threading
import codecs
import subprocess

import watchdog.observers
import watchdog.events

import linkdown.convert

def convertcmd(options):
    """
    
    Arguments:
    - `options`:
    """

    linkdown.convert.convert(options.format, options.source, options.output, options.templates, options.markdown_template, options.compress)

def runserver(options):
    """
    
    Arguments:
    - `options`:
    """

    httpd = _runserver_main(options.root, options.port)
    httpd.serve_forever()



def _runserver_main(root, port):
    """
    
    Arguments:
    - `root`:
    - `port`:
    """

    os.chdir(root)
    
    import SimpleHTTPServer
    import SocketServer

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("127.0.0.1", port), Handler)

    print "serving at http://127.0.0.1:{}/".format(port)
    return httpd
    

def suggest_newfilename(path):
    """
    
    Arguments:
    - `path`:
    """

    convertdict = {'md': 'html',
                   'markdown': 'html',
                   'rst': 'html',
                   'rest': 'html',
                   'less': 'css',
                   'coffeescript': 'js',
                   'coffee': 'js'}

    for key, value in convertdict.iteritems():
        if path.endswith(key):
            return path[:-len(key)]+value
    return path
    

class ConvertEventHandler(watchdog.events.FileSystemEventHandler):
    """
    """
    
    def __init__(self, options):
        """
        
        Arguments:
        - `options`:
        """
        watchdog.events.FileSystemEventHandler.__init__(self)
        self._options = options

    def on_any_event(self, event):
        """
        
        Arguments:
        - `self`:
        - `event`:
        """
        if event.is_directory:
            return
        if os.path.basename(event.src_path)[0] == '#':
            return
        if os.path.basename(event.src_path)[-1] == '~':
            return
        print event
        _convertall_main(self._options)
        print 'Converted'


def convertall(options):
    """
    
    Arguments:
    - `options`:
    """
    
    _convertall_main(options)

    if options.watch:
        event_handler = ConvertEventHandler(options)
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, options.sourcedir, recursive=True)
        observer.start()
        try:
            server = None
            if options.run_server:
                server = subprocess.Popen([sys.argv[0], 'runserver', '--port', str(options.port), options.destdir])
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            if server:
                server.terminate()
        observer.join()
        print >>sys.stderr, '\rObserver is stopped'
        return
    


def _convertall_main(options):
    """
    
    Arguments:
    - `options`:
    """

    exclude_suffix = options.exclude_suffix.split(',')
    exclude_prefix = options.exclude_prefix.split(',')

    for root, dirs, files in os.walk(options.sourcedir):
        for onedir in dirs:
            relpath = os.path.relpath(os.path.join(root, onedir), options.sourcedir)
            if any([relpath.endswith(x) for x in exclude_suffix]):
                continue
            if any([relpath.startswith(x) for x in exclude_prefix]):
                continue
            if not os.path.isdir(os.path.join(options.destdir, relpath)):
                os.makedirs(os.path.join(options.destdir, relpath))

        for onefile in files:
            relpath = os.path.relpath(os.path.join(root, onefile), options.sourcedir)
            basename = os.path.basename(relpath)
            if any([relpath.endswith(x) for x in exclude_suffix]):
                continue
            if any([relpath.startswith(x) for x in exclude_prefix]):
                continue
            if any([basename.startswith(x) for x in ['.', '#']]):
                continue
            
            linkdown.convert.convert('guess',
                    file(os.path.join(options.sourcedir, relpath), 'rb'),
                    file(os.path.join(options.destdir, suggest_newfilename(relpath)), 'wb'),
                    options.sourcedir, options.markdown_template, options.compress)

def initialize(options):
    """
    
    Arguments:
    - `options`:
    """

    if os.path.isdir(options.directory):
        sys.exit('This directory is exists.')

    import pkgutil

    datalist = pkgutil.get_data('linkdown', 'datalist.txt').split('\n')

    os.makedirs(options.directory)

    with file(os.path.join(options.directory, 'Makefile'), 'w') as f:
        print >>f, pkgutil.get_data('linkdown', 'templates/Makefile')

    templatedir = 'templates/'+options.template
    for i in [x for x in datalist if x.startswith(templatedir)]:
        destfile = os.path.join(options.directory, 'source', i[len(templatedir)+1:])
        if not os.path.isdir(os.path.dirname(destfile)):
            os.makedirs(os.path.dirname(destfile))
        with file(destfile, 'wb') as f:
            f.write(pkgutil.get_data('linkdown', i))



def _main():
    parser = argparse.ArgumentParser(description='Build Webpage with Markdown, Jinja2 templates, LESS or some recent tools.')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_ch = subparsers.add_parser('convert', help='convert documents to web pages')
    parser_ch.set_defaults(which='convert')
    parser_ch.add_argument('source', type=argparse.FileType('r'), help='Source file')
    parser_ch.add_argument('output', type=argparse.FileType('w'), help='Output file (default: stdout)', nargs='?', default=sys.stdout)
    parser_ch.add_argument('--compress', help='Compress output', action='store_true')
    parser_ch.add_argument('--templates', help='Root directory for jinja2 (default: %(default)s)', default='./source')
    parser_ch.add_argument('--markdown-template', help='Jinja2 Template HTML for Markdown. Relative path from templates directory (default: %(default)s)', default='templates/markdown.html')
    parser_ch.add_argument('--format', choices=('guess', 'markdown', 'jinja2', 'less', 'coffeescript'), default='guess', help='Input file format (default:%(default)s)')

    parser_server = subparsers.add_parser('runserver', help='Run Simple HTTP web server')
    parser_server.set_defaults(which='runserver')
    parser_server.add_argument('root', help='Root directory to serve.', nargs='?', default='public_html')
    parser_server.add_argument('-p', '--port', help='Web server port', nargs='?', default=8000, type=int)

    parser_init = subparsers.add_parser('init', help='Initialize project directory')
    parser_init.set_defaults(which='init')
    parser_init.add_argument('directory', help='Project directory')
    parser_init.add_argument('--template', choices=['basic', 'bootstrap'], help='Project template', default='basic')

    parser_all = subparsers.add_parser('all', help='Convert all')
    parser_all.set_defaults(which='all')
    parser_all.add_argument('sourcedir', help='Source directory (default: %(default)s)', default='source', nargs='?')
    parser_all.add_argument('destdir', help='Destination directory (default: %(default)s)', default='public_html', nargs='?')
    parser_all.add_argument('--exclude-suffix', default='.xcf,.psd,.DS_Store,.git,.hg,.svn', help='separated by comma defualt:%(default)s')
    parser_all.add_argument('--exclude-prefix', default='templates', help='separated by comma default:%(default)s')
    parser_all.add_argument('-c', '--compress', help='Compress output', action='store_true')
    #parser_all.add_argument('--templates', help='Root directory for jinja2 (default: %(default)s)', default='./source')
    parser_all.add_argument('--markdown-template', help='Jinja2 Template HTML for Markdown. Relative path from templates directory (default: %(default)s)', default='templates/markdown.html')
    parser_all.add_argument('-w', '--watch', action='store_true', help='Watch file changes and run convert automatically')
    parser_all.add_argument('-s', '--run-server', action='store_true', help='Run http server (only works with --watch)')
    parser_all.add_argument('-p', '--port', help='Web server port', nargs='?', default=8000, type=int)

    options = parser.parse_args()

    if options.which == 'convert':
        return convertcmd(options)
    elif options.which == 'runserver':
        return runserver(options)
    elif options.which == 'all':
        return convertall(options)
    elif options.which == 'init':
        return initialize(options)
    else:
        raise NotImplementedError
    

if __name__ == '__main__':
    _main()


