from setuptools import setup, find_packages

setup(
    name='django-prelaunch',
    description='A Django app to gather email addresses of people interested in your prelaunch-stage website.',
    version='0.1',
    packages = find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
    ],
    keywords='django',
    author='Johan Beyers',
    author_email='jbeyers@juizi.com',
    url='http://github.com/jbeyers/django-prelaunch',
    license='BSD',
    install_requires = []
)
