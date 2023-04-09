# Performance Analysis of Modern Garabge Collectors in JDK 20

***Help***
+ ``--b_suite``: Evaluation benchmark suite (``dacapo``, ``renaissance``)
+ ``--benchmark``: Evaluation benchmark dataset
+ ``--max_heap``: Maximum heap size available (in power of 2 and greater than 512 MB)
+``--varying_heap``: Varying heap size

***Example***
For `xalan` benchmark dataset from `dacapo` benchmark suite with ``max_heap = 2048`` in ``varying_heap`` environment the GC Logs can generate using -
```python
python performance_analysis --b_suite dacapo --benchmark xalan --max_heap 2048 --varying_heap True
```
