"""
Flask-MicroServices
-------------

Brings a form of the 'Micro Service' concept to Flask with self contained apps and Django style URL routing.
"""

from setuptools import setup


setup(
    name='Flask-MicroServices',
    version='0.22',
    url='http://github.com/noisek/Flask-MicroServices',
    license='MIT',
    author='Noi Sek',
    author_email='noi.t.sek@gmail.com',
    description='Self contained apps and Django style URL routing for Flask.',
    long_description=__doc__,
    py_modules=['flask_microservices'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
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
