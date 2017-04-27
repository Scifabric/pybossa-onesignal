from setuptools import setup, find_packages

setup(
    name='pybossa-onesignal',
    version='1.0',
    packages=find_packages(),
    install_requires=['requests>=0.13.0'],
    # metadata for upload to PyPI
    author='Scifabric LTD',
    # TODO: change
    author_email='info@scifabric.com',
    description='pybossa-onesignal is a small library to send Web PUSH notifications within PYBOSSA ecosystem.',
    long_description='''PYBOSSA is a crowdsourcing framework. This tiny library allows you to send Web PUSH notifications to your users.''',
    license='AGPLv3',
    url='https://github.com/Scifabric/pybossa-onesignal',
    download_url='https://github.com/Scifabric/pybossa-onesignal/zipball/master',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points=''''''
)
