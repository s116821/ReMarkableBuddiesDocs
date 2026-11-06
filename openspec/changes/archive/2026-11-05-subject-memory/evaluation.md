# Focused memory-component evaluation

Primary sources inspected October 12, 2026. These are source/documentation
observations, not measured tablet performance or legal advice. No component was
installed or run. Source availability does not establish native suitability.

| Candidate | Observed capabilities and dependencies | Fit decision |
| --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0/tree/d26ba5e4518cef7fff3c66d4f715b21adf9feabe) | Apache-2.0; Python/TypeScript libraries and self-hosted option; memory add/search and user scope. The basic library needs an LLM and embeddings, with configurable providers. README distinguishes managed benchmark optimizations from the OSS SDK. | Evaluate first as required. A future optional replaceable extraction/retrieval adapter is possible. Its own persistence/runtime is not the offline tablet authority; neither managed benchmarks nor setup examples prove our preservation/conflict/forget contract. |
| [Graphiti](https://github.com/getzep/graphiti/tree/0a3b1711b018e5590cf5c44a3ee3e67d6733ee13) | Apache-2.0; temporal facts, episode provenance and hybrid retrieval. Requires Python and a supported graph backend; inference/embedding providers are configurable, including compatible local servers. README warns about structured-output reliability. | Useful temporal/provenance reference and possible optional backend. An additional graph/model runtime would require independent deployment, bounds and measured effectiveness evidence; do not make it a default dependency. |

Both repositories had recent upstream commits (October 12 and October 11,
respectively) when inspected. This indicates current activity, not a maintenance
guarantee. No upstream code is copied or vendored by this decision.

Initial implementation decision: explicit portable facts over the existing Store,
with deterministic bounded lexical retrieval and independent confidence/provenance
fields. This is an engineering inference from the offline/storage constraints,
not evidence that lexical retrieval matches semantic embeddings. Evaluate actual
term relevance, contradiction handling and disabled behavior in production-facing
calls. Derived search state is rebuildable; canonical records and tombstones stay
in the existing generic engine. More capable retrieval can replace the domain
query boundary after bounded, representative evidence.

[remarkable-mcp](https://github.com/praveensehgal/remarkable-mcp) and
[reMark](https://github.com/BGGBTAC/reMark) remain the issue's ingestion and tablet
normalization references. They do not select the memory architecture or authorize
tablet ingestion. Source-document normalization/research is a separate capability.
