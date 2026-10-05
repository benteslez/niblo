# -*- coding: utf-8 -*-
"""Convierte los esquemas de procedimiento del PDF M108 en SVG vectorial (cajas, flechas y textos tal cual) y saca las
casillas (cajas con texto) para que la app las haga clicables.  Uso:  python3 esquemas_svg.py <pdf> <salida>"""
import sys, os, json, base64, html
import pymupdf
PDF, OUT = sys.argv[1], sys.argv[2]
d = pymupdf.open(PDF)
# clave: (página, (x0, y0, x1, y1) en pt, sección por defecto)
E = {
 "art7_1": (6, (45, 446, 556, 636), "s6"), "art7_2": (7, (44, 139, 545, 324), "s6"), "art354_238": (7, (40, 369, 540, 525), "s6"),
 "art11_4": (8, (338, 504, 526, 535), "s6b"),
 "art48_ordinario": (10, (45, 74, 556, 432), "s10b"), "art48_6": (11, (44, 154, 555, 304), "s10b"), "art48_7": (11, (44, 306, 555, 438), "s10b"),
 "art49": (12, (46, 473, 559, 664), "s13"), "art50": (13, (45, 342, 559, 513), "s15"),
 "art329_1": (15, (45, 300, 559, 415), "s18"), "art331_1": (15, (46, 646, 560, 761), "s18"),
 "art329_2": (16, (43, 215, 556, 348), "s18"), "art331_2": (16, (43, 546, 557, 666), "s18"),
}
hx = lambda t: "#%02x%02x%02x" % tuple(round(v * 255) for v in t[:3])
def ir(txt, defecto):
    x = txt.lower()
    if "consejo europeo" in x: return "B2T02"
    if "parlamentos nacionales" in x or x.strip() in ("pn",): return "B2T01:s6b"
    if "parlamento europeo" in x: return "B2T03"
    if "bce" in x: return "B2T03"
    if "alto representante" in x: return "B2T06"
    if "comisión" in x or "comision" in x: return "B2T02"
    if "consejo" in x: return "B2T02"
    if "convención" in x or "cig" in x or "conferencia" in x: return "B2T01:s10b"
    if "ratificación" in x: return "B2T01:s3"
    return "B2T01:" + defecto
def trazo_items(items):
    """Camino continuo: solo se abre un subcamino nuevo (M) cuando el segmento no empieza donde acabó el anterior."""
    out, ult = [], None
    for it in items:
        t = it[0]
        if t == "re":
            r = it[1]; out.append(f"M{r.x0:.2f} {r.y0:.2f}H{r.x1:.2f}V{r.y1:.2f}H{r.x0:.2f}Z"); ult = None; continue
        if t == "qu":
            q = it[1]; out.append(f"M{q.ul.x:.2f} {q.ul.y:.2f}L{q.ur.x:.2f} {q.ur.y:.2f}L{q.lr.x:.2f} {q.lr.y:.2f}L{q.ll.x:.2f} {q.ll.y:.2f}Z"); ult = None; continue
        p0 = it[1]
        if ult is None or abs(p0.x - ult.x) > .01 or abs(p0.y - ult.y) > .01: out.append(f"M{p0.x:.2f} {p0.y:.2f}")
        if t == "l": out.append(f"L{it[2].x:.2f} {it[2].y:.2f}"); ult = it[2]
        elif t == "c": out.append(f"C{it[2].x:.2f} {it[2].y:.2f} {it[3].x:.2f} {it[3].y:.2f} {it[4].x:.2f} {it[4].y:.2f}"); ult = it[4]
    return "".join(out)
meta = {}
for nombre, (pg, (x0, y0, x1, y1), sec) in E.items():
    p = d[pg - 1]; R = pymupdf.Rect(x0, y0, x1, y1); W, H = x1 - x0, y1 - y0
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W:.2f} {H:.2f}" width="{W:.2f}" height="{H:.2f}" font-family="Calibri,Carlito,\'Segoe UI\',Arial,sans-serif"><rect width="100%" height="100%" fill="#fff"/><g transform="translate({-x0:.2f} {-y0:.2f})">']
    cajas = []
    for dr in p.get_drawings():
        r = dr["rect"]
        if not r.intersects(R): continue
        path = trazo_items(dr["items"]) + ("Z" if dr.get("closePath") else "")
        if not path: continue
        fill = hx(dr["fill"]) if dr.get("fill") else "none"
        st = hx(dr["color"]) if dr.get("color") else "none"
        sw = dr.get("width") or 0
        eo = ' fill-rule="evenodd"' if (dr.get("even_odd") or path.count("M") > 1) else ""
        out.append(f'<path d="{path}"{eo} fill="{fill}" stroke="{st}" stroke-width="{sw:.2f}" stroke-linejoin="round"/>')
        # casillas: rectángulos con trazo de color (no el marco gris) y tamaño de caja
        if len(dr["items"]) == 1 and dr["items"][0][0] == "re" and dr.get("color") and 12 < r.height < 95 and 25 < r.width < 260:
            c = dr["color"]
            if not (abs(c[0] - c[1]) < .05 and abs(c[1] - c[2]) < .05): cajas.append(r)
    textos = []
    for b in p.get_text("dict", clip=R)["blocks"]:
        for l in b.get("lines", []):
            for sp in l["spans"]:
                t = sp["text"]
                if not t.strip(): continue
                bb = sp["bbox"]; textos.append((bb, t))
                col = "#%06x" % sp["color"]; neg = ' font-weight="700"' if sp["flags"] & 16 else ""; ita = ' font-style="italic"' if sp["flags"] & 2 else ""
                out.append(f'<text x="{sp["origin"][0]:.2f}" y="{sp["origin"][1]:.2f}" font-size="{sp["size"]:.2f}" fill="{col}"{neg}{ita} textLength="{bb[2] - bb[0]:.2f}" lengthAdjust="spacingAndGlyphs" xml:space="preserve">{html.escape(t.replace(chr(0xf0fe), chr(0x2611)).replace(chr(0xf078), chr(0x2612)))}</text>')
    for im in p.get_images(full=True):
        for rr in p.get_image_rects(im[0]):
            if rr.intersects(R) and rr.width < 40:
                png = p.get_pixmap(clip=rr, dpi=300).tobytes("png")
                out.append(f'<image x="{rr.x0:.2f}" y="{rr.y0:.2f}" width="{rr.width:.2f}" height="{rr.height:.2f}" xlink:href="data:image/png;base64,{base64.b64encode(png).decode()}"/>')
    out.append("</g></svg>")
    open(os.path.join(OUT, nombre + ".svg"), "w", encoding="utf-8").write("".join(out))
    hs = []
    for r in cajas:
        txt = " ".join(t for bb, t in textos if pymupdf.Rect(bb).intersects(r) and pymupdf.Rect(bb).get_area() and (pymupdf.Rect(bb) & r).get_area() / pymupdf.Rect(bb).get_area() > .5).strip()
        if txt: hs.append({"x": round(r.x0 - x0, 1), "y": round(r.y0 - y0, 1), "w": round(r.width, 1), "h": round(r.height, 1), "t": txt, "go": ir(txt, sec)})
    meta[nombre] = {"w": round(W, 1), "h": round(H, 1), "sec": sec, "h_": hs}
    print(nombre, os.path.getsize(os.path.join(OUT, nombre + ".svg")) // 1024, "KB", len(hs), "casillas")
json.dump(meta, open(os.path.join(OUT, "esquemas.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
