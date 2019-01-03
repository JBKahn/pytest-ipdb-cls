pytest-ipdb-cls
===============

Installation and usage
----------------------

To install

    pip install pytest-ipdb-cls
  
To use: run pytest with `--pdbcls=pytest_ipdb_cls:Debugger`.

Usage with Pytest
-----------------

To enter into the dbeugger, complete with syntax highlighting and tab completion add:
```python
import pytest
pytest.set_trace()
```
to the code and it will enter the trace. This does not require you to paass `-s` as it will handle capture correctly.

You can also enter the debugger on failure by executing pytest with `--pdbcls=pytest_ipdb_cls:Debugger --pdb`.
