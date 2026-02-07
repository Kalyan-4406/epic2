def generate_api_docs(report):
    apis = []
    for c in report["changes"]:
        apis.extend(c["features"].get("api_endpoints", []))

    lines = ["# API Reference\n"]
    for api in apis:
        lines.append(f"- `{api}`")

    return "\n".join(lines)
