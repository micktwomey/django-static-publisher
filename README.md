# django-static-publisher

Publish your Django site statically

# How it Works

You develop your Django site as normal, using admin and runserver to view and edit content. You can even deploy it somewhere.

You create `static_publish.py` files with patterns specifying how to query for content and which views to use to render it. These are very similar to URL patterns

You then run `python manage.py static_publish /some/destination/folder` to walk over your content and write it out to the specified folder as HTML. Your static files will also be collected and written to the destination.

# Settings

## `STATIC_PUBLISHER_EXTRA_PATTERN_MODULES`

Default: `[]`

Add extra modules to import and search for static publish patterns.

Example:
```python
STATIC_PUBLISHER_EXTRA_MODULES = ["myblog.static_publish"]
```
