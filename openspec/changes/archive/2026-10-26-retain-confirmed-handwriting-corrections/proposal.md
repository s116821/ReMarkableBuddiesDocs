# Why

Generic Store supports the Handwriting namespace, but the application has no
typed confirmed-correction domain. A canceled or uncertain recognition must not
quietly become learning data. Explicit typed corrections are a distinct unfinished
product requirement, independent of the proposed large-notebook schemas.

# What changes

Add a small offline domain/provider and one-shot command for deliberately
confirming, inspecting, querying and invalidating image/text correction pairs.
Retain exact sample bytes, original interpretation, confirmed replacement and
asserted provenance in existing Store/CAS/operation/media primitives. Restrict
the first implementation to local ordinary mode. Preserve unsupported data and
refuse selected/sync activation rather than imply domain compatibility.

Use the existing Handwriting namespace/domain version 1 only for an explicitly
discriminated new payload. Domain ownership and complete precode review precede
implementation. No Source3/Conversation3 allocation, native hook, recognition
call, model training, automatic learning or Manager interface is included.

# Evidence and limits

Current Source9be88628 has generic namespace support but no handwriting module;
current open PRs cover other Reader/memory/native work and remain preserved.
Central Docs basea14df94 includes the delivered research consumer; the notebook
candidate remains separately frozen at970489e. No empty enum space is treated as
an ownership reservation. No inference/accuracy/native claim follows from durable
storage of a user assertion. This is one future paired implementation delivery,
not a planning-only merge or completion of the full learning capability.
