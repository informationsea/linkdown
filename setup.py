from distutils.core import setup

setup(name='linkdown',
      version='0.1',
      description='Build Webpage with Markdown, Jinja2 templates, LESS or some recent tools.',
      packages=['linkdown'],
      author='Y.Okamura',
      license='GPL3+',
      url='https://github.com/informationsea/linkdown',
      install_requires = ['Markdown>=2.2.0', 'Jinja2>=2.6', 'watchdog>=0.6.0'],
      scripts=['scripts/linkdown']
      )
