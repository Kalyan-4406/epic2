def generate_adr(report):
    return f"""
# ADR-001

## Context
Automated documentation generation.

## Decision
Use CI-based doc generation.

## Status
Accepted

## Commit
{report['context']['commit_sha']}
"""
