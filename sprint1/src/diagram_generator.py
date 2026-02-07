def system_diagram():
    return """
graph TD
Repo --> CI
CI --> Docs
"""

def sequence_diagram():
    return """
sequenceDiagram
Developer->>CI: Push Code
CI->>Docs: Generate
"""

def er_diagram():
    return """
erDiagram
REPO ||--o{ FILE : contains
FILE ||--o{ FUNCTION : defines
"""
