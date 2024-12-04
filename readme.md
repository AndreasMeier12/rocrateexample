# RO-Crate example with schema

This is a small example of an ro crate with a RDFS schema expressed in JSON-LD.  
It is intended for discussion purposes, it is not canonical.

To build the RO-Crate, execute `ro-crate-metadata-export-test/create.sh` from this directory.

To check that it can be read in, run `ro-crate-metadata-export-test/open.py` from this directory,
this requires the library `rocrate`, it's specified
in requirements.txt.

`ro-crate-metadata` contains the proposed implementation of the metadata and their schema in RO
Crate metadata.

`reference-openbis-export` contains an example of an export from openBIS, the metadata and schema is
in `reference-openbis-export/metadata.xlsx`. `reference-openbis-export/data` contains two example
data sets. The keys and types of the dataset are encoded in the directory name of each data set.

`ro-crate-metadata-export-test` has scripts for creating and reading the RO Crate.