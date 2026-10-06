# -*- coding: utf-8 -*-
"""Índice de B2T01 = el de la guía M108 (petición del usuario, 6-10-2026).

Los apartados y unidades de B2T01.py se escriben con su numeración de trabajo (bloques I-VI); aquí se
REORDENAN y RENUMERAN según los epígrafes de la propia guía (5 bloques) y se reasignan todas las remisiones
(«→ III.2.4») de apartados, flashcards, glosario, cronología y test. Así el contenido se mantiene y solo cambia
dónde está."""
import re

# Orden de la guía M108 (epígrafes en rojo = bloques; epígrafes en negrita = apartados)
#   I   La Unión Europea: Antecedentes
#   II  Objetivos y naturaleza jurídica. Los Tratados originarios y modificativos
#   III El Tratado de la Unión Europea y el Tratado de Funcionamiento de la Unión Europea
#   IV  El proceso de ampliación
#   V   Las cooperaciones reforzadas
# Cada apartado: (id, rótulo, [(apartado de origen, unidad|"pre")…]); la unidad es el «N.M» de B2T01.py.
PLAN = [
 ("bI", "I. La Unión Europea: antecedentes", [
   ("s1", "Del fin de la Segunda Guerra Mundial a la Declaración Schuman y el Día de Europa", [("s1", "pre"), ("s1", "1.1"), ("s1", "1.2"), ("s1", "1.3")]),
   ("s2", "Del fracaso de la CED a la Conferencia de Mesina (ampliación de la guía)", [("s2", "pre"), ("s2", "2.1")])]),
 ("bII", "II. Objetivos y naturaleza jurídica. Los Tratados originarios y modificativos", [
   ("s3", "Naturaleza jurídica", [("s3", "1.4"), ("s3", "1.3"), ("s3", "1.5")]),
   ("s3b", "La Unión Europea (TUE, art. 1)", [("s3", "1.1"), ("s3", "1.2"), ("s3", "1.7")]),
   ("s4", "Valores de la Unión Europea (TUE, art. 2)", [("s4", "2.1"), ("s4", "2.2")]),
   ("s4b", "Objetivos de la Unión Europea (TUE, art. 3)", [("s4", "2.3"), ("s4", "2.4")]),
   ("s7", "Tratados originarios y modificativos: de París a Lisboa", [("s10", "4.2"), ("s3", "1.6"), ("s7", "1.1"), ("s7", "1.2"),
        ("s8", "2.1"), ("s8", "2.2"), ("s8", "2.3"), ("s8", "2.4"), ("s8", "2.5"), ("s9", "3.1"), ("s9", "3.3"), ("s9", "3.2")]),
   ("s10", "Tratados originarios y modificativos: el cuadro maestro (guía M108)", [("s10", "4.1"), ("s10", "4.3"), ("s10", "4.4"), ("s10", "4.5")])]),
 ("bIII", "III. El Tratado de la Unión Europea y el Tratado de Funcionamiento de la Unión Europea", [
   ("s12", "El Tratado de la Unión Europea: origen y estructura", [("s12", "1.1"), ("s12", "1.2")]),
   ("s5", "Principios en el reparto competencial (TUE, arts. 4 y 5)", [("s5", "2.1"), ("s5", "2.2"), ("s5", "2.3")]),
   ("s6a", "Carta de los Derechos Fundamentales de la Unión Europea (TUE, art. 6)", [("s6", "3.1")]),
   ("s6", "Procedimientos de alerta temprana y de violación de los valores de la UE (TUE, art. 7)", [("s6", "3.2"), ("s6", "3.3")]),
   ("s6c", "Vecindad (TUE, art. 8)", [("s6", "3.4")]),
   ("s6b", "Disposiciones sobre los principios democráticos (TUE, arts. 9 a 12)", [("s6b", "4.1"), ("s6b", "4.2"), ("s6b", "4.3"), ("s6b", "4.4")]),
   ("s10b", "Disposiciones finales: revisión de los Tratados (TUE, arts. 47 a 55)", [("s10b", "5.1"), ("s10b", "5.2"), ("s10b", "5.3"), ("s10b", "5.4")]),
   ("s11", "El Tratado de Funcionamiento de la Unión Europea (TFUE)", [("s11", "6.1"), ("s11", "6.2"), ("s11", "6.3"), ("s11", "6.4")])]),
 ("bIV", "IV. El proceso de ampliación", [
   ("s13", "Procedimiento de adhesión (TUE, art. 49) y criterios de Copenhague", [("s13", "1.1"), ("s13", "1.2"), ("s13", "1.3"), ("s13", "1.4")]),
   ("s15", "Procedimiento de retirada (TUE, art. 50)", [("s15", "3.1"), ("s15", "3.2"), ("s15", "3.3")]),
   ("s14", "Ampliaciones, retiradas y candidaturas a la Unión Europea", [("s14", "2.1"), ("s14", "2.2"), ("s14", "2.3")])]),
 ("bV", "V. Las cooperaciones reforzadas", [
   ("s16", "Concepto, finalidad y condiciones (TUE, art. 20; TFUE, arts. 326 a 328)", [("s16", "1.1"), ("s16", "1.2"), ("s16", "1.3"), ("s17", "2.1"), ("s17", "2.2"), ("s17", "2.3")]),
   ("s18", "Autorización, votación y participación posterior (TFUE, arts. 329 a 331)", [("s18", "3.1"), ("s18", "3.2"), ("s18", "3.3"), ("s18", "3.4")]),
   ("s19", "Gastos, pasarelas y coherencia (TFUE, arts. 332 a 334)", [("s19", "4.1"), ("s19", "4.2"), ("s19", "4.3"), ("s19", "4.4")])]),
]
# apartados de trabajo que desaparecen al fundirse en otro (glosario y cronología apuntan al nuevo)
FUSIONADOS = {"s8": "s7", "s9": "s7", "s17": "s16"}
ROM = ["I", "II", "III", "IV", "V", "VI"]
RES = r"\n*@> \*\*▸ En resumen\.\*\*\n(?:@> .*\n?)+\s*$"
UNIDAD = re.compile(r"(?m)^### (\d+\.\d+) (.*)$")


def _trocear(body):
    """body → {"pre": texto, "N.M": texto con su «### N.M título»}."""
    m = list(UNIDAD.finditer(body))
    out = {"pre": body[:m[0].start()].strip("\n") if m else body.strip("\n")}
    for i, x in enumerate(m):
        out[x.group(1)] = body[x.start(): m[i + 1].start() if i + 1 < len(m) else len(body)].strip("\n")
    return out


def reorganizar(T, bloques, bare):
    """T: Tema con T.S en el orden de trabajo. bloques: {id de bloque: (donde(...) ya compuesto, resumen ya compuesto)}.
    bare: [(texto viejo, texto nuevo)] para las remisiones sin flecha que hay que escribir a mano (se aplican tras renumerar)."""
    viejo = {s["id"]: s for s in T.S}
    codigo_viejo = {i: s["title"].split(" ")[0] for i, s in viejo.items() if re.match(r"^(I{1,3}|IV|V|VI)\.\d+$", s["title"].split(" ")[0])}
    trozos = {i: _trocear(s["body"]) for i, s in viejo.items() if i in codigo_viejo}
    # el «En resumen» de cada apartado viejo se retira: lo sustituye el de cada bloque nuevo
    for i, t in trozos.items():
        ultima = [k for k in t if k != "pre"][-1] if len(t) > 1 else "pre"
        t[ultima] = re.sub(RES, "", t[ultima] + "\n")
    # --- correspondencia vieja → nueva ---
    usados, mapa_u, mapa_a, nuevos = set(), {}, {}, []
    for b, (bid, bt, aps) in enumerate(PLAN):
        rom = ROM[b]
        for k, (aid, rotulo, items) in enumerate(aps, 1):
            cod = f"{rom}.{k}"; j = 0; partes = []
            for (o, u) in items:
                assert (o, u) not in usados, ("UNIDAD REPETIDA", o, u); usados.add((o, u))
                txt = trozos[o][u]
                if u == "pre":
                    if txt.strip(): partes.append(txt)
                    continue
                j += 1; m = UNIDAD.match(txt); assert m, (o, u)
                partes.append(f"### {k}.{j} {m.group(2)}" + txt[m.end():])
                mapa_u[f"{codigo_viejo[o]}.{u.split('.')[1]}"] = f"{cod}.{j}"
                mapa_a.setdefault(codigo_viejo[o], cod)
            nuevos.append(dict(id=aid, bloque=bid, title=f"{cod} {rotulo}", body="\n\n".join(partes), nivel=2))
    for i, t in trozos.items():   # nada se queda sin colocar
        for u in t:
            if u == "pre" and not t[u].strip(): continue
            assert (i, u) in usados, ("SIN COLOCAR", i, u)
    # --- remisiones ---
    def remitir(txt):
        def f(m):
            a, u = m.group(1), m.group(2)
            if u:
                assert f"{a}.{u}" in mapa_u, ("REMISIÓN SIN DESTINO", m.group(0)); return "→ " + mapa_u[f"{a}.{u}"]
            assert a in mapa_a, ("REMISIÓN SIN DESTINO", m.group(0)); return "→ " + mapa_a[a]
        return re.sub(r"→ ((?:I{1,3}|IV|V|VI)\.\d+)(?:\.(\d+))?", f, txt)
    marca = {}
    def proteger(txt):          # las remisiones sin flecha se escriben a mano: se apartan antes y se ponen después
        for n, (v, _) in enumerate(bare):
            marca[n] = "\u0001%d\u0002" % n; txt = txt.replace(v, marca[n])
        return txt
    def poner(txt):
        for n, (_, nuevo) in enumerate(bare): txt = txt.replace(marca[n], nuevo)
        return txt
    def tratar(txt): return poner(remitir(proteger(txt)))
    # --- apartados nuevos con sus cabeceras de bloque y sus resúmenes ---
    S = [s for s in T.S if s["id"] == "s0"]
    for (bid, bt, aps) in PLAN:
        cab, res = bloques[bid]
        S.append(dict(id=bid, title=bt, body=cab, nivel=1))
        mios = [n for n in nuevos if n["bloque"] == bid]
        mios[-1]["body"] += "\n\n" + res
        S += [dict(id=n["id"], title=n["title"], body=n["body"], nivel=2) for n in mios]
    S += [s for s in T.S if s["title"].startswith("Cierre")]
    for s in S: s["body"] = tratar(s["body"])
    T.S = S
    for f in T.FC: f["q"], f["a"] = tratar(f["q"]), tratar(f["a"])
    for g in T.G: g["d"] = tratar(g["d"]); g["section"] = FUSIONADOS.get(g["section"], g["section"])
    for h in T.H: h["txt"], h["cons"] = tratar(h["txt"]), tratar(h["cons"]); h["target"] = FUSIONADOS.get(h["target"], h["target"])
    for q in T.Q: q["e"] = tratar(q["e"])
    return mapa_u, mapa_a
