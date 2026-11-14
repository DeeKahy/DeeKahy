#!/usr/bin/env python3
"""Generate the animated SVGs for the DeeKahy profile README."""
Usage: python3 assets/generate.py .  (writes assets/hero.svg and assets/mitos.svg)
import random, sys
from html import escape

out = sys.argv[1]
random.seed(7)
MONO = "ui-monospace, SFMono-Regular, Menlo, 'DejaVu Sans Mono', 'Cascadia Mono', Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"

# ---------------------------------------------------------------- hero
W, H = 1000, 330
phrases = [
    "software student @ Aalborg University",
    "writes all of it in the Mitos editor",
    "runs a NixOS homelab at smallapp.cc",
    "ships Rust, Go, Swift & TypeScript",
    "builds things nobody asked for, lovingly",
]
FS, CW = 22, 13.2          # font size, approx mono char width
TX, TY = 112, 238          # typing line origin
SLOT = 4.0
TOTAL = SLOT * len(phrases)

def kt(points):
    """points: [(t_seconds, value)] -> (keyTimes, values) strings"""
    pts = []
    for t, v in points:
        if pts and abs(pts[-1][0] - t) < 1e-9:
            pts[-1] = (t, v)
        else:
            pts.append((t, v))
    return ";".join(f"{t/TOTAL:.4f}" for t, _ in pts), ";".join(f"{v:.1f}" for _, v in pts)

stars = []
for _ in range(70):
    x, y = random.uniform(10, W - 10), random.uniform(10, H - 10)
    r = random.choice([0.6, 0.8, 1, 1.2, 1.6])
    d = random.uniform(2, 6); b = random.uniform(0, 6)
    stars.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff"><animate attributeName="opacity" values="0.1;0.9;0.1" dur="{d:.1f}s" begin="{b:.1f}s" repeatCount="indefinite"/></circle>')

typing, cursor_pts = [], [(0, TX)]
for i, p in enumerate(phrases):
    w = len(p) * CW
    s = i * SLOT
    t0, t1, t2, t3 = s + 0.2, s + 0.2 + len(p) * 0.045, s + 3.2, s + 3.65
    k, v = kt([(0, 0), (t0, 0), (t1, w), (t2, w), (t3, 0), (TOTAL, 0)])
    cursor_pts += [(t0, TX), (t1, TX + w), (t2, TX + w), (t3, TX)]
    typing.append(f'''<clipPath id="c{i}"><rect x="{TX}" y="{TY-24}" height="34" width="0"><animate attributeName="width" values="{v}" keyTimes="{k}" dur="{TOTAL}s" repeatCount="indefinite"/></rect></clipPath>
<text x="{TX}" y="{TY}" clip-path="url(#c{i})" class="mono" font-size="{FS}" fill="#e2e8f0" textLength="{w:.1f}" lengthAdjust="spacing">{escape(p)}</text>''')
cursor_pts.append((TOTAL, TX))
ck, cv = kt(cursor_pts)

# orbit on the right
cx, cy = 820, 165
orbits = []
for r, dur, col, n, rev in [(46, 9, "#22d3ee", 1, False), (78, 14, "#a78bfa", 2, True), (112, 22, "#f472b6", 3, False)]:
    dots = "".join(
        f'<circle cx="{cx + r}" cy="{cy}" r="{5 - n}" fill="{col}" transform="rotate({k*360/n} {cx} {cy})" filter="url(#glow)"/>'
        for k in range(n))
    a, b = (360, 0) if rev else (0, 360)
    orbits.append(f'''<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-opacity="0.25" stroke-dasharray="2 6"/>
<g>{dots}<animateTransform attributeName="transform" type="rotate" from="{a} {cx} {cy}" to="{b} {cx} {cy}" dur="{dur}s" repeatCount="indefinite"/></g>''')

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Hi, I'm DeeKahy">
<title>Hi, I'm DeeKahy</title>
<style>
  .mono {{ font-family: {MONO}; }}
  .sans {{ font-family: {SANS}; }}
</style>
<defs>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0b0b1a"/><stop offset="1" stop-color="#120a24"/>
  </linearGradient>
  <linearGradient id="name" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="640" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="#a78bfa"/><stop offset="0.33" stop-color="#22d3ee"/>
    <stop offset="0.66" stop-color="#f472b6"/><stop offset="1" stop-color="#a78bfa"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="640 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="softglow" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="10" result="b"/><feComponentTransfer in="b" result="b2"><feFuncA type="linear" slope="0.55"/></feComponentTransfer><feMerge><feMergeNode in="b2"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity="0.9"/></linearGradient>
  <mask id="gridmask"><rect y="200" width="{W}" height="{H-200}" fill="url(#fade)"/></mask>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <g filter="url(#blur)" opacity="0.75">
    <circle cx="180" cy="60" r="140" fill="#7c3aed"><animateTransform attributeName="transform" type="translate" values="0 0;120 60;0 0" dur="16s" repeatCount="indefinite"/></circle>
    <circle cx="760" cy="300" r="150" fill="#0891b2"><animateTransform attributeName="transform" type="translate" values="0 0;-140 -50;0 0" dur="19s" repeatCount="indefinite"/></circle>
    <circle cx="520" cy="40" r="110" fill="#db2777" opacity="0.7"><animateTransform attributeName="transform" type="translate" values="0 0;60 90;0 0" dur="13s" repeatCount="indefinite"/></circle>
  </g>
  <g mask="url(#gridmask)" stroke="#a78bfa" stroke-opacity="0.35" stroke-width="1">
    {"".join(f'<line x1="{500 + (i*90)}" y1="{H}" x2="{500 + i*14}" y2="200"/>' for i in range(-12, 13))}
    <g>
      {"".join(f'<line x1="0" x2="{W}" y1="{200 + (k*k)*1.6:.1f}" y2="{200 + (k*k)*1.6:.1f}"/>' for k in range(1, 12))}
    </g>
  </g>
  {"".join(stars)}
  {"".join(orbits)}
  <circle cx="{cx}" cy="{cy}" r="18" fill="#a78bfa" filter="url(#glow)"><animate attributeName="r" values="16;20;16" dur="3s" repeatCount="indefinite"/></circle>
  <text x="{cx}" y="{cy+6}" text-anchor="middle" class="mono" font-size="16" font-weight="700" fill="#0b0b1a">{{}}</text>

  <text x="{TX}" y="92" class="mono" font-size="18" fill="#94a3b8">hi there, i'm<animate attributeName="opacity" values="0;1" dur="1s" fill="freeze"/></text>
  <text x="{TX-6}" y="182" class="sans" font-size="104" font-weight="800" letter-spacing="-3" fill="url(#name)" filter="url(#softglow)">DeeKahy</text>
  <text x="{TX-34}" y="{TY}" class="mono" font-size="{FS}" fill="#22d3ee" font-weight="700">❯</text>
  {"".join(typing)}
  <rect x="{TX}" y="{TY-20}" width="11" height="26" fill="#f472b6">
    <animate attributeName="x" values="{cv}" keyTimes="{ck}" dur="{TOTAL}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0" dur="0.9s" calcMode="discrete" repeatCount="indefinite"/>
  </rect>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="22" fill="none" stroke="#a78bfa" stroke-opacity="0.35"/>
</g>
</svg>'''
open(f"{out}/assets/hero.svg", "w").write(hero)

# ---------------------------------------------------------------- mitos editor card
C = dict(bg="#1e1e2e", bar="#181825", text="#cdd6f4", kw="#cba6f7", str="#a6e3a1", ty="#f9e2af",
         fn="#89b4fa", com="#6c7086", pun="#9399b2", field="#89dceb", num="#fab387", gut="#45475a")
FS2, CW2, LH = 15, 9.0, 23
X0, Y0 = 70, 74
code = [
    [("use", "kw"), (" mitos", "text"), ("::", "pun"), ("prelude", "text"), ("::", "pun"), ("*", "pun"), (";", "pun")],
    [],
    [("/// The human behind this profile.", "com")],
    [("fn", "kw"), (" ", "text"), ("main", "fn"), ("() {", "pun")],
    [("    let", "kw"), (" me ", "text"), ("=", "pun"), (" ", "text"), ("Developer", "ty"), (" {", "pun")],
    [("        name", "field"), (":     ", "pun"), ('"DeeKahy"', "str"), (",", "pun")],
    [("        based_in", "field"), (": ", "pun"), ('"Denmark"', "str"), (",", "pun")],
    [("        studying", "field"), (": ", "pun"), ('"Software @ Aalborg University"', "str"), (",", "pun")],
    [("        editor", "field"), (":   ", "pun"), ("Editor", "ty"), ("::", "pun"), ("Mitos", "ty"), (",", "pun"), ("  // modal. selection-first. fast.", "com")],
    [("        os", "field"), (":       ", "pun"), ("Os", "ty"), ("::", "pun"), ("NixOS", "ty"), (",", "pun"), ("     // declarative everything", "com")],
    [("        homelab", "field"), (":  ", "pun"), ('"smallapp.cc"', "str"), (",", "pun"), (" // proxmox + nixos + caddy", "com")],
    [("    }", "pun"), (";", "pun")],
    [],
    [("    me", "text"), (".", "pun"), ("build", "fn"), ("()", "pun"), (".", "pun"), ("ship", "fn"), ("()", "pun"), (".", "pun"), ("repeat", "fn"), ("();", "pun")],
    [("}", "pun")],
]
EW = 1000
EH = Y0 + len(code) * LH + 70

def col_x(c): return X0 + c * CW2
def line_y(i): return Y0 + i * LH

lines_svg = []
for i, toks in enumerate(code):
    y = line_y(i)
    lines_svg.append(f'<text x="{X0-22}" y="{y}" text-anchor="end" fill="{C["gut"]}">{i+1}</text>')
    if not toks:
        continue
    n = sum(len(t) for t, _ in toks)
    spans = "".join(f'<tspan fill="{C[k]}">{escape(t)}</tspan>' for t, k in toks)
    lines_svg.append(f'<text x="{X0}" y="{y}" xml:space="preserve" textLength="{n*CW2:.1f}" lengthAdjust="spacing">{spans}</text>')

def phase(n):  # n of 3 phases visible, 12s loop
    vals = ";".join("1" if j == n else "0" for j in range(3))
    return f'<animate attributeName="opacity" values="{vals}" keyTimes="0;0.3333;0.6667" calcMode="discrete" dur="12s" repeatCount="indefinite"/>'

blink = '<animate attributeName="opacity" values="1;0.15" dur="1s" calcMode="discrete" repeatCount="indefinite"/>'
mitos_col = len("        editor:   Editor::")   # start of "Mitos"
# phase 0 (NOR): block cursor on the M of Mitos
p0 = f'<g opacity="1">{phase(0)}<rect x="{col_x(mitos_col)}" y="{line_y(8)-15}" width="{CW2}" height="20" fill="{C["text"]}">{blink}</rect></g>'
# phase 1 (SEL): multi-selection over the four values
sels = []
for li, start, ln in [(5, 18, 9), (6, 18, 9), (7, 18, 31), (8, 18, 13)]:
    sels.append(f'<rect x="{col_x(start)}" y="{line_y(li)-16}" width="{ln*CW2}" height="21" rx="2" fill="#f5c2e7" fill-opacity="0.22" stroke="#f5c2e7" stroke-opacity="0.5"/>')
    sels.append(f'<rect x="{col_x(start+ln-1)}" y="{line_y(li)-16}" width="{CW2}" height="21" fill="#f5c2e7" fill-opacity="0.6">{blink}</rect>')
p1 = f'<g opacity="0">{phase(1)}{"".join(sels)}</g>'
# phase 2 (INS): bar cursor after Mitos + completion popup
px, py = col_x(mitos_col), line_y(8) + 10
items = [("Mitos", "the one true editor", True), ("Helix", "where it came from", False), ("Vim", "grandparent, respected", False), ("Notepad", "absolutely not", False)]
pop = [f'<rect x="{px-6}" y="{py}" width="330" height="{len(items)*24+10}" rx="6" fill="#11111b" stroke="#585b70"/>']
for j, (a, b, on) in enumerate(items):
    yy = py + 8 + j * 24
    if on:
        pop.append(f'<rect x="{px-2}" y="{yy}" width="322" height="22" rx="4" fill="#313244"/>')
    pop.append(f'<text x="{px+4}" y="{yy+16}" fill="{C["kw"]}">E</text><text x="{px+24}" y="{yy+16}" fill="{C["text"] if on else C["pun"]}">{a}</text><text x="{px+316}" y="{yy+16}" text-anchor="end" fill="{C["com"]}" font-style="italic">{b}</text>')
p2 = f'''<g opacity="0">{phase(2)}<rect x="{col_x(mitos_col+5)}" y="{line_y(8)-15}" width="2" height="20" fill="{C["text"]}">{blink}</rect>{"".join(pop)}</g>'''

sy = EH - 48
modes = [("NOR", "#89b4fa", "1 sel", "9:27"), ("SEL", "#fab387", "4 sels", "6:22"), ("INS", "#a6e3a1", "1 sel", "9:32")]
status = []
for n, (m, col, sel, pos) in enumerate(modes):
    status.append(f'''<g opacity="{1 if n == 0 else 0}">{phase(n)}
<rect x="0" y="{sy}" width="62" height="26" fill="{col}"/><text x="31" y="{sy+18}" text-anchor="middle" font-weight="700" fill="#11111b">{m}</text>
<text x="{EW-20}" y="{sy+18}" text-anchor="end" fill="{C["pun"]}">●  rust-analyzer   {sel}   {pos}   rust</text></g>''')

msg = ['"src/main.rs" 15L, 412B written', "s  — select the four values", "Mitos  ⏎  accept completion"]
msgs = "".join(f'<text x="14" y="{EH-8}" fill="{C["com"]}" opacity="{1 if n == 0 else 0}">{phase(n)}{escape(t)}</text>' for n, t in enumerate(msg))

editor = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {EW} {EH}" width="{EW}" height="{EH}" role="img" aria-label="DeeKahy's code open in the Mitos editor">
<title>Written in Mitos</title>
<style>text {{ font-family: {MONO}; font-size: {FS2}px; }}</style>
<defs><clipPath id="win"><rect width="{EW}" height="{EH}" rx="14"/></clipPath></defs>
<g clip-path="url(#win)">
<rect width="{EW}" height="{EH}" fill="{C["bg"]}"/>
<rect width="{EW}" height="38" fill="{C["bar"]}"/>
<circle cx="22" cy="19" r="6.5" fill="#f38ba8"/><circle cx="44" cy="19" r="6.5" fill="#f9e2af"/><circle cx="66" cy="19" r="6.5" fill="#a6e3a1"/>
<text x="{EW/2}" y="24" text-anchor="middle" fill="{C["pun"]}">mitos — ~/deekahy/src/main.rs</text>
<rect x="0" y="38" width="{EW}" height="0" fill="none"/>
<rect x="0" y="{line_y(8)-16}" width="{EW}" height="22" fill="#313244" fill-opacity="0.35"/>
{p1}{p0}
{"".join(lines_svg)}
{p2}
<rect x="0" y="{sy}" width="{EW}" height="26" fill="{C["bar"]}"/>
<text x="76" y="{sy+18}" fill="{C["text"]}">src/main.rs</text>
{"".join(status)}
{msgs}
<rect x="0.5" y="0.5" width="{EW-1}" height="{EH-1}" rx="14" fill="none" stroke="#45475a"/>
</g>
</svg>'''
open(f"{out}/assets/mitos.svg", "w").write(editor)
print("ok", EH)
