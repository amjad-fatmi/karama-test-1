"""Karama page content. Plain English, about a 9th-grade reading level.

Anything the Karama team still has to confirm is wrapped in <span class="todo">.
Sample news posts carry a visible "sample" note until real stories replace them.
"""
from components import ORG

T = lambda s: f'<span class="todo">{s}</span>'  # noqa: E731  marks a detail to fill in

# ------------------------------------------------------------------ programs
PROGRAMS = [
    {
        "slug": "english-literacy", "label": "English Literacy", "img": "classroom",
        "title": "Opening Doors Through English",
        "text": "Free classes that help adults read, write and speak English with confidence, at work, at the doctor and at their children's school.",
        "intro": """<p>Speaking English makes daily life easier. It helps people find better jobs, talk with their children's teachers, see a doctor and become citizens. Karama offers free English classes for adults at every level, taught by trained volunteers who are patient and kind.</p>
<p>You don't need to know any English to start. We'll meet you where you are.</p>""",
        "bubble": "We help adults learn to read, write and speak English, from the first letters of the alphabet to writing a work email.",
        "feature": ("Learning Together", "Classes are small and friendly. Many students say the best part is making new friends from all over the world.", "community", "sky"),
        "faqs": [
            ("How much do classes cost?", "<p>Nothing. Classes, books and materials are free.</p>"),
            ("What if I don't know any English?", "<p>That's okay. Our beginner class starts with the alphabet, numbers and everyday words.</p>"),
            ("Is childcare available?", f"<p>Childcare is offered during some classes. {T('Confirm which class times include childcare.')}</p>"),
            ("When do classes meet?", f"<p>{T('Add class days, times and term dates.')}</p>"),
        ],
        "subs": [
            {"slug": "esl-classes", "label": "ESL Classes", "img": "classroom",
             "title": "ESL Classes for Adults",
             "text": "English as a Second Language classes from beginner to advanced.",
             "body": f"""<h2>Find Your Level</h2>
<p>When you sign up, a teacher will give you a short, friendly placement check. It helps us put you in the right class. There is no pass or fail.</p>
<dl><dt>Beginner</dt><dd>Alphabet, numbers, greetings, filling out simple forms.</dd>
<dt>Intermediate</dt><dd>Everyday conversations, reading notices and letters, talking on the phone.</dd>
<dt>Advanced</dt><dd>Work English, writing emails, job interviews, reading the news.</dd></dl>
<h2>Class Details</h2>
<dl><dt>Where</dt><dd>{ORG["address_1"]}</dd><dt>When</dt><dd>{T("Class schedule")}</dd><dt>Cost</dt><dd>Free, including books</dd></dl>
<p><a class="btn solid" href="@/need-help/#intake">Sign Up for ESL</a></p>"""},
            {"slug": "adult-literacy", "label": "Adult Literacy", "img": "writing",
             "title": "Reading and Writing Basics",
             "text": "Help for adults who want to build reading and writing skills in English.",
             "body": """<h2>It's Never Too Late</h2>
<p>Some adults never had the chance to go to school, in any language. Our literacy tutors work one-on-one or in very small groups, at your pace, with no judgment.</p>
<h3>What you'll practice</h3>
<ul><li>Reading signs, labels, bills and forms</li><li>Writing your name, address and short notes</li><li>Reading with your children</li><li>Using a phone or computer to read and write</li></ul>
<p><a class="btn solid" href="@/need-help/#intake">Ask About a Tutor</a></p>"""},
            {"slug": "conversation-circles", "label": "Conversation Circles", "img": "community",
             "title": "Conversation Circles",
             "text": "Relaxed, small-group practice speaking English about everyday life.",
             "body": f"""<h2>Practice Speaking, Make Friends</h2>
<p>Conversation circles are casual. A volunteer leads a small group through real-life topics like shopping, the weather, holidays, jobs and family. Tea is usually involved.</p>
<p>Circles are a great fit for students who can read some English but want to speak more confidently.</p>
<dl><dt>When</dt><dd>{T("Circle days and times")}</dd><dt>Who</dt><dd>Intermediate and advanced students</dd></dl>
<p><a class="btn solid" href="@/need-help/#intake">Join a Circle</a></p>"""},
        ],
    },
    {
        "slug": "financial-literacy", "label": "Financial Literacy", "img": "money",
        "title": "Building Financial Security",
        "text": "Workshops and one-on-one help with budgeting, banking, credit, saving and taxes, so families can plan with confidence.",
        "intro": """<p>Money is stressful when the rules are new or confusing. Karama's financial literacy program explains how things work in plain language: opening a bank account, making a budget, building credit, avoiding scams and filing taxes.</p>
<p>We also respect families who want interest-free, faith-sensitive options and can talk through those choices.</p>""",
        "bubble": "Budgeting, banking, credit and taxes, explained in plain language so families can plan ahead with confidence.",
        "feature": ("Avoiding Scams", "Scammers often target newcomers. We teach families how to spot fake calls, texts and offers, and what to do if something feels wrong.", "heart", "yellow"),
        "faqs": [
            ("Do I need a bank account to join?", "<p>No. We can help you understand your options and open one if you want to.</p>"),
            ("Will you ask about my income?", "<p>Only if you want one-on-one help with a budget. Everything you share stays private.</p>"),
            ("Is there help that avoids interest?", "<p>Yes. We can talk through interest-free and faith-sensitive ways to save, borrow and pay.</p>"),
        ],
        "subs": [
            {"slug": "budgeting-and-banking", "label": "Budgeting & Banking", "img": "money",
             "title": "Budgeting & Banking",
             "text": "Make a plan for your money and learn how banks work.",
             "body": """<h2>Make a Budget That Works</h2>
<p>A budget is a plan for your money. In our workshop, you'll list what comes in, what goes out and what you want to save for. You'll leave with a simple budget you can actually use.</p>
<h2>Banking Basics</h2>
<ul><li>Checking vs. savings accounts</li><li>What ID you may need to open an account</li><li>Debit cards, fees and how to avoid overdrafts</li><li>Sending money to family safely</li></ul>
<p><a class="btn solid" href="@/need-help/#intake">Join a Workshop</a></p>"""},
            {"slug": "credit-and-debt", "label": "Credit & Debt", "img": "writing",
             "title": "Credit & Debt",
             "text": "Understand credit scores, build credit from zero and make a plan for debt.",
             "body": """<h2>Why Credit Matters</h2>
<p>In the U.S., your credit history can affect renting an apartment, getting a phone plan or buying a car. Many newcomers start with no credit history at all. That's normal, and it can be built.</p>
<h3>You'll learn</h3>
<ul><li>What a credit score is and who uses it</li><li>Safe ways to start building credit</li><li>How to read a credit report for free</li><li>How to make a plan to pay down debt</li></ul>
<p><a class="btn solid" href="@/need-help/#intake">Get Help With Credit</a></p>"""},
            {"slug": "free-tax-help", "label": "Free Tax Help", "img": "family",
             "title": "Free Tax Help",
             "text": "Learn what tax forms mean and find free, trusted help filing.",
             "body": f"""<h2>Taxes Without the Stress</h2>
<p>Every year, many families pay fees they don't need to or miss credits they qualify for. We explain the basics and connect you with free, trusted filing help.</p>
<h3>What to bring to a tax session</h3>
<ul><li>Photo ID and Social Security cards or ITINs for everyone on the return</li><li>W-2 and 1099 forms from every job</li><li>Last year's tax return, if you have it</li><li>Bank account and routing number for direct deposit</li></ul>
<p class="note">Karama does not prepare tax returns itself unless noted. {T("Add your tax-season partner and dates.")}</p>"""},
        ],
    },
    {
        "slug": "immigration-support", "label": "Immigration Support", "img": "passport",
        "title": "Welcoming New Neighbors",
        "text": "Know-your-rights sessions, citizenship test prep and connections to licensed legal help, so no one faces the system alone.",
        "intro": """<p>Moving to a new country is hard. The rules are complex, the paperwork is long and bad advice is everywhere. Karama helps newcomers understand the basics, prepare for the citizenship test and connect with licensed, trustworthy legal help.</p>
<p class="note">Karama shares general information. We do not give legal advice. For advice about your case, we refer you to a licensed immigration attorney or a DOJ-accredited representative.</p>""",
        "bubble": "Know-your-rights sessions, citizenship test prep and referrals to licensed, trusted legal help.",
        "feature": ("Beware of Notario Fraud", "In some countries a “notario” is a lawyer. In the U.S., a notary public cannot give legal advice. Only licensed attorneys and accredited representatives can.", "passport", "navy"),
        "faqs": [
            ("Will you ask about my immigration status?", "<p>Not to use our pantry, classes or events. We only ask about status if you want help with an immigration question, and it stays private.</p>"),
            ("Can Karama fill out my immigration forms?", "<p>No. Only licensed attorneys and accredited representatives should give legal help with forms. We'll help you find one.</p>"),
            ("Do you charge for referrals?", "<p>No. Our information sessions and referrals are free.</p>"),
        ],
        "subs": [
            {"slug": "know-your-rights", "label": "Know Your Rights", "img": "passport",
             "title": "Know Your Rights",
             "text": "General information sessions about everyone's basic rights in the U.S.",
             "body": f"""<h2>Everyone Has Rights</h2>
<p>Our sessions explain, in plain language, the basic rights that apply to everyone in the U.S. We offer them in several languages, and you can ask questions privately afterward.</p>
<h3>Topics we cover</h3>
<ul><li>Your rights at home, at work and in public</li><li>How to find trustworthy legal help</li><li>How to spot and report fraud</li><li>Making a family safety plan</li></ul>
<p>Next session: {T("date and time")}. <a href="@/events/?type=Workshop">See workshops</a>.</p>
<p class="note">This is general information, not legal advice.</p>"""},
            {"slug": "citizenship-prep", "label": "Citizenship Prep", "img": "classroom",
             "title": "Citizenship Test Prep",
             "text": "Study for the civics and English parts of the naturalization test.",
             "body": """<h2>Get Ready for the Test</h2>
<p>Our citizenship class helps you study the civics questions, practice reading and writing sentences and rehearse the interview with a volunteer.</p>
<ul><li>Weekly study sessions with practice quizzes</li><li>Mock interviews</li><li>Vocabulary support for English learners</li></ul>
<p><a class="btn solid" href="@/need-help/#intake">Join Citizenship Class</a></p>"""},
            {"slug": "legal-referrals", "label": "Legal Referrals", "img": "partners",
             "title": "Finding Trusted Legal Help",
             "text": "We connect you with licensed immigration attorneys and accredited representatives.",
             "body": f"""<h2>The Right Help Matters</h2>
<p>Bad legal advice can hurt your case. We refer people only to licensed attorneys and DOJ-accredited representatives.</p>
<h3>How it works</h3>
<ol><li>Tell us what you need help with, using the form on our <a href="@/need-help/">Need Help</a> page.</li><li>A Karama staff member contacts you privately.</li><li>We share referral options that fit your situation, including free and low-cost choices.</li></ol>
<p>{T("List referral partners once agreements are in place.")}</p>"""},
        ],
    },
    {
        "slug": "vocational-training", "label": "Vocational Training", "img": "tools",
        "title": "Training for Good Jobs",
        "text": "Job skills, certifications, résumé help and introductions to local employers who are hiring.",
        "intro": f"""<p>A steady job with fair pay changes everything for a family. Karama's vocational training helps adults build skills employers want, earn certifications and get ready to apply and interview.</p>
<p>Training tracks: {T("list your tracks, e.g. computer skills, trades, healthcare support, food handling")}.</p>""",
        "bubble": "Job skills, certifications, résumé help and introductions to local employers who are hiring.",
        "feature": ("Your Résumé, Ready", "Volunteers help you turn your experience, including work from your home country, into a clear U.S.-style résumé.", "writing", "sky"),
        "faqs": [
            ("Do I need to speak English well?", "<p>Some tracks need basic English. We'll help you build it at the same time through our ESL classes.</p>"),
            ("Does training cost money?", "<p>Training is free to participants.</p>"),
            ("Will you help me find a job?", "<p>Yes. We help with applications and introduce graduates to our employer partners.</p>"),
        ],
        "subs": [
            {"slug": "job-readiness", "label": "Job Readiness", "img": "writing",
             "title": "Job Readiness",
             "text": "Résumés, applications, interviews and workplace basics.",
             "body": """<h2>Get Ready to Get Hired</h2>
<ul><li>Write a U.S.-style résumé and cover letter</li><li>Fill out online job applications</li><li>Practice interviews with a volunteer coach</li><li>Learn workplace expectations and your rights at work</li></ul>
<p><a class="btn solid" href="@/need-help/#intake">Book a Coaching Session</a></p>"""},
            {"slug": "career-training", "label": "Career Training", "img": "tools",
             "title": "Career Training Tracks",
             "text": "Hands-on training and certifications that lead to steady work.",
             "body": f"""<h2>Build Skills Employers Want</h2>
<p>Each track combines classroom learning with hands-on practice. Graduates get help with certification exams and job placement.</p>
<dl><dt>Tracks</dt><dd>{T("Training tracks")}</dd><dt>Length</dt><dd>{T("Weeks per track")}</dd><dt>Cost</dt><dd>Free to participants</dd></dl>
<p><a class="btn solid" href="@/need-help/#intake">Apply for Training</a></p>"""},
            {"slug": "employer-partners", "label": "Employer Partners", "img": "partners",
             "title": "Hire With Karama",
             "text": "Employers: meet motivated, trained candidates from our community.",
             "body": """<h2>For Employers</h2>
<p>Our graduates are motivated, dependable and ready to work. Many speak two or more languages. Partner with Karama to find great hires and help build a stronger local workforce.</p>
<ul><li>Post openings with our job coaches</li><li>Speak at a class or join a job fair</li><li>Offer internships or on-the-job training</li></ul>
<p><a class="btn solid" href="@/how-you-can-help/partner-with-us/">Become a Partner</a></p>"""},
        ],
    },
    {
        "slug": "food-pantry", "label": "Food Pantry", "img": "pantry",
        "title": "No Family Goes Hungry",
        "text": "Groceries for any family who needs them, served with dignity at Masjid Sabour.",
        "intro": """<p>The Karama food pantry at Masjid Sabour gives groceries to families who need them. It's run by volunteers and stocked by neighbors, local businesses and donors.</p>
<p>The pantry is open to everyone. You don't have to be Muslim or a member of the masjid. Halal options and culturally familiar foods are offered whenever possible.</p>""",
        "bubble": "Groceries for any family who needs them, including halal options, served with dignity at Masjid Sabour.",
        "feature": ("Give Food, Give Dignity", "Canned goods, rice, lentils and cooking oil keep our shelves full. See the most-needed list and drop off during pantry hours.", "volunteers", ""),
        "faqs": [
            ("Do I need an ID?", f"<p>{T('Confirm whether ID or proof of address is requested.')}</p>"),
            ("How often can I visit?", f"<p>{T('Confirm visit frequency policy.')}</p>"),
            ("Is the food halal?", "<p>We offer halal options whenever possible, and volunteers can point them out.</p>"),
            ("Can someone pick up for me?", "<p>Yes, in most cases. Call us first so we can plan with you.</p>"),
        ],
        "subs": [
            {"slug": "visit-the-pantry", "label": "Visit the Pantry", "img": "pantry",
             "title": "Visit the Food Pantry",
             "text": "Where, when and what to expect on your first visit.",
             "body": f"""<h2>Pantry Details</h2>
<dl><dt>Where</dt><dd>{ORG["address_1"]}, {ORG["address_2"]}, {ORG["city"]}</dd><dt>When</dt><dd>{ORG["pantry_hours"]}</dd><dt>Phone</dt><dd>{ORG["phone"]}</dd></dl>
<h2>Your First Visit</h2>
<ol><li>A volunteer will greet you at the door.</li><li>You may be asked a few simple questions for our records. {T("Confirm intake questions.")}</li><li>You'll choose groceries or receive a pre-packed box.</li><li>Bring bags if you have them.</li></ol>
<p class="note">Can't come during open hours? Call us. We'll try to arrange a pickup time, especially for seniors and people with disabilities.</p>"""},
            {"slug": "donate-food", "label": "Donate Food", "img": "volunteers",
             "title": "Donate Food",
             "text": "What we need most and how to drop it off.",
             "body": """<h2>Most-Needed Items</h2>
<ul><li>Rice, lentils, beans and pasta</li><li>Canned vegetables, tomatoes and fruit</li><li>Canned tuna, salmon and halal chicken</li><li>Cooking oil, flour, sugar and tea</li><li>Diapers, baby formula and wipes</li><li>Soap, toothpaste and other hygiene items</li></ul>
<h2>Please Don't Donate</h2>
<ul><li>Opened or expired food</li><li>Pork products or items containing alcohol</li><li>Homemade food</li></ul>
<p><a class="btn solid" href="@/how-you-can-help/host-a-drive/">Host a Food Drive</a></p>"""},
        ],
    },
]

# ------------------------------------------------------------------ news
NEWS = [
    {"slug": "fall-esl-enrollment-is-open", "cat": "Announcements", "img": "classroom", "date": "September 2026", "sample": True,
     "title": "Fall ESL Enrollment Is Open",
     "desc": "Free English classes for adults start this fall at Masjid Sabour. Here's how to sign up.",
     "body": f"""<p>Karama's free English classes for adults are enrolling now. Classes are offered at beginner, intermediate and advanced levels, and books are provided.</p>
<h2>How to Sign Up</h2><ol><li>Fill out the short form on our <a href="@/need-help/#intake">Need Help</a> page and check "English / ESL."</li><li>We'll call you to schedule a quick, friendly placement check.</li><li>You'll get your class day, time and room.</li></ol>
<p>Class start date: {T("start date")}.</p>"""},
    {"slug": "five-steps-to-build-credit-from-zero", "cat": "Guides", "img": "money", "date": "August 2026", "sample": False,
     "title": "Five Steps to Build Credit From Zero",
     "desc": "New to the U.S. credit system? These simple steps can help you start.",
     "body": """<p>Many newcomers arrive with no U.S. credit history. That isn't bad credit. It just means there's no record yet. Here are five common first steps.</p>
<ol><li><strong>Open a bank account.</strong> It shows stability and makes paying bills easier.</li><li><strong>Ask about a secured card or credit-builder loan.</strong> These are designed for people starting out.</li><li><strong>Pay every bill on time.</strong> Payment history matters most.</li><li><strong>Keep balances low.</strong> Try to use only a small part of your credit limit.</li><li><strong>Check your credit report for free.</strong> Look for mistakes and report them.</li></ol>
<p>Want help making a plan? Join our <a href="@/our-impact/financial-literacy/credit-and-debt/">Credit &amp; Debt workshop</a>.</p>
<p class="note">This is general education, not personal financial advice.</p>"""},
    {"slug": "what-to-expect-at-the-food-pantry", "cat": "Guides", "img": "pantry", "date": "August 2026", "sample": False,
     "title": "What to Expect at the Food Pantry",
     "desc": "A simple guide to your first visit to the Karama pantry at Masjid Sabour.",
     "body": """<p>If you've never visited a food pantry before, it's normal to feel unsure. Our volunteers are here to make it easy and respectful.</p>
<h2>Before You Come</h2><ul><li>Check pantry hours on our <a href="@/our-impact/food-pantry/visit-the-pantry/">Visit the Pantry</a> page.</li><li>Bring reusable bags if you have them.</li></ul>
<h2>When You Arrive</h2><ul><li>A volunteer will welcome you and explain the steps.</li><li>Ask for halal options or foods your family prefers.</li><li>Tell us if you need other help, like English classes or job support. We'll connect you.</li></ul>"""},
    {"slug": "spotting-immigration-scams", "cat": "Guides", "img": "passport", "date": "July 2026", "sample": False,
     "title": "How to Spot Immigration Scams",
     "desc": "Warning signs of fraud and how to find help you can trust.",
     "body": """<p>Immigration scams cost families money and can harm their cases. Watch for these warning signs.</p>
<ul><li>Someone promises a guaranteed result or a "special connection."</li><li>A "notario" or notary offers legal advice. In the U.S., notaries cannot give legal advice.</li><li>You're asked to sign blank forms or forms with false information.</li><li>Someone keeps your original documents.</li><li>You're pressured to pay in cash with no receipt.</li></ul>
<h2>Where to Find Trusted Help</h2><p>Only licensed attorneys and DOJ-accredited representatives should give immigration legal advice. Karama can help you find one. Visit <a href="@/our-impact/immigration-support/legal-referrals/">Legal Referrals</a>.</p>
<p class="note">General information, not legal advice.</p>"""},
    {"slug": "heritage-nights-celebrate-every-neighbor", "cat": "Community", "img": "heritage", "date": "July 2026", "sample": True,
     "title": "Heritage Nights Celebrate Every Neighbor",
     "desc": "Each month, Karama builds an evening around a community in our area. Everyone is invited.",
     "body": """<p>Karama's heritage nights are built around the cultures that make up our community, including Black, Hispanic and Latino, Asian American and Pacific Islander, Native American and Arab American neighbors, and many more.</p>
<p>Each evening includes food, music, stories and time to meet new people. Community members help plan every event.</p>
<p>See the full calendar on our <a href="@/in-your-community/heritage-months/">Heritage Months</a> page, or <a href="@/about/contact/">tell us about an event idea</a>.</p>"""},
    {"slug": "your-resume-from-home-counts", "cat": "Guides", "img": "writing", "date": "June 2026", "sample": False,
     "title": "Your Work From Home Counts",
     "desc": "How to show experience from your home country on a U.S. résumé.",
     "body": """<p>Many newcomers have years of valuable work experience that doesn't show up clearly on a U.S.-style résumé. Here's how to make it count.</p>
<ul><li>List your job title, employer, city and country, and years worked.</li><li>Describe what you did with action words: "managed," "built," "trained," "served."</li><li>Add numbers when you can: team size, customers served, projects finished.</li><li>List languages you speak. It's a real skill employers value.</li><li>Ask about getting degrees or licenses evaluated for the U.S.</li></ul>
<p>Get one-on-one help at <a href="@/our-impact/vocational-training/job-readiness/">Job Readiness</a>.</p>"""},
]

# ------------------------------------------------------------------ events (sample schedule; edit dates)
EVENTS = [
    ("2026-10-04", "Classes", "Fall ESL Enrollment Day", "10:00 AM – 1:00 PM", "Masjid Sabour, community hall", "Take a quick placement check and pick a class time."),
    ("2026-10-11", "Culture", "Hispanic Heritage Month Community Night", "6:00 – 8:30 PM", "Masjid Sabour", "Food, music and stories with our Latino neighbors. All families welcome."),
    ("2026-10-18", "Workshop", "Money Basics: Build Your Credit", "11:00 AM – 12:30 PM", "Classroom B", "How credit scores work and how to start building one."),
    ("2026-10-25", "Workshop", "Know Your Rights Information Session", "2:00 – 3:30 PM", "Masjid Sabour", "General information in several languages. Not legal advice."),
    ("2026-11-08", "Careers", "Job Fair & Résumé Clinic", "10:00 AM – 2:00 PM", "Community hall", "Meet local employers and get your résumé reviewed."),
    ("2026-11-15", "Culture", "Native American Heritage Month Gathering", "5:00 – 7:30 PM", "Masjid Sabour", "An evening of learning and friendship with Indigenous community guests."),
    ("2026-11-22", "Food", "Thanksgiving Food Distribution", "9:00 AM – 12:00 PM", "Masjid Sabour pantry", "Holiday grocery boxes for families. Volunteers needed the day before."),
    ("2026-12-13", "Food", "Winter Coat & Supply Drive", "12:00 – 4:00 PM", "Community hall", "Drop off or pick up coats, blankets and hygiene kits."),
]

HERITAGE = [
    ("February", "Black History Month", "Honoring African American history, culture and leadership."),
    ("March", "Women's History Month", "Celebrating women who lead our families and community."),
    ("April", "Arab American Heritage Month", "Food, poetry and stories from across the Arab world."),
    ("May", "AAPI Heritage Month", "Asian American and Pacific Islander culture and history."),
    ("June", "Immigrant Heritage Month", "Celebrating the journeys that brought us here."),
    ("Sep 15 – Oct 15", "Hispanic Heritage Month", "Music, food and traditions from Latin America."),
    ("November", "Native American Heritage Month", "Learning from and honoring Indigenous nations."),
    ("Year-round", "Eid & Holiday Gatherings", "Open community meals around Eid and other holidays."),
]
