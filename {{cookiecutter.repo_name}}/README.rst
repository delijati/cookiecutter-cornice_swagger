Documentation
=============

Put a brief description of '{{cookiecutter.project_title}}'.

Requirements
------------

- nodeenv for nodejs

- bower for swagger.ui

- virtualenv + pip

Installation
------------

Install app::

   $ cd {{cookiecutter.repo_name}}
   $ virtualenv env
   $ source env/bin/activate
   $ pip install -e .

Install swagger-ui::

   $ nodeenv nenv
   $ source nenv/bin/activate
   $ npm install -g bower
   $ cd {{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}/static
   $ bower install

Run::

   $ pserve dev.ini 
