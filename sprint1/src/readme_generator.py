def generate_readme(report):
    return f"""
# {report['context']['repository']}

## Overview
Auto-generated documentation based on code changes.

## Branch
{report['context']['branch']}

## Commit
{report['context']['commit_sha']}

## Severity
{report['analysis_summary']['highest_severity']}
"""
