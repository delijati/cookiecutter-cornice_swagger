import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst")) as f:
    README = f.read()


setup(name="{{cookiecutter.repo_name}}",
      version=0.1,
      description="{{cookiecutter.repo_name}}",
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author="",
      author_email="",
      url="",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "cornice",
          "pyramid_chameleon",
          "cornice_swagger",
          "waitress",
          "colander"
      ],
      entry_points="""\
      [paste.app_factory]
      main={{cookiecutter.repo_name}}:main
      """,
      paster_plugins=["pyramid"])
