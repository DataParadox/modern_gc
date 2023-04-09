# A Performance Analysis of Modern Garbage Collectors in the JDK 20 Environment

***Help***
+ ``--b_suite``: Evaluation benchmark suite (``dacapo``, ``renaissance``)
+ ``--benchmark``: Evaluation benchmark dataset
+ ``--max_heap``: Maximum heap size available (in power of 2 and greater than 512 MB)
+``--varying_heap``: Varying heap size

***Example***
+ For `xalan` benchmark dataset from `dacapo` benchmark suite with ``max_heap = 2048`` in ``varying_heap`` environment the GC Logs can generate using -
```python
python performance_analysis.py --b_suite dacapo --benchmark xalan --max_heap 2048 --varying_heap True
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

***Renaissance Benchmark Suite:*** The following is the complete list of benchmarks, separated into groups.
+ ``apache-spark:``
  - ``als`` - Runs the ALS algorithm from the Spark ML library.
  - ``chi-square`` - Runs the chi-square test from Spark MLlib.
  - ``dec-tree`` - Runs the Random Forest algorithm from the Spark ML library.
  - ``gauss-mix`` - Computes a Gaussian mixture model using expectation-maximization.
  - ``log-regression`` - Runs the Logistic Regression algorithm from the Spark ML library.
  - ``movie-lens`` - Recommends movies using the ALS algorithm.
  - ``naive-bayes`` - Runs the multinomial Naive Bayes algorithm from the Spark ML library.
  - ``page-rank`` - Runs a number of PageRank iterations, using RDDs.
+ ``concurrency:``
  - ``akka-uct`` - Runs the Unbalanced Cobwebbed Tree actor workload in Akka.
  - ``fj-kmeans`` - Runs the k-means algorithm using the fork/join framework.
  - ``reactors`` - Runs benchmarks inspired by the Savina microbenchmark workloads in a sequence on Reactors.IO.
+ ``database:``
  - ``db-shootout`` - Executes a shootout test using several in-memory databases.
  - ``neo4j-analytics`` - Executes Neo4J graph queries against a movie database.
+ ``functional:``
  - ``future-genetic`` - Runs a genetic algorithm using the Jenetics library and futures.
  - ``mnemonics`` - Solves the phone mnemonics problem using JDK streams.
  - ``par-mnemonics`` - Solves the phone mnemonics problem using parallel JDK streams.
  - ``rx-scrabble`` - Solves the Scrabble puzzle using the Rx streams.
  - ``scrabble`` - Solves the Scrabble puzzle using JDK Streams.
+ ``scala:``
  - ``dotty`` - Runs the Dotty compiler on a set of source code files.
  - ``philosophers`` - Solves a variant of the dining philosophers problem using ScalaSTM.
  - ``scala-doku`` - Solves Sudoku Puzzles using Scala collections.
  - ``scala-kmeans`` - Runs the K-Means algorithm using Scala collections.
  - ``scala-stm-bench7`` - Runs the stmbench7 benchmark using ScalaSTM.
+ ``web:``
  - ``finagle-chirper`` - Simulates a microblogging service using Twitter Finagle.
  - ``finagle-http`` - Sends many small Finagle HTTP requests to a Finagle HTTP server and awaits response.
