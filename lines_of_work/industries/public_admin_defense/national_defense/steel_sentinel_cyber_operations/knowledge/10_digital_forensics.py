title = "Digital Forensics Procedures"

content = """
Digital forensics in a military context must satisfy two simultaneous requirements:
preserve evidence to the standard required for potential legal proceedings, and
produce timely intelligence to support ongoing defensive operations. These objectives
can create tension; following documented procedures resolves it.

**Chain of Custody:** Every piece of digital evidence is assigned a unique case number.
The acquiring analyst completes a chain-of-custody form documenting: acquisition date
and time, the system acquired from, acquisition method, hash value of the acquired
image, and every individual who subsequently handles the evidence. Breaks in chain of
custody compromise legal admissibility.

**Acquisition Methods:** Acquire volatile memory (RAM) before powering down a suspect
system — volatile data is lost on shutdown and may contain encryption keys, running
processes, and network connection state. Disk images are acquired using write-blocking
hardware to prevent modification. Images are verified by comparing MD5 and SHA-256 hash
values of the source and the copy.

**Evidence Storage:** Forensic images are stored on encrypted, access-controlled storage
designated for case evidence. Images are not processed in place; analysts work from a
verified copy, never the original. Evidence storage is audited quarterly.

**Artifact Analysis:** Prioritize artifacts most likely to answer key investigative
questions: system event logs, security logs, prefetch files, browser history, email
artifacts, and recently accessed file lists. Memory analysis targets running processes,
injected code, and network sockets to reconstruct adversary activity.

**Reporting:** Forensic reports follow a structured format: executive summary, evidence
inventory, methodology, detailed findings, timeline of adversary activity, and analyst
conclusions. Reports are reviewed by a second analyst before release to ensure accuracy
and identify analytical gaps.
"""

version = "0.0.1"
