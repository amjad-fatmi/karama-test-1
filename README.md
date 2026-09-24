# Karama website

Website for **Karama**, a nonprofit at Masjid Sabour offering free English/ESL classes, financial literacy, immigration support, vocational training, a community food pantry and heritage-month events.

## View it

Open `site/index.html` in a browser, or serve it locally:

```bash
python3 -m http.server 8090 --directory site
```

Then visit http://localhost:8090.

## Deploy

`netlify.toml` tells Netlify to publish the `site/` folder. No build step runs on Netlify, so run the build locally and commit `site/` before pushing.

## Edit and rebuild

Pages are generated from the files in `src/`:

| File | What it holds |
| --- | --- |
| `src/content.py` | Programs, news posts, events, heritage calendar |
| `src/components.py` | Contact details (`ORG`), navigation menus, footer, section templates |
| `src/build.py` | Every page's layout, plus the route checker |
| `src/art.py` | Placeholder illustrations |
| `src/assets/` | Styles and site behavior |

```bash
python3 src/build.py
```

The build writes the site to `site/` and then crawls it breadth-first from the homepage. It fails if any link is broken or any page can't be reached. The route table is saved to `routes.txt`.

## Before launch

- Fill in everything highlighted in yellow on the site: address, hours, phone, email, EIN, staff and class times.
- Replace the sample news posts and event dates.
- Connect the forms and donations to real services. Right now they only show a thank-you message.
- Swap the placeholder illustrations for real photos in `site/img/` and set `IMG_EXT` in `src/components.py`.
