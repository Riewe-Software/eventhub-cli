from setuptools import setup

setup(
    name="eventhub-cli",
    version='0.0.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        eventhub-cli=cli:cli
    ''',
)