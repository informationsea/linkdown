Markdown Extensions
===================

Some extensions are included in python markdown library.

[Back to basic syntax &raquo;](./markdown.html){: .btn .btn-primary }

Table
-----


    Head1 | Head2 | Head3
    ----- | ----- | -----
    body1 | body2 | body3
    foo1  | foo2  | foo3


Head1 | Head2 | Head3
----- | ----- | -----
body1 | body2 | body3
foo1  | foo2  | foo3

    <table>
      <thead><tr><th>Head1</th><th>Head2</th><th>Head3</th></tr></thead>
      <tbody>
        <tr><td>body1</td><td>body2</td><td>body3</td></tr>
        <tr><td>foo1</td><td>foo2</td><td>foo3</td></tr>
      </tbody>
    </table>

Abbreviations
-------------

    OpenVPN is one of most secure VPN.
    
    *[VPN]: Virtual Private Network

OpenVPN is one of most secure VPN.

*[VPN]: Virtual Private Network

    OpenVPN is one of most secure <abbr title="Virtual Private Network">VPN</abbr>.

Attribute Lists
---------------

Add attributes to HTML tag.

    Sample button [Button](http://example.com){: class="btn btn-success" title="Sample!" }
    {: .well }

Sample button [Button](http://example.com){: class="btn btn-success" title="Sample!" }
{: .well }

    <p class="well">Sample button <a class="btn btn-success" href="http://example.com" title="Sample!">Button</a></p>


Definition Lists
----------------

    HTML
    :    Hyper Text Markup Language, widely used at the Internet

HTML
:    Hyper Text Markup Language, widely used at the Internet.

<div class="workaround"></div>

    <dl>
    <dt>HTML</dt>
    <dd>Hyper Text Markup Language, widely used at the Internet</dd>
    </dl>

Fenced Code Blocks
------------------

    ~~~~~~~~~~~~~{.python}
    #!/usr/bin/env python
    
    print "Hello, world!"
    ~~~~~~~~~~~~~

~~~~~~~~~~~~~{.python}
#!/usr/bin/env python

print "Hello, world!"
~~~~~~~~~~~~~

    <pre><code class="python">#!/usr/bin/env python
    
    print &quot;Hello, world!&quot;
    </code></pre>

Footnotes
---------

    This text[^1] has footnotes.
    
    [^1]: This is footnote

This text[^1] has footnotes.

[^1]: This is footnote

///Footnotes Go Here///


