"""HTML components mirroring the reference site's section types.

All internal links are written as "@/path/" and resolved to relative paths per page at
build time, so the output works both from a local server and by double-clicking files.
"""
from html import escape

IMG_EXT = "svg"  # switch to "jpg" once real photos are dropped into site/img/

ORG = {
    "name": "Karama",
    "tagline": "Dignity Through Opportunity",
    "address_1": "Masjid Sabour",
    "address_2": '<span class="todo">Street address</span>',
    "city": '<span class="todo">City, State ZIP</span>',
    "phone": '<span class="todo">(000) 000-0000</span>',
    "email": '<span class="todo">info@karama.org</span>',
    "pantry_hours": '<span class="todo">Pantry days and hours</span>',
    "office_hours": '<span class="todo">Office hours</span>',
    "ein": '<span class="todo">EIN</span>',
}

CHEV = '<svg class="chev" aria-hidden="true" viewBox="0 0 13 22"><path d="M9 11 .4 2.4A1.4 1.4 0 0 1 2.4.4L12.9 11 2.4 21.4a1.4 1.4 0 0 1-2-2Z"/></svg>'
CHEV_SM = '<svg aria-hidden="true" viewBox="0 0 13 22"><path d="M9 11 .4 2.4A1.4 1.4 0 0 1 2.4.4L12.9 11 2.4 21.4a1.4 1.4 0 0 1-2-2Z"/></svg>'

LOGO_MARK = """<svg class="mark" viewBox="0 0 80 80" aria-hidden="true">
<circle cx="40" cy="40" r="38" fill="#fff" stroke="#fad42f" stroke-width="4"/>
<path d="M40 12c6 10 16 15 24 15-2 18-12 30-24 36-12-6-22-18-24-36 8 0 18-5 24-15z" fill="#0044b5"/>
<path d="M40 25c3.5 5.5 9 8.5 14 8.5-1.2 10-7 17-14 20-7-3-12.8-10-14-20 5 0 10.5-3 14-8.5z" fill="#ffba00"/>
<path d="M22 60c10 7 26 7 36 0" stroke="#21296b" stroke-width="4" fill="none" stroke-linecap="round"/>
</svg>"""


def img(name, alt=""):
    return f'<img src="@/img/{name}.{IMG_EXT}" alt="{escape(alt)}" loading="lazy">'


def logo(tag="a"):
    return (f'<a class="logo" href="@/" aria-label="Karama home">{LOGO_MARK}'
            f'<span class="word">Karama<small>{ORG["tagline"]}</small></span></a>')


# ---------------------------------------------------------------- navigation data
MEGA = {
    "Our Impact": {
        "href": "@/our-impact/",
        "intro": "Five programs that help neighbors learn, earn, settle in and eat well.",
        "cols": [
            ("English Literacy", "@/our-impact/english-literacy/", [
                ("ESL Classes", "@/our-impact/english-literacy/esl-classes/"),
                ("Adult Literacy", "@/our-impact/english-literacy/adult-literacy/"),
                ("Conversation Circles", "@/our-impact/english-literacy/conversation-circles/")]),
            ("Financial Literacy", "@/our-impact/financial-literacy/", [
                ("Budgeting & Banking", "@/our-impact/financial-literacy/budgeting-and-banking/"),
                ("Credit & Debt", "@/our-impact/financial-literacy/credit-and-debt/"),
                ("Free Tax Help", "@/our-impact/financial-literacy/free-tax-help/")]),
            ("Immigration Support", "@/our-impact/immigration-support/", [
                ("Know Your Rights", "@/our-impact/immigration-support/know-your-rights/"),
                ("Citizenship Prep", "@/our-impact/immigration-support/citizenship-prep/"),
                ("Legal Referrals", "@/our-impact/immigration-support/legal-referrals/")]),
            ("Vocational Training", "@/our-impact/vocational-training/", [
                ("Job Readiness", "@/our-impact/vocational-training/job-readiness/"),
                ("Career Training", "@/our-impact/vocational-training/career-training/"),
                ("Employer Partners", "@/our-impact/vocational-training/employer-partners/")]),
            ("Food Pantry", "@/our-impact/food-pantry/", [
                ("Visit the Pantry", "@/our-impact/food-pantry/visit-the-pantry/"),
                ("Donate Food", "@/our-impact/food-pantry/donate-food/")]),
        ],
    },
    "In Your Community": {
        "href": "@/in-your-community/",
        "intro": "Karama is rooted at Masjid Sabour and open to every neighbor.",
        "cols": [
            ("Meeting Local Needs", "@/in-your-community/meeting-local-needs/", []),
            ("Heritage Months", "@/in-your-community/heritage-months/", []),
            ("Masjid Sabour", "@/in-your-community/masjid-sabour/", []),
            ("Community Events", "@/events/", []),
        ],
    },
    "How You Can Help": {
        "href": "@/how-you-can-help/",
        "intro": "Give, volunteer, partner or speak up. Every kind of help counts.",
        "cols": [
            ("Why Donate?", "@/how-you-can-help/why-donate/", [
                ("Make a Gift", "@/how-you-can-help/why-donate/make-a-gift/"),
                ("Zakat & Sadaqah", "@/how-you-can-help/why-donate/zakat-and-sadaqah/"),
                ("Plan Your Gift", "@/how-you-can-help/why-donate/plan-your-gift/")]),
            ("Why Volunteer?", "@/how-you-can-help/why-volunteer/", [
                ("Host a Drive", "@/how-you-can-help/host-a-drive/")]),
            ("Partner With Us", "@/how-you-can-help/partner-with-us/", [
                ("Partner Resources", "@/how-you-can-help/partner-with-us/partner-resources/")]),
            ("Speak Out", "@/how-you-can-help/speak-out/", [
                ("Stay Informed", "@/news/")]),
        ],
    },
}

FOOTER_COLS = [
    ("About", [("Our History", "@/about/our-history/"), ("Our Mission and Values", "@/about/our-mission-and-values/"),
               ("Our Leadership", "@/about/leadership-team/"), ("Public Reporting", "@/about/public-reporting/"),
               ("Careers", "@/about/careers/")]),
    ("Newsroom", [("News", "@/news/"), ("Events", "@/events/"), ("Heritage Months", "@/in-your-community/heritage-months/")]),
    ("For Media", [("Contact", "@/about/contact/"), ("About Karama", "@/about/")]),
    ("More Resources", [("FAQ", "@/about/frequently-asked-questions/"), ("Get Involved", "@/how-you-can-help/"),
                        ("Need Help?", "@/need-help/"), ("Site Map", "@/sitemap/")]),
]

LANGS = [("en", "English"), ("ar", "العربية Arabic"), ("es", "Español Spanish"), ("so", "Soomaali Somali"),
         ("ur", "اردو Urdu"), ("fr", "Français French"), ("ps", "پښتو Pashto"), ("fa", "فارسی Dari/Farsi")]

SOCIAL = {
    "Facebook": '<path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.5 1.6-1.5h1.7V4.5a22 22 0 0 0-2.5-.1c-2.4 0-4.1 1.5-4.1 4.2v2.3H7.5V14h2.7v8z"/>',
    "Instagram": '<path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4Zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6Zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0ZM21.9 8c-.1-1.6-.4-3-1.6-4.2S17.6 2.2 16 2.1C14.3 2 9.7 2 8 2.1 6.4 2.2 5 2.5 3.8 3.7S2.2 6.4 2.1 8C2 9.7 2 14.3 2.1 16c.1 1.6.4 3 1.6 4.2S6.4 21.8 8 21.9c1.7.1 6.3.1 8 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.7.1-6.3 0-8Zm-2.2 10.3a3.3 3.3 0 0 1-1.9 1.9c-1.3.5-4.3.4-5.8.4s-4.5.1-5.8-.4a3.3 3.3 0 0 1-1.9-1.9c-.5-1.3-.4-4.3-.4-5.8s-.1-4.5.4-5.8a3.3 3.3 0 0 1 1.9-1.9C7.5 4.3 10.5 4.4 12 4.4s4.5-.1 5.8.4a3.3 3.3 0 0 1 1.9 1.9c.5 1.3.4 4.3.4 5.8s.1 4.5-.4 5.8Z"/>',
    "YouTube": '<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8ZM10 15V9l5.2 3Z"/>',
    "WhatsApp": '<path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.6.1a8 8 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.5 13.5 0 0 0 5.2 4.6c1.9.8 2.7.9 3.6.7a3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.1-.3-.2-.6-.3ZM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.3a8.3 8.3 0 0 1-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.3 8.3 0 1 1 12 20.3Z"/>',
}


def link_list(links):
    return "<ul>" + "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in links) + "</ul>"


def header(current_top=None):
    mega_items = []
    for label, m in MEGA.items():
        cols = "".join(
            f'<div class="mega-col"><h3><a href="{h}">{t}</a></h3>'
            + (link_list(subs) if subs else "")
            + "</div>" for t, h, subs in m["cols"])
        cur = ' aria-current="page"' if current_top == label else ""
        mega_items.append(
            f'<li class="has-mega"><a href="{m["href"]}" aria-haspopup="true" aria-expanded="false"{cur}>{label}</a>'
            f'<div class="mega"><div class="mega-inner"><div class="mega-intro"><h2>{label}</h2><p>{m["intro"]}</p>'
            f'<a class="btn" href="{m["href"]}">Learn More</a></div><div class="mega-cols">{cols}</div></div></div></li>')
    langs = "".join(f'<li><button type="button" data-lang="{c}">{n}</button></li>' for c, n in LANGS)
    return f"""<a class="skip" href="#main">Skip to main content</a>
<header class="site-header"><div class="bar">
  {logo()}
  <button class="menu-toggle" aria-expanded="false" aria-controls="navs"><span>Menu</span></button>
  <div class="navs" id="navs">
    <ul class="util">
      <li class="lang"><button class="lang-btn" type="button" aria-haspopup="true">Select Language
        <svg width="10" height="7" viewBox="0 0 10 7" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="2" fill="none"/></svg></button>
        <ul class="lang-menu">{langs}</ul><div id="gt" hidden></div></li>
      <li><a href="@/our-impact/food-pantry/visit-the-pantry/">Find the Food Pantry</a></li>
      <li><a href="@/news/">News</a></li>
      <li><a href="@/how-you-can-help/partner-with-us/">Partner With Us</a></li>
      <li><a class="btn" href="@/how-you-can-help/why-donate/make-a-gift/">Donate</a></li>
      <li><button class="search-btn" type="button" aria-label="Search"><svg viewBox="0 0 24 24"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg></button></li>
    </ul>
    <ul class="main-nav">
      {"".join(mega_items)}
      <li><a class="need-help" href="@/need-help/"{' aria-current="page"' if current_top == "Need Help" else ""}>Need Help?</a></li>
    </ul>
  </div>
</div></header>
<div class="search-overlay" role="dialog" aria-label="Search the site">
  <button class="close" type="button" aria-label="Close search">&times;</button>
  <form action="@/search/" method="get" role="search">
    <label class="sr" for="site-q">Search</label>
    <input id="site-q" name="q" type="search" placeholder="Search Karama (try “pantry” or “ESL”)">
    <button class="btn yellow" type="submit">Search</button>
  </form>
</div>"""


def footer():
    cols = "".join(f'<div class="col"><h2>{h}</h2>{link_list(links)}</div>' for h, links in FOOTER_COLS)
    social = "".join(f'<a href="#" aria-label="{n} (link coming soon)"><svg viewBox="0 0 24 24">{p}</svg></a>' for n, p in SOCIAL.items())
    return f"""<footer class="site-footer"><div class="inner">
  <div class="top">{logo()}<div class="social"><span>Follow us</span>{social}</div></div>
  <div class="cols">
    <div><address><p>Karama<br>at {ORG["address_1"]}</p><p>{ORG["address_2"]}<br>{ORG["city"]}</p><p>{ORG["phone"]}<br>{ORG["email"]}</p></address></div>
    {cols}
  </div>
  <div class="legal"><span>&copy; <span data-year>2026</span> Karama. A 501(c)(3) nonprofit organization, {ORG["ein"]}.</span>
    <span><a href="@/about/privacy-policy/">Privacy Policy</a><a href="@/about/terms/">Terms</a><a href="@/about/accessibility/">Accessibility</a></span></div>
</div></footer>"""


# ---------------------------------------------------------------- section components
def home_hero(title, text, btn, image, alt):
    return f"""<section class="home-hero" aria-label="Welcome">
  <div class="arc" aria-hidden="true"></div>
  <div class="photo">{img(image, alt)}</div>
  <div class="text reveal"><h1>{title}</h1><p>{text}</p><a class="btn" href="{btn[1]}">{btn[0]}</a></div>
</section>"""


def landing_hero(title, text, image=None, eyebrow="", crumbs=None, ctas=None):
    crumb = ""
    if crumbs:
        crumb = '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(
            f'<a href="{u}">{t}</a>' for t, u in crumbs) + "</nav>"
    cta = ""
    if ctas:
        cta = '<div class="ctas">' + "".join(f'<a class="btn {c}" href="{u}">{t}</a>' for t, u, c in ctas) + "</div>"
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    photo = f'<div class="photo">{img(image)}</div>' if image else ""
    cls = "landing-hero" + ("" if image else " plain")
    return f'<section class="{cls}"><div class="text">{crumb}{eb}<h1>{title}</h1><p>{text}</p>{cta}</div>{photo}</section>'


def secnav(label, items, current):
    cur = ' aria-current="page"'
    lis = "".join(f'<li><a href="{u}"{cur if u == current else ""}>{t}</a></li>' for t, u in items)
    return (f'<nav class="secnav" aria-label="{escape(label)} pages"><button class="toggle" type="button" aria-expanded="false">'
            f'{escape(label)} <span aria-hidden="true">☰</span></button><ul>{lis}</ul></nav>')


def rich(html, wide=False):
    return f'<section class="rich"><div class="wrap"><div class="inner{" wide" if wide else ""} reveal">{html}</div></div></section>'


def sec_head(title, desc="", btn=None, tag="h2"):
    b = f'<a class="btn" href="{btn[1]}">{btn[0]}</a>' if btn else ""
    d = f"<p>{desc}</p>" if desc else ""
    return f'<div class="sec-head reveal"><div><{tag}>{title}</{tag}>{d}</div>{b}</div>'


def stats(title, text, items):
    rows = "".join(f'<div class="stat reveal"><div class="num">{n}</div><p>{t}</p></div>' for n, t in items)
    return (f'<section class="stats"><div class="shape" aria-hidden="true"></div><div class="wrap">'
            f'<div class="intro reveal"><h2>{title}</h2><p>{text}</p></div><div>{rows}</div></div></section>')


def acards(title, cards, btn=None, desc=""):
    cs = "".join(f'<a class="acard reveal" href="{c["href"]}"><div class="img">{img(c["img"])}</div>'
                 f'<div class="cat">{c["cat"]}</div><div class="title">{c["title"]}</div>'
                 + (f'<div class="meta">{c["meta"]}</div>' if c.get("meta") else "") + "</a>" for c in cards)
    return f'<section class="sec"><div class="wrap">{sec_head(title, desc, btn)}<div class="acards">{cs}</div></div></section>'


def feature(title, text, btn, image, eyebrow="", variant="", reverse=False):
    cls = " ".join(x for x in ["feature", variant, "reverse" if reverse else ""] if x)
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    b = f'<div><a class="btn white" href="{btn[1]}">{btn[0]}</a></div>' if btn else ""
    return f'<section class="{cls}"><div class="photo">{img(image)}</div><div class="panel reveal">{eb}<h2>{title}</h2><p>{text}</p>{b}</div></section>'


def icp(title, desc, panes):
    tabs = "".join(f'<li><button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}">{p["label"]}</button></li>'
                   for i, p in enumerate(panes))
    ps = "".join(f'<div class="pane{" active" if i == 0 else ""}" role="tabpanel"><div class="circle-photo">{img(p["img"])}</div>'
                 f'<div class="bubble"><div class="bubble-inner"><p>{p["text"]}</p><a class="chev-link" href="{p["href"]}">See how {CHEV_SM}</a></div></div></div>'
                 for i, p in enumerate(panes))
    return (f'<section class="icp"><div class="wrap"><div class="reveal"><h2>{title}</h2><p>{desc}</p>'
            f'<ul class="tabs" role="tablist">{tabs}</ul></div><div class="stage">{ps}</div></div></section>')


def mcards(title, cards, desc="", btn=None, cols=3):
    cls = {2: "mcards two", 3: "mcards", 4: "mcards four"}[cols]
    cs = "".join(f'<a class="mcard" href="{u}"><h3>{t}</h3><p>{d}</p>{CHEV}</a>' for t, d, u in cards)
    return f'<section class="sec"><div class="wrap">{sec_head(title, desc, btn)}<div class="{cls} reveal">{cs}</div></div></section>'


def featured(title, desc, big, side):
    def card(c):
        return (f'<a class="fa-card" href="{c["href"]}"><div class="img"><span class="tag">{c["cat"]}</span>{img(c["img"])}</div>'
                f'<div class="title">{c["title"]}</div></a>')
    return (f'<section class="sec"><div class="wrap">{sec_head(title, desc)}<div class="fa reveal"><div class="big">{card(big)}</div>'
            f'<div class="side">{"".join(card(c) for c in side)}</div></div></div></section>')


def signup():
    return """<section class="signup"><div class="wrap reveal">
  <h2>Stay Informed. Stay Involved.</h2>
  <p>Get Karama updates: class sign-ups, pantry news, events and ways to help.</p>
  <form data-local>
    <div><label for="su-first">First Name*</label><input id="su-first" type="text" required autocomplete="given-name"></div>
    <div><label for="su-last">Last Name*</label><input id="su-last" type="text" required autocomplete="family-name"></div>
    <div><label for="su-email">Email*</label><input id="su-email" type="email" required autocomplete="email"></div>
    <div><label for="su-zip">ZIP code*</label><input id="su-zip" type="text" required inputmode="numeric" autocomplete="postal-code"></div>
    <label class="consent"><input type="checkbox" required> I agree to Karama's Privacy Policy and want to get emails from Karama. I can unsubscribe at any time.</label>
    <div class="actions"><button class="btn white" type="submit">Sign Up</button></div>
    <div class="success" role="status">Thank you! You're on the list.</div>
  </form>
</div></section>"""


def fwcta(title, text, btns):
    b = "".join(f'<a class="btn {c}" href="{u}">{t}</a>' for t, u, c in btns)
    return f'<section class="fwcta"><div class="wrap reveal"><div><h2>{title}</h2><p>{text}</p></div><div class="btns">{b}</div></div></section>'


def single_stat(num, text):
    return f'<section class="single-stat"><div class="wrap reveal"><div class="num">{num}</div><p>{text}</p></div></section>'


def accordions(title, items, desc=""):
    ds = "".join(f'<details><summary>{q}</summary><div class="body">{a}</div></details>' for q, a in items)
    head = sec_head(title, desc) if title else ""
    return f'<section class="sec"><div class="wrap">{head}<div class="acc reveal">{ds}</div></div></section>'


def article_hero(cat, title, desc, by):
    return (f'<section class="article-hero"><div class="inner"><div class="eyebrow">{cat}</div><h1>{title}</h1>'
            f'<p>{desc}</p><div class="by">{by}</div><a class="btn" href="#share" data-share>Share This</a></div></section>')


def section(html, cls="sec"):
    return f'<section class="{cls}"><div class="wrap">{html}</div></section>'
