========
linkdown
========

Build static webpages with Markdown_, reStructuredText_, Jinja2_ templates, LESS_ or some recent tools.

* Built in Twitter Bootstrap template
* Built in web server for development
* linkdown watch your file changes and convert them automatically
* Automatic content list generator for Markdown and reStructuredText in Bootstrap template (Shown in bottom)

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

-------------------
License & Copyright
-------------------

:strong:`Linkdown`

Copyright (C) 2012 Y.OKAMURA

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


:strong:`Twitter Bootstrap`

Copyright 2012 Twitter, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

:strong:`jQuery`

Copyright 2012 jQuery Foundation and other contributors

<http://jquery.com/>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
