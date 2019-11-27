from codecs     import open
from inspect    import getsource
from os.path    import abspath, dirname, join
from setuptools import setup

here = abspath(dirname(getsource(lambda:0)))

with open(join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name             = 'pyPlayMusic',
      version          = '0.1.0',
      description      = long_description.splitlines()[2][1:-1],
      long_description = long_description,
      url              = 'https://github.com/davinnovation/pyPlayMusic',
      author           = 'Davi Innovation',
      author_email     = 'davinnovation@gmail.com',
      license          = 'MIT',
      classifiers      = ['Development Status :: 5 - Production/Stable',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: MIT License',
                          'Operating System :: OS Independent',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.1',
                          'Programming Language :: Python :: 3.2',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
                          'Programming Language :: Python :: 3.5',
                          'Topic :: Multimedia :: Sound/Audio :: MIDI',
                          'Topic :: Multimedia :: Sound/Audio :: Players',],
      keywords         = 'play wave wav mp3 & play notes with async, sync',
      py_modules       = ['pyplaymusic'])