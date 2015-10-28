from distutils.core import setup

install_requires = ['lxml']
    
setup(name='MinimalCoreNLPParser',
      version='1.0',
      description='Minimal CoreNLP XML Parser in Python',
      author='Florian Boudin',
      author_email='florian.boudin@univ-nantes.fr',
      packages=['corenlp_parser'],
      url="https://github.com/boudinfl/corenlp_parser"
     )
