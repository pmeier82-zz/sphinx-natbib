.. DANGER::
   FORKED FROM https://bitbucket.org/wnielson/sphinx-natbib
   WITH CHANGES FROM https://github.com/jterrace/sphinxtr

sphinx-natbib
=============

This is an extension for Sphinx that is meant to provide similar functionality
as the natbib package for latex.  This is a very early work in progress.


Install
-------

  1) Install pybtex (easy_install pybtex)
  2) Add ``natbib`` to your Sphinx project's ``extensions`` option

Usage
-----

Right now there isn't much in the way of configuration and only HTML output
works.  That said, you can tell Sphinx about a .bib file by adding the
following to your ``conf.py``::

    natbib = {
      "file": "example.bib"
    }

Now, in your project you can cite references with :cite:p:`cite-key` or
:cite:t:`cite-key`.

Run `make html` and see your citations show up.

For more examples of how this works, check out the ``docs`` folder.

Like I said, this is a work in progress.  If you want to help, please do!
