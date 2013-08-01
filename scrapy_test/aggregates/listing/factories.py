from scrapy_test.aggregates.listing.models import Listing


def construct_listing(url, title, description, listing_source):
  listing = Listing(url=url, title=title, description=description, listing_source=listing_source)
  listing.set_requires_sanity_checking()
  return listing
