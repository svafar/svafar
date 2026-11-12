"""Recompute every number cited in HANDOFF.md.

Run: python3 check.py
Method: OKLab ΔE ×100 (dE), WCAG 2 contrast ratio (cr), colour-vision deficiency
simulated with Machado, Oliveira & Fernandes (2009) at severity 1.0 for protan,
deutan and tritan; "cvd" is the smallest ΔE of the three simulations.
Tokens are the Hacking Hunger design system v13 (tokens-v13.json).
"""
from colour import T, oklch, cr, dE, dEcvd, shade

NEW = {
    # GLP-1 family
    'semaglutide': '#217871', 'glp1': '#5d928a', 'glp1-spent': '#909b9a',
    'orforglipron': '#206079', 'camp': '#4c9ea1',
    'liquid': '#9dd8d4', 'liquid-edge': '#68ada8',
    # locks and relays
    'glp1r': '#a18fb9', 'gprotein': '#788f62', 'adenylyl-cyclase': '#66718f',
    'pka': '#907c6c', 'epac2': '#766558',
    # insulin and islet
    'glut4': '#be859b', 'glucagon': '#947aa8', 'somatostatin': '#956186',
    # blood, fat, other
    'dpp4': '#585a66', 'adiponectin': '#5774a9', 'glucose': '#ba7e2d',
    'nausea': '#a5aa73',
    # field
    'extra-ground': '#f3bfbd',
}
OLD = {'semaglutide': T['mol-semaglutide'], 'glp1r': T['mol-glp1r'],
       'gprotein': T['mol-gprotein'], 'liquid': '#C3D1EA', 'albumin': T['mol-albumin'],
       'adenylyl-cyclase': T['mol-adenylyl-cyclase'], 'adiponectin-grain': '#4F7A52',
       'glut4': T['mol-glut4'], 'extra-ground': T['extra-ground']}
STEEL, CREAM, FAT_GROUND = '#AEB4C2', '#F1DFBB', '#E7C3AE'
IG, BF = T['intra-ground'], T['bilayer-fill']


def row(label, a, b):
    m, d = dEcvd(a, b)
    print(f'  {label:58s} cr {cr(a, b):4.2f}  dE {dE(a, b):5.1f}  cvd {m:5.1f}')


print('1. Why teal: hue of the family vs the hues the body already uses')
h_teal = oklch(NEW['semaglutide'])[2]
h_blue = oklch(T['mol-semaglutide'])[2]
for k in ['extra-ground', 'intra-ground', 'blood-ground', 'wash-gut', 'wash-pancreas',
          'cavity-ground', 'silhouette', 'shadow-gut', 'shadow-pancreas', 'mol-shadow-tint',
          'nucleus', 'wash-blood']:
    h = oklch(T[k])[2]
    dt = min(abs(h - h_teal), 360 - abs(h - h_teal))
    db = min(abs(h - h_blue), 360 - abs(h - h_blue))
    print(f'  {k:18s} hue {h:5.0f}   from teal {dt:5.0f}°   from slate {db:5.0f}°')
row('drug on silhouette, now (slate)', OLD['semaglutide'], T['silhouette'])
row('drug on silhouette, proposed (teal)', NEW['semaglutide'], T['silhouette'])
row('drug liquid vs steel needle, now', OLD['liquid'], STEEL)
row('drug liquid vs steel needle, proposed', NEW['liquid'], STEEL)
row('drug liquid vs cream fat, now', OLD['liquid'], CREAM)
row('drug liquid vs cream fat, proposed', NEW['liquid'], CREAM)

print('\n2. Hero frame (7KI0): drug, receptor, G protein')
row('drug in receptor, now (slate in sage)', OLD['semaglutide'], OLD['glp1r'])
row('drug in receptor, teal in sage (rejected)', NEW['semaglutide'], OLD['glp1r'])
row('drug in receptor, proposed (teal in lilac)', NEW['semaglutide'], NEW['glp1r'])
row('receptor vs G protein, now', OLD['glp1r'], OLD['gprotein'])
row('receptor vs G protein, proposed', NEW['glp1r'], NEW['gprotein'])
row('albumin vs receptor, now (the olive problem)', OLD['albumin'], OLD['glp1r'])
row('albumin vs receptor, proposed', OLD['albumin'], NEW['glp1r'])
row('albumin (straw, kept) vs drug', OLD['albumin'], NEW['semaglutide'])
row('albumin gold #a48534 (withdrawn) vs drug', '#a48534', NEW['semaglutide'])
row('G protein vs albumin (across the membrane)', NEW['gprotein'], OLD['albumin'])
print('  lightness ladder L: drug %.0f, G protein %.0f, receptor %.0f' % tuple(
    oklch(NEW[k])[0] * 100 for k in ('semaglutide', 'gprotein', 'glp1r')))
for k in ('glp1r',):
    print(f'  receptor on bilayer: now {cr(OLD[k], BF):.2f}, proposed {cr(NEW[k], BF):.2f}')

print('\n3. The GLP-1 family among itself and in the receptor')
row('native GLP-1 vs semaglutide (siblings)', NEW['glp1'], NEW['semaglutide'])
row('native GLP-1 in the lilac receptor (6X18)', NEW['glp1'], NEW['glp1r'])
row('orforglipron in the lilac receptor (6XOX)', NEW['orforglipron'], NEW['glp1r'])
row('orforglipron first value #5a92ab (withdrawn)', '#5a92ab', NEW['glp1r'])
row('orforglipron vs semaglutide', NEW['orforglipron'], NEW['semaglutide'])
row('DPP-4 vs native GLP-1', NEW['dpp4'], NEW['glp1'])

print('\n4. S06: the crowded scene, on the honey interior')
row('cAMP pale #96d1c3 (withdrawn) on honey', '#96d1c3', IG)
row('cAMP proposed on honey', NEW['camp'], IG)
row('glucose light #F5C766 on honey', '#F5C766', IG)
row('glucose deep (proposed in cells) on honey', NEW['glucose'], IG)
row('adenylyl cyclase now (steel) vs cAMP', OLD['adenylyl-cyclase'], NEW['camp'])
row('adenylyl cyclase proposed (slate) vs cAMP', NEW['adenylyl-cyclase'], NEW['camp'])
row('adenylyl cyclase proposed vs G protein', NEW['adenylyl-cyclase'], NEW['gprotein'])
row('adenylyl cyclase proposed vs receptor', NEW['adenylyl-cyclase'], NEW['glp1r'])
row('PKA vs EPAC2', NEW['pka'], NEW['epac2'])
row('PKA vs cAMP', NEW['pka'], NEW['camp'])
row('PKA vs glucose', NEW['pka'], NEW['glucose'])
row('PKA vs insulin (not touching)', NEW['pka'], T['mol-insulin'])
row('EPAC2 vs insulin (not touching)', NEW['epac2'], T['mol-insulin'])
row('cAMP vs glucose', NEW['camp'], NEW['glucose'])
row('cAMP vs insulin', NEW['camp'], T['mol-insulin'])
row('DPP-4 vs adenylyl cyclase (other scene)', NEW['dpp4'], NEW['adenylyl-cyclase'])

print('\n5. Other scenes')
row('GLUT4 vs insulin, now', OLD['glut4'], T['mol-insulin'])
row('GLUT4 vs insulin, proposed', NEW['glut4'], T['mol-insulin'])
row('adiponectin grains now (green) vs drug', OLD['adiponectin-grain'], NEW['semaglutide'])
row('adiponectin proposed (blue) on fat ground', NEW['adiponectin'], FAT_GROUND)
row('nausea olive vs drug', NEW['nausea'], NEW['semaglutide'])
row('glucagon vs receptor (grammar tension)', NEW['glucagon'], NEW['glp1r'])
row('alpha cell vs receptor', T['cell-alpha'], NEW['glp1r'])
row('placebo grey vs spent grey (S12 chart)', '#9a9098', NEW['glp1-spent'])

print('\n6. Outside vs inside the cell')
row('extra vs intra ground, now', OLD['extra-ground'], IG)
row('extra vs intra ground, proposed', NEW['extra-ground'], IG)
row('extra ground proposed vs blood ground', NEW['extra-ground'], T['blood-ground'])

print('\n7. Every proposed molecule on the fields it sits on (rule: 1.7:1)')
for k in ('semaglutide', 'glp1', 'orforglipron', 'glp1r', 'gprotein', 'dpp4', 'glucagon',
          'somatostatin', 'glut4'):
    print(f'  {k:16s} rose {cr(NEW[k], NEW["extra-ground"]):4.2f}  honey {cr(NEW[k], IG):4.2f}')
for k in ('camp', 'adenylyl-cyclase', 'pka', 'epac2', 'glucose'):
    print(f'  {k:16s} honey {cr(NEW[k], IG):4.2f}')

print('\n8. Outline colours (fill at 55%) and their lightness')
for k in ('semaglutide', 'glp1', 'orforglipron', 'camp', 'glp1r', 'gprotein', 'adenylyl-cyclase',
          'pka', 'epac2', 'glut4', 'glucagon', 'somatostatin', 'dpp4', 'adiponectin'):
    ln = shade(NEW[k], .55)
    print(f'  {k:16s} {NEW[k]} -> {ln}  L {oklch(ln)[0] * 100:4.1f}')
cur = sorted(round(oklch(T[k])[0] * 100) for k in T if k.startswith('mol-') and k.endswith('-line'))
print(f'  current molecule outlines span L {cur[0]}–{cur[-1]}')
print('  chroma: drug %.3f, albumin %.3f, insulin %.3f' % (
    oklch(NEW['semaglutide'])[1], oklch(OLD['albumin'])[1], oklch(T['mol-insulin'])[1]))
