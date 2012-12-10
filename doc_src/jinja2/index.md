Jinja2
======

Jinja2 is one of most powerful template engine for python web applications.
You have to write headers and footers only once, and other documents includes them.

Read documents
--------------

You can find Jinja2 documents at <http://jinja.pocoo.org/docs/>

Linkdown extension
------------------

Some built-in variables are available for jinja2 templates.

Variable Name  | Description                           | Example
-------------- | ------------------------------------- | -------------------
mtime          | Last Modified time                    | {{ mtime }}
ctime          | File create time                      | {{ ctime }}
mdate          | Last Modified date                    | {{ mdate }}
cdate          | File create date                      | {{ cdate }}
size           | File size                             | {{ size }}
originalpath   | Original file path                    | {{ originalpath }}
relpath        | Relative path from root               | {{ relpath }}
root           | Relative path to root                 | {{ root }}

Examples
--------

Examples of tempalte

[base.html](../../doc_src/templates/base.html){: .btn } Master template

[markdown.html](../../doc_src/templates/markdown.html){: .btn } A template for markdown and reStructuredText
