import math

WIDTH, HEIGHT = 1200, 360
R = 90
CENTERS = [(150, 150), (430, 150), (710, 150), (990, 150)]
CHOICES = [
    (9, 35, 'ア'),
    (7, 45, 'イ'),
    (10, 35, 'ウ'),
    (9, 30, 'エ'),
]


def polar(cx, cy, radius, degree):
    rad = math.radians(degree)
    return cx + radius * math.cos(rad), cy - radius * math.sin(rad)


def hand_end(cx, cy, length, degree):
    return polar(cx, cy, length, degree)

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}">',
    '<rect width="100%" height="100%" fill="white"/>',
    '<text x="600" y="35" text-anchor="middle" font-size="28" font-family="sans-serif">問3の時計（ア〜エ）</text>'
]

for (cx, cy), (hour, minute, label) in zip(CENTERS, CHOICES):
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="black" stroke-width="3"/>')

    for n in range(60):
        deg = 90 - n * 6
        outer_x, outer_y = polar(cx, cy, R - 2, deg)
        inner_r = R - 18 if n % 5 == 0 else R - 10
        inner_x, inner_y = polar(cx, cy, inner_r, deg)
        sw = 2 if n % 5 == 0 else 1
        parts.append(
            f'<line x1="{inner_x:.2f}" y1="{inner_y:.2f}" x2="{outer_x:.2f}" y2="{outer_y:.2f}" stroke="black" stroke-width="{sw}"/>'
        )

    for num in range(1, 13):
        deg = 90 - num * 30
        tx, ty = polar(cx, cy, R - 32, deg)
        parts.append(f'<text x="{tx:.2f}" y="{ty + 6:.2f}" text-anchor="middle" font-size="18" font-family="sans-serif">{num}</text>')

    min_deg = 90 - minute * 6
    hour_deg = 90 - ((hour % 12) * 30 + minute * 0.5)
    mx, my = hand_end(cx, cy, R - 28, min_deg)
    hx, hy = hand_end(cx, cy, R - 45, hour_deg)

    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{mx:.2f}" y2="{my:.2f}" stroke="black" stroke-width="4"/>')
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{hx:.2f}" y2="{hy:.2f}" stroke="black" stroke-width="7"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="black"/>')
    parts.append(f'<text x="{cx}" y="300" text-anchor="middle" font-size="28" font-family="sans-serif">{label}</text>')

parts.append('</svg>')

with open('q3_clocks.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))

print('Saved q3_clocks.svg')
