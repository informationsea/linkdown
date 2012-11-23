linkdown
========

Build Webpage with Markdown, Jinja2 templates, LESS or some recent tools.

Requirements
------------

* Python
    * Python 2.7
    * jinja2
    * markdown
    * watchdog
* Nodejs
    * less
    * coffeescript

How to install
--------------

1. Install [Python 2.7](http://www.python.org/) and [NodeJS](http://nodejs.org/)
2. Install [LESS](http://lesscss.org/) and [Coffeescript](http://coffeescript.org/)
3. Install [pip](http://pypi.python.org/pypi/pip)
    * I recommend to use [virtualenv](http://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper)
4. Install linkdown
    * just `pip install linkdown`


How to use
----------

1. Initialize project directory
   `linkdown init projectdir`
2. Change directory
   `cd projectdir`
3. Run server, file observer and converter
   `linkdown all -ws` or `make`

How to write
------------

Read jinja2, markdown, coffeescript and less documents

* [Jinja2 template syntax](http://jinja.pocoo.org/docs/templates/)
* [Markdown syntax](http://daringfireball.net/projects/markdown/syntax)
* [LESS](http://lesscss.org/)
* [Coffeescript](http://coffeescript.org/)




