#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import time
import subprocess
import re
import urllib

import jinja2
import markdown
import markdown.treeprocessors

import linkdown.htmlhelper

def convert(format, source, output, templates, markdown_template, compress):
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

    options = dict()
    options['mtime'] = time.strftime("%H:%M %d/%B/%Y %Z", time.localtime(os.path.getmtime(source.name)))
    options['ctime'] = time.strftime("%H:%M %d/%B/%Y %Z", time.localtime(os.path.getctime(source.name)))
    options['size'] = os.path.getsize(source.name)
    options['originalpath'] = source.name
    options['relpath'] = os.path.relpath(source.name, templates)

    if format == 'less':
        output_data = convert_with_external_program(['lessc', source.name])
    elif format == 'jinja2':
        output_data = convert_jinja2html(source.read(), templates, options=options, compress=compress)
    elif format == 'markdown':
        output_data = convert_markdown2html(source.read(), templates,
                                            markdown_template=markdown_template, options=options, compress=compress)
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

    try:
        process = subprocess.Popen(program, stdout=subprocess.PIPE)
        out, err = process.communicate()
    except OSError as e:
        sys.exit('ERROR: Command `{program}` is not found'.format(program=program[0]))
    return out


def convert_markdown2html(source, templatedir, markdown_template, options=dict(), compress=False):
    options['content'] = markdown.markdown(unicode(source, 'utf-8'), [MarkdownHeadlineExtension()])

    parser = linkdown.htmlhelper.HeadlineParser()
    parser.feed(options['content'])
    options['title'] = parser.h1
    options['headlines'] = parser.headlines
    
    return convert_jinja2html(file(os.path.join(templatedir, markdown_template)).read(), templatedir, options, compress)

def convert_jinja2html(source, templatedir, options=dict(), compress=False):
    """
    
    Arguments:
    - `input`: input text
    - `templatedir`: template directory
    """

    env = jinja2.Environment(loader=jinja2.ChoiceLoader([jinja2.DictLoader({'inputtemplate':unicode(source, 'utf-8')}),
                                                         jinja2.FileSystemLoader(templatedir)]))
    output = env.get_template('inputtemplate').render(**options)
    if compress:
        return linkdown.htmlhelper.compress_html(output).encode('utf-8')
    return output.encode('utf-8')


class MarkdownHeadlineExtension(markdown.Extension):
    """ Headline ID Extension """
    def __init__(self):
        """
        
        Arguments:
        - `self`:
        """

        pass

    def extendMarkdown(self, md, md_globals):
        """
        
        Arguments:
        - `self`:
        - `md`:
        - `md_globals`:
        """

        md.registerExtension(self)
        self.parser = md.parser
        self.md = md

        md.treeprocessors["headline"] = MarkdownHeadlineIDTreeProcessor()

_clean2 = re.compile(r'[^\w\d\s\-\,. \\/]')
_clean = re.compile(r'[^\w\d]')

import base64

def clean_name(name):
    """
    
    Arguments:
    - `name`:
    """

    if _clean2.search(name):
        return base64.urlsafe_b64encode(name.encode('utf-8')).replace('=','')

    return _clean.sub('-', name)
        
class MarkdownHeadlineIDTreeProcessor(markdown.treeprocessors.Treeprocessor):

    def __init__(self):
        """
        
        Arguments:
        - `self`:
        """
        
        pass
    
    def run(self, root):
        """
        
        Arguments:
        - `self`:
        - `root`:
        """

        return self.set_id(root)

    def set_id(self, element):
        """
        
        Arguments:
        - `self`:
        - `element`:
        """

        if element.tag == 'h1':
            #element.set("id", urllib.quote(element.text.encode('utf-8')))
            element.set("id", clean_name(element.text))
        elif element.tag == 'h2':
            #element.set("id", urllib.quote(element.text.encode('utf-8')))
            element.set("id", clean_name(element.text))
        elif element.tag == 'h3':
            #element.set("id", urllib.quote(element.text.encode('utf-8')))
            element.set("id", clean_name(element.text))

        for child in element:
            self.set_id(child)