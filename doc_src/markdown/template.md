Markdown templates
==================

Linkdown use Jinja2 template to render markdown documents.
You can find template at `templates/markdown.html` if you are using default template.
This template will be also used for render reStructuredText.

Variables for markdown template
-------------------------------

### content

The variable `content` contains HTML converted from the markdown document.

### headlines

The variable `headlines` contains headlines in the markdown document.
List of tuples, each tuples have 3 element, tag name, headline text, headline tag id.

    [
    ('h1', 'Markdown templates', 'Markdown-templates'),
    ('h2', 'Variables for markdown template', 'Variables-for-markdown-template'),
    ('h3', 'content', 'content')
    ]

Read sample template to learn more.
