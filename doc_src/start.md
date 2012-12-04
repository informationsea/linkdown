Start linkdown
==============

Let's start linkdown

Initialize project
------------------

    $ linkdown init --template bootstarp projectdir

There are two template, `basic` and `bootstrap`. I recommend `bootstrap` template because it's beauty!

Run web server and file observer
--------------------------------

Linkdown has built-in web server and file observer.
You don't have to install Apache to develop.

    $ cd projectdir
    $ linkdown all -ws

If you just want to convert files, run `linkdown all`.

Sometimes linkdown miss file change events. Please save your file again to convert or run `linkdown all`.

Customize title and navibar
---------------------------

To customize title and navibar, open `templates/base.html` and edit it.
Please read [Twitter Bootstrap](http://twitter.github.com/bootstrap/) to customize navibar.


