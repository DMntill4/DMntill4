import html, os
OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
BG, CARD, LINE = "#070b14", "#0c1322", "#1e293b"
BLUE, CYAN, VIOLET = "#3b82f6", "#06b6d4", "#6366f1"
WHITE, MUTED, GREEN = "#f8fafc", "#94a3b8", "#34d399"
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Courier New',monospace"
e = html.escape

DEFS = f'''<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#38bdf8"/><stop offset=".5" stop-color="#3b82f6"/><stop offset="1" stop-color="#6366f1"/></linearGradient>
<linearGradient id="fadeline" x1="0" x2="1"><stop offset="0" stop-color="#38bdf8" stop-opacity=".85"/><stop offset="1" stop-color="#6366f1" stop-opacity="0"/></linearGradient>
<radialGradient id="glow1" cx=".15" cy=".1" r=".75"><stop offset="0" stop-color="#38bdf8" stop-opacity=".22"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2" cx=".92" cy=".92" r=".65"><stop offset="0" stop-color="#3b82f6" stop-opacity=".24"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>
<pattern id="dotgrid" width="22" height="22" patternUnits="userSpaceOnUse">
  <circle cx="2" cy="2" r="1" fill="#38bdf8" fill-opacity="0.09"/>
</pattern>
<pattern id="diag" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
  <line x1="0" y1="0" x2="0" y2="12" stroke="#38bdf8" stroke-opacity="0.04" stroke-width="1"/>
</pattern>
</defs>'''

def svg(w, h, body, name):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">\n{DEFS}\n{body}\n</svg>')

def panel(w, h, rx=20, glow=True, shadow_color="#38bdf8"):
    # Neo-brutalist / Cartoon Tech hard drop-shadow + thick border
    s = f'<rect x="6" y="6" width="{w-8}" height="{h-8}" rx="{rx}" fill="{shadow_color}" fill-opacity="0.22"/>'
    s += f'<rect x="2" y="2" width="{w-8}" height="{h-8}" rx="{rx}" fill="{CARD}" stroke="url(#g)" stroke-width="2.5"/>'
    s += f'<rect x="2" y="2" width="{w-8}" height="{h-8}" rx="{rx}" fill="url(#dotgrid)"/>'
    if glow:
        s += f'<rect x="2" y="2" width="{w-8}" height="{h-8}" rx="{rx}" fill="url(#glow1)"/>'
        s += f'<rect x="2" y="2" width="{w-8}" height="{h-8}" rx="{rx}" fill="url(#glow2)"/>'
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
def get_icon(icon_type):
    # Cartoon/clean vector icons inside the 46x46 badge (centered at x=47, y=47)
    if icon_type == "bot":
        # Cute robot / AI spark
        return (f'<rect x="33" y="36" width="28" height="22" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2.2"/>'
                f'<line x1="47" y1="36" x2="47" y2="30" stroke="#38bdf8" stroke-width="2.2" stroke-linecap="round"/>'
                f'<circle cx="47" cy="29" r="2.5" fill="#38bdf8"/>'
                f'<circle cx="41" cy="46" r="2.8" fill="#38bdf8"/>'
                f'<circle cx="53" cy="46" r="2.8" fill="#38bdf8"/>'
                f'<line x1="42" y1="53" x2="52" y2="53" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>')
    elif icon_type == "eye":
        # Biometric scanner eye
        return (f'<path d="M31 47 Q47 33 63 47 Q47 61 31 47 Z" fill="#0f172a" stroke="#34d399" stroke-width="2.2" stroke-linejoin="round"/>'
                f'<circle cx="47" cy="47" r="6" fill="none" stroke="#34d399" stroke-width="2.2"/>'
                f'<circle cx="47" cy="47" r="2.2" fill="#34d399"/>')
    elif icon_type == "gear":
        # Enterprise wrench / gear
        return (f'<circle cx="47" cy="47" r="10" fill="none" stroke="#fbbf24" stroke-width="2.4" stroke-dasharray="4 3"/>'
                f'<circle cx="47" cy="47" r="4.5" fill="#fbbf24"/>')
    elif icon_type == "chef":
        # Restora SaaS dish / leaf / sparkles
        return (f'<path d="M35 52 H59 M38 52 C38 41 56 41 56 52" fill="#0f172a" stroke="#a855f7" stroke-width="2.2" stroke-linecap="round"/>'
                f'<circle cx="47" cy="39" r="2" fill="#a855f7"/>')
    return f'<text x="47" y="54" text-anchor="middle" font-family="{MONO}" font-size="17" font-weight="700" fill="{WHITE}">{e(icon_type)}</text>'

def project(name, icon_type, title, l1, l2, tech, status, dot, is_wip=False):
    w, h = 446, 226
    b = panel(w, h, 20, shadow_color=dot)
    # Icon box with cartoon shadow
    b += f'<rect x="27" y="27" width="46" height="46" rx="13" fill="{dot}" fill-opacity="0.25"/>'
    b += f'<rect x="24" y="24" width="46" height="46" rx="13" fill="#0b1220" stroke="{dot}" stroke-width="2.2"/>'
    b += get_icon(icon_type)
    sw = len(status) * 8.6 + 40
    b += f'<rect x="{w-26-sw:.0f}" y="31" width="{sw:.0f}" height="26" rx="13" fill="{BG}" stroke="{dot}" stroke-opacity="0.6" stroke-width="1.5"/>'
    b += f'<circle cx="{w-26-sw+16:.0f}" cy="44" r="4.5" fill="{dot}"/>'
    b += f'<text x="{w-26-sw+27:.0f}" y="48" font-family="{MONO}" font-size="11" font-weight="700" fill="{WHITE}" letter-spacing="1">{e(status)}</text>'
    b += f'<text x="24" y="108" font-family="{SANS}" font-size="25" font-weight="800" fill="{WHITE}">{e(title)}</text>'
    b += f'<text x="24" y="134" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l1)}</text>'
    b += f'<text x="24" y="153" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l2)}</text>'
    b += pills(24, 178, tech)
    
    if is_wip:
        b += f'<circle cx="{w-42}" cy="{h-42}" r="16" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>'
        b += f'<rect x="{w-48}" y="{h-42}" width="12" height="10" rx="2" fill="none" stroke="{MUTED}" stroke-width="2"/>'
        b += f'<path d="M{w-46} {h-42} v-3 a4 4 0 0 1 8 0 v3" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>'
    else:
        b += f'<circle cx="{w-40}" cy="{h-40}" r="16" fill="{dot}" fill-opacity="0.25"/>'
        b += f'<circle cx="{w-42}" cy="{h-42}" r="16" fill="url(#g)"/>'
        b += f'<path d="M{w-48} {h-36} L{w-36} {h-48} M{w-46} {h-48} H{w-36} V{h-38}" stroke="{BG}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    svg(w, h, b, f"project-{name}.svg")

project("ai-back-office", "bot", "AI Back Office", "Autonomous ReAct agent for procurement & logistics", "with Grok xAI, Supabase PG & Drizzle ORM.", ["Grok", "TypeScript", "PostgreSQL", "Fastify"], "AGENT", CYAN)
project("sica", "eye", "SICA: Access Control", "Hexagonal Java 21 architecture + 128D facial AI", "biometrics, web self-service & Swing GUI.", ["Java 21", "Computer Vision", "JWT", "MySQL"], "ENTERPRISE", GREEN)
project("opus-rentals", "gear", "Opus Rentals", "Full-stack rental platform: Spring Boot 3, DDD,", "4NF relational DB and responsive web client.", ["Java 21", "Spring Boot", "MySQL", "Docker"], "ENTERPRISE", "#fbbf24")
project("restora", "chef", "Restora (SaaS B2B)", "Multi-tenant restaurant ops & anti-waste inventory", "with FEFO engine, WhatsApp alerts & AI OCR.", ["Java 21", "Spring Boot", "FastAPI", "React"], "WORK IN PROGRESS", "#a855f7", is_wip=True)

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
    
    # Clean Modern Cat Silhouette (just ears + contour + aggressive glowing eyes)
    # Centered at (cx + 135, cy + 88)
    cat_cx, cat_cy = cx + 135, cy + 86
    
    # Sleek minimal cat head silhouette (single continuous path matching reference shape)
    b += f'''<path d="M {cat_cx-32} {cat_cy-6}
                     C {cat_cx-31} {cat_cy-22}, {cat_cx-26} {cat_cy-35}, {cat_cx-22} {cat_cy-39}
                     C {cat_cx-20} {cat_cy-41}, {cat_cx-12} {cat_cy-32}, {cat_cx-8} {cat_cy-26}
                     C {cat_cx-3} {cat_cy-28}, {cat_cx+3} {cat_cy-28}, {cat_cx+8} {cat_cy-26}
                     C {cat_cx+12} {cat_cy-32}, {cat_cx+20} {cat_cy-41}, {cat_cx+22} {cat_cy-39}
                     C {cat_cx+26} {cat_cy-35}, {cat_cx+31} {cat_cy-22}, {cat_cx+32} {cat_cy-6}
                     C {cat_cx+34} {cat_cy+14}, {cat_cx+18} {cat_cy+26}, {cat_cx} {cat_cy+26}
                     C {cat_cx-18} {cat_cy+26}, {cat_cx-34} {cat_cy+14}, {cat_cx-32} {cat_cy-6} Z"
                  fill="#060911" stroke="url(#g)" stroke-width="2.2"/>'''
                  
    # Sharp aggressive slanted eyes inside the silhouette
    b += f'<polygon points="{cat_cx-20},{cat_cy-6} {cat_cx-6},{cat_cy-1} {cat_cx-16},{cat_cy+4}" fill="#38bdf8"/>'
    b += f'<polygon points="{cat_cx+20},{cat_cy-6} {cat_cx+6},{cat_cy-1} {cat_cx+16},{cat_cy+4}" fill="#38bdf8"/>'
    
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
    b += f'<text x="{gx+gw-20}" y="{gy+32}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{GREEN}">⚡ {total_commits} contributions in the last year</text>'
    
    # Render commit graph grid (last 42 weeks to fit cleanly)
    # 7 rows (weekdays), square size 9px, spacing 2.5px
    disp_weeks = weeks_data[-42:] if len(weeks_data) >= 42 else weeks_data
    start_grid_x = gx + 20
    start_grid_y = gy + 52
    sq = 9.5
    gap = 3
    
    def get_color(cnt):
        if cnt == 0: return "#161f30"
        if cnt <= 2: return "#0e4429"
        if cnt <= 5: return "#006d32"
        if cnt <= 9: return "#26a641"
        return "#39d353"
        
    for c_idx, w_obj in enumerate(disp_weeks):
        col_x = start_grid_x + c_idx * (sq + gap)
        for day in w_obj.get('contributionDays', []):
            row_y = start_grid_y + day['weekday'] * (sq + gap)
            color = get_color(day['contributionCount'])
            b += f'<rect x="{col_x:.1f}" y="{row_y:.1f}" width="{sq}" height="{sq}" rx="2" fill="{color}"/>'
            
    # Legend below graph
    b += f'<text x="{start_grid_x}" y="{gy+gh-22}" font-family="{MONO}" font-size="11" fill="{MUTED}">Less</text>'
    for idx, col in enumerate(["#161f30", "#0e4429", "#006d32", "#26a641", "#39d353"]):
        lx = start_grid_x + 38 + idx * 14
        b += f'<rect x="{lx}" y="{gy+gh-30}" width="10" height="10" rx="2" fill="{col}"/>'
    b += f'<text x="{start_grid_x+116}" y="{gy+gh-22}" font-family="{MONO}" font-size="11" fill="{MUTED}">More</text>'
    b += f'<text x="{gx+gw-20}" y="{gy+gh-22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{CYAN}">github.com/DMntill4</text>'
    
    svg(w, h, b, "activity-card.svg")

build_activity_card()
print(sorted(os.listdir(OUT)))
