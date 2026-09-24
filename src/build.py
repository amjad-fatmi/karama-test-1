"""Build the Karama site into ../site, then crawl it breadth-first to prove every
route is reachable from the homepage and every internal link resolves.

    python3 src/build.py
"""
import json
import os
import re
import shutil
import sys
from collections import deque
from datetime import date
from html import escape, unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import art  # noqa: E402
from components import (ORG, CHEV_SM, accordions, acards, article_hero, featured, feature, footer, fwcta,  # noqa: E402
                        header, home_hero, icp, img, landing_hero, mcards, rich, sec_head, secnav, section,
                        signup, single_stat, stats)
from content import EVENTS, HERITAGE, NEWS, PROGRAMS, T  # noqa: E402

SRC = Path(__file__).parent
OUT = SRC.parent / "site"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@700&family=Palanquin+Dark:wght@600&family=Palanquin:wght@400;700&display=swap" rel="stylesheet">')

PAGES = []  # (path, title, desc, top_section, body_html, body_class)


def page(path, title, desc, body, top=None, cls=""):
    PAGES.append({"path": path, "title": title, "desc": desc, "top": top, "body": body, "cls": cls})


def u(path):
    return "@/" + path


# ================================================================== HOME
home = home_hero(
    "Karama Is Dignity Through Opportunity",
    "Karama brings neighbors together to learn, earn and belong. We teach English, build money skills, guide newcomers, train people for good jobs and keep our food pantry at Masjid Sabour stocked for every family.",
    ("Learn More", u("about/")), "community", "Neighbors at a Karama community event")
home += stats("Karama Is a Community Built on Dignity",
              "We bring people and resources together so every family has a fair start.",
              [("5", "core programs, from English classes to our food pantry"),
               ("$0", "cost to families for every Karama class and service"),
               ("All", "faiths, backgrounds and languages are welcome here")])
home += acards("Karama News", [
    {"href": u(f"news/{n['slug']}/"), "img": n["img"], "cat": n["cat"], "title": n["title"]} for n in NEWS[:3]],
    btn=("More News Stories", u("news/")))
home += feature("Food for Every Family",
                "Our pantry at Masjid Sabour offers groceries, including halal options, to anyone who needs them. No one is turned away.",
                ("Visit the Pantry", u("our-impact/food-pantry/visit-the-pantry/")), "pantry", eyebrow="Food Pantry", reverse=True)
home += icp("Our Impact", "Every day, we're working to help our neighbors thrive.",
            [{"label": p["label"], "img": p["img"], "text": p["bubble"], "href": u(f"our-impact/{p['slug']}/")} for p in PROGRAMS])
home += mcards("What You Can Do", [
    ("Donate Now", "Your gift keeps every class free and every pantry shelf full.", u("how-you-can-help/why-donate/make-a-gift/")),
    ("Volunteer Locally", "Tutor English, sort food, coach job seekers or help at events.", u("how-you-can-help/why-volunteer/")),
    ("Share Your Voice", "Speak up for newcomers, fair opportunity and food security.", u("how-you-can-help/speak-out/"))],
    desc="Take action and make a difference!", btn=("More You Can Do", u("how-you-can-help/")))
home += featured("Uniting for Action", "Together, we're creating opportunities so everyone can thrive.",
                 {"href": u(f"news/{NEWS[4]['slug']}/"), "img": NEWS[4]["img"], "cat": "Community", "title": NEWS[4]["title"]},
                 [{"href": u(f"news/{n['slug']}/"), "img": n["img"], "cat": "Guide", "title": n["title"]} for n in (NEWS[1], NEWS[5])])
home += signup()
page("", "Karama | Dignity Through Opportunity",
     "Karama is a nonprofit offering free English classes, financial literacy, immigration support, job training and a food pantry at Masjid Sabour.",
     home, cls="home")


# ================================================================== OUR IMPACT
impact_nav = [("Overview", u("our-impact/"))] + [(p["label"], u(f"our-impact/{p['slug']}/")) for p in PROGRAMS]
body = landing_hero("Our Impact", "Five programs that work together to help families learn, earn, settle in and eat well.",
                    "classroom", eyebrow="What We Do", crumbs=[("Home", u(""))])
body += secnav("Our Impact", impact_nav, u("our-impact/"))
body += rich("""<p>Karama means <em>dignity</em>. We believe every person deserves the tools to care for their family and take part in their community. Our programs are free, open to everyone and built around real life, so a family that comes for groceries can also find an English class, a budgeting workshop or a job coach.</p>""")
body += stats("One Door, Many Paths", "Most families connect with more than one program. That's by design.",
              [("5", "programs under one roof at Masjid Sabour"), ("$0", "cost to participants"), ("1", "simple form to get started")])
body += icp("Explore Our Programs", "Pick a program to learn more.",
            [{"label": p["label"], "img": p["img"], "text": p["bubble"], "href": u(f"our-impact/{p['slug']}/")} for p in PROGRAMS])
body += mcards("Get Started", [
    ("Need Help?", "Tell us what you need and we'll connect you with the right program.", u("need-help/")),
    ("Volunteer", "Share your time and skills with families in our community.", u("how-you-can-help/why-volunteer/")),
    ("Give", "Fund classes, groceries and job training for neighbors.", u("how-you-can-help/why-donate/"))])
body += fwcta("Every Gift Opens a Door", "Books, groceries, training supplies and more. Your support keeps every program free.",
              [("Donate", u("how-you-can-help/why-donate/make-a-gift/"), "yellow")])
body += signup()
page("our-impact/", "Our Impact | Karama", "Karama's five programs: English literacy, financial literacy, immigration support, vocational training and food pantry.", body, "Our Impact")

for p in PROGRAMS:
    base = f"our-impact/{p['slug']}/"
    pnav = [("Overview", u(base))] + [(s["label"], u(base + s["slug"] + "/")) for s in p["subs"]]
    body = landing_hero(p["title"], p["text"], p["img"], eyebrow=p["label"],
                        crumbs=[("Home", u("")), ("Our Impact", u("our-impact/"))])
    body += secnav(p["label"], pnav, u(base))
    body += rich(p["intro"])
    ft, fx, fimg, fvar = p["feature"]
    body += feature(ft, fx, None, fimg, eyebrow=p["label"], variant=fvar or "")
    body += mcards(f"Explore {p['label']}", [(s["label"], s["text"], u(base + s["slug"] + "/")) for s in p["subs"]],
                   cols=len(p["subs"]) if len(p["subs"]) in (2, 3, 4) else 3)
    body += accordions("Common Questions", p["faqs"])
    body += fwcta("Ready to Get Started?", "It only takes a few minutes. Tell us what you need and a Karama team member will reach out.",
                  [("Sign Up", u("need-help/#intake"), "yellow"), ("Volunteer", u("how-you-can-help/why-volunteer/"), "white")])
    body += signup()
    page(base, f"{p['label']} | Karama", p["text"], body, "Our Impact")

    for s in p["subs"]:
        path = base + s["slug"] + "/"
        body = landing_hero(s["title"], s["text"], s["img"], eyebrow=p["label"],
                            crumbs=[("Home", u("")), ("Our Impact", u("our-impact/")), (p["label"], u(base))])
        body += secnav(p["label"], pnav, u(path))
        body += rich(s["body"])
        others = [x for x in p["subs"] if x is not s]
        body += mcards("Related", [(x["label"], x["text"], u(base + x["slug"] + "/")) for x in others]
                       + [("Back to " + p["label"], "See the full program overview.", u(base))],
                       cols=len(others) + 1 if len(others) + 1 in (2, 3, 4) else 3)
        body += signup()
        page(path, f"{s['title']} | Karama", s["text"], body, "Our Impact")


# ================================================================== IN YOUR COMMUNITY
comm_nav = [("Overview", u("in-your-community/")), ("Meeting Local Needs", u("in-your-community/meeting-local-needs/")),
            ("Heritage Months", u("in-your-community/heritage-months/")), ("Masjid Sabour", u("in-your-community/masjid-sabour/")),
            ("Events", u("events/"))]
body = landing_hero("In Your Community", "Karama is rooted at Masjid Sabour and open to every neighbor, whatever their faith, background or first language.",
                    "community", eyebrow="Local", crumbs=[("Home", u(""))])
body += secnav("In Your Community", comm_nav, u("in-your-community/"))
body += rich("""<p>Our community is made of families from all over the world. Some arrived last month; some have been here for generations. Karama exists so that everyone can find help, share their gifts and feel at home.</p>""")
body += feature("Built Around Every Culture", "Each month we build an event around a community in our area, with food, music and stories, planned together with neighbors.",
                ("Heritage Months", u("in-your-community/heritage-months/")), "heritage", eyebrow="Heritage Nights", variant="navy")
body += mcards("Explore", [
    ("Meeting Local Needs", "How Karama listens to neighbors and responds.", u("in-your-community/meeting-local-needs/")),
    ("Masjid Sabour", "Our home base, and a welcoming place for all.", u("in-your-community/masjid-sabour/")),
    ("Community Events", "Workshops, fairs, heritage nights and drives.", u("events/"))])
body += signup()
page("in-your-community/", "In Your Community | Karama", "Karama at Masjid Sabour: local needs, heritage months and community events.", body, "In Your Community")

body = landing_hero("Meeting Local Needs", "We listen first, then build programs around what neighbors tell us they need.", "volunteers",
                    eyebrow="In Your Community", crumbs=[("Home", u("")), ("In Your Community", u("in-your-community/"))])
body += secnav("In Your Community", comm_nav, u("in-your-community/meeting-local-needs/"))
body += rich(f"""<h2>How We Decide What to Offer</h2>
<p>Karama's programs grew out of real conversations: parents who wanted to talk with their children's teachers, workers who wanted better jobs, families who needed groceries to get through the month.</p>
<ul><li><strong>We ask.</strong> Surveys, listening sessions and everyday conversations at the pantry.</li><li><strong>We partner.</strong> We work with schools, employers, clinics and other nonprofits instead of starting from scratch.</li><li><strong>We follow up.</strong> We check in with families to learn what worked.</li></ul>
<p>{T("Add a short local needs summary or data your team has collected.")}</p>""")
body += single_stat("1", "simple intake form connects a family with every Karama program they need.")
body += mcards("Take the Next Step", [("Need Help?", "Tell us what you need.", u("need-help/")),
                                      ("Partner With Us", "Bring your organization to the table.", u("how-you-can-help/partner-with-us/")),
                                      ("Volunteer", "Lend a hand where it matters.", u("how-you-can-help/why-volunteer/"))])
page("in-your-community/meeting-local-needs/", "Meeting Local Needs | Karama", "How Karama listens to neighbors and builds programs around real needs.", body, "In Your Community")

months = "".join(f'<div class="month reveal"><div class="m">{m}</div><h3>{t}</h3><p>{d}</p></div>' for m, t, d in HERITAGE)
body = landing_hero("Heritage Months", "Each month, we build an evening around a community in our area. Everyone is invited to learn, eat and celebrate together.",
                    "heritage", eyebrow="In Your Community", crumbs=[("Home", u("")), ("In Your Community", u("in-your-community/"))])
body += secnav("In Your Community", comm_nav, u("in-your-community/heritage-months/"))
body += rich("""<p>Karama's heritage nights celebrate the many cultures that make up our neighborhood. Community members plan the menu, music and program. Events are free, family-friendly and open to all.</p>""")
body += section(sec_head("Our Heritage Calendar", "Dates are announced on the Events page.", ("See Events", u("events/"))) + f'<div class="months">{months}</div>')
body += fwcta("Want to Plan a Heritage Night?", "Tell us about your community and your idea. We'll help with space, promotion and volunteers.",
              [("Propose an Event", u("about/contact/"), "yellow")])
body += signup()
page("in-your-community/heritage-months/", "Heritage Months | Karama", "Karama's year-round calendar of heritage nights and community celebrations.", body, "In Your Community")

body = landing_hero("Masjid Sabour", "Karama's home base, and a welcoming place for neighbors of every faith.", "masjid",
                    eyebrow="In Your Community", crumbs=[("Home", u("")), ("In Your Community", u("in-your-community/"))])
body += secnav("In Your Community", comm_nav, u("in-your-community/masjid-sabour/"))
body += rich(f"""<h2>Visit Us</h2>
<dl><dt>Address</dt><dd>{ORG["address_1"]}<br>{ORG["address_2"]}<br>{ORG["city"]}</dd><dt>Pantry hours</dt><dd>{ORG["pantry_hours"]}</dd><dt>Office hours</dt><dd>{ORG["office_hours"]}</dd><dt>Phone</dt><dd>{ORG["phone"]}</dd></dl>
<h2>Getting Here</h2><p>{T("Parking, bus lines and accessible entrance details.")}</p>
<h2>Everyone Is Welcome</h2><p>You do not need to be Muslim to use any Karama program. Our volunteers are glad to explain anything about the building or its customs so that every guest feels comfortable.</p>""")
body += signup()
page("in-your-community/masjid-sabour/", "Masjid Sabour | Karama", "Visit Karama at Masjid Sabour: address, hours and directions.", body, "In Your Community")


# ================================================================== EVENTS
chips = '<div class="chips" data-filter-for="event-list"><button class="chip" aria-pressed="true" data-value="">All</button>' + "".join(
    f'<button class="chip" aria-pressed="false" data-value="{c}">{c}</button>' for c in sorted({e[1] for e in EVENTS})) + "</div>"
rows = ""
for d, cat, title, time, where, desc in EVENTS:
    dt = date.fromisoformat(d)
    rows += (f'<article class="ev" data-cat="{cat}"><div class="date"><span class="m">{dt.strftime("%b")}</span><span class="d">{dt.day}</span></div>'
             f'<div><div class="cat">{cat}</div><h3>{title}</h3><p>{desc}</p><div class="where">{dt.strftime("%A")} · {time} · {where}</div></div>'
             f'<a class="btn" href="#rsvp" data-rsvp="{escape(title)}">RSVP</a></article>')
opts = "".join(f"<option>{escape(e[2])}</option>" for e in EVENTS)
body = landing_hero("Events", "Workshops, heritage nights, job fairs and food drives. All Karama events are free and open to everyone.",
                    "heritage", eyebrow="Community Calendar", crumbs=[("Home", u(""))])
body += section(sec_head("Upcoming Events", f"Sample schedule. {T('Replace with confirmed dates.')}") + chips
                + f'<div class="ev-list" id="event-list" data-filter-list>{rows}</div><p class="empty" data-empty-for="event-list" hidden>No events in this category right now.</p>')
body += section(sec_head("RSVP", "Let us know you're coming so we can plan food and seating.")
                + f"""<div class="form-block" id="rsvp"><form data-local><div class="form-grid">
<div class="full"><label for="rsvp-event">Event</label><select id="rsvp-event">{opts}</select></div>
<div><label for="rsvp-name">Name</label><input id="rsvp-name" required autocomplete="name"></div>
<div><label for="rsvp-contact">Phone or email</label><input id="rsvp-contact" required></div>
<div><label for="rsvp-n">How many people?</label><input id="rsvp-n" type="number" min="1" value="1"></div>
<div><label for="rsvp-help">Can you volunteer?</label><select id="rsvp-help"><option>No, just attending</option><option>Yes, I can help</option></select></div>
<div class="full"><button class="btn solid" type="submit">Send RSVP</button></div><div class="success" role="status">You're in! See you there.</div></div></form></div>""")
body += signup()
page("events/", "Events | Karama", "Upcoming Karama events: workshops, heritage nights, job fairs and food drives.", body, "In Your Community")


# ================================================================== HOW YOU CAN HELP
help_nav = [("Overview", u("how-you-can-help/")), ("Why Donate?", u("how-you-can-help/why-donate/")),
            ("Why Volunteer?", u("how-you-can-help/why-volunteer/")), ("Partner With Us", u("how-you-can-help/partner-with-us/")),
            ("Host a Drive", u("how-you-can-help/host-a-drive/")), ("Speak Out", u("how-you-can-help/speak-out/"))]
body = landing_hero("How You Can Help", "Give, volunteer, partner or speak up. Every kind of help strengthens our community.",
                    "volunteers", eyebrow="Get Involved", crumbs=[("Home", u(""))])
body += secnav("How You Can Help", help_nav, u("how-you-can-help/"))
body += mcards("Ways to Help", [
    ("Donate", "Keep classes free and shelves full.", u("how-you-can-help/why-donate/")),
    ("Volunteer", "Tutor, sort food, coach or interpret.", u("how-you-can-help/why-volunteer/")),
    ("Partner", "Businesses, schools and faith groups.", u("how-you-can-help/partner-with-us/")),
    ("Host a Drive", "Collect food, coats or supplies.", u("how-you-can-help/host-a-drive/")),
    ("Speak Out", "Raise your voice for your neighbors.", u("how-you-can-help/speak-out/")),
    ("Stay Informed", "News, guides and stories.", u("news/"))])
body += feature("Zakat & Sadaqah", "Karama welcomes zakat and sadaqah. Gifts marked for the zakat fund go to eligible families.",
                ("Learn More", u("how-you-can-help/why-donate/zakat-and-sadaqah/")), "heart", eyebrow="Faithful Giving", variant="yellow")
body += signup()
page("how-you-can-help/", "How You Can Help | Karama", "Donate, volunteer, partner, host a drive or speak out with Karama.", body, "How You Can Help")

donate_nav = [("Why Donate?", u("how-you-can-help/why-donate/")), ("Make a Gift", u("how-you-can-help/why-donate/make-a-gift/")),
              ("Zakat & Sadaqah", u("how-you-can-help/why-donate/zakat-and-sadaqah/")), ("Plan Your Gift", u("how-you-can-help/why-donate/plan-your-gift/"))]
body = landing_hero("Why Donate?", "Your gift goes straight to books, groceries, training and the events that bring us together.",
                    "heart", eyebrow="How You Can Help", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/"))],
                    ctas=[("Donate Now", u("how-you-can-help/why-donate/make-a-gift/"), "yellow")])
body += secnav("Why Donate?", donate_nav, u("how-you-can-help/why-donate/"))
body += rich("""<h2>Where Your Gift Goes</h2>
<ul><li><strong>English classes:</strong> textbooks, workbooks and classroom supplies</li><li><strong>Food pantry:</strong> groceries, halal protein and baby supplies</li><li><strong>Job training:</strong> certification fees, tools and coaching</li><li><strong>Community events:</strong> food and supplies for heritage nights</li></ul>
<p>Karama is a 501(c)(3) nonprofit. Gifts are tax-deductible to the extent allowed by law.</p>""")
body += mcards("Ways to Give", [(t, d, h) for (t, h), d in zip(donate_nav[1:], [
    "Give once or monthly online.", "Zakat and sadaqah for eligible families.", "Stock, estate and employer matching gifts."])])
body += signup()
page("how-you-can-help/why-donate/", "Why Donate? | Karama", "How your gift to Karama helps families in our community.", body, "How You Can Help")

give_widget = """<form class="give" data-local><h3>Choose Your Gift</h3>
<div class="seg" data-group="#gift-freq"><button type="button" aria-pressed="true" data-value="once">One-Time</button><button type="button" aria-pressed="false" data-value="monthly">Monthly</button></div>
<input type="hidden" id="gift-freq" value="once">
<div class="amts" data-group="#gift-amount"><button type="button" aria-pressed="false" data-value="25">$25</button><button type="button" aria-pressed="true" data-value="50">$50</button><button type="button" aria-pressed="false" data-value="100">$100</button><button type="button" aria-pressed="false" data-value="250">$250</button><button type="button" aria-pressed="false" data-value="500">$500</button><button type="button" aria-pressed="false" data-value="">Other</button></div>
<label for="gift-amount">Amount (USD)</label><input id="gift-amount" type="number" min="1" value="50" required>
<label for="gift-fund">Direct my gift to</label><select id="gift-fund"><option>Where it's needed most</option><option>Food pantry</option><option>English literacy</option><option>Financial literacy</option><option>Immigration support</option><option>Vocational training</option><option>Zakat fund</option></select>
<p><strong>Your gift:</strong> <span id="gift-summary"></span></p>
<button class="btn solid" type="submit" style="width:100%">Continue</button>
<p class="form-note">Online payments are not connected yet. <span class="todo">Connect a payment processor before launch.</span></p>
<div class="success" role="status">Thank you! (Preview only: no payment was taken.)</div></form>"""
body = landing_hero("Make a Gift", "Give once or every month. Every dollar helps a neighbor take the next step.",
                    "heart", eyebrow="Why Donate?", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/")), ("Why Donate?", u("how-you-can-help/why-donate/"))])
body += secnav("Why Donate?", donate_nav, u("how-you-can-help/why-donate/make-a-gift/"))
body += section(f"""<div class="give-layout"><div class="reveal"><h2>Give Today</h2>
<p>Monthly gifts are especially helpful. They let us plan classes and stock the pantry ahead of time.</p>
<h3>Other ways to give</h3><ul style="font-size:18px;line-height:28px"><li>Mail a check payable to Karama: {ORG["address_2"]}, {ORG["city"]}</li><li>Ask your employer to match your gift</li><li>Donate food or supplies: see <a href="@/our-impact/food-pantry/donate-food/">most-needed items</a></li></ul></div>{give_widget}</div>""")
body += accordions("Giving Questions", [
    ("Is my gift tax-deductible?", f"<p>Karama is a 501(c)(3) nonprofit ({ORG['ein']}). Gifts are tax-deductible to the extent allowed by law. You'll get a receipt by email.</p>"),
    ("Can I cancel a monthly gift?", "<p>Yes, at any time. Contact us and we'll take care of it.</p>"),
    ("Can I give in someone's honor?", "<p>Yes. Add a note with your gift and we'll send an acknowledgment if you'd like.</p>")])
page("how-you-can-help/why-donate/make-a-gift/", "Make a Gift | Karama", "Donate to Karama once or monthly.", body, "How You Can Help")

body = landing_hero("Zakat & Sadaqah", "Faithful giving that reaches families in our own community.", "heart",
                    eyebrow="Why Donate?", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/")), ("Why Donate?", u("how-you-can-help/why-donate/"))])
body += secnav("Why Donate?", donate_nav, u("how-you-can-help/why-donate/zakat-and-sadaqah/"))
body += rich(f"""<h2>Zakat</h2><p>Gifts marked for Karama's zakat fund go to eligible families in our community. {T("Confirm zakat eligibility and distribution policy wording with leadership and scholars.")}</p>
<h2>Sadaqah</h2><p>Sadaqah supports all of Karama's work: English classes, the food pantry, job training and more.</p>
<p><a class="btn solid" href="@/how-you-can-help/why-donate/make-a-gift/">Give Zakat or Sadaqah</a></p>""")
body += signup()
page("how-you-can-help/why-donate/zakat-and-sadaqah/", "Zakat & Sadaqah | Karama", "Give zakat and sadaqah through Karama.", body, "How You Can Help")

body = landing_hero("Plan Your Gift", "Stock gifts, estate gifts and employer matching can multiply your impact.", "family",
                    eyebrow="Why Donate?", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/")), ("Why Donate?", u("how-you-can-help/why-donate/"))])
body += secnav("Why Donate?", donate_nav, u("how-you-can-help/why-donate/plan-your-gift/"))
body += accordions("Ways to Plan a Gift", [
    ("Employer matching", "<p>Many employers match employee gifts. Ask your HR team and name Karama as the recipient.</p>"),
    ("Gifts of stock", f"<p>Giving stock can reduce taxes for you. {T('Add brokerage transfer details.')}</p>"),
    ("Gifts in your will", "<p>Name Karama in your will or as a beneficiary to leave a lasting legacy. Talk to your attorney, then let us know so we can thank you.</p>"),
    ("Questions?", '<p>Contact us through our <a href="@/about/contact/">contact page</a>.</p>')])
page("how-you-can-help/why-donate/plan-your-gift/", "Plan Your Gift | Karama", "Planned giving options for Karama.", body, "How You Can Help")

body = landing_hero("Why Volunteer?", "Share an hour, a skill or a language. You'll change a neighbor's week, and maybe your own.", "volunteers",
                    eyebrow="How You Can Help", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/"))])
body += secnav("How You Can Help", help_nav, u("how-you-can-help/why-volunteer/"))
body += mcards("Volunteer Roles", [
    ("ESL Tutor", "Help adults practice English. No teaching degree needed.", "#vol-form"),
    ("Pantry Crew", "Sort donations and welcome families.", "#vol-form"),
    ("Job Coach", "Review résumés and run mock interviews.", "#vol-form"),
    ("Interpreter", "Arabic, Spanish, Somali, Urdu, Dari and more.", "#vol-form"),
    ("Workshop Leader", "Teach budgeting, credit or computer basics.", "#vol-form"),
    ("Event Team", "Set up, serve food and welcome guests.", "#vol-form")])
body += section(sec_head("Sign Up to Volunteer", "We'll contact you about training and a first shift.") + """<div class="form-block" id="vol-form"><form data-local><div class="form-grid">
<div><label for="v-name">Name</label><input id="v-name" required autocomplete="name"></div><div><label for="v-email">Email</label><input id="v-email" type="email" required autocomplete="email"></div>
<div><label for="v-phone">Phone</label><input id="v-phone" type="tel" autocomplete="tel"></div><div><label for="v-when">Availability</label><select id="v-when"><option>Weekdays</option><option>Evenings</option><option>Weekends</option><option>Flexible</option></select></div>
<div class="full"><span class="fieldset-label">I'm interested in</span><div class="checks"><label><input type="checkbox"> ESL tutoring</label><label><input type="checkbox"> Food pantry</label><label><input type="checkbox"> Job coaching</label><label><input type="checkbox"> Interpreting</label><label><input type="checkbox"> Workshops</label><label><input type="checkbox"> Events</label></div></div>
<div class="full"><label for="v-skills">Skills or languages</label><textarea id="v-skills" rows="3"></textarea></div>
<div class="full"><button class="btn solid" type="submit">Sign Up</button></div><div class="success" role="status">Thank you! Our volunteer coordinator will be in touch.</div></div></form></div>""")
page("how-you-can-help/why-volunteer/", "Why Volunteer? | Karama", "Volunteer with Karama as a tutor, pantry helper, job coach or interpreter.", body, "How You Can Help")

partner_nav = [("Partner With Us", u("how-you-can-help/partner-with-us/")), ("Partner Resources", u("how-you-can-help/partner-with-us/partner-resources/"))]
body = landing_hero("Partner With Us", "Businesses, employers, schools, masjids, churches and nonprofits: let's build a stronger community together.", "partners",
                    eyebrow="How You Can Help", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/"))])
body += secnav("Partner With Us", partner_nav, u("how-you-can-help/partner-with-us/"))
body += rich("<p>Karama works best with partners. Together we can reach more families, offer better training and keep the pantry stocked year-round.</p>")
body += accordions("Ways to Partner", [
    ("Hire our graduates", '<p>Share openings and meet trained, motivated candidates. See <a href="@/our-impact/vocational-training/employer-partners/">Employer Partners</a>.</p>'),
    ("Sponsor a program or event", "<p>Fund a class term, a workshop series or a heritage night. We'll recognize your support.</p>"),
    ("Offer space, supplies or expertise", "<p>Classrooms, computers, food, or professionals who can teach a workshop.</p>"),
    ("Refer families", "<p>Schools, clinics and caseworkers can refer families to any Karama program.</p>")])
body += fwcta("Let's Talk", "Tell us about your organization and how you'd like to help.", [("Contact Us", u("about/contact/"), "yellow")])
page("how-you-can-help/partner-with-us/", "Partner With Us | Karama", "Partner with Karama as an employer, sponsor or community organization.", body, "How You Can Help")

body = landing_hero("Partner Resources", "Tools and information for Karama partners.", "partners",
                    eyebrow="Partner With Us", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/")), ("Partner With Us", u("how-you-can-help/partner-with-us/"))])
body += secnav("Partner With Us", partner_nav, u("how-you-can-help/partner-with-us/partner-resources/"))
body += accordions("Resources", [
    ("Referral guide", f"<p>How to refer a family to Karama programs. {T('Add referral form or PDF.')}</p>"),
    ("Logo and brand use", f"<p>Guidelines for using the Karama name and logo. {T('Add brand guide.')}</p>"),
    ("Sponsorship levels", f"<p>{T('Add sponsorship tiers and benefits.')}</p>"),
    ("Food donation guidelines", '<p>See <a href="@/our-impact/food-pantry/donate-food/">Donate Food</a> for accepted items.</p>')])
page("how-you-can-help/partner-with-us/partner-resources/", "Partner Resources | Karama", "Resources for Karama partners.", body, "How You Can Help")

body = landing_hero("Host a Drive", "Rally your school, office or friends to collect food and supplies for families.", "volunteers",
                    eyebrow="How You Can Help", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/"))])
body += secnav("How You Can Help", help_nav, u("how-you-can-help/host-a-drive/"))
body += rich("""<h2>How to Host a Drive</h2><ol><li><strong>Pick a focus:</strong> food, winter coats, school supplies, baby items or hygiene kits.</li><li><strong>Set a goal and a date.</strong> One to two weeks works well.</li><li><strong>Share the list.</strong> Use our <a href="@/our-impact/food-pantry/donate-food/">most-needed items</a>.</li><li><strong>Schedule a drop-off</strong> through our <a href="@/about/contact/">contact page</a>.</li></ol>""")
body += signup()
page("how-you-can-help/host-a-drive/", "Host a Drive | Karama", "Host a food or supply drive for Karama.", body, "How You Can Help")

body = landing_hero("Speak Out", "Your voice can help build a community where everyone has a fair start.", "community",
                    eyebrow="How You Can Help", crumbs=[("Home", u("")), ("How You Can Help", u("how-you-can-help/"))])
body += secnav("How You Can Help", help_nav, u("how-you-can-help/speak-out/"))
body += rich("""<h2>Ways to Speak Up</h2><ul><li>Share Karama's programs with a family who could use them.</li><li>Tell local leaders why adult English classes, job training and food security matter.</li><li>Follow us on social media and share our posts.</li><li>Invite Karama to speak at your school, workplace or place of worship.</li></ul>
<p class="note">Karama is a nonpartisan nonprofit and does not support or oppose candidates for office.</p>""")
body += signup()
page("how-you-can-help/speak-out/", "Speak Out | Karama", "Raise your voice for newcomers, fair opportunity and food security.", body, "How You Can Help")


# ================================================================== NEED HELP (the "211" equivalent)
finder_opts = "".join(f'<option value="@/our-impact/{p["slug"]}/">{p["label"]}</option>' for p in PROGRAMS)
body = landing_hero("Need Help?", "All Karama services are free. You don't need to be Muslim, and you don't need to speak English well to ask.",
                    "family", eyebrow="Get Help", crumbs=[("Home", u(""))],
                    ctas=[("Find Food", u("our-impact/food-pantry/visit-the-pantry/"), "yellow"), ("Sign Up", "#intake", "white")])
body += section(f"""<form class="reveal" data-finder style="display:flex;gap:14px;flex-wrap:wrap;align-items:end;max-width:900px;margin:0 auto">
<div style="flex:1;min-width:260px"><label for="finder" style="font-weight:700;display:block;margin-bottom:6px">What do you need help with?</label>
<select id="finder" style="width:100%;height:54px;border-radius:40px;border:2px solid var(--blue);padding:0 22px;font:inherit;font-size:18px" required><option value="">Choose one…</option>{finder_opts}<option value="@/events/">Community events</option></select></div>
<button class="btn solid" type="submit" style="min-height:54px">Go</button></form>""")
body += mcards("Common Needs", [
    ("I Need Food", "Groceries from our pantry at Masjid Sabour.", u("our-impact/food-pantry/visit-the-pantry/")),
    ("I Want to Learn English", "Free classes for every level.", u("our-impact/english-literacy/esl-classes/")),
    ("I Need a Job", "Training, résumés and job fairs.", u("our-impact/vocational-training/job-readiness/")),
    ("Help With Money", "Budgeting, credit and taxes.", u("our-impact/financial-literacy/")),
    ("Immigration Questions", "Information and trusted referrals.", u("our-impact/immigration-support/")),
    ("Something Else", "Tell us and we'll figure it out together.", "#intake")])
body += section(sec_head("Tell Us What You Need", "A Karama team member will contact you, usually within a few days.") + f"""<div class="form-block" id="intake"><form data-local><div class="form-grid">
<div><label for="i-first">First name</label><input id="i-first" required autocomplete="given-name"></div><div><label for="i-last">Last name</label><input id="i-last" required autocomplete="family-name"></div>
<div><label for="i-phone">Phone</label><input id="i-phone" type="tel" required autocomplete="tel"></div><div><label for="i-email">Email (optional)</label><input id="i-email" type="email" autocomplete="email"></div>
<div><label for="i-lang">Preferred language</label><select id="i-lang"><option>English</option><option>Arabic</option><option>Spanish</option><option>Somali</option><option>Urdu</option><option>Dari / Farsi</option><option>Pashto</option><option>French</option><option>Other</option></select></div>
<div><label for="i-time">Best time to call</label><select id="i-time"><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div>
<div class="full"><span class="fieldset-label">I need help with</span><div class="checks"><label><input type="checkbox"> English / ESL</label><label><input type="checkbox"> Money, credit or taxes</label><label><input type="checkbox"> Immigration information</label><label><input type="checkbox"> Job training or a job</label><label><input type="checkbox"> Food</label><label><input type="checkbox"> Something else</label></div></div>
<div class="full"><label for="i-msg">Anything else we should know?</label><textarea id="i-msg" rows="4"></textarea></div>
<p class="form-note full">We keep your information private and only use it to contact you about Karama services. We do not ask about immigration status for food or classes.</p>
<div class="full"><button class="btn solid" type="submit">Send</button></div><div class="success" role="status">Thank you! We received your request and will reach out soon.</div></div></form></div>""")
body += section(f'<div class="reveal" style="max-width:900px;margin:0 auto"><h2>In an Emergency</h2><p>If you or someone else is in danger, call <strong>911</strong>. For help finding local services any time, dial <strong>211</strong>. For a mental health crisis, call or text <strong>988</strong>.</p></div>', "sec single-stat")
page("need-help/", "Need Help? | Karama", "Get free help from Karama: food, English classes, money help, immigration information and job training.", body, "Need Help")


# ================================================================== NEWS
cats = sorted({n["cat"] for n in NEWS})
items = "".join(f'<li data-cat="{n["cat"]}"><a class="news-item" href="@/news/{n["slug"]}/"><div class="img">{img(n["img"])}</div><div>'
                f'<div class="cat">{n["cat"]}</div><div class="title">{n["title"]}</div><p>{n["desc"]}</p><div class="date">{n["date"]}</div></div></a></li>'
                for n in NEWS)
body = landing_hero("News", "Announcements, helpful guides and stories from the Karama community.", "community",
                    eyebrow="Newsroom", crumbs=[("Home", u(""))])
body += section(f"""<div class="news-filter"><div><label for="nf-cat">Category</label><select id="nf-cat" data-filter-for="news-list"><option value="">All categories</option>{"".join(f"<option>{c}</option>" for c in cats)}</select></div>
<div><label for="nf-q">Search news</label><input id="nf-q" type="search" data-filter-for="news-list" placeholder="Keyword"></div></div>
<ul class="news-list" id="news-list" data-filter-list>{items}</ul><p class="empty" data-empty-for="news-list" hidden>No stories match. Try another word.</p>""")
body += mcards("More From Karama", [("Events", "See what's coming up.", u("events/")), ("Need Help?", "Find free services.", u("need-help/")),
                                    ("Get Involved", "Donate, volunteer or partner.", u("how-you-can-help/"))])
page("news/", "News | Karama", "Karama news, announcements and guides.", body)

for i, n in enumerate(NEWS):
    note = (f'<p class="note"><strong>Sample post.</strong> {T("Replace with a real Karama story before launch.")}</p>' if n["sample"] else "")
    body = article_hero(n["cat"], n["title"], n["desc"], f'By Karama Staff · {n["date"]}')
    body += f'<figure class="article-image">{"<div class=frame>" + img(n["img"]) + "</div>"}</figure>'
    body += rich(note + n["body"])
    others = [x for x in NEWS if x is not n][:3]
    body += acards("More Stories", [{"href": u(f"news/{x['slug']}/"), "img": x["img"], "cat": x["cat"], "title": x["title"]} for x in others],
                   btn=("All News", u("news/")))
    page(f"news/{n['slug']}/", f"{n['title']} | Karama", n["desc"], body)


# ================================================================== ABOUT
about_nav = [("About", u("about/")), ("Our History", u("about/our-history/")), ("Mission & Values", u("about/our-mission-and-values/")),
             ("Leadership", u("about/leadership-team/")), ("Public Reporting", u("about/public-reporting/")), ("Contact", u("about/contact/"))]
body = landing_hero("About Karama", "<em>Karama</em> (كرامة) means dignity. We help every neighbor build a secure, independent life.",
                    "masjid", eyebrow="Who We Are", crumbs=[("Home", u(""))])
body += secnav("About", about_nav, u("about/"))
body += rich(f"""<p>Karama is a nonprofit based at {ORG["address_1"]}. We offer free English and literacy classes, financial literacy workshops, immigration information and referrals, vocational training and a community food pantry. We also host events that celebrate the many cultures in our neighborhood.</p>
<p>Our work is powered by volunteers, donors and partners who believe that opportunity should be open to everyone.</p>""")
body += mcards("Learn More", [(t, d, h) for (t, h), d in zip(about_nav[1:], [
    "How Karama began.", "What we believe and how we work.", "The people who guide Karama.", "Financials and annual reports.", "Visit, call or write."])],
    cols=3)
body += signup()
page("about/", "About | Karama", "About Karama: our mission, history, leadership and contact information.", body)

body = landing_hero("Our History", "How a few neighbors at Masjid Sabour started something bigger.", "masjid",
                    eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += secnav("About", about_nav, u("about/our-history/"))
body += rich(f"""<p>{T("Tell Karama's founding story in a few short paragraphs: who started it, when and why.")}</p>
<ol class="timeline"><li><div class="yr">{T("Year")}</div><p>Karama is founded at Masjid Sabour.</p></li><li><div class="yr">{T("Year")}</div><p>Food pantry opens.</p></li><li><div class="yr">{T("Year")}</div><p>First ESL classes begin.</p></li><li><div class="yr">{T("Year")}</div><p>Financial literacy and job training programs launch.</p></li></ol>""")
page("about/our-history/", "Our History | Karama", "The story of Karama.", body)

body = landing_hero("Our Mission and Values", "Why we exist and how we treat every person who walks through our doors.", "community",
                    eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += secnav("About", about_nav, u("about/our-mission-and-values/"))
body += rich("""<h2>Our Mission</h2><p>Karama helps immigrants, refugees and neighbors in need build secure, independent lives through education, economic opportunity, food security and community connection, always with dignity.</p>""")
body += mcards("Our Values", [("Dignity", "We serve with respect. No one should feel small for asking for help.", "#main"),
                              ("Welcome", "Every faith, culture and language belongs here.", "#main"),
                              ("Self-Reliance", "We build skills that last, not dependence.", "#main"),
                              ("Trust", "We protect people's privacy and are honest about what we can do.", "#main")], cols=4)
page("about/our-mission-and-values/", "Our Mission and Values | Karama", "Karama's mission and values.", body)

people = "".join(f'<div class="person reveal"><div class="ph">{art.portrait(i)}</div><h3>{T("Name")}</h3><p>{r}</p></div>'
                 for i, r in enumerate(["Executive Director", "Board Chair", "Programs Director", "Pantry Coordinator", "Board Treasurer", "Board Secretary", "Volunteer Coordinator", "Board Member"]))
body = landing_hero("Our Leadership", "The staff and board members who guide Karama's work.", "community",
                    eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += secnav("About", about_nav, u("about/leadership-team/"))
body += section(sec_head("Board & Staff", T("Add names, photos and short bios.")) + f'<div class="people">{people}</div>')
page("about/leadership-team/", "Our Leadership | Karama", "Karama's staff and board.", body)

body = landing_hero("Public Reporting", "We believe in being open about how we use every gift.", None,
                    eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += secnav("About", about_nav, u("about/public-reporting/"))
body += rich(f"""<h2>Financials</h2><ul><li>IRS determination letter: {T("link")}</li><li>Form 990: {T("link")}</li><li>Annual report: {T("link")}</li><li>Audited financial statements: {T("link, if applicable")}</li></ul>""")
page("about/public-reporting/", "Public Reporting | Karama", "Karama financial reports and public documents.", body)

body = landing_hero("Contact", "Questions, partnerships, media or event ideas. We'd love to hear from you.", None,
                    eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += secnav("About", about_nav, u("about/contact/"))
body += section(f"""<div class="give-layout"><div class="reveal"><h2>Visit or Call</h2><div class="rich" style="padding:0"><dl>
<dt>Address</dt><dd>{ORG["address_1"]}<br>{ORG["address_2"]}<br>{ORG["city"]}</dd><dt>Phone</dt><dd>{ORG["phone"]}</dd><dt>Email</dt><dd>{ORG["email"]}</dd><dt>Office</dt><dd>{ORG["office_hours"]}</dd></dl></div>
<p>Need a service? Use our <a href="@/need-help/#intake">Need Help form</a> instead so the right person gets back to you.</p></div>
<form class="give" data-local><h3>Send a Message</h3>
<label for="c-name">Name</label><input id="c-name" required autocomplete="name"><label for="c-email">Email or phone</label><input id="c-email" required>
<label for="c-topic">Topic</label><select id="c-topic"><option>General question</option><option>Partnership</option><option>Media</option><option>Propose an event</option><option>Food drop-off</option></select>
<label for="c-msg">Message</label><textarea id="c-msg" rows="5" required style="width:100%;border:2px solid var(--line);border-radius:12px;padding:12px 16px;font:inherit;margin-bottom:14px"></textarea>
<button class="btn solid" type="submit">Send Message</button><div class="success" role="status">Thanks for reaching out! We'll reply soon.</div></form></div>""")
page("about/contact/", "Contact | Karama", "Contact Karama at Masjid Sabour.", body)

body = landing_hero("Frequently Asked Questions", "Quick answers about Karama's programs and services.", None,
                    eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += accordions("", [
    ("Do Karama's programs cost money?", "<p>No. All programs are free to participants.</p>"),
    ("Do I have to be Muslim?", "<p>No. Karama serves everyone, whatever their faith or background.</p>"),
    ("Do you ask about immigration status?", "<p>Not for food, classes or events. We only discuss status if you ask for help with an immigration question, and it stays private.</p>"),
    ("What languages do you speak?", "<p>Our volunteers speak English, Arabic and often other languages. Tell us your language and we'll try to match you.</p>"),
    ("Do you give legal advice?", '<p>No. We share general information and refer people to licensed attorneys and accredited representatives. See <a href="@/our-impact/immigration-support/legal-referrals/">Legal Referrals</a>.</p>'),
    ("How can I help?", '<p>Donate, volunteer, partner or host a drive. Start at <a href="@/how-you-can-help/">How You Can Help</a>.</p>'),
    ("Where are you located?", f"<p>{ORG['address_1']}, {ORG['address_2']}, {ORG['city']}.</p>")])
page("about/frequently-asked-questions/", "FAQ | Karama", "Frequently asked questions about Karama.", body)

body = landing_hero("Careers at Karama", "Join a team that puts dignity first.", "volunteers", eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))])
body += rich(f"""<h2>Open Positions</h2><p>{T("List open roles, or keep this note:")} There are no open staff positions right now. We're always looking for <a href="@/how-you-can-help/why-volunteer/">volunteers</a>.</p>
<p>Karama is an equal opportunity employer.</p>""")
page("about/careers/", "Careers | Karama", "Jobs at Karama.", body)

for slug, title, text in [
    ("privacy-policy", "Privacy Policy", f"""<p>Karama respects your privacy. We collect only the information you choose to give us, such as your name and contact details when you fill out a form, and we use it only to respond to you and provide services.</p><p>We do not sell your information. We do not ask about immigration status for food, classes or events.</p><p>{T("Have this policy reviewed before launch.")}</p>"""),
    ("terms", "Terms of Use", f"""<p>Information on this website is for general education and is not legal, tax or financial advice. Links to other websites are provided for convenience.</p><p>{T("Have these terms reviewed before launch.")}</p>"""),
    ("accessibility", "Accessibility", """<p>Karama wants everyone to be able to use this website. We aim to meet WCAG 2.1 AA guidelines, with readable text, keyboard navigation and screen-reader labels.</p><p>If something doesn't work for you, please <a href="@/about/contact/">contact us</a> and we'll help.</p>""")]:
    page(f"about/{slug}/", f"{title} | Karama", f"Karama {title.lower()}.",
         landing_hero(title, "", None, eyebrow="About", crumbs=[("Home", u("")), ("About", u("about/"))]) + rich(text))


# ================================================================== SEARCH, SITEMAP, 404
body = landing_hero("Search", "Find programs, pages and guides across the Karama site.", None, crumbs=[("Home", u(""))])
body += section("""<form action="." method="get" role="search" style="display:flex;gap:12px;max-width:760px"><label class="sr" for="search-q">Search</label>
<input id="search-q" name="q" type="search" style="flex:1;height:54px;border-radius:40px;border:2px solid var(--blue);padding:0 22px;font:inherit;font-size:18px">
<button class="btn solid" type="submit" style="min-height:54px">Search</button></form><p id="search-count" style="margin-top:20px"></p><ul class="results" id="search-results" data-base="../"></ul>""")
page("search/", "Search | Karama", "Search the Karama website.", body, cls="search")


def build_sitemap():
    tree = {}
    for p in PAGES:
        if p["path"] in ("search/", "sitemap/", "404/"):
            continue
        node = tree
        for part in [x for x in p["path"].split("/") if x]:
            node = node.setdefault(part, {})
        node["__page"] = p

    def render(node, prefix=""):
        out = ""
        for k in sorted(k for k in node if k != "__page"):
            child = node[k]
            pg = child.get("__page")
            label = pg["title"].split(" | ")[0] if pg else k
            href = f'@/{prefix}{k}/'
            out += f'<li><a href="{href}">{label}</a>{("<ul>" + render(child, prefix + k + "/") + "</ul>") if len(child) > 1 else ""}</li>'
        return out
    return '<ul class="tree"><li><a href="@/">Home</a></li>' + render(tree) + "</ul>"


body404 = landing_hero("Page Not Found", "Sorry, we couldn't find that page.", None, crumbs=[("Home", u(""))],
                       ctas=[("Go Home", u(""), "yellow"), ("Need Help?", u("need-help/"), "white")])


# ================================================================== RENDER
def rel_href(target, cur_dir):
    target, _, frag = target.partition("#")
    target, _, query = target.partition("?")
    if target == "" or target.endswith("/"):
        target += "index.html"
    r = os.path.relpath(target, cur_dir).replace(os.sep, "/")
    return r + (("?" + query) if query else "") + (("#" + frag) if frag else "")


def render(p):
    cur_dir = p["path"].rstrip("/") or "."
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(p["title"])}</title><meta name="description" content="{escape(p["desc"])}">
<link rel="icon" href="@/img/favicon.svg" type="image/svg+xml">{FONTS}<link rel="stylesheet" href="@/assets/site.css"></head>
<body class="{p["cls"]}">{header(p["top"])}<main id="main">{p["body"]}</main>{footer()}
{('<script src="@/assets/search-index.js"></script>' if p["cls"] == "search" else "")}<script src="@/assets/site.js"></script></body></html>"""
    return re.sub(r'@/([^"\'\s<>]*)', lambda m: rel_href(m.group(1), cur_dir), html)


def strip_tags(s):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def main():
    page("sitemap/", "Site Map | Karama", "Every page on the Karama website.",
         landing_hero("Site Map", "Every page on the Karama website.", None, crumbs=[("Home", u(""))]) + section(build_sitemap()))
    page("404/", "Page Not Found | Karama", "Page not found.", body404)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "img").mkdir()
    shutil.copy(SRC / "assets/site.css", OUT / "assets/site.css")
    shutil.copy(SRC / "assets/site.js", OUT / "assets/site.js")
    for name, fn in art.SCENES.items():
        (OUT / "img" / f"{name}.svg").write_text(fn())
    (OUT / "img/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80"><circle cx="40" cy="40" r="38" fill="#0044b5"/><path d="M40 14c6 10 16 15 24 15-2 18-12 30-24 36-12-6-22-18-24-36 8 0 18-5 24-15z" fill="#ffba00"/></svg>')

    index = []
    for p in PAGES:
        dest = OUT / (p["path"] + "index.html") if p["path"] else OUT / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(p))
        if p["path"] not in ("404/", "search/"):
            index.append({"t": p["title"].split(" | ")[0], "u": (p["path"] + "index.html") if p["path"] else "index.html",
                          "d": p["desc"], "k": strip_tags(p["body"])[:1500]})
    (OUT / "404.html").write_text((OUT / "404/index.html").read_text().replace('href="../', 'href="').replace('src="../', 'src="'))
    (OUT / "assets/search-index.js").write_text("window.KARAMA_INDEX=" + json.dumps(index, ensure_ascii=False) + ";")
    print(f"Built {len(PAGES)} pages into {OUT}")
    return crawl()


def crawl():
    """Breadth-first crawl from the homepage (unit-weight shortest paths, i.e. Dijkstra
    with every link costing 1). Verifies every link and asset resolves and every page
    is reachable, and writes the route table to routes.txt (outside the published site)."""
    all_pages = {p.relative_to(OUT).as_posix() for p in OUT.rglob("index.html")}
    dist, parent, broken = {"index.html": 0}, {"index.html": None}, []
    q = deque(["index.html"])
    ref = re.compile(r'(?:href|src|action)="([^"]+)"')
    while q:
        cur = q.popleft()
        html = (OUT / cur).read_text()
        for link in ref.findall(html):
            if link == "." or re.match(r"^(https?:|mailto:|tel:|#|data:)", link):
                continue
            path = link.split("#")[0].split("?")[0]
            if not path:
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(cur), path)).replace(os.sep, "/")
            if (OUT / target).is_dir():
                target = target.rstrip("/") + "/index.html"
            if not (OUT / target).exists():
                broken.append((cur, link))
                continue
            if target.endswith(".html") and target not in dist:
                dist[target], parent[target] = dist[cur] + 1, cur
                q.append(target)
    unreachable = sorted(all_pages - set(dist) - {"404/index.html"})

    lines = [f"{'hops':>4}  route  (via)"]
    for t in sorted(dist, key=lambda x: (dist[x], x)):
        route = "/" + t.replace("index.html", "")
        via = "/" + parent[t].replace("index.html", "") if parent[t] else "-"
        lines.append(f"{dist[t]:>4}  {route}  (via {via})")
    (OUT.parent / "routes.txt").write_text("\n".join(lines) + "\n")

    print(f"Crawled {len(dist)} reachable pages (max {max(dist.values())} hops from home).")
    if broken:
        print(f"BROKEN LINKS ({len(broken)}):")
        for s, l in broken[:50]:
            print(f"  {s} -> {l}")
    if unreachable:
        print(f"UNREACHABLE PAGES ({len(unreachable)}): {unreachable}")
    ok = not broken and not unreachable
    print("Link check: OK" if ok else "Link check: FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
