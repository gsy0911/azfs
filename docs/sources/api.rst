#############
API Reference
#############

AzFileClient
************

.. autoclass:: azfs.AzFileClient


get/download
============

.. autofunction:: azfs.AzFileClient.get

.. autofunction:: azfs.AzFileClient.read_line_iter

.. autofunction:: azfs.AzFileClient.read_csv

.. autofunction:: azfs.AzFileClient.read_table

.. autofunction:: azfs.AzFileClient.read_pickle

.. autofunction:: azfs.AzFileClient.read_json

pyspark-like method
-------------------

You can read multiple files, using multiprocessing or filters,

.. autofunction:: azfs.AzFileClient.read

put/upload
==========

.. autofunction:: azfs.AzFileClient.put

.. autofunction:: azfs.AzFileClient.write_csv

.. autofunction:: azfs.AzFileClient.write_table

.. autofunction:: azfs.AzFileClient.write_pickle

.. autofunction:: azfs.AzFileClient.write_json


file enumerating
================

.. autofunction:: azfs.AzFileClient.ls

.. autofunction:: azfs.AzFileClient.glob

.. autofunction:: azfs.AzFileClient.exists

file manipulating
=================


.. autofunction:: azfs.AzFileClient.info

.. autofunction:: azfs.AzFileClient.rm

.. autofunction:: azfs.AzFileClient.cp



TableStorage
************


.. autoclass:: azfs.TableStorage

.. autoclass:: azfs.TableStorageWrapper


BlobPathDecoder
***************


.. autoclass:: azfs.BlobPathDecoder
