title = "PCI DSS Compliance Basics"

content = """
Merchants who store, process, or transmit cardholder data must comply with the
Payment Card Industry Data Security Standard (PCI DSS). Nordstern assists
merchants in understanding their obligations.

**Scope Reduction:** The most effective approach is to avoid handling card data
directly. Use hosted payment pages, tokenization, or payment links so that
card data never touches the merchant's systems. This significantly reduces
PCI scope, often to a simple self-assessment questionnaire (SAQ A).

**SAQ Levels:** Depending on integration method, merchants complete different
SAQs. SAQ A: fully outsourced, no card data. SAQ A-EP: e-commerce with
JavaScript redirect, no card data stored. SAQ D: merchants with direct
card handling — most comprehensive and burdensome.

**Annual Requirements:** Most merchants must complete an annual self-assessment
and possibly a quarterly network scan by an approved vendor if they have
external-facing IPs. Nordstern may request proof of compliance as part of
merchant agreements.

**Breach Implications:** Non-compliance increases breach risk. Breaches
involving card data can result in fines, chargebacks, and scheme penalties.
Merchants must report suspected breaches immediately.
"""  # noqa: E501

version = "0.0.1"
