from transliterate import slugify
import re

def slug_generator_title(title):
    slug = title.lower()
    if bool(re.search('[a-zA-Z]', slug)):
        slug = slugify(slug)
    else:
        slug = slug.replace(" ", "-")
    return slug

