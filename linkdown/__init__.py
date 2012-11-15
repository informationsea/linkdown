#!/usr/bin/env python
# -*- python -*-

import argparse
import jinja2
import markdown
import subprocess
import sys
import os

def convertcmd(options):
    """
    
    Arguments:
    - `options`:
    """

    convert(options.format, options.source, options.output, options.templates, options.markdown_template)


def convert(format, source, output, templates, markdown_template):
    """
    
    Arguments:
    - `options`: options from argparse
    """

    if format == 'guess':
        if source.name.lower().endswith('less'):
            format = 'less'
        elif source.name.lower().endswith('html'):
            format = 'jinja2'
        elif source.name.lower().endswith('md') or source.name.lower().endswith('markdown') :
            format = 'markdown'
        elif source.name.lower().endswith('coffeescript') or source.name.lower().endswith('coffee') :
            format = 'coffeescript'
        else:
            format = 'copy'
            #print 'Unknown file type:'+source.name

    if format == 'less':
        output_data = convert_with_external_program(['lessc', source.name])
    elif format == 'jinja2':
        output_data = convert_jinja2html(source.read(), templates)
    elif format == 'markdown':
        output_data = convert_markdown2html(source.read(), templates, markdown_template)
    elif format == 'coffeescript':
        output_data = convert_with_external_program(['coffee', '-pb', source.name])
    else:
        #print 'copy...'+source.name
        output_data = source.read()

    output.write(output_data)

def convert_with_external_program(program):
    """
    
    Arguments:
    - `source`:
    - `program`: list of program name and arguments
    """

    process = subprocess.Popen(program, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out


def convert_markdown2html(source, templatedir, markdown_template):
    options=dict()
    options['content'] = markdown.markdown(source)
    return convert_jinja2html(file(os.path.join(templatedir, markdown_template)).read(), templatedir, options)

def convert_jinja2html(source, templatedir, options=dict()):
    """
    
    Arguments:
    - `input`: input text
    - `templatedir`: template directory
    """

    env = jinja2.Environment(loader=jinja2.ChoiceLoader([jinja2.DictLoader({'inputtemplate':source}),
                                                         jinja2.FileSystemLoader(templatedir)]))
    return env.get_template('inputtemplate').render(**options)

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

def suggest_newfilename(path):
    """
    
    Arguments:
    - `path`:
    """

    convertdict = {'md': 'html',
                   'markdown': 'html',
                   'less': 'css',
                   'coffeescript': 'js',
                   'coffee': 'js'}

    for key, value in convertdict.iteritems():
        if path.endswith(key):
            return path[:-len(key)]+value
    return path
    


def convertall(options):
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

            convert('guess',
                    file(os.path.join(options.sourcedir, relpath), 'rb'),
                    file(os.path.join(options.destdir, suggest_newfilename(relpath)), 'wb'),
                    options.templates, options.markdown_template)


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
    #parser_init.add_argument
    parser_init.add_argument('--directory', help='Project directory', nargs='?', default='.')

    parser_all = subparsers.add_parser('all', help='Convert all')
    parser_all.set_defaults(which='all')
    parser_all.add_argument('sourcedir', help='Source directory')
    parser_all.add_argument('destdir', help='Destination directory')
    parser_all.add_argument('--exclude-suffix', default='.xcf,.psd,.DS_Store,.git,.hg,.svn', help='separated by comma defualt:%(default)s')
    parser_all.add_argument('--exclude-prefix', default='templates', help='separated by comma defualt:%(default)s')
    parser_all.add_argument('--templates', help='Root directory for jinja2 (default: %(default)s)', default='./source')
    parser_all.add_argument('--markdown-template', help='Jinja2 Template HTML for Markdown. Relative path from templates directory (default: %(default)s)', default='templates/markdown.html')

    options = parser.parse_args()

    if options.which == 'convert':
        return convertcmd(options)
    elif options.which == 'runserver':
        return runserver(options)
    elif options.which == 'all':
        return convertall(options)
    elif options.which == 'init':
        raise NotImplementedError
    else:
        raise NotImplementedError
    

if __name__ == '__main__':
    _main()


