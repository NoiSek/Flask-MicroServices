"""
Flask-MicroServices
-------------

Brings a form of the microservices concept to Flask with self contained modules and Django style URL routing.
"""

from setuptools import setup


setup(
    name='Flask-MicroServices',
    version='0.34.5',
    url='http://github.com/noisek/Flask-MicroServices',
    license='MIT',
    author='Noi Sek',
    author_email='noi.t.sek@gmail.com',
    description='Self contained modules and Django style URL routing for Flask.',
    zip_safe=True,
    packages = ['flask_microservices'],
    include_package_data=True,
    package_data={
        'examples': ['example', 'README.md']
    },
    platforms='any',
    install_requires=[
        'Flask'
    ],
    setup_requires=['pandoc', 'setuptools-markdown'],
    long_description_markdown_filename='README.md',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['Flask', 'Django', 'Routes', 'Routing', 'URLs', 'Templates', 'Templating', 'Microservices']
)
