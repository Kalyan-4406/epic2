def generate_tree(report):
    files = [c["file"] for c in report["changes"]]
    return "\n".join(files)
