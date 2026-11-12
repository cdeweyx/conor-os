"""Line fan: a generated backdrop for a home screen.

Thirty seeded random walks in three pre-blended field grays,
a dashed envelope, a baseline, and one hero walk that leaves the band and exits with air
around its endpoint. Pure Python, compact SVG, every color a DESIGN.md token.

Paper notes: clipPath is ignored. A paper-colored mask rect over the text zone showed as a hard
cut and a box behind the input, so the generator bends the walks under the form instead (guard).
stroke-opacity is ignored, so depth is three grays at full opacity.

Usage:
  python3 linefield.py 7            # writes fan-7.html for seed 7
  python3 linefield.py 0 20         # writes fan-0.html .. fan-19.html to pick from

Default parameters: field 0.6, envelope 0.8, hero 0.9 / 1.5 / 2.2 (Chaikin-smoothed, three
segments), tip at x<=1340, hero_top 330, no mask: walks are bent away from the form zone (x 380 to 1080, above y 568, overshoot scaled 0.25).
The 0.6 field weight is under the scorecard's 1px floor, a deliberate miss.

For a new surface, change W, H, base, mask, hero_top, tip_x, the weights, and layer in build(), and keep
the guard's x range and top in sync with the form's real bounds plus a margin (the form moves when copy
wraps). Output runs about 54KB at 30 walks by 72 samples, more than the main context can carry in one
write_html call, so hand the write to a `worker` agent (Model: worker role) that reads the file and calls
write_html replace on the old layer. Fewer samples changes the field; coarser RDP barely helps. Record the
seed and parameters in the layer name and a hand-back note so the build can regenerate the layer. Other
field types keep the simplify, smooth, rank, mask, and seed-loop steps and swap the walk generator.
"""
import random, math, sys
W,H=1440,900
FIELD=["var(--color-field-1)","var(--color-field-2)","var(--color-field-3)"]
def walks(seed,N=30,T=72,step=7.5):
    r=random.Random(seed); out=[]
    for i in range(N):
        y=0; drift=r.gauss(0,0.35); pts=[0.0]
        for t in range(1,T): y+=r.gauss(drift,step); pts.append(y)
        out.append(pts)
    return out
def rdp(pts,eps):
    if len(pts)<3: return pts
    (x1,y1),(x2,y2)=pts[0],pts[-1]; dmax=0;idx=0
    dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy) or 1
    for i in range(1,len(pts)-1):
        x,y=pts[i]; d=abs(dy*x-dx*y+x2*y1-y2*x1)/L
        if d>dmax: dmax,idx=d,i
    if dmax>eps: return rdp(pts[:idx+1],eps)[:-1]+rdp(pts[idx:],eps)
    return [pts[0],pts[-1]]
def cr2bez(p):
    if len(p)<2: return ""
    d=f"M{p[0][0]:.0f},{p[0][1]:.0f}"
    for i in range(len(p)-1):
        p0=p[i-1] if i>0 else p[i]; p1=p[i]; p2=p[i+1]; p3=p[i+2] if i+2<len(p) else p2
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6); c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f" C{c1[0]:.0f},{c1[1]:.0f} {c2[0]:.0f},{c2[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}"
    return d
def build(seed,base=640,hero_top=330,tip_x=1340,field_w=0.6,env_w=0.8,hero_w=(0.9,1.5,2.2),
          mask=None,guard=(380,1080,568,0.25),layer="Home/Line fan v3"):
    ws=walks(seed); T=len(ws[0])
    xs=[-100+(W+200)*t/(T-1) for t in range(T)]
    if guard:
        # bend walks away from the form zone instead of masking them: above `top` between x0 and x1,
        # the overshoot is scaled by `k`, so lines curve under the form rather than stopping at an edge
        gx0,gx1,gtop,gk=guard; lim=base-gtop
        for w in ws:
            for t in range(T):
                if gx0<=xs[t]<=gx1 and w[t]>lim: w[t]=lim+(w[t]-lim)*gk
    hi=max(range(len(ws)),key=lambda i:ws[i][-1]); ws.pop(hi)
    # hero: in-band until 66% of the width, then an eased rise to hero_top
    r=random.Random(seed+99); out=[]; y=0
    for t in range(T):
        f=t/(T-1)
        if f<0.66: y+=r.gauss(0.2,4.5); out.append(y)
        else:
            g=(f-0.66)/0.34; ease=g*g*(3-2*g)
            out.append(out[-1]*0.65+(base-hero_top)*ease*0.35+r.gauss(0,1.5))
    hero=out
    rank=sorted(range(len(ws)),key=lambda i:abs(ws[i][-1]))
    tone={i:FIELD[min(2,(k*3)//len(ws))] for k,i in enumerate(rank)}
    p=[]
    p.append(f'<svg layer-name="{layer}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" style="position:absolute; left:0px; top:0px; width:{W}px; height:{H}px;">')
    env_up=[(xs[t], base-1.6*math.sqrt(t)*7.5*0.55) for t in range(T)]
    env_dn=[(xs[t], base+1.6*math.sqrt(t)*7.5*0.55) for t in range(T)]
    for e in (env_up,env_dn):
        p.append(f'<path d="{cr2bez(rdp(e,0.5))}" stroke="{FIELD[1]}" stroke-width="{env_w}" stroke-dasharray="2 5" stroke-linecap="round"/>')
    for i,w in enumerate(ws):
        pts=[(xs[t], base-w[t]) for t in range(T)]
        p.append(f'<path d="{cr2bez(rdp(pts,0.6))}" stroke="{tone[i]}" stroke-width="{field_w}" stroke-linecap="round" stroke-linejoin="round"/>')
    p.append(f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="var(--color-line)" stroke-width="1"/>')
    if mask:
        x0,y0,x1,y1=mask
        p.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="var(--color-paper)"/>')
    hp=[(xs[t], base-hero[t]) for t in range(T) if xs[t]<=tip_x]
    hs=rdp(hp,0.6)
    # densify, then Chaikin twice, so the hero reads as one drawn line rather than a jointed walk
    dense=[]
    for i in range(len(hs)-1):
        for k in range(6):
            f=k/6; dense.append((hs[i][0]+(hs[i+1][0]-hs[i][0])*f, hs[i][1]+(hs[i+1][1]-hs[i][1])*f))
    dense.append(hs[-1])
    for _ in range(2):
        nd=[dense[0]]
        for i in range(len(dense)-1):
            a,b=dense[i],dense[i+1]
            nd.append((a[0]*0.75+b[0]*0.25,a[1]*0.75+b[1]*0.25)); nd.append((a[0]*0.25+b[0]*0.75,a[1]*0.25+b[1]*0.75))
        nd.append(dense[-1]); dense=nd
    hs=rdp(dense,0.3)
    n=len(hs); a=n//3; b=(2*n)//3
    segs=[hs[:a+1],hs[a:b+1],hs[b:]]
    for seg,w in zip(segs,hero_w):
        d="M"+" L".join(f"{x:.0f},{y:.0f}" for x,y in seg)
        p.append(f'<path d="{d}" stroke="var(--color-positive)" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    tx,ty=hs[-1]
    p.append(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="3.5" fill="var(--color-positive)" stroke="var(--color-paper)" stroke-width="1.5"/>')
    p.append('</svg>')
    s="\n".join(p)
    return s,(tx,ty),len(s)
if __name__=="__main__":
    a=int(sys.argv[1]); b=int(sys.argv[2]) if len(sys.argv)>2 else a+1
    for seed in range(a,b):
        s,tip,n=build(seed); open(f"fan-{seed}.html","w").write(s); print(seed,round(tip[0]),round(tip[1]),n)
