import os


def _psqlsearch_enabled() -> bool:
    plugins = os.environ.get("CKAN__PLUGINS", "")
    return "psqlsearch" in plugins.split()


if _psqlsearch_enabled():
    try:
        import ckan.lib.search as search
        import ckan.lib.search.common as search_common
    except Exception:
        pass
    else:
        search.check_solr_schema_version = lambda *args, **kwargs: None
        search.is_available = lambda: True
        search_common.is_available = lambda: True
