title = "DNS, Private Hosted Zones, and Resolver Issues"

content = """
- NimbusCore DNS uses the `nc-dns.internal` resolver at the VPC base IP +2; customers often misconfigure to the public resolver `8.8.8.8` and lose private zone resolution.
- Private Hosted Zone association requires both a VPC association and the `enableDnsHostnames` and `enableDnsSupport` VPC attributes set to `true`.
- TTL behavior: SOA minimum TTL controls negative caching; if a customer complains that "old records keep coming back", check this value first.
- For split-horizon DNS, never recommend that a customer modify their own `/etc/hosts`; route them to the Private Hosted Zone pattern instead.
- DNSSEC is supported on public zones only; flag any request to enable it on a private zone as a configuration error.
"""  # noqa: E501

version = "0.0.1"
