.. Sphinx Natbib Extension documentation master file, created by
   sphinx-quickstart on Wed Dec 15 08:22:53 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _section-overview:

Overview
========

The goal of `sphinx-natbib`_ is to implement the functionality of
`natbib for latex`_, but for `Sphinx`_.  The current implementation is far from
complete and does not provide all of the functions of natbib for latex.  Below
are the currently available commands that have been implemented in
``sphinx-natbib``.

The initial version of ``sphinx-natbib`` simply added a bunch of ReST roles
into the default domain.  However, as of version 0.2 all of the functionality
is added via a custom ``cite`` domain.

.. _sphinx-natbib: https://bitbucket.org/wnielson/sphinx-natbib
.. _natbib for latex: http://merkel.zoneo.net/Latex/natbib.php
.. _Sphinx: http://sphinx.pocoo.org/


.. _section-commands:

Basic Commands
==============

The two most common commands, ``:cite:p:`` and ``:cite:t:``, behave just like
they do in the original natbib.  The following examples are in the default
``'authoryear'`` format.

.. cite:conf:: authoryear

.. list-table::
  :header-rows: 1

  * - Latex
    - Sphinx (ReStructuredText)
    - Ouput

  * - ``\citet{Marten+As:1900}``
    - ``:cite:t:`Marten+As:1900```
    - :cite:t:`Marten+As:1900`
  * - ``\citet[chap. 2]{Marten+As:1900}``
    - ``:cite:t:`Marten+As:1900 [chap. 2]```
    - :cite:t:`Marten+As:1900 [chap. 2]`
  * - ``\citep{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900```
    - :cite:p:`Marten+As:1900`
  * - ``\citep[chap. 2]{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900 [chap. 2]```
    - :cite:p:`Marten+As:1900 [chap. 2]`
  * - ``\citep[see][]{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900 [see][]```
    - :cite:p:`Marten+As:1900 [see][]`
  * - ``\citep[see][chap. 2]{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900 [see][chap. 2]```
    - :cite:p:`Marten+As:1900 [see][chap. 2]`
  * - ``\citet*{Marten+As:1900}``
    - ``:cite:ts:`Marten+As:1900```
    - :cite:ts:`Marten+As:1900`
  * - ``\citep*{Marten+As:1900}``
    - ``:cite:ps:`Marten+As:1900```
    - :cite:ps:`Marten+As:1900`


.. _section-multiple:

Multiple Citations
==================

Multiple citations can be referenced via a single cite command by simply
joining cite keys with commas.

.. list-table::
  :header-rows: 1

  * - Latex
    - Sphinx (ReStructuredText)
    - Ouput
  * - ``\citet{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:t:`Marten+As:1900,vanWilgen:1910```
    - :cite:t:`Marten+As:1900,vanWilgen:1910`
  * - ``\citep{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:p:`Marten+As:1900,vanWilgen:1910```
    - :cite:p:`Marten+As:1900,vanWilgen:1910`
  * - ``\citet*{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:ts:`Marten+As:1900,vanWilgen:1910```
    - :cite:ts:`Marten+As:1900,vanWilgen:1910`
  * - ``\citep*{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:ps:`Marten+As:1900,vanWilgen:1910```
    - :cite:ps:`Marten+As:1900,vanWilgen:1910`


.. _section-numerical:

Numerical Mode
==============

Just like in the original natbib, ``sphinx-natbib`` supports alternate citation
styles.  By default, ``sphinx-natbib`` is configured to output citation in
``'authoryear'`` format (see the :ref:`section-config` section below for
details on how to change the citation style on a global basis).  Additionally,
it is possible to change citation style on a per-page or per-block basis (see
:ref:`section-changing_styles`).

Style: ``numbers``
------------------

.. cite:conf:: numbers
 :brackets: []

.. list-table::
  :header-rows: 1

  * - Latex
    - Sphinx (ReStructuredText)
    - Ouput

  * - ``\citet{Marten+As:1900}``
    - ``:cite:t:`Marten+As:1900```
    - :cite:t:`Marten+As:1900`
  * - ``\citet[chap. 2]{Marten+As:1900}``
    - ``:cite:t:`Marten+As:1900 [chap. 2]```
    - :cite:t:`Marten+As:1900 [chap. 2]`
  * - ``\citep{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900```
    - :cite:p:`Marten+As:1900`
  * - ``\citep[chap. 2]{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900 [chap. 2]```
    - :cite:p:`Marten+As:1900 [chap. 2]`
  * - ``\citep[see][]{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900 [see][]```
    - :cite:p:`Marten+As:1900 [see][]`
  * - ``\citep[see][chap. 2]{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900 [see][chap. 2]```
    - :cite:p:`Marten+As:1900 [see][chap. 2]`
  * - ``\citep{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:p:`Marten+As:1900,vanWilgen:1910```
    - :cite:p:`Marten+As:1900,vanWilgen:1910`
  * - ``\citet*{Marten+As:1900}``
    - ``:cite:ts:`Marten+As:1900```
    - :cite:ts:`Marten+As:1900`
  * - ``\citep*{Marten+As:1900}``
    - ``:cite:ps:`Marten+As:1900```
    - :cite:ps:`Marten+As:1900`

Style: ``super``
----------------

The one major caveat with the ``super`` citation style is that any pre- and
post-citation text does not look very good.  For this reason, it is suggested
to avoid such text if you use the ``super`` citation style.

.. cite:conf:: super

.. list-table::
  :header-rows: 1

  * - Latex
    - Sphinx (ReStructuredText)
    - Ouput

  * - ``\citet{Marten+As:1900}``
    - ``:cite:t:`Marten+As:1900```
    - :cite:t:`Marten+As:1900`
  * - ``\citep{Marten+As:1900}``
    - ``:cite:p:`Marten+As:1900```
    - :cite:p:`Marten+As:1900`
  * - ``\citep{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:p:`Marten+As:1900,vanWilgen:1910```
    - :cite:p:`Marten+As:1900,vanWilgen:1910`
  * - ``\citet*{Marten+As:1900}``
    - ``:cite:ts:`Marten+As:1900```
    - :cite:ts:`Marten+As:1900`
  * - ``\citep*{Marten+As:1900}``
    - ``:cite:ps:`Marten+As:1900```
    - :cite:ps:`Marten+As:1900`

.. _section-suppressed_parentheses:

Suppressed Parentheses
======================

.. cite:conf:: authoryear

.. list-table::
  :header-rows: 1

  * - Latex
    - Sphinx (ReStructuredText)
    - Ouput
  * - ``\citealt{Marten+As:1900}``
    - ``:cite:alt:`Marten+As:1900```
    - :cite:alt:`Marten+As:1900`
  * - ``\citealt*{Marten+As:1900}``
    - ``:cite:alts:`Marten+As:1900```
    - :cite:alts:`Marten+As:1900`
  * - ``\citealp{Marten+As:1900}``
    - ``:cite:alp:`Marten+As:1900```
    - :cite:alp:`Marten+As:1900`
  * - ``\citealp*{Marten+As:1900}``
    - ``:cite:alps:`Marten+As:1900```
    - :cite:alps:`Marten+As:1900`
  * - ``\citealp{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:alp:`Marten+As:1900,vanWilgen:1910```
    - :cite:alp:`Marten+As:1900,vanWilgen:1910`
  * - ``\citealp[pg. 32]{Marten+As:1900}``
    - ``:cite:alp:`Marten+As:1900 [pg. 32]```
    - :cite:alp:`Marten+As:1900 [pg. 32]`
  * - ``\citetext{priv. comm.}``
    - ``:cite:text:`priv. comm.```
    - :cite:text:`priv. comm.`

.. _section-partial:

Partial Citations
=================

.. cite:conf:: authoryear

.. list-table::
  :header-rows: 1

  * - Latex
    - Sphinx (ReStructuredText)
    - Ouput
  * - ``\citeauthor{Marten+As:1900}``
    - ``:cite:author:`Marten+As:1900```
    - :cite:author:`Marten+As:1900`
  * - ``\citeauthor*{Marten+As:1900}``
    - ``:cite:authors:`Marten+As:1900```
    - :cite:authors:`Marten+As:1900`
  * - ``\citeyear{Marten+As:1900}``
    - ``:cite:year:`Marten+As:1900```
    - :cite:year:`Marten+As:1900`
  * - ``\citeyear{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:year:`Marten+As:1900,vanWilgen:1910```
    - :cite:year:`Marten+As:1900,vanWilgen:1910`
  * - ``\citeyearpar{Marten+As:1900}``
    - ``:cite:yearpar:`Marten+As:1900```
    - :cite:yearpar:`Marten+As:1900`
  * - ``\citeyearpar{Marten+As:1900,vanWilgen:1910}``
    - ``:cite:yearpar:`Marten+As:1900,vanWilgen:1910```
    - :cite:yearpar:`Marten+As:1900,vanWilgen:1910`


.. _section-changing_styles:

Changing Styles
===============

It is possible to temporarily change the default citation style on a per-page
or per-block basis.  The ``cite`` directive provides this ability, like so:

.. code-block:: rst

 .. cite:conf:: [style]

The argument ``[style]`` can be one of four options; ``authordate``,
``numbers``, ``super`` or nothing.  If the argument is nothing, then the
default style will be used.  When this directive is used it will change the
citation style until the end of the page is reached or until another ``cite``
directive is encountered.  Additionally, the ``cite`` directive supports
the following options:

 ``brackets``
   Define the characters to use for brackets; string.
 ``separator``
   Define the separator between multiple citations; character.
 ``sort``
   Whether or not to sort multiple citations; True or False.
 ``sort_compress``
   Same as ``sort`` but will also compress numbers when in numerical citation
   mode; True or False.

For example, to temporarily change to numerical citation mode and the brackets
from the default ``()`` to ``[]``, the following ``cite`` directive can be
used:

.. code-block:: rst

 .. cite:conf:: numbers
   :brackets: []


.. _section-config:

Configuration Options
=====================

You can tweak the behavior and output of ``sphinx-natbib`` through
the ``natbib`` dictionary in your doc's ``conf.py`` file. Available
configuration options are:

 ``'file'``
   **Required**: The bibtex file to use.  This should be a string representing
   the path to the bibtex file that contains references.
 ``'brackets'``
   Open and closing brackets to use in citations, default ``'()'``.
 ``'separator'``
   Character to use between multiple citations, default ``';'``.
 ``'style'``
   The global style for citations, default ``'authoryear'``.  The other possible
   values are ``'numbers'`` or ``'super'``.
 ``'sort'``
   Whether or not to sort multiple citations in the same order in which they
   appear in the list of references, default ``False``.
 ``'sort_compress'``
   The same as ``'sort'``, but compresses citations if possible, default
   ``False``.


.. _section-displaying_references:

Displaying References
=====================

In order for links to references to be generated, you must define where the
references should be included.  The ``refs`` directive should therefor be used
where you want the list of references to be displayed.  The following directive
produces the output seen in the :ref:`section-references` section below:

.. code-block:: rst

 .. cite:refs::


.. _section-references:

References
==========

.. cite:refs::
.. :path: example.bib
