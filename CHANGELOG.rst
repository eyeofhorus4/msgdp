Changelog
=========

Versions are year-based with a strict backwards compatibility policy.
The third digit is only for regressions.


1.0.1 (2016-07-19)
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


1.0.0 (2016-07-19)
-------------------

Changes:
^^^^^^^^

Initial release.