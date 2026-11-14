import html, os
OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
BG, CARD, LINE = "#0d1117", "#111827", "#243044"
BLUE, CYAN, VIOLET = "#4a90d9", "#22d3ee", "#8b5cf6"
WHITE, MUTED, GREEN = "#f0f6fc", "#8b9bb4", "#7ee787"
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Courier New',monospace"
e = html.escape

DEFS = f'''<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{BLUE}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
<linearGradient id="fadeline" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".8"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>
<radialGradient id="glow1" cx=".15" cy=".1" r=".7"><stop offset="0" stop-color="{BLUE}" stop-opacity=".30"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2" cx=".95" cy=".95" r=".6"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".28"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
</defs>'''

def svg(w, h, body, name):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">\n{DEFS}\n{body}\n</svg>')

def panel(w, h, rx=20, glow=True):
    s = f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="{CARD}" stroke="url(#g)" stroke-width="1.5"/>'
    if glow:
        s += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="url(#glow1)"/>'
        s += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="url(#glow2)"/>'
    return s

def pill(x, y, text, color=BLUE, size=12):
    w = len(text) * size * 0.62 + 24
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{color}" fill-opacity=".12" stroke="{color}" stroke-opacity=".55"/>'
            f'<text x="{x+w/2:.0f}" y="{y+17}" text-anchor="middle" font-family="{MONO}" font-size="{size}" fill="{WHITE}">{e(text)}</text>'), w

def pills(x, y, items):
    out = ""
    for t in items:
        s, w = pill(x, y, t); out += s; x += w + 8
    return out

# ---------------- HEADER ----------------
b = panel(900, 300, 24)
b += f'<text x="48" y="62" font-family="{MONO}" font-size="13" fill="{CYAN}" letter-spacing="2">~/diego-mantilla</text>'
b += f'<text x="46" y="132" font-family="{SANS}" font-size="58" font-weight="800" fill="{WHITE}">Diego Mantilla</text>'
b += f'<text x="48" y="172" font-family="{SANS}" font-size="22" font-weight="600" fill="url(#g)">Junior Software Engineer</text>'
b += f'<text x="48" y="204" font-family="{SANS}" font-size="16" fill="{MUTED}">I build SaaS products with AI built in.</text>'
b += pills(48, 232, ["React", "Python", "MySQL", "Docker"])
# code panel
px, py, pw, ph = 548, 44, 310, 212
b += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="14" fill="{BG}" stroke="{LINE}"/>'
b += f'<path d="M{px} {py+14} a14 14 0 0 1 14 -14 h{pw-28} a14 14 0 0 1 14 14 v22 h-{pw} z" fill="#161f30"/>'
for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    b += f'<circle cx="{px+20+i*18}" cy="{py+18}" r="5" fill="{c}"/>'
b += f'<text x="{px+pw-16}" y="{py+22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}">profile.js</text>'
def line(n, indent, parts):
    y = py + 62 + n * 22
    t = f'<text x="{px+18}" y="{y}" font-family="{MONO}" font-size="12" fill="#4b5a73">{n+1}</text>'
    t += f'<text x="{px+40+indent*8}" y="{y}" font-family="{MONO}" font-size="13">'
    t += "".join(f'<tspan fill="{c}">{e(x)}</tspan>' for x, c in parts)
    return t + '</text>'
lines = [
    (0, [("const ", VIOLET), ("diego ", WHITE), ("= {", WHITE)]),
    (2, [("role", BLUE), (": ", WHITE), ('"Junior Engineer"', GREEN), (",", WHITE)]),
    (2, [("focus", BLUE), (": ", WHITE), ('["SaaS", "AI"]', GREEN), (",", WHITE)]),
    (2, [("stack", BLUE), (": ", WHITE), ('["React", "Python"]', GREEN), (",", WHITE)]),
    (2, [("location", BLUE), (": ", WHITE), ('"Colombia"', GREEN), (",", WHITE)]),
    (2, [("openToWork", BLUE), (": ", WHITE), ("true", CYAN), (",", WHITE)]),
    (0, [("};", WHITE)]),
]
for i, (ind, l) in enumerate(lines):
    b += line(i, ind, l)
svg(900, 300, b, "header.svg")

# ---------------- SECTION BARS ----------------
def section(num, title, name):
    tw = 100 + len(title) * 15
    b = f'<rect x="1" y="1" width="898" height="54" rx="14" fill="{CARD}" stroke="{LINE}"/>'
    b += f'<rect x="12" y="11" width="34" height="34" rx="9" fill="url(#g)"/>'
    b += f'<text x="29" y="33" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="{BG}">{num}</text>'
    b += f'<text x="60" y="37" font-family="{SANS}" font-size="24" font-weight="700" fill="{WHITE}">{e(title)}</text>'
    b += f'<line x1="{tw}" y1="28" x2="880" y2="28" stroke="url(#fadeline)" stroke-width="2" stroke-linecap="round"/>'
    svg(900, 56, b, name)

section("01", "Projects", "section-projects.svg")
section("02", "Stack", "section-stack.svg")
section("03", "Contact", "section-contact.svg")

# ---------------- PROJECT CARDS (2x2 bento) ----------------
def project(name, glyph, title, l1, l2, tech, status, dot):
    w, h = 446, 226
    b = panel(w, h, 20)
    b += f'<rect x="24" y="24" width="46" height="46" rx="13" fill="url(#g)" fill-opacity=".18" stroke="url(#g)"/>'
    b += f'<text x="47" y="54" text-anchor="middle" font-family="{MONO}" font-size="17" font-weight="700" fill="{WHITE}">{e(glyph)}</text>'
    sw = len(status) * 8.6 + 40
    b += f'<rect x="{w-24-sw:.0f}" y="31" width="{sw:.0f}" height="26" rx="13" fill="{BG}" stroke="{LINE}"/>'
    b += f'<circle cx="{w-24-sw+16:.0f}" cy="44" r="4" fill="{dot}"/>'
    b += f'<text x="{w-24-sw+27:.0f}" y="48" font-family="{MONO}" font-size="11" fill="{MUTED}" letter-spacing="1">{e(status)}</text>'
    b += f'<text x="24" y="108" font-family="{SANS}" font-size="25" font-weight="800" fill="{WHITE}">{e(title)}</text>'
    b += f'<text x="24" y="134" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l1)}</text>'
    b += f'<text x="24" y="153" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l2)}</text>'
    b += pills(24, 178, tech)
    b += f'<circle cx="{w-40}" cy="{h-40}" r="16" fill="url(#g)"/>'
    b += f'<path d="M{w-46} {h-34} L{w-34} {h-46} M{w-44} {h-46} H{w-34} V{h-36}" stroke="{BG}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    svg(w, h, b, f"project-{name}.svg")

project("deliverybot", "</>", "DeliveryBot", "Cafeteria ordering over Telegram, run by an n8n", "workflow and logged in Google Sheets.", ["n8n", "Telegram", "Sheets"], "WORKFLOW", CYAN)
project("portfolio", "{ }", "Portfolio", "Responsive personal site with my work,", "built with React and deployed on Vercel.", ["React", "Vite", "Tailwind"], "LIVE", GREEN)
project("pizzeria-db", "DB", "Pizzeria DB", "Relational model for restaurant operations:", "normalization, FKs and reporting queries.", ["MySQL", "SQL"], "DATABASE", BLUE)
project("next", "AI", "Next: SaaS + AI", "A product in progress that pairs a solid backend", "with AI features that solve a real problem.", ["Python", "LLM APIs"], "IN PROGRESS", "#febc2e")

# ---------------- CONTACT ----------------
b = panel(900, 170, 24)
b += f'<text x="48" y="64" font-family="{MONO}" font-size="13" fill="{CYAN}" letter-spacing="2">// available</text>'
b += f'<text x="46" y="108" font-family="{SANS}" font-size="38" font-weight="800" fill="{WHITE}">Have an idea? Let\'s talk.</text>'
b += f'<text x="48" y="138" font-family="{SANS}" font-size="16" fill="{MUTED}">Open to junior software engineer roles and collaborations.</text>'
for r, o in [(70, .10), (50, .16), (30, .24)]:
    b += f'<circle cx="790" cy="85" r="{r}" fill="none" stroke="url(#g)" stroke-opacity="{o*3:.2f}" stroke-width="1.5"/>'
b += f'<circle cx="790" cy="85" r="18" fill="url(#g)"/>'
b += f'<path d="M782 93 L798 77 M784 77 H798 V91" stroke="{BG}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
svg(900, 170, b, "contact.svg")
print(sorted(os.listdir(OUT)))
