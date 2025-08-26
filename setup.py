from setuptools import setup, find_packages

setup(
    name='cgi_processor',
    version='0.1.1',
    packages=find_packages(),
    description='Модуль для предобработки текстов журнала «Цифровые гуманитарные исследования»',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Boris Orekhov',
    author_email='nevmenandr@gmail.com',
    url='https://github.com/nevmenandr/cgi_processor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

