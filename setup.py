from setuptools import setup, find_packages
import os
import os.path

packagedir = os.path.join(os.path.dirname(__file__), 'linkdown')
package_data = []
for root, dirs, files in os.walk(packagedir):
    for i, onedir in enumerate(dirs):
        if onedir[0] == '.':
            del dirs[i]
        elif onedir[0] == 'public_html':
            del dirs[i]
    if '__init__.py' not in files: # not package dir
        package_data += [os.path.relpath(os.path.join(root, x), packagedir) for x in files if x[0] != '.']

with file(os.path.join(packagedir, 'datalist.txt'), 'w') as f:
    for one in package_data:
        print >>f, one

setup(name='linkdown',
      version='0.1',
      description='Build static webpages with Jinja2, Markdown, LESS, Coffeescript',
      packages=['linkdown'],
      author='Y.Okamura',
      author_email='okamura@informationsea.info',
      license='GPL3+',
      url='https://github.com/informationsea/linkdown',
      install_requires = ['Markdown>=2.2.0', 'Jinja2>=2.6', 'watchdog>=0.6.0'],
      scripts=['scripts/linkdown'],
      package_data={'linkdown': package_data + ['datalist.txt']},
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Environment :: Web Environment']
      )
