from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

TRACKERS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", 
    "gclid", "gclsrc", "fbclid", "fb_action_ids", "fb_action_types",
    "t", "s", "tag", "ref_", "_encoding", "psc", "msclkid",
    "_r", "is_copy_url", "is_from_webapp", "mc_cid", "mc_eid"
}

def clean_url(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    cleaned = {
        k: v for k, v in params.items()
        if k not in TRACKERS
    }

    new_query = urlencode(cleaned, doseq=True)

    return urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        new_query,
        parsed.fragment
    ))