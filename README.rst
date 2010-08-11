
===============
bitbucket-batch
===============

``bitbucket-batch`` is a command-line tool for making bulk access updates to 
`Bitbucket`_ repositories. It is useful in a corporate team situation where 
a single company account exists for managing private repositories with each 
team member having their own account with write access to these repositories.
When a new member joins or leaves the team, the process of manually adding or 
removing write access to all of the company's repositories can be tedious.
``bitbucket-batch`` allows you to make access updates to all of the company's 
repositories in a single command.

Installation
============

Assuming you have `setuptools`_ installed, the easiest method is to install 
directly from pypi by running the following command::

    $ easy_install -U bitbucket-batch

Otherwise you can download ``bitbucket-batch`` and install it directly from 
source::

    $ python setup.py install
    
Usage
=====

Once installed, the command ``bitbucket-batch`` should be available which 
can be run in the following format::

    $ bitbucket-batch repo_owner operation role user

Each of the required arguments are:

  * repo_owner: The Bitbucket username for the owner of the repositories the bulk update will be made to.
  * operation: The operation to apply which is either ``add`` or ``remove``.
  * role: The role to use for the operation which is either ``reader``, ``writer`` or ``admin``.
  * user: The Bitbucket username that the operation will be made for.
  
For example, to add the user ``stephenmcd`` as a ``writer`` to all 
repositories owned by the user ``citrus``, the command would be::

    $ bitbucket-batch citrus add writer stephenmcd
    
.. _`Bitbucket`: http://bitbucket.org/
.. _`setuptools`: http://pypi.python.org/pypi/setuptools

