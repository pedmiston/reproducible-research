import sys
from invoke import task
import pywikibot
import pandas

@task
def get(ctx, title, n_revisions=10, content=False, output_csv=None):
    """Get the last n revisions of a Wikipedia article by title."""
    site = pywikibot.Site('en', 'wikipedia')
    page = pywikibot.Page(site, title)
    revisions = page.revisions(content=content)
    records = [next(revisions).__dict__ for _ in range(n_revisions)]
    table = pandas.DataFrame.from_records(records)
    table.insert(0, 'title', title)
    table.to_csv(output_csv or sys.stdout, index=False)
