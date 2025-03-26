import requests

# match these
requests.get("semgrep.dev", timeout=30, verify=True)
requests.get("semgrep.dev", verify=True, timeout=10)

# but do not match these
requests.get("semgrep.dev", timeout=10)
requests.get("semgrep.dev", verify=True)
requests.get("semgrep.dev", verify=False, timeout=10)
requests.get("semgrep.dev", secure=True, timeout=10)
