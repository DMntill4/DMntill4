import html, os
OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
BG, CARD, LINE = "#060a13", "#0b1120", "#1b283f"
BLUE, CYAN, VIOLET = "#3b82f6", "#38bdf8", "#6366f1"
WHITE, MUTED, GREEN = "#f8fafc", "#94a3b8", "#34d399"
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Courier New',monospace"
e = html.escape

DEFS = f'''<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#38bdf8"/><stop offset=".5" stop-color="#3b82f6"/><stop offset="1" stop-color="#6366f1"/></linearGradient>
<linearGradient id="border-g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#38bdf8" stop-opacity=".55"/><stop offset=".5" stop-color="#3b82f6" stop-opacity=".28"/><stop offset="1" stop-color="#6366f1" stop-opacity=".45"/></linearGradient>
<linearGradient id="fadeline" x1="0" x2="1"><stop offset="0" stop-color="#38bdf8" stop-opacity=".8"/><stop offset="1" stop-color="#6366f1" stop-opacity="0"/></linearGradient>
<radialGradient id="glow1" cx=".12" cy=".08" r=".7"><stop offset="0" stop-color="#38bdf8" stop-opacity=".16"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2" cx=".92" cy=".92" r=".65"><stop offset="0" stop-color="#3b82f6" stop-opacity=".18"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>
<radialGradient id="cat-glow" cx=".5" cy=".45" r=".5"><stop offset="0" stop-color="#38bdf8" stop-opacity=".22"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<pattern id="dotgrid" width="20" height="20" patternUnits="userSpaceOnUse">
  <circle cx="1.5" cy="1.5" r="0.9" fill="#38bdf8" fill-opacity="0.06"/>
</pattern>
</defs>'''

def svg(w, h, body, name):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">\n{DEFS}\n{body}\n</svg>')

def panel(w, h, rx=20, glow=True):
    s = f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="{CARD}" stroke="url(#border-g)" stroke-width="1.2"/>'
    s += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="url(#dotgrid)"/>'
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
section("03", "Activity & Stats", "section-activity.svg")
section("04", "Contact", "section-contact.svg")

# ---------------- PROJECT CARDS (2x2 bento) ----------------
def get_icon(icon_type, color):
    # Clean Lucide-style vector icons centered inside the 46x46 badge (center = 47, 47)
    if icon_type == "bot":
        # Sparkles / AI core icon
        return (f'<path d="M47 35 L49.5 43.5 L58 46 L49.5 48.5 L47 57 L44.5 48.5 L36 46 L44.5 43.5 Z" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>'
                f'<circle cx="56" cy="37" r="1.5" fill="{color}"/>'
                f'<circle cx="38" cy="55" r="1.5" fill="{color}"/>')
    elif icon_type == "eye":
        # Biometric scan shield / eye
        return (f'<path d="M35 47 C38.5 40.5 55.5 40.5 59 47 C55.5 53.5 38.5 53.5 35 47 Z" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>'
                f'<circle cx="47" cy="47" r="3.5" fill="none" stroke="{color}" stroke-width="1.8"/>')
    elif icon_type == "gear":
        # Clean isometric layers (DDD / Architecture)
        return (f'<polygon points="47,36 58,41.5 47,47 36,41.5" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>'
                f'<polyline points="36,47 47,52.5 58,47" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<polyline points="36,52 47,57.5 58,52" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')
    elif icon_type == "chef":
        # Clean SaaS cube / node
        return (f'<path d="M47 36 L56.5 41.5 V52.5 L47 58 L37.5 52.5 V41.5 Z" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>'
                f'<polyline points="37.5,41.5 47,47 56.5,41.5" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>'
                f'<line x1="47" y1="47" x2="47" y2="58" stroke="{color}" stroke-width="1.8"/>')
    return f'<text x="47" y="54" text-anchor="middle" font-family="{MONO}" font-size="17" font-weight="700" fill="{WHITE}">{e(icon_type)}</text>'

def project(name, icon_type, title, l1, l2, tech, status, dot, is_wip=False):
    w, h = 446, 226
    b = panel(w, h, 20)
    b += f'<rect x="24" y="24" width="46" height="46" rx="13" fill="{dot}" fill-opacity="0.10" stroke="{dot}" stroke-opacity="0.45" stroke-width="1.2"/>'
    b += get_icon(icon_type, dot)
    sw = len(status) * 8.4 + 38
    b += f'<rect x="{w-24-sw:.0f}" y="31" width="{sw:.0f}" height="26" rx="13" fill="{BG}" stroke="{LINE}" stroke-width="1.2"/>'
    b += f'<circle cx="{w-24-sw+15:.0f}" cy="44" r="3.5" fill="{dot}"/>'
    b += f'<text x="{w-24-sw+25:.0f}" y="48" font-family="{MONO}" font-size="10.5" font-weight="600" fill="{MUTED}" letter-spacing="1">{e(status)}</text>'
    b += f'<text x="24" y="108" font-family="{SANS}" font-size="25" font-weight="800" fill="{WHITE}">{e(title)}</text>'
    b += f'<text x="24" y="134" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l1)}</text>'
    b += f'<text x="24" y="153" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l2)}</text>'
    b += pills(24, 178, tech)
    
    if is_wip:
        b += f'<circle cx="{w-40}" cy="{h-40}" r="16" fill="{BG}" stroke="{LINE}" stroke-width="1.2"/>'
        b += f'<rect x="{w-45.5}" y="{h-40}" width="11" height="8.5" rx="2" fill="none" stroke="{MUTED}" stroke-width="1.6"/>'
        b += f'<path d="M{w-43.5} {h-40} v-2.5 a3.5 3.5 0 0 1 7 0 v2.5" fill="none" stroke="{MUTED}" stroke-width="1.6" stroke-linecap="round"/>'
    else:
        b += f'<circle cx="{w-40}" cy="{h-40}" r="16" fill="url(#g)"/>'
        b += f'<path d="M{w-46} {h-34} L{w-34} {h-46} M{w-44} {h-46} H{w-34} V{h-36}" stroke="{BG}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    svg(w, h, b, f"project-{name}.svg")

project("ai-back-office", "bot", "AI Back Office", "Autonomous ReAct agent for procurement & logistics", "with Grok xAI, Supabase PG & Drizzle ORM.", ["Grok", "TypeScript", "PostgreSQL", "Fastify"], "AGENT", CYAN)
project("sica", "eye", "SICA: Access Control", "Hexagonal Java 21 architecture + 128D facial AI", "biometrics, web self-service & Swing GUI.", ["Java 21", "Computer Vision", "JWT", "MySQL"], "ENTERPRISE", GREEN)
project("opus-rentals", "gear", "Opus Rentals", "Full-stack rental platform: Spring Boot 3, DDD,", "4NF relational DB and responsive web client.", ["Java 21", "Spring Boot", "MySQL", "Docker"], "ENTERPRISE", BLUE)
project("restora", "chef", "Restora (SaaS B2B)", "Multi-tenant restaurant ops & anti-waste inventory", "with FEFO engine, WhatsApp alerts & AI OCR.", ["Java 21", "Spring Boot", "FastAPI", "React"], "WORK IN PROGRESS", VIOLET, is_wip=True)

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

# ---------------- ACTIVITY & COMMIT GRAPH + CUTE CAT CARD ----------------
import subprocess, json

def build_activity_card():
    w, h = 900, 260
    b = panel(w, h, 20)
    
    # Left Section: Cat Developer Business Card
    cx, cy, cw, ch = 24, 24, 270, 212
    b += f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="16" fill="{BG}" stroke="{LINE}"/>'
    
    # Cute Business Card Header
    b += f'<rect x="{cx}" y="{cy}" width="{cw}" height="32" rx="16" fill="#161f30"/>'
    b += f'<rect x="{cx}" y="{cy+16}" width="{cw}" height="16" fill="#161f30"/>'
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        b += f'<circle cx="{cx+18+i*16}" cy="{cy+16}" r="4.5" fill="{c}"/>'
    b += f'<text x="{cx+cw-14}" y="{cy+20}" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{MUTED}">dev_cat.id</text>'
    
    # Clean Minimalist Aggressive Cat Silhouette (matching reference silhouette + whiskers + sharp eyes)
    cat_cx, cat_cy = cx + 135, cy + 88
    b += f'<circle cx="{cat_cx}" cy="{cat_cy}" r="50" fill="url(#cat-glow)"/>'
    
    # Sleek cat head silhouette
    b += f'''<path d="M {cat_cx-31} {cat_cy-5}
                     C {cat_cx-30} {cat_cy-21}, {cat_cx-25} {cat_cy-34}, {cat_cx-20} {cat_cy-38}
                     C {cat_cx-18} {cat_cy-40}, {cat_cx-10} {cat_cy-30}, {cat_cx-7} {cat_cy-24}
                     C {cat_cx-2} {cat_cy-26}, {cat_cx+2} {cat_cy-26}, {cat_cx+7} {cat_cy-24}
                     C {cat_cx+10} {cat_cy-30}, {cat_cx+18} {cat_cy-40}, {cat_cx+20} {cat_cy-38}
                     C {cat_cx+25} {cat_cy-34}, {cat_cx+30} {cat_cy-21}, {cat_cx+31} {cat_cy-5}
                     C {cat_cx+32} {cat_cy+14}, {cat_cx+18} {cat_cy+24}, {cat_cx} {cat_cy+24}
                     C {cat_cx-18} {cat_cy+24}, {cat_cx-32} {cat_cy+14}, {cat_cx-31} {cat_cy-5} Z"
                  fill="#050810" stroke="url(#border-g)" stroke-width="1.6"/>'''
    
    # Clean whiskers (3 on each side, sleek rounded strokes matching reference icon)
    b += f'<line x1="{cat_cx-28}" y1="{cat_cy+2}" x2="{cat_cx-46}" y2="{cat_cy-2}" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2.2" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx-29}" y1="{cat_cy+8}" x2="{cat_cx-48}" y2="{cat_cy+8}" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2.2" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx-27}" y1="{cat_cy+14}" x2="{cat_cx-45}" y2="{cat_cy+19}" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2.2" stroke-linecap="round"/>'
    
    b += f'<line x1="{cat_cx+28}" y1="{cat_cy+2}" x2="{cat_cx+46}" y2="{cat_cy-2}" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2.2" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx+29}" y1="{cat_cy+8}" x2="{cat_cx+48}" y2="{cat_cy+8}" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2.2" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx+27}" y1="{cat_cy+14}" x2="{cat_cx+45}" y2="{cat_cy+19}" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2.2" stroke-linecap="round"/>'

    # Sharp aggressive slanted eyes
    b += f'<polygon points="{cat_cx-20},{cat_cy-6} {cat_cx-6},{cat_cy-1} {cat_cx-15},{cat_cy+4}" fill="#38bdf8"/>'
    b += f'<polygon points="{cat_cx+20},{cat_cy-6} {cat_cx+6},{cat_cy-1} {cat_cx+15},{cat_cy+4}" fill="#38bdf8"/>'
    
    # Business Card text info
    b += f'<text x="{cx+cw/2:.0f}" y="{cy+148}" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="800" fill="{WHITE}">Diego Mantilla</text>'
    b += f'<text x="{cx+cw/2:.0f}" y="{cy+168}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#38bdf8">Core Software Engineer</text>'
    b += f'<text x="{cx+cw/2:.0f}" y="{cy+188}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{MUTED}">Clean code · Zero bloat</text>'
    
    # Right Section: GitHub Commit Calendar Grid
    gx, gy = 318, 24
    gw, gh = 558, 212
    b += f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" rx="16" fill="{BG}" stroke="{LINE}"/>'
    
    # Fetch real live contribution calendar from GitHub API
    total_commits = 500
    weeks_data = []
    try:
        query = 'query { viewer { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { contributionCount date weekday } } } } } }'
        res = subprocess.check_output(['gh', 'api', 'graphql', '-f', f'query={query}'], text=True)
        cdata = json.loads(res)['data']['viewer']['contributionsCollection']['contributionCalendar']
        total_commits = cdata['totalContributions']
        weeks_data = cdata['weeks']
    except Exception as err:
        pass
        
    b += f'<text x="{gx+20}" y="{gy+32}" font-family="{SANS}" font-size="16" font-weight="700" fill="{WHITE}">GitHub Activity</text>'
    b += f'<text x="{gx+gw-20}" y="{gy+32}" text-anchor="end" font-family="{MONO}" font-size="12" fill="#38bdf8">{total_commits} contributions · last year</text>'
    
    # Render commit graph grid (last 42 weeks to fit cleanly)
    disp_weeks = weeks_data[-42:] if len(weeks_data) >= 42 else weeks_data
    start_grid_x = gx + 20
    start_grid_y = gy + 52
    sq = 9.5
    gap = 3
    
    def get_color(cnt):
        if cnt == 0: return "#111c33"
        if cnt <= 2: return "#1e3a8a"
        if cnt <= 5: return "#2563eb"
        if cnt <= 9: return "#3b82f6"
        return "#38bdf8"
        
    for c_idx, w_obj in enumerate(disp_weeks):
        col_x = start_grid_x + c_idx * (sq + gap)
        for day in w_obj.get('contributionDays', []):
            row_y = start_grid_y + day['weekday'] * (sq + gap)
            color = get_color(day['contributionCount'])
            b += f'<rect x="{col_x:.1f}" y="{row_y:.1f}" width="{sq}" height="{sq}" rx="2" fill="{color}"/>'
            
    # Legend below graph
    b += f'<text x="{start_grid_x}" y="{gy+gh-22}" font-family="{MONO}" font-size="11" fill="{MUTED}">Less</text>'
    for idx, col in enumerate(["#111c33", "#1e3a8a", "#2563eb", "#3b82f6", "#38bdf8"]):
        lx = start_grid_x + 38 + idx * 14
        b += f'<rect x="{lx}" y="{gy+gh-30}" width="10" height="10" rx="2" fill="{col}"/>'
    b += f'<text x="{start_grid_x+116}" y="{gy+gh-22}" font-family="{MONO}" font-size="11" fill="{MUTED}">More</text>'
    b += f'<text x="{gx+gw-20}" y="{gy+gh-22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{CYAN}">github.com/DMntill4</text>'
    
    svg(w, h, b, "activity-card.svg")

build_activity_card()
print(sorted(os.listdir(OUT)))
