How to make a releases of this package
======================================

* Update package, make sure that GitHub subrepository is updated as well.
* Make sure all tests pass by running ``bin/test``.
* Use ``zest.releaser`` to release this package on pypi (usually just call
  ``fullrelease``)
  * Make sure the version matches the one of the package released at bower.
