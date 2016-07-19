Changelog
=========

Versions are based on `Semantic Versioning 2.0.0 <semver.org>`_.

Given a version number MAJOR.MINOR.PATCH, increment the:

    - MAJOR version when you make incompatible API changes,
    - MINOR version when you add functionality in a backwards-compatible manner, and
    - PATCH version when you make backwards-compatible bug fixes.


1.0.1 (2016-07-19)
-------------------

Changes:
^^^^^^^^

Placeholder refs
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