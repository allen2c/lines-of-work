title = "Block Storage (NCS-EBS) and Filesystem Issues"

content = """
- EBS volume types: gp3 (default, 3000 IOPS baseline, 125 MB/s baseline), io2 (provisioned IOPS, up to 64,000), st1 (throughput-optimized HDD), sc1 (cold HDD).
- A gp3 volume that needs more than 3000 IOPS must have its provisioned IOPS explicitly raised; baseline does not auto-scale.
- `VolumeInUse` errors during detach usually mean a customer-initated mount inside the OS is holding the device; ask the customer to `umount` first.
- For `I/O exceeded` events, the top three causes are: undersized volume, instance bandwidth cap (varies by instance family), or an application-level retry storm.
- Snapshot copy between regions is async and can take from minutes to hours; do not promise a specific ETA, only that copy starts within 5 minutes of API call.
"""  # noqa: E501

version = "0.0.1"
