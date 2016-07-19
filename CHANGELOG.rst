Changelog
=========

Versions are year-based with a strict backwards compatibility policy.
The third digit is only for regressions.


15.1.0 (2015-08-20)
-------------------

Changes:
^^^^^^^^

- Add ``attr.validators.optional`` that wraps other validators allowing attributes to be ``None``.
  `#16 <https://github.com/hynek/attrs/issues/16>`_
- Fix multi-level inheritance.
  `#24 <https://github.com/hynek/attrs/issues/24>`_
- Fix ``__repr__`` to work for non-redecorated subclasses.
  `#20 <https://github.com/hynek/attrs/issues/20>`_


----


15.0.0 (2015-04-15)
-------------------

Changes:
^^^^^^^^

Initial release.