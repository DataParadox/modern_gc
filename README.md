# Performance Analysis of Modern Garabge Collectors in JDK 20

***Help***
+ ``--b_suite``: Evaluation benchmark suite (``dacapo``, ``renaissance``)
+ ``--benchmark``: Evaluation benchmark dataset
+ ``--max_heap``: Maximum heap size available (in power of 2 and greater than 512 MB)
+``--varying_heap``: Varying heap size

***Example***
+ For `xalan` benchmark dataset from `dacapo` benchmark suite with ``max_heap = 2048`` in ``varying_heap`` environment the GC Logs can generate using -
```python
python performance_analysis --b_suite dacapo --benchmark xalan --max_heap 2048 --varying_heap True
```
***Dacapo Benchmark Suite:*** The DaCapo-9.12-bach benchmark suite, released in 2009, consists of the following benchmarks:
+ ``avrora`` - simulates a number of programs run on a grid of AVR microcontrollers
+ ``batik`` - produces a number of Scalable Vector Graphics (SVG) images based on the unit tests in Apache Batik
+ ``eclipse`` - executes some of the (non-gui) jdt performance tests for the Eclipse IDE
+ ``fop`` - takes an XSL-FO file, parses it and formats it, generating a PDF file.
+ ``h2`` - executes a JDBCbench-like in-memory benchmark, executing a number of transactions against a model of a banking application, replacing the hsqldb benchmark
+ ``jython`` - inteprets a the pybench Python benchmark
+ ``luindex`` - Uses lucene to indexes a set of documents; the works of Shakespeare and the King James Bible
+ ``lusearch`` - Uses lucene to do a text search of keywords over a corpus of data comprising the works of Shakespeare and the King James Bible
+ ``pmd`` - analyzes a set of Java classes for a range of source code problems
+ ``sunflow`` - renders a set of images using ray tracing
+ ``tomcat`` - runs a set of queries against a Tomcat server retrieving and verifying the resulting webpages
+ ``tradebeans`` - runs the daytrader benchmark via a Jave Beans to a GERONIMO backend with an in memory h2 as the underlying database
+ ``tradesoap`` - runs the daytrader benchmark via a SOAP to a GERONIMO backend with in memory h2 as the underlying database
+ ``xalan`` - transforms XML documents into HTML
