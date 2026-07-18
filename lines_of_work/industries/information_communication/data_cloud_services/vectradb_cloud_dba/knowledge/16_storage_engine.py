title = "Storage Layout and IO Tuning"

content = """
- PostgreSQL: separate volumes for PGDATA (NVMe, 3000 IOPS, 125 MB/s baseline, burst to 3000 MB/s), pg_wal (NVMe, dedicated), and pg_backup (staging before S3 upload). random_page_cost 1.1, effective_io_concurrency 200, shared_buffers 25 percent of RAM, work_mem 64 MB, maintenance_work_mem 2 GB.
- MySQL: innodb_buffer_pool_size 70 percent of RAM, innodb_log_file_size 4 GB, innodb_flush_log_at_trx_commit 2 (paired with semisync to avoid loss), innodb_io_capacity 2000.
- MongoDB: WiredTiger cache 50 percent of RAM, storage.wiredTiger.collectionConfig.blockCompressor snappy.
- ClickHouse: max_server_memory_usage 80 percent of RAM, merges_mutations_memory_usage_soft_limit 4 GB per cluster tier.
"""  # noqa: E501

version = "0.0.1"
