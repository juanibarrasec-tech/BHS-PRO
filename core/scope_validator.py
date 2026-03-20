import re
from urllib.parse import urlparse

ALLOWED_DOMAINS = [r".*\.example\.com$", r"hackerone\.com"]

def is_in_scope(url):
    hostname = urlparse(url).hostname or url
    return any(re.match(pattern, hostname) for pattern in ALLOWED_DOMAINS)
