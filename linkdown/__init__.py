#!/usr/bin/env python
# -*- python -*-

import argparse
import jinja2
import markdown
import sys
import os

def convert(options):
    """
    
    Arguments:
    - `options`: options from argparse
    """

    if options.format == 'guess':
        if options.source.name.lower().endswith('less'):
            format = 'less'
        elif options.source.name.lower().endswith('html'):
            format = 'jinja2'
        elif options.source.name.lower().endswith('md'):
            format = 'markdown'
        else:
            sys.exit('Unknown file type:'+options.input.name)
    else:
        format = options.format

    if format == 'less':
        raise NotImplementedError
        output = convert_less2css(options.source.read())
    elif format == 'jinja2':
        output = convert_jinja2html(options.source.read(), options.templates)
    elif format == 'markdown':
        raise NotImplementedError
        output = convert_markdown2html(options.source.read(), options.templates, options.markdown_tempalte)
    else:
        raise NotImplementedError

    options.output.write(output)

def convert_jinja2html(source, templatedir):
    """
    
    Arguments:
    - `input`: input text
    - `templatedir`: template directory
    """

    env = jinja2.Environment(loader=jinja2.ChoiceLoader([jinja2.DictLoader({'inputtemplate':source}),
                                                         jinja2.FileSystemLoader(templatedir)]))
    return env.get_template('inputtemplate').render()

def runserver(options):
    """
    
    Arguments:
    - `options`:
    """

    os.chdir(options.root)
    
    import SimpleHTTPServer
    import SocketServer

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("127.0.0.1", options.port), Handler)

    print "serving at http://127.0.0.1:{}/".format(options.port)
    httpd.serve_forever()


def _main():
    parser = argparse.ArgumentParser(description='Build Webpage with Markdown, Jinja2 templates, LESS or some recent tools.')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_ch = subparsers.add_parser('convert', help='convert documents to web pages')
    parser_ch.set_defaults(which='convert')
    parser_ch.add_argument('source', type=argparse.FileType('r'), help='Source file')
    parser_ch.add_argument('output', type=argparse.FileType('w'), help='Output file (default: stdout)', nargs='?', default=sys.stdout)
    parser_ch.add_argument('--templates', help='Root directory for jinja2 (default: %(default)s)', nargs='?', default='./source')
    parser_ch.add_argument('--markdown-template', help='Jinja2 Template HTML for Markdown. Relative path from templates directory (default: %(default)s)', default='templates/markdown.html')
    parser_ch.add_argument('--format', choices=('guess', 'markdown', 'jinja2', 'LESS'), default='guess', help='Input file format (default:%(default)s)')

    parser_server = subparsers.add_parser('runserver', help='Run Simple HTTP web server')
    parser_server.set_defaults(which='runserver')
    parser_server.add_argument('root', help='Root directory to serve.', nargs='?', default='public_html')
    parser_server.add_argument('-p', '--port', help='Web server port', nargs='?', default=8000, type=int)

    parser_init = subparsers.add_parser('init', help='Initialize project directory')
    parser_init.set_defaults(which='init')
    parser_init.add_argument
    parser_init.add_argument('--directory', help='Project directory', nargs='?', default='.')

    options = parser.parse_args()

    if options.which == 'convert':
        return convert(options)
    elif options.which == 'runserver':
        return runserver(options)
    elif options.which == 'directory':
        raise NotImplementedError
    else:
        raise NotImplementedError
    

if __name__ == '__main__':
    _main()


