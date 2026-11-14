import html, os
OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
BG, CARD, LINE = "#060911", "#0b1120", "#1e293b"
BLUE, CYAN, VIOLET = "#3b82f6", "#38bdf8", "#6366f1"
WHITE, MUTED, GREEN = "#f8fafc", "#94a3b8", "#34d399"
SANS = "-apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',sans-serif"
MONO = "'SF Mono','SFMono-Regular',Consolas,'Courier New',monospace"
e = html.escape

DEFS = f'''<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#38bdf8"/><stop offset=".55" stop-color="#3b82f6"/><stop offset="1" stop-color="#6366f1"/></linearGradient>
<linearGradient id="border-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity=".22"/><stop offset=".45" stop-color="#38bdf8" stop-opacity=".26"/><stop offset="1" stop-color="#3b82f6" stop-opacity=".14"/></linearGradient>
<linearGradient id="glass-top" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff" stop-opacity="0"/><stop offset=".5" stop-color="#ffffff" stop-opacity=".18"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>
<linearGradient id="fadeline" x1="0" x2="1"><stop offset="0" stop-color="#38bdf8" stop-opacity=".65"/><stop offset="1" stop-color="#6366f1" stop-opacity="0"/></linearGradient>
<radialGradient id="glow1" cx=".12" cy=".08" r=".72"><stop offset="0" stop-color="#38bdf8" stop-opacity=".12"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<radialGradient id="glow2" cx=".92" cy=".92" r=".65"><stop offset="0" stop-color="#3b82f6" stop-opacity=".14"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>
<radialGradient id="cat-glow" cx=".5" cy=".45" r=".5"><stop offset="0" stop-color="#38bdf8" stop-opacity=".18"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<pattern id="dotgrid" width="20" height="20" patternUnits="userSpaceOnUse">
  <circle cx="1.5" cy="1.5" r="0.8" fill="#38bdf8" fill-opacity="0.045"/>
</pattern>
<clipPath id="arena-clip"><rect x="2" y="2" width="896" height="144"/></clipPath>
</defs>'''

def svg(w, h, body, name, style=""):
    st = f"<style>\n{style}\n</style>\n" if style else ""
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">\n{DEFS}\n{st}{body}\n</svg>')

def panel(w, h, rx=0, glow=True):
    # Apple Dark Glass: square precision corners (rx=0), translucent hairline border + subtle top specular highlight
    s = f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="0" fill="{CARD}" fill-opacity="0.92" stroke="url(#border-g)" stroke-width="1.2"/>'
    s += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="0" fill="url(#dotgrid)"/>'
    if glow:
        s += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="0" fill="url(#glow1)"/>'
        s += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="0" fill="url(#glow2)"/>'
    s += f'<line x1="2" y1="2" x2="{w-2}" y2="2" stroke="url(#glass-top)" stroke-width="1.2"/>'
    return s

def pill(x, y, text, color=BLUE, size=11.5):
    w = len(text) * size * 0.62 + 22
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="24" rx="0" fill="{color}" fill-opacity=".10" stroke="{color}" stroke-opacity=".35" stroke-width="1"/>'
            f'<text x="{x+w/2:.0f}" y="{y+16}" text-anchor="middle" font-family="{MONO}" font-size="{size}" fill="{WHITE}" fill-opacity="0.92">{e(text)}</text>'), w

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
b += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="0" fill="{BG}" fill-opacity="0.85" stroke="#ffffff" stroke-opacity="0.14"/>'
b += f'<rect x="{px}" y="{py}" width="{pw}" height="34" rx="0" fill="#111a2e" fill-opacity="0.8"/>'
for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    b += f'<circle cx="{px+20+i*18}" cy="{py+17}" r="4.5" fill="{c}" fill-opacity="0.9"/>'
b += f'<text x="{px+pw-16}" y="{py+21}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}">profile.js</text>'
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
    b = f'<rect x="1" y="1" width="898" height="54" rx="0" fill="{CARD}" fill-opacity="0.9" stroke="url(#border-g)" stroke-width="1.2"/>'
    b += f'<rect x="12" y="11" width="34" height="34" rx="0" fill="url(#g)" fill-opacity="0.9"/>'
    b += f'<text x="29" y="33" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="{BG}">{num}</text>'
    b += f'<text x="60" y="37" font-family="{SANS}" font-size="22" font-weight="700" fill="{WHITE}" letter-spacing="-0.3">{e(title)}</text>'
    b += f'<line x1="{tw}" y1="28" x2="880" y2="28" stroke="url(#fadeline)" stroke-width="1.5"/>'
    svg(900, 56, b, name)

section("01", "Projects", "section-projects.svg")
section("02", "Stack", "section-stack.svg")
section("03", "Activity & Stats", "section-activity.svg")
section("04", "Contact", "section-contact.svg")

# ---------------- PROJECT CARDS (2x2 bento) ----------------
PROJECT_STYLE = """
@keyframes softFloat { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-2px); } }
@keyframes softPulse { 0%,100% { opacity: 0.55; } 50% { opacity: 1; } }
.anim-float { animation: softFloat 3.6s ease-in-out infinite; }
.anim-pulse { animation: softPulse 2.4s ease-in-out infinite; }
"""

def get_icon(icon_type, color):
    # Clean Apple-style 2D vector icons centered inside 46x46 square frame (center = 47, 47)
    if icon_type == "bot":
        return (f'<g class="anim-float">'
                f'<rect x="35" y="38" width="24" height="18" rx="2" fill="none" stroke="{color}" stroke-width="1.7"/>'
                f'<line x1="47" y1="38" x2="47" y2="33" stroke="{color}" stroke-width="1.7"/>'
                f'<circle class="anim-pulse" cx="47" cy="31.5" r="1.8" fill="{color}"/>'
                f'<circle cx="42" cy="46" r="1.8" fill="{color}"/>'
                f'<circle cx="52" cy="46" r="1.8" fill="{color}"/>'
                f'</g>')
    elif icon_type == "eye":
        return (f'<g class="anim-float">'
                f'<path d="M35 47 C38.5 40.5 55.5 40.5 59 47 C55.5 53.5 38.5 53.5 35 47 Z" fill="none" stroke="{color}" stroke-width="1.7" stroke-linejoin="round"/>'
                f'<circle class="anim-pulse" cx="47" cy="47" r="3.5" fill="none" stroke="{color}" stroke-width="1.7"/>'
                f'</g>')
    elif icon_type == "gear":
        return (f'<g class="anim-float">'
                f'<polygon points="47,36 58,41.5 47,47 36,41.5" fill="none" stroke="{color}" stroke-width="1.7" stroke-linejoin="round"/>'
                f'<polyline points="36,47 47,52.5 58,47" fill="none" stroke="{color}" stroke-width="1.7" stroke-linejoin="round"/>'
                f'<polyline points="36,52 47,57.5 58,52" fill="none" stroke="{color}" stroke-width="1.7" stroke-linejoin="round"/>'
                f'</g>')
    elif icon_type == "chef":
        return (f'<g class="anim-float">'
                f'<path d="M47 36 L56.5 41.5 V52.5 L47 58 L37.5 52.5 V41.5 Z" fill="none" stroke="{color}" stroke-width="1.7" stroke-linejoin="round"/>'
                f'<polyline points="37.5,41.5 47,47 56.5,41.5" fill="none" stroke="{color}" stroke-width="1.7" stroke-linejoin="round"/>'
                f'<line x1="47" y1="47" x2="47" y2="58" stroke="{color}" stroke-width="1.7"/>'
                f'</g>')
    return f'<text x="47" y="54" text-anchor="middle" font-family="{MONO}" font-size="17" font-weight="700" fill="{WHITE}">{e(icon_type)}</text>'

def project(name, icon_type, title, l1, l2, tech, status, dot, is_wip=False):
    w, h = 446, 226
    b = panel(w, h, 0)
    b += f'<rect x="24" y="24" width="46" height="46" rx="0" fill="{dot}" fill-opacity="0.08" stroke="{dot}" stroke-opacity="0.35" stroke-width="1.1"/>'
    b += get_icon(icon_type, dot)
    sw = len(status) * 8.4 + 38
    b += f'<rect x="{w-24-sw:.0f}" y="31" width="{sw:.0f}" height="24" rx="0" fill="{BG}" fill-opacity="0.7" stroke="#ffffff" stroke-opacity="0.14" stroke-width="1"/>'
    b += f'<circle cx="{w-24-sw+14:.0f}" cy="43" r="3" fill="{dot}"/>'
    b += f'<text x="{w-24-sw+24:.0f}" y="47" font-family="{MONO}" font-size="10.5" font-weight="600" fill="{MUTED}" letter-spacing="1">{e(status)}</text>'
    b += f'<text x="24" y="108" font-family="{SANS}" font-size="24" font-weight="700" fill="{WHITE}" letter-spacing="-0.4">{e(title)}</text>'
    b += f'<text x="24" y="134" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l1)}</text>'
    b += f'<text x="24" y="153" font-family="{SANS}" font-size="13.5" fill="{MUTED}">{e(l2)}</text>'
    b += pills(24, 178, tech)
    
    if is_wip:
        b += f'<rect x="{w-56}" y="{h-56}" width="32" height="32" rx="0" fill="{BG}" fill-opacity="0.7" stroke="#ffffff" stroke-opacity="0.14" stroke-width="1"/>'
        b += f'<rect x="{w-45.5}" y="{h-40}" width="11" height="8.5" rx="0" fill="none" stroke="{MUTED}" stroke-width="1.5"/>'
        b += f'<path d="M{w-43.5} {h-40} v-2.5 a3.5 3.5 0 0 1 7 0 v2.5" fill="none" stroke="{MUTED}" stroke-width="1.5" stroke-linecap="square"/>'
    else:
        b += f'<rect x="{w-56}" y="{h-56}" width="32" height="32" rx="0" fill="url(#g)" fill-opacity="0.9"/>'
        b += f'<path d="M{w-46} {h-34} L{w-34} {h-46} M{w-44} {h-46} H{w-34} V{h-36}" stroke="{BG}" stroke-width="2" fill="none" stroke-linecap="square"/>'
    svg(w, h, b, f"project-{name}.svg", PROJECT_STYLE)

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
    b = panel(w, h, 0)
    
    act_style = """
    @keyframes catFloat { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-2.5px); } }
    @keyframes catBlink { 0%,92%,100% { transform: scaleY(1); } 96% { transform: scaleY(0.12); } }
    .cat-wrap { animation: catFloat 3.6s ease-in-out infinite; }
    .cat-eyes { animation: catBlink 4.5s infinite; transform-origin: 159px 110px; }
    """
    
    # Left Section: Cat Developer Business Card (Square Apple Glass)
    cx, cy, cw, ch = 24, 24, 270, 212
    b += f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="0" fill="{BG}" fill-opacity="0.75" stroke="#ffffff" stroke-opacity="0.14" stroke-width="1"/>'
    
    # Clean header bar
    b += f'<rect x="{cx}" y="{cy}" width="{cw}" height="30" rx="0" fill="#111a2e" fill-opacity="0.8"/>'
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        b += f'<circle cx="{cx+16+i*15}" cy="{cy+15}" r="4" fill="{c}" fill-opacity="0.85"/>'
    b += f'<text x="{cx+cw-14}" y="{cy+19}" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{MUTED}">dev_cat.id</text>'
    
    # Clean Minimalist Aggressive Cat Silhouette (Apple Dark Glass + Subtle 2D Animation)
    cat_cx, cat_cy = cx + 135, cy + 88
    b += f'<g class="cat-wrap">'
    b += f'<circle cx="{cat_cx}" cy="{cat_cy}" r="46" fill="url(#cat-glow)"/>'
    b += f'''<path d="M {cat_cx-31} {cat_cy-5}
                     C {cat_cx-30} {cat_cy-21}, {cat_cx-25} {cat_cy-34}, {cat_cx-20} {cat_cy-38}
                     C {cat_cx-18} {cat_cy-40}, {cat_cx-10} {cat_cy-30}, {cat_cx-7} {cat_cy-24}
                     C {cat_cx-2} {cat_cy-26}, {cat_cx+2} {cat_cy-26}, {cat_cx+7} {cat_cy-24}
                     C {cat_cx+10} {cat_cy-30}, {cat_cx+18} {cat_cy-40}, {cat_cx+20} {cat_cy-38}
                     C {cat_cx+25} {cat_cy-34}, {cat_cx+30} {cat_cy-21}, {cat_cx+31} {cat_cy-5}
                     C {cat_cx+32} {cat_cy+14}, {cat_cx+18} {cat_cy+24}, {cat_cx} {cat_cy+24}
                     C {cat_cx-18} {cat_cy+24}, {cat_cx-32} {cat_cy+14}, {cat_cx-31} {cat_cy-5} Z"
                  fill="#050810" stroke="url(#border-g)" stroke-width="1.4"/>'''
    
    # Sleek whiskers
    b += f'<line x1="{cat_cx-28}" y1="{cat_cy+2}" x2="{cat_cx-46}" y2="{cat_cy-2}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.8" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx-29}" y1="{cat_cy+8}" x2="{cat_cx-48}" y2="{cat_cy+8}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.8" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx-27}" y1="{cat_cy+14}" x2="{cat_cx-45}" y2="{cat_cy+19}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.8" stroke-linecap="round"/>'
    
    b += f'<line x1="{cat_cx+28}" y1="{cat_cy+2}" x2="{cat_cx+46}" y2="{cat_cy-2}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.8" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx+29}" y1="{cat_cy+8}" x2="{cat_cx+48}" y2="{cat_cy+8}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.8" stroke-linecap="round"/>'
    b += f'<line x1="{cat_cx+27}" y1="{cat_cy+14}" x2="{cat_cx+45}" y2="{cat_cy+19}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.8" stroke-linecap="round"/>'

    # Blinking sharp aggressive eyes
    b += f'<g class="cat-eyes">'
    b += f'<polygon points="{cat_cx-20},{cat_cy-6} {cat_cx-6},{cat_cy-1} {cat_cx-15},{cat_cy+4}" fill="#38bdf8"/>'
    b += f'<polygon points="{cat_cx+20},{cat_cy-6} {cat_cx+6},{cat_cy-1} {cat_cx+15},{cat_cy+4}" fill="#38bdf8"/>'
    b += f'</g>'
    b += f'</g>'
    
    # Business Card text info
    b += f'<text x="{cx+cw/2:.0f}" y="{cy+148}" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="700" fill="{WHITE}" letter-spacing="-0.2">Diego Mantilla</text>'
    b += f'<text x="{cx+cw/2:.0f}" y="{cy+168}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#38bdf8">Core Software Engineer</text>'
    b += f'<text x="{cx+cw/2:.0f}" y="{cy+188}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{MUTED}">Clean code · Zero bloat</text>'
    
    # Right Section: GitHub Commit Calendar Grid (Square Apple Glass)
    gx, gy = 318, 24
    gw, gh = 558, 212
    b += f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" rx="0" fill="{BG}" fill-opacity="0.75" stroke="#ffffff" stroke-opacity="0.14" stroke-width="1"/>'
    
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
        
    b += f'<text x="{gx+20}" y="{gy+32}" font-family="{SANS}" font-size="15.5" font-weight="700" fill="{WHITE}" letter-spacing="-0.2">GitHub Activity</text>'
    b += f'<text x="{gx+gw-20}" y="{gy+32}" text-anchor="end" font-family="{MONO}" font-size="11.5" fill="#38bdf8">{total_commits} contributions · last year</text>'
    
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
            b += f'<rect x="{col_x:.1f}" y="{row_y:.1f}" width="{sq}" height="{sq}" rx="0" fill="{color}"/>'
            
    # Legend below graph
    b += f'<text x="{start_grid_x}" y="{gy+gh-22}" font-family="{MONO}" font-size="11" fill="{MUTED}">Less</text>'
    for idx, col in enumerate(["#111c33", "#1e3a8a", "#2563eb", "#3b82f6", "#38bdf8"]):
        lx = start_grid_x + 38 + idx * 14
        b += f'<rect x="{lx}" y="{gy+gh-30}" width="10" height="10" rx="0" fill="{col}"/>'
    b += f'<text x="{start_grid_x+116}" y="{gy+gh-22}" font-family="{MONO}" font-size="11" fill="{MUTED}">More</text>'
    b += f'<text x="{gx+gw-20}" y="{gy+gh-22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{CYAN}">github.com/DMntill4</text>'
    
    svg(w, h, b, "activity-card.svg", act_style)

build_activity_card()

# ---------------- MINI-GAME: CAT VS BUGS (APPLE GLASS RUNNER) ----------------
def build_cat_runner():
    w, h = 900, 148
    b = panel(w, h, 0)
    
    runner_style = """
    @keyframes groundScroll {
      0% { transform: translateX(0px); }
      100% { transform: translateX(-180px); }
    }
    @keyframes bgParallax {
      0% { transform: translateX(0px); }
      100% { transform: translateX(-300px); }
    }
    @keyframes catJump {
      0%, 8% { transform: translateY(0px) rotate(0deg); }
      14% { transform: translateY(-42px) rotate(-5deg); }
      17% { transform: translateY(-46px) rotate(0deg); }
      26%, 58% { transform: translateY(0px) rotate(0deg); }
      64% { transform: translateY(-42px) rotate(-5deg); }
      67% { transform: translateY(-46px) rotate(0deg); }
      76%, 100% { transform: translateY(0px) rotate(0deg); }
    }
    @keyframes bugScroll {
      0% { transform: translateX(920px); }
      100% { transform: translateX(-280px); }
    }
    @keyframes pulseDot {
      0%, 100% { opacity: 0.35; }
      50% { opacity: 1; }
    }
    @keyframes rainSlow {
      0% { transform: translate(0px, -148px); }
      100% { transform: translate(-26px, 0px); }
    }
    @keyframes rainFast {
      0% { transform: translate(0px, -148px); }
      100% { transform: translate(-32px, 0px); }
    }
    .ground-track { animation: groundScroll 1.2s linear infinite; }
    .bg-code { animation: bgParallax 12s linear infinite; }
    .runner-cat { animation: catJump 4.8s cubic-bezier(0.35, 0, 0.25, 1) infinite; transform-origin: 120px 100px; }
    .obs-1 { animation: bugScroll 4.8s linear infinite; }
    .obs-2 { animation: bugScroll 4.8s linear -2.4s infinite; }
    .live-dot { animation: pulseDot 1.6s ease-in-out infinite; }
    .rain-a { animation: rainSlow 1.1s linear infinite; }
    .rain-b { animation: rainFast 0.78s linear infinite; }
    """
    
    # Top HUD bar
    b += f'<text x="20" y="24" font-family="{MONO}" font-size="11" fill="{CYAN}" letter-spacing="1.2">cat_runner.sh</text>'
    b += f'<circle class="live-dot" cx="716" cy="20" r="3.2" fill="{GREEN}"/>'
    b += f'<text x="726" y="24" font-family="{MONO}" font-size="10.5" fill="{MUTED}" letter-spacing="0.8">DODGING BUGS · HI 99999</text>'
    
    b += '<g clip-path="url(#arena-clip)">'
    
    # Subtle diagonal rain effect (2 depth layers, seamless loop)
    b += '<g class="rain-a" stroke="#38bdf8" stroke-opacity="0.14" stroke-width="1">'
    for rx_pos in range(20, 960, 42):
        ry_off = (rx_pos * 17) % 120
        for dy in (0, 148):
            y1 = ry_off + dy
            b += f'<line x1="{rx_pos}" y1="{y1}" x2="{rx_pos-4}" y2="{y1+14}"/>'
    b += '</g>'
    b += '<g class="rain-b" stroke="#93c5fd" stroke-opacity="0.20" stroke-width="1">'
    for rx_pos in range(38, 960, 68):
        ry_off = (rx_pos * 23) % 110
        for dy in (0, 148):
            y1 = ry_off + dy
            b += f'<line x1="{rx_pos}" y1="{y1}" x2="{rx_pos-5}" y2="{y1+18}"/>'
    b += '</g>'
    
    # Subtle parallax code tokens in background
    b += '<g class="bg-code" opacity="0.16">'
    for idx, tok in enumerate(["{ }", "0x1A", "</>", "git push", "=>", "200 OK", "async"]):
        tx = 80 + idx * 165
        ty = 48 + (idx % 2) * 16
        b += f'<text x="{tx}" y="{ty}" font-family="{MONO}" font-size="11" fill="{CYAN}">{e(tok)}</text>'
    b += '</g>'
    
    # Ground line & scrolling ticks
    gy = 118
    b += f'<line x1="2" y1="{gy}" x2="{w-2}" y2="{gy}" stroke="#ffffff" stroke-opacity="0.16" stroke-width="1"/>'
    b += '<g class="ground-track">'
    for tx in range(0, 1140, 36):
        b += f'<line x1="{tx}" y1="{gy+6}" x2="{tx+14}" y2="{gy+6}" stroke="#38bdf8" stroke-opacity="0.25" stroke-width="1.2"/>'
        if tx % 72 == 0:
            b += f'<line x1="{tx+18}" y1="{gy+12}" x2="{tx+24}" y2="{gy+12}" stroke="#6366f1" stroke-opacity="0.25" stroke-width="1.2"/>'
    b += '</g>'
    
    # Runner Cat (Sleek minimalist cat at x=120, resting on ground y=118)
    cat_cx, cat_cy = 120, 96
    b += '<g class="runner-cat">'
    b += f'<circle cx="{cat_cx}" cy="{cat_cy}" r="26" fill="url(#cat-glow)"/>'
    b += f'''<path d="M {cat_cx-18} {cat_cy-3}
                     C {cat_cx-17} {cat_cy-12}, {cat_cx-14} {cat_cy-20}, {cat_cx-11} {cat_cy-22}
                     C {cat_cx-10} {cat_cy-23}, {cat_cx-6} {cat_cy-17}, {cat_cx-4} {cat_cy-14}
                     C {cat_cx-1} {cat_cy-15}, {cat_cx+1} {cat_cy-15}, {cat_cx+4} {cat_cy-14}
                     C {cat_cx+6} {cat_cy-17}, {cat_cx+10} {cat_cy-23}, {cat_cx+11} {cat_cy-22}
                     C {cat_cx+14} {cat_cy-20}, {cat_cx+17} {cat_cy-12}, {cat_cx+18} {cat_cy-3}
                     C {cat_cx+19} {cat_cy+8}, {cat_cx+10} {cat_cy+15}, {cat_cx} {cat_cy+15}
                     C {cat_cx-10} {cat_cy+15}, {cat_cx-19} {cat_cy+8}, {cat_cx-18} {cat_cy-3} Z"
                  fill="#050810" stroke="url(#border-g)" stroke-width="1.3"/>'''
    # Whiskers
    b += f'<line x1="{cat_cx-16}" y1="{cat_cy+2}" x2="{cat_cx-26}" y2="{cat_cy}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.3"/>'
    b += f'<line x1="{cat_cx-16}" y1="{cat_cy+6}" x2="{cat_cx-26}" y2="{cat_cy+7}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.3"/>'
    b += f'<line x1="{cat_cx+16}" y1="{cat_cy+2}" x2="{cat_cx+26}" y2="{cat_cy}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.3"/>'
    b += f'<line x1="{cat_cx+16}" y1="{cat_cy+6}" x2="{cat_cx+26}" y2="{cat_cy+7}" stroke="#38bdf8" stroke-opacity="0.55" stroke-width="1.3"/>'
    # Sharp aggressive eyes
    b += f'<polygon points="{cat_cx-11},{cat_cy-4} {cat_cx-3},{cat_cy-1} {cat_cx-8},{cat_cy+2}" fill="#38bdf8"/>'
    b += f'<polygon points="{cat_cx+11},{cat_cy-4} {cat_cx+3},{cat_cy-1} {cat_cx+8},{cat_cy+2}" fill="#38bdf8"/>'
    b += '</g>'
    
    # Obstacle 1: BUG block
    b += '<g class="obs-1">'
    b += f'<rect x="0" y="{gy-26}" width="38" height="26" rx="0" fill="#ef4444" fill-opacity="0.16" stroke="#ef4444" stroke-opacity="0.65" stroke-width="1.2"/>'
    b += f'<text x="19" y="{gy-9}" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="700" fill="#fca5a5">BUG</text>'
    b += '</g>'
    
    # Obstacle 2: 404 block
    b += '<g class="obs-2">'
    b += f'<rect x="0" y="{gy-24}" width="42" height="24" rx="0" fill="#8b5cf6" fill-opacity="0.16" stroke="#a855f7" stroke-opacity="0.65" stroke-width="1.2"/>'
    b += f'<text x="21" y="{gy-8}" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="700" fill="#d8b4fe">404</text>'
    b += '</g>'
    
    b += '</g>'
    svg(w, h, b, "cat-vs-bugs.svg", runner_style)

build_cat_runner()
print(sorted(os.listdir(OUT)))
