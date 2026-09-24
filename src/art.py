"""Original flat illustrations used as photo stand-ins.

Every scene is a 1600x900 SVG (16:9) drawn with `preserveAspectRatio="xMidYMid slice"`,
so it can fill any frame (card, circle, hero). Replace a scene with a real photo by
dropping `site/img/<name>.jpg` in place and changing IMG_EXT in build.py.
"""

SKIN = ["#8d5524", "#c68642", "#e0ac69", "#f1c27d", "#5c3a21", "#a86b3c"]
NAVY, BLUE, MID, LIGHT, SKY, ARC = "#21296b", "#0044b5", "#1c45b4", "#5a84e6", "#a7d2ff", "#e4eefc"
LAV, LAVD, YEL, AMB, CREAM = "#6c76d3", "#4e4aa6", "#fad42f", "#ffba00", "#fbf6ec"
TEAL, CORAL, GREEN = "#1f8a7a", "#e2674a", "#5aa469"


def person(x, y, s=1.0, skin=0, shirt=BLUE, hijab=None, hair="#2b1d14", arm=None):
    """A seated/standing bust. (x, y) is the base center; s scales it."""
    sk = SKIN[skin % len(SKIN)]
    head_r = 46 * s
    hy = y - 250 * s
    parts = [f'<path d="M{x-120*s},{y} C{x-120*s},{y-140*s} {x-80*s},{y-190*s} {x},{y-190*s} '
             f'C{x+80*s},{y-190*s} {x+120*s},{y-140*s} {x+120*s},{y} Z" fill="{shirt}"/>',
             f'<rect x="{x-18*s}" y="{hy+30*s}" width="{36*s}" height="{40*s}" fill="{sk}"/>']
    if hijab:
        parts.append(f'<path d="M{x-66*s},{hy+60*s} C{x-72*s},{hy-50*s} {x+72*s},{hy-50*s} {x+66*s},{hy+60*s} '
                     f'C{x+60*s},{hy+95*s} {x-60*s},{hy+95*s} {x-66*s},{hy+60*s} Z" fill="{hijab}"/>')
        parts.append(f'<ellipse cx="{x}" cy="{hy+8*s}" rx="{36*s}" ry="{42*s}" fill="{sk}"/>')
    else:
        parts.append(f'<circle cx="{x}" cy="{hy}" r="{head_r}" fill="{sk}"/>')
        parts.append(f'<path d="M{x-head_r},{hy-4*s} C{x-head_r},{hy-62*s} {x+head_r},{hy-62*s} {x+head_r},{hy-4*s} '
                     f'C{x+30*s},{hy-30*s} {x-30*s},{hy-30*s} {x-head_r},{hy-4*s} Z" fill="{hair}"/>')
    if arm:
        ax, ay = arm
        parts.append(f'<path d="M{x+80*s},{y-120*s} L{ax},{ay}" stroke="{shirt}" stroke-width="{34*s}" stroke-linecap="round"/>')
        parts.append(f'<circle cx="{ax}" cy="{ay}" r="{19*s}" fill="{sk}"/>')
    return "".join(parts)


def wrap(bg, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" '
            f'role="img" aria-label="{title}"><rect width="1600" height="900" fill="{bg}"/>{body}</svg>')


def blobs(*specs):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>' for x, y, r, c, o in specs)


def classroom():
    b = blobs((1350, 120, 320, SKY, .5), (150, 820, 260, YEL, .35))
    b += f'<rect x="260" y="110" width="760" height="400" rx="14" fill="{NAVY}"/><rect x="290" y="140" width="700" height="340" fill="#2f3a86"/>'
    b += '<g fill="#fff" font-family="Arial, sans-serif" font-weight="700">'
    b += '<text x="330" y="235" font-size="84">A a  B b  C c</text><text x="330" y="330" font-size="52" opacity=".85">Hello — مرحبا — Hola</text>'
    b += '<text x="330" y="420" font-size="44" opacity=".7">I am learning English.</text></g>'
    b += f'<rect x="120" y="700" width="1400" height="40" rx="10" fill="#c9924f"/>'
    b += person(420, 900, 1.1, 1, TEAL, hijab=LAVD) + person(800, 900, 1.15, 4, AMB) + person(1180, 900, 1.1, 2, CORAL, hair="#6b3e1f")
    b += f'<rect x="1040" y="640" width="160" height="110" rx="6" fill="#fff" transform="rotate(-8 1120 695)"/><rect x="1060" y="660" width="120" height="8" fill="{LIGHT}" transform="rotate(-8 1120 695)"/>'
    b += person(1420, 740, .8, 3, BLUE, arm=(1300, 470))
    return wrap(ARC, b, "Adults in an English class")


def money():
    b = blobs((1300, 700, 360, YEL, .45), (240, 160, 220, SKY, .6))
    b += f'<rect x="220" y="230" width="600" height="440" rx="30" fill="#fff"/><rect x="220" y="230" width="600" height="90" rx="30" fill="{BLUE}"/>'
    for i, h in enumerate([120, 200, 160, 260, 320]):
        b += f'<rect x="{280+i*100}" y="{620-h}" width="64" height="{h}" rx="8" fill="{[LIGHT, MID, LIGHT, MID, AMB][i]}"/>'
    b += '<text x="260" y="292" font-family="Arial" font-weight="700" font-size="44" fill="#fff">My Budget</text>'
    for i in range(4):
        b += f'<circle cx="{1080+i*18}" cy="{520-i*46}" r="90" fill="{AMB}" stroke="#d99a00" stroke-width="10"/>'
    b += '<text x="1098" y="410" font-family="Arial" font-weight="700" font-size="100" fill="#8a5a00" text-anchor="middle">$</text>'
    b += person(1380, 900, 1.05, 0, NAVY, hijab=TEAL)
    return wrap(CREAM, b, "Budget chart and coins")


def passport():
    b = blobs((1250, 250, 380, SKY, .55), (260, 760, 300, LAV, .3))
    b += f'<circle cx="520" cy="430" r="250" fill="{BLUE}"/>'
    b += f'<path d="M270,430 H770 M520,180 C420,300 420,560 520,680 M520,180 C620,300 620,560 520,680 M300,320 H740 M300,540 H740" stroke="{SKY}" stroke-width="10" fill="none"/>'
    b += f'<g transform="rotate(8 1000 470)"><rect x="860" y="250" width="300" height="420" rx="22" fill="{NAVY}"/>'
    b += f'<circle cx="1010" cy="410" r="70" fill="none" stroke="{AMB}" stroke-width="10"/><rect x="920" y="530" width="180" height="16" rx="8" fill="{AMB}"/><rect x="950" y="570" width="120" height="12" rx="6" fill="{AMB}" opacity=".7"/></g>'
    b += person(1330, 900, 1.05, 5, CORAL, hair="#1a120c")
    b += f'<path d="M180,190 q60,-40 120,0 q60,40 120,0" stroke="{NAVY}" stroke-width="8" fill="none" opacity=".4"/>'
    return wrap(ARC, b, "Globe and passport")


def tools():
    b = blobs((200, 180, 260, YEL, .5), (1400, 760, 340, SKY, .5))
    b += f'<rect x="640" y="250" width="620" height="400" rx="20" fill="{NAVY}"/><rect x="670" y="280" width="560" height="320" rx="8" fill="{ARC}"/>'
    b += f'<rect x="580" y="650" width="740" height="30" rx="12" fill="#9aa3c7"/>'
    b += f'<rect x="710" y="320" width="300" height="24" rx="12" fill="{BLUE}"/><rect x="710" y="370" width="460" height="16" rx="8" fill="{LIGHT}"/><rect x="710" y="405" width="420" height="16" rx="8" fill="{LIGHT}"/>'
    b += f'<rect x="710" y="450" width="200" height="110" rx="10" fill="{AMB}"/><rect x="940" y="450" width="230" height="110" rx="10" fill="{SKY}"/>'
    b += person(360, 900, 1.15, 2, BLUE, hair="#3a2414") + person(1420, 900, .95, 4, AMB, hijab=NAVY, arm=(1260, 560))
    b += f'<g transform="translate(160 330) rotate(-30)"><rect width="30" height="200" rx="10" fill="#8b5e34"/><rect x="-40" y="-20" width="110" height="50" rx="10" fill="#7d8597"/></g>'
    return wrap(CREAM, b, "Job training on a laptop")


def pantry():
    b = blobs((1400, 160, 300, YEL, .45), (180, 800, 280, SKY, .5))
    b += f'<rect x="150" y="160" width="1300" height="24" fill="#b07a45"/><rect x="150" y="400" width="1300" height="24" fill="#b07a45"/>'
    cols = [CORAL, AMB, GREEN, BLUE, TEAL, YEL, LAV]
    for i in range(13):
        c = cols[i % len(cols)]
        b += f'<rect x="{180+i*98}" y="{70+(i%3)*8}" width="70" height="{90-(i%3)*8}" rx="8" fill="{c}"/>'
        b += f'<rect x="{180+i*98}" y="{300+(i%2)*12}" width="70" height="{100-(i%2)*12}" rx="{35 if i%2 else 8}" fill="{cols[(i+3)%len(cols)]}"/>'
    b += f'<path d="M520,560 H1080 L1030,860 H570 Z" fill="#d9a066"/><path d="M600,560 L660,470 M1000,560 L940,470" stroke="#b07a45" stroke-width="18" stroke-linecap="round"/>'
    b += f'<circle cx="660" cy="545" r="52" fill="{CORAL}"/><circle cx="780" cy="520" r="62" fill="{GREEN}"/><circle cx="905" cy="540" r="54" fill="{AMB}"/><rect x="960" y="470" width="60" height="90" rx="10" fill="{BLUE}"/>'
    b += person(300, 900, 1.0, 3, TEAL, hijab=CORAL) + person(1310, 900, 1.05, 0, NAVY, arm=(1090, 600))
    return wrap(ARC, b, "Food pantry shelves and grocery basket")


def community():
    b = blobs((800, -100, 600, YEL, .35), (1450, 700, 300, LAV, .35), (120, 650, 260, SKY, .6))
    for i in range(9):
        x = 120 + i * 170
        b += f'<path d="M{x},120 q85,70 170,0" stroke="{NAVY}" stroke-width="4" fill="none" opacity=".5"/>'
        b += f'<path d="M{x+60},150 l25,50 l25,-50 z" fill="{[CORAL, AMB, TEAL, LAV][i%4]}"/>'
    b += f'<rect x="100" y="700" width="1400" height="30" rx="10" fill="#c9924f"/>'
    for i, (x, sk, sh, hj) in enumerate([(260, 0, CORAL, None), (520, 3, BLUE, TEAL), (800, 4, AMB, None), (1080, 1, LAVD, None), (1340, 2, TEAL, NAVY)]):
        b += person(x, 900, 1.0 if i % 2 else 1.1, sk, sh, hijab=hj, hair=["#2b1d14", "#6b3e1f", "#111"][i % 3])
    b += f'<circle cx="640" cy="690" r="34" fill="{CORAL}"/><circle cx="960" cy="690" r="30" fill="{GREEN}"/><rect x="760" y="650" width="70" height="50" rx="8" fill="#fff"/>'
    return wrap(CREAM, b, "Neighbors at a community celebration")


def heritage():
    b = f'<rect width="1600" height="900" fill="{NAVY}"/>' + blobs((1300, 200, 380, LAVD, .7), (200, 800, 300, BLUE, .6))
    for i in range(7):
        x = 170 + i * 210
        h = 140 + (i % 3) * 30
        c = [AMB, CORAL, YEL, TEAL, LAV, AMB, CORAL][i]
        b += f'<line x1="{x}" y1="0" x2="{x}" y2="{110+(i%2)*40}" stroke="#fff" stroke-width="3" opacity=".6"/>'
        b += f'<rect x="{x-45}" y="{110+(i%2)*40}" width="90" height="{h}" rx="40" fill="{c}"/><rect x="{x-30}" y="{110+(i%2)*40+h}" width="60" height="16" rx="4" fill="#fff" opacity=".7"/>'
    for i in range(40):
        b += f'<circle cx="{(i*137)%1600}" cy="{(i*89)%420+20}" r="{2+(i%3)}" fill="#fff" opacity=".6"/>'
    b += person(420, 900, 1.1, 4, AMB, hijab=CORAL) + person(800, 900, 1.2, 1, TEAL) + person(1180, 900, 1.1, 2, LAV, hair="#5a3a22")
    return wrap(NAVY, b, "Lanterns at a heritage night")


def volunteers():
    b = blobs((1350, 150, 300, YEL, .5), (180, 180, 220, SKY, .6))
    b += f'<rect x="100" y="620" width="1400" height="40" rx="12" fill="#9aa3c7"/>'
    for i in range(5):
        b += f'<rect x="{360+i*190}" y="{470-(i%2)*30}" width="150" height="{150+(i%2)*30}" rx="10" fill="#d9a066"/><rect x="{360+i*190}" y="{470-(i%2)*30}" width="150" height="26" fill="#c08850"/>'
    b += person(260, 900, 1.1, 2, BLUE, hair="#3a2414", arm=(420, 560)) + person(800, 900, 1.05, 0, BLUE, hijab=YEL) + person(1340, 900, 1.1, 5, BLUE, arm=(1180, 560))
    b += '<g font-family="Arial" font-weight="700" fill="#fff" font-size="30"><text x="215" y="800">VOLUNTEER</text><text x="1290" y="800">VOLUNTEER</text></g>'
    return wrap(ARC, b, "Volunteers packing boxes")


def partners():
    b = blobs((300, 200, 320, SKY, .6), (1350, 720, 360, YEL, .4))
    b += f'<path d="M380,560 C520,470 640,470 760,530 L840,570 C900,600 900,660 840,660 L700,640" stroke="{SKIN[1]}" stroke-width="80" fill="none" stroke-linecap="round"/>'
    b += f'<path d="M1220,560 C1080,470 960,470 840,530 L760,570 C700,600 700,660 760,660 L900,640" stroke="{SKIN[4]}" stroke-width="80" fill="none" stroke-linecap="round"/>'
    b += f'<rect x="120" y="470" width="300" height="200" rx="30" fill="{BLUE}"/><rect x="1180" y="470" width="300" height="200" rx="30" fill="{NAVY}"/>'
    b += f'<circle cx="800" cy="260" r="110" fill="{AMB}"/><path d="M800,200 l20,40 44,6 -32,31 8,44 -40,-21 -40,21 8,-44 -32,-31 44,-6 z" fill="#fff"/>'
    return wrap(CREAM, b, "Two hands shaking in partnership")


def masjid():
    b = blobs((1300, 180, 280, YEL, .55))
    b += f'<rect x="0" y="720" width="1600" height="180" fill="{GREEN}" opacity=".5"/>'
    b += f'<rect x="420" y="430" width="760" height="300" fill="#fff"/><path d="M560,430 C560,250 1040,250 1040,430 Z" fill="{TEAL}"/>'
    b += f'<rect x="300" y="250" width="70" height="480" fill="#fff"/><path d="M290,250 L335,170 L380,250 Z" fill="{TEAL}"/>'
    b += f'<rect x="1230" y="250" width="70" height="480" fill="#fff"/><path d="M1220,250 L1265,170 L1310,250 Z" fill="{TEAL}"/>'
    for i in range(5):
        b += f'<path d="M{480+i*140},730 V600 C{480+i*140},560 {560+i*140},560 {560+i*140},600 V730 Z" fill="{NAVY}" opacity=".85"/>'
    b += f'<path d="M800,250 v-40" stroke="{AMB}" stroke-width="8"/><circle cx="800" cy="200" r="14" fill="{AMB}"/>'
    b += person(160, 900, .8, 1, CORAL) + person(1450, 900, .8, 3, LAV, hijab=NAVY)
    return wrap(SKY, b, "A welcoming masjid building")


def family():
    b = blobs((1300, 200, 360, YEL, .45), (240, 760, 300, SKY, .55))
    b += f'<path d="M300,900 V520 L800,220 L1300,520 V900 Z" fill="#fff"/><path d="M240,540 L800,190 L1360,540" stroke="{CORAL}" stroke-width="40" fill="none" stroke-linejoin="round"/>'
    b += f'<rect x="1040" y="580" width="140" height="140" fill="{SKY}"/><path d="M1110,580 v140 M1040,650 h140" stroke="#fff" stroke-width="10"/>'
    b += person(560, 900, 1.05, 4, BLUE) + person(800, 900, 1.0, 4, TEAL, hijab=LAVD) + person(690, 900, .6, 4, AMB) + person(950, 900, .55, 4, CORAL, hair="#111")
    return wrap(ARC, b, "A family in front of their home")


def heart():
    b = blobs((250, 200, 300, SKY, .6), (1350, 760, 340, LAV, .35))
    b += f'<path d="M800,780 C520,600 380,470 380,330 C380,220 470,150 570,150 C670,150 740,210 800,290 C860,210 930,150 1030,150 C1130,150 1220,220 1220,330 C1220,470 1080,600 800,780 Z" fill="{CORAL}"/>'
    b += f'<path d="M560,560 C640,610 720,620 800,600" stroke="{SKIN[2]}" stroke-width="70" fill="none" stroke-linecap="round"/>'
    b += f'<path d="M1040,560 C960,610 880,620 800,600" stroke="{SKIN[0]}" stroke-width="70" fill="none" stroke-linecap="round"/>'
    b += f'<circle cx="800" cy="400" r="60" fill="{AMB}"/><text x="800" y="428" font-family="Arial" font-weight="700" font-size="80" fill="#fff" text-anchor="middle">$</text>'
    return wrap(CREAM, b, "Hands holding a heart")


def writing():
    b = blobs((1300, 700, 320, YEL, .45), (250, 180, 240, SKY, .6))
    b += f'<rect x="420" y="160" width="760" height="560" rx="16" fill="#fff" transform="rotate(-3 800 440)"/>'
    b += f'<g transform="rotate(-3 800 440)" font-family="Arial" font-weight="700"><text x="480" y="260" font-size="54" fill="{NAVY}">Résumé</text>'
    for i in range(7):
        b += f'<rect x="480" y="{310+i*52}" width="{560-(i%3)*90}" height="18" rx="9" fill="{[LIGHT, SKY, ARC][i%3]}"/>'
    b += '</g>'
    b += f'<g transform="translate(1120 180) rotate(35)"><rect width="36" height="360" rx="10" fill="{AMB}"/><path d="M0,360 L18,410 L36,360 Z" fill="#333"/></g>'
    b += person(240, 900, 1.0, 5, TEAL, hair="#111")
    return wrap(ARC, b, "Writing a résumé")


def portrait(i):
    colors = [BLUE, TEAL, CORAL, LAVD, AMB, NAVY]
    hj = [None, LAVD, None, TEAL, None, CORAL][i % 6]
    b = f'<circle cx="800" cy="450" r="600" fill="{[SKY, ARC, "#ffe7a3", "#d9dcf7"][i % 4]}"/>' + person(800, 1000, 2.2, i, colors[i % 6], hijab=hj)
    return wrap(ARC, b, "Portrait placeholder")


SCENES = {
    "classroom": classroom, "money": money, "passport": passport, "tools": tools, "pantry": pantry,
    "community": community, "heritage": heritage, "volunteers": volunteers, "partners": partners,
    "masjid": masjid, "family": family, "heart": heart, "writing": writing,
}
