========
linkdown
========

Build static webpages with Markdown_, reStructuredText_, Jinja2_ templates, LESS_ or some recent tools.

* Built in Twitter Bootstrap template
* Built in web server for development
* linkdown watch your file changes and convert them automatically
* Automatic content list generator for Markdown and reStructuredText in Bootstrap template

------------
Requirements
------------

* Python
    * Python 2.7
    * jinja2
    * markdown
    * watchdog
    * Docutils
    * rst2html5
* Nodejs
    * less
    * coffeescript

--------------
How to install
--------------

1. Install `Python 2.7`_ and NodeJS_
    * I recommend to use MacPorts_ or Homebrew_ to install them if you are Mac OS X user.
2. Install LESS_ and CoffeeScript_
    * If you don't use LESS_ and CoffeeScript_, you don't have to instal them.
3. Install pip_
    * I recommend to use virtualenv_ and virtualenvwrapper_
4. Install linkdown
    * just ``pip install linkdown``
    * All dependencies will be installed automatically

.. _MacPorts: http://www.macports.org/
.. _Homebrew: http://mxcl.github.com/homebrew/
.. _Python 2.7: http://www.python.org/
.. _NodeJS: http://nodejs.org/
.. _LESS: http://lesscss.org/
.. _CoffeeScript: http://coffeescript.org/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _virtualenvwrapper: http://pypi.python.org/pypi/virtualenvwrapper
.. _pip: http://pypi.python.org/pypi/pip

-----------
Quick Start
-----------

1. Initialize project directory
   
   ``linkdown init --template bootstrap projectdir``

2. Change directory
   
   ``cd projectdir``

3. Run server, file observer and converter. linkdown detects file modification event and convert automatically.
   
   ``linkdown all -ws`` or ``make``

4. Make your content under ``source`` directory


-----------------------------
Built in variables for Jinja2
-----------------------------

============ ===================================
Name         Description
============ ===================================
mdate        Last Modified date and time
cdate        File create date and time
size         File size
originalpath Original file path
relpath      Relative output path from html root
============ ===================================

----------
References
----------

Read jinja2, markdown, coffeescript and less documents to write. Of course, you can use plain JavaScript and CSS (But not plain HTML).

* Jinja2_
* Markdown_
* LESS_
* CoffeeScript_
* reStructuredText_
* Bootstrap_

.. _Jinja2: http://jinja.pocoo.org/docs/templates/
.. _Markdown: http://daringfireball.net/projects/markdown/syntax
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Bootstrap: http://twitter.github.com/bootstrap/

