# seminar_2_major_assignment documentation!

## Description

Seminar 2 Major Assignment

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `gsutil rsync` to recursively sync files in `data/` up to `gs://https://console.cloud.google.com/storage/browser/user-bucket-badereli-bc-edu-lsehd-datascience-buckets;tab=objects?forceOnBucketsSortingFiltering=true&project=lsehd-datascience-buckets/data/`.
* `make sync_data_down` will use `gsutil rsync` to recursively sync files in `gs://https://console.cloud.google.com/storage/browser/user-bucket-badereli-bc-edu-lsehd-datascience-buckets;tab=objects?forceOnBucketsSortingFiltering=true&project=lsehd-datascience-buckets/data/` to `data/`.


