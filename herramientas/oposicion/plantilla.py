# -*- coding: utf-8 -*-
"""Plantilla común de los temas (método del I.2) sobre los textos del BOE/EUR-Lex
que da boe/boe.py. Todo lo literal se comprueba por programa; si algo no casa,
el generador se detiene.

Uso en temas/<ID>.py:
    from plantilla import *
    T = Tema("B4T02")
    T.ap("s0", "Mapa del tema…", cuerpo)            # apartados (nivel 1 o 2)
    lit("CE", "Artículo 86", resaltar=[…])          # bloque literal («>»)
    c("CE", "Artículo 86", "fragmento")             # cita literal en línea «…»
    unidad(cabecera, lit(…), fichab(…))             # artículo: ley + ficha
    examen("L", 47, porque={…}, apoyo=[…])          # pregunta oficial interactiva
    T.q(ley, art, cat, enunciado, [correcta, d1, d2, d3], explicación, [fragmentos])
    T.real("L", 47, cat)                            # pregunta oficial en el test
    T.fc(…), T.glos(…), T.hito(…); T.publicar()
"""
import json, os, re, sys, datetime
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe")]
sys.argv = sys.argv[:1]
import boe

RAIZ = os.path.dirname(os.path.dirname(AQUI))
_n = lambda x: " ".join(str(x).replace("\xa0", " ").split())
_lit = lambda x: _n(x).replace("«", "").replace("»", "").replace('"', "").replace("“", "").replace("”", "")
_norm = lambda x: _lit(x).lower()
# Citas y apoyos literales: se comparan CON mayúsculas (_lit); _norm (sin ellas) solo para
# comparar opciones de examen entre sí.

# Nombre corto de cada norma en las cabeceras de los bloques literales (la CE va sin él).
CORTO = {"CE": "", "L39": "Ley 39/2015", "L40": "Ley 40/2015", "LGOB": "Ley 50/1997, del Gobierno", "LOTC": "LOTC",
         "LJCA": "LJCA", "RCD": "Reglamento del Congreso", "TREBEP": "TREBEP", "LCSP": "LCSP", "LGP": "LGP",
         "LGS": "Ley 38/2003", "LEF": "LEF", "LPAP": "Ley 33/2003", "LOEP": "LO 2/2012", "LGT": "LGT", "CC": "Código Civil", "LO3_1980": "LO 3/1980, del Consejo de Estado", "LOPJ": "LOPJ"}
# Fuente (etiqueta) de cada norma: BOE salvo las de EUR-Lex.
def fuente(k): return "DOUE" if boe.IDS[k].startswith("CELEX:") else "BOE"


def bid(k, b): return b if b in boe.ley(k) else boe.bloque(k, b)
def parrafos(k, art): return boe.parrafos(k, bid(k, art))
def texto(k, art): return _n(" ".join(parrafos(k, art)))


def c(k, art, frag):
    """Cita literal en línea, entre comillas latinas; «…» une trozos. Se comprueba."""
    t = _lit(texto(k, art))
    for parte in frag.split("…"):
        p = _lit(parte.replace("**", ""))
        if p: assert p in t, ("CITA NO LITERAL", k, art, p)
    return "«" + frag + "»"


def lit(k, art, resaltar=(), solo=None, titulo=None):
    """Bloque literal del artículo (sin la línea de cabecera del BOE, que va como título).
    solo: índices de párrafo (el 0 es la cabecera «Artículo N. Rúbrica.»). resaltar: negritas literales."""
    ps = parrafos(k, art)
    cab_boe = ps[0]
    idx = solo if solo is not None else list(range(1, len(ps)))
    out, usados = [], set()
    for i in idx:
        p = ps[i]
        for r in resaltar:
            if r in p and r not in usados:
                p = p.replace(r, "**" + r + "**", 1); usados.add(r)
        out.append(p)
    falta = [r for r in resaltar if r not in usados]
    assert not falta, ("NEGRITA NO LITERAL", k, art, falta)
    if titulo is None:
        titulo = cab_boe.rstrip(".") + (f" ({CORTO.get(k, k)})" if CORTO.get(k, k) else "")
    cab = ["> [[DOUE]]"] if fuente(k) == "DOUE" else []
    return "\n".join(cab + ["> **" + titulo + "**"] + ["> " + p for p in out])


# --- Fichas, guías y unidades (idénticas a las del I.2: v4_util) -------------
OJO = "⚠ Ojo en el examen"
def _fila(k, v):
    if v is None or v == "": v = "—"
    if isinstance(v, (list, tuple)):
        v = list(v); cab = v.pop(0)[2:] if v and v[0].startswith("::") else ""
        # «::Subtítulo:» fuera de la primera posición: el visor no lo trata → negrita.
        return [f"=> {k}: {cab}"] + [f"=> - **{x[2:].replace('**', '').strip()}**" if x.startswith("::") else f"=> - {x}" for x in v]
    return [f"=> {k}: {v}"]
def _ficha(pares):
    out = []
    for k, v in pares: out += _fila(k, v)
    return "\n".join(out)
def ficha(titulares, contenido, limites, proteccion, ojo):
    return _ficha([("Titulares", titulares), ("Contenido", contenido), ("Límites", limites), ("Protección", proteccion), (OJO, ojo)])
def fichab(que, quien, como, plazos, ojo):
    return _ficha([("Qué", que), ("Quién", quien), ("Cómo", como), ("Plazos y mayorías", plazos), (OJO, ojo)])
def unidad(cab, *partes): return "### " + cab + "\n\n" + "\n\n".join(p.strip("\n") for p in partes if p)
def guia(*lineas): return "\n".join("@> " + l for l in lineas)
def donde(texto, puntos): return guia("**▸ Dónde estamos.** " + texto, "**▸ Qué vas a ver.** " + " · ".join(puntos))
def resumen(lineas, siguiente): return guia("**▸ En resumen.**", *["• " + l for l in lineas], "**→ " + siguiente + "**")
def clave(t): return "!> " + t
def trampa(t): return "?> " + t


# --- Preguntas de los exámenes oficiales ---------------------------------------
import importlib
EXAMENES = {"L": ("examen25L", "GACE-L 2025 · 1.er ejercicio"), "P": ("examen25P", "GACE-P 2025 · 1.er ejercicio"),
            "X": ("examen25X", "GACE-L 2025 extraordinario · 1.er ejercicio")}
_EX = {}
def _qs(cod):
    if cod not in _EX:
        m = importlib.import_module(EXAMENES[cod][0]); _EX[cod] = {q["n"]: q for q in m.qs}
    return _EX[cod]
PORQUE = {}

def examen(cod, n, porque, apoyo):
    """Pregunta oficial interactiva. porque: {letra: explicación}. apoyo: [(dato en la opción
    correcta, norma, artículo, fragmento literal)] → coherencia plantilla ↔ ley (se detiene si no casa)."""
    q = _qs(cod)[n]; assert not q["anulada"], (cod, n)
    ok = "abcd"[q["c"]]; PORQUE[(cod, n)] = dict(porque)
    assert sorted(porque) == list("abcd") and apoyo, (cod, n)
    for dato, k, art, frag in apoyo:
        assert _lit(frag) in _lit(texto(k, art)), ("APOYO NO LITERAL", cod, n, k, art, frag)
        assert _norm(dato) in _norm(q["o"][ok]), ("LA PLANTILLA NO CASA CON LA LEY", cod, n, ok, dato)
    for x in "abcd":
        if x != ok: assert not all(_norm(d) in _norm(q["o"][x]) for d, *_ in apoyo), ("DISTRACTOR IGUAL DE APOYADO", cod, n, x)
    lin = [f"**📋 Pregunta real · {EXAMENES[cod][1]} · n.º {n}**", "«" + q["q"] + "»"]
    lin += [f"[{'x' if x == ok else ' '}] {x}) {q['o'][x]} || {porque[x]}" for x in "abcd"]
    lin.append(f"= **Respuesta correcta: {ok})**, según la plantilla definitiva, y coherente con el texto legal citado.")
    return "\n".join("%> " + l for l in lin)


class Tema:
    def __init__(self, id, subtitulo, etiquetas):
        self.id = id; self.S = []; self.Q = []; self.FC = []; self.G = []; self.H = []
        prog = _programa()[id]
        self.meta = {"id": id, "group": id[:2], "number": int(id[3:]), "codigo": prog["c"], "title": prog["e"],
                     "subtitle": subtitulo, "etiquetas": etiquetas}

    def ap(self, id, title, body, nivel=1):
        assert not any(s["id"] == id for s in self.S), id
        self.S.append({"id": id, "title": title, "body": body.strip("\n"), "nivel": nivel})

    def q(self, k, art, cat, enunciado, opciones, explicacion, frags):
        """Pregunta de test: opciones[0] es la correcta (la app baraja). Los fragmentos
        en que se apoya tienen que estar literales en el artículo."""
        assert len(opciones) == 4 and len(set(map(_norm, opciones))) == 4, enunciado
        for f in ([frags] if isinstance(frags, str) else frags):
            assert _lit(f) in _lit(texto(k, art)), ("PREGUNTA SIN APOYO LITERAL", k, art, f)
        self.Q.append({"q": enunciado, "o": opciones, "c": 0, "e": explicacion, "cat": cat})

    def real(self, cod, n, cat):
        q = _qs(cod)[n]; ok = "abcd"[q["c"]]; P = PORQUE[(cod, n)]
        e = f"Respuesta {ok}) según la plantilla definitiva. " + " ".join(("✅ " if x == ok else "✗ ") + f"{x}) " + P[x] for x in "abcd").replace("**", "")
        self.Q.append({"q": q["q"], "o": [q["o"][x] for x in "abcd"], "c": q["c"], "e": e, "cat": cat,
                       "real": f"Examen {EXAMENES[cod][1].replace(' · ', ' · ')} · pregunta {n}"})

    def fc(self, q, a, cat): self.FC.append({"q": q, "a": a, "cat": cat})
    def glos(self, t, d, section, cat): self.G.append({"t": t, "d": d, "section": section, "cat": cat})
    def hito(self, y, txt, cons, cat, target): self.H.append({"y": y, "txt": txt, "cons": cons, "cat": cat, "target": target})

    def _cierre1_al_test(self):
        """Las preguntas de exámenes oficiales NO van en los apuntes (petición del usuario, 5-10-2026): viven en el test del tema
        («Práctica activa»). Se quita el apartado «Cierre 1»; las preguntas de sus recuadros que aún no estén en el test se pasan
        a él (con su `real`, su respuesta y el porqué de cada opción) y el consejo «Cómo se pregunta» se traslada al repaso final."""
        c1 = [x for x in self.S if x["title"].startswith("Cierre 1")]
        if not c1: return
        vistas = {_norm(q["q"]) for q in self.Q}
        body = c1[0]["body"]
        for bloque in re.findall(r"(?:^%> .*\n?)+", body, re.M):
            L = [l[3:] for l in bloque.strip("\n").split("\n")]
            hd = re.match(r"\*\*(?:📋 Pregunta real · (.+?) · n\.º (\d+)|🎓 Pregunta de la guía M108 · n\.º (\d+))", L[0])
            if not hd: continue
            enun = L[1].strip("«»")
            if _norm(enun) in vistas: continue
            ops = [re.match(r"\[( |x)\] ([a-d])\) (.*?) \|\| (.*)$", l) for l in L[2:6]]
            assert all(ops), ("OPCIONES NO LEÍDAS", self.id, L[:3])
            ok = [m.group(1) for m in ops].index("x")
            e = f"Respuesta {'abcd'[ok]}) según la plantilla definitiva. " + " ".join(("✅ " if i == ok else "✗ ") + f"{m.group(2)}) " + m.group(4) for i, m in enumerate(ops)).replace("**", "")
            q = {"q": enun, "o": [m.group(3) for m in ops], "c": ok, "e": e, "cat": "Examen real"}
            if hd.group(1): q["real"] = f"Examen {hd.group(1)} · pregunta {hd.group(2)}"
            else: q["ac"] = f"M108 · pregunta {hd.group(3)}"; q["cat"] = "Guía M108"
            self.Q.append(q); vistas.add(_norm(enun))
        tip = re.search(r"### Cómo se pregunta\n\n(.*?)(?=\n### |\Z)", body, re.S)
        self.S = [x for x in self.S if x is not c1[0]]
        cierre = [x for x in self.S if x["title"].startswith("Cierre 2")]
        if cierre:
            cierre[0]["title"] = cierre[0]["title"].replace("Cierre 2.", "Cierre.", 1)
            if tip: cierre[0]["body"] += "\n\n### Cómo se pregunta\n\n" + tip.group(1).strip()
        sust = [(r"Siguiente: Cierre 1\.[^*\n]*", "Siguiente: Cierre. Repaso en 10 minutos (por bloques)"),
                (r"\*\*Cierre 1\*\* \([^)]*\) y \*\*Cierre 2\*\* \(([^)]*)\)", "el **Cierre** (\\1); las preguntas de exámenes oficiales están en el **test** («Práctica activa», barra lateral)"),
                (r"\(→ Cierre 1\)", "(está en el test)"), (r", → Cierre 1\)", ", está en el test)"), (r"; → Cierre 1\)", "; está en el test)"),
                (r"→ Cierre 1", "está en el test"),
                (r"Para fijarlo: Cierre 1 \(preguntas oficiales de 2025\) y Cierre 2 \(repaso por bloques\)", "Para fijarlo: el repaso del Cierre y el test («Práctica activa»), donde están las preguntas oficiales de 2025"),
                (r"- Al final: \*\*Cierre 1\*\* \(las preguntas oficiales de 2025 sobre este tema\) y \*\*Cierre 2\*\* \(repaso por bloques\)\.",
                 "- Al final: el **Cierre** (repaso por bloques). Las preguntas de exámenes oficiales de este tema están en el **test** («Práctica activa», barra lateral)."),
                (r"del Cierre 2\b", "del Cierre")]
        for x in self.S:
            for a_, b_ in sust: x["body"] = re.sub(a_, b_, x["body"])
        for f in self.FC: f["a"] = re.sub(r"→ Cierre 1", "está en el test", f["a"])

    def publicar(self):
        ids = {s["id"] for s in self.S}
        for g in self.G: assert g["section"] in ids, g
        for h in self.H: assert h["target"] in ids, h
        # Remisiones «→ II.4» o «→ II.4.2»: tienen que existir
        tit = {s["title"].split(" ")[0]: s for s in self.S}
        for s in ([] if os.environ.get("NIBLO_SIN_REMISIONES") else self.S):
            for m in re.finditer(r"→ ((?:I{1,3}|IV|V|VI)\.\d+)(?:\.(\d+))?", s["body"]):
                assert m.group(1) in tit, ("REMISIÓN ROTA", s["id"], m.group(0))
                if m.group(2): assert f"### {m.group(1).split('.')[1]}.{m.group(2)} " in tit[m.group(1)]["body"], ("REMISIÓN ROTA", s["id"], m.group(0))
        self._cierre1_al_test()
        sello = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
        data = dict(self.meta, sections=self.S, glossary=self.G, timeline=self.H, flashcards=self.FC, questions=self.Q, cargado=sello)
        out = {"_format": "gestion_hub_config", "_version": 2, "_exportedAt": sello, "ajustes": None, "temas": {self.id: data}}
        # NIBLO_SALIDA=<carpeta>: prueba sin tocar temas/ ni el índice (auditorías en paralelo).
        if os.environ.get("NIBLO_SALIDA"):
            os.makedirs(os.environ["NIBLO_SALIDA"], exist_ok=True)
            open(os.path.join(os.environ["NIBLO_SALIDA"], self.id + ".json"), "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
            print(self.id, "· generado en", os.environ["NIBLO_SALIDA"], file=sys.stderr); return
        d = os.path.join(RAIZ, "temas")
        open(os.path.join(d, self.id + ".json"), "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
        ip = os.path.join(d, "indice.json"); idx = json.load(open(ip, encoding="utf-8"))
        idx["temas"][self.id] = sello
        json.dump(idx, open(ip, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(self.id, "· apartados", len(self.S), "· preguntas", len(self.Q), "· flashcards", len(self.FC),
              "· glosario", len(self.G), "· hitos", len(self.H), "· literales", sum(s["body"].count("\n> **") + s["body"].startswith("> **") for s in self.S), file=sys.stderr)


_PROG = None
def _programa():
    """TEMAS_PROGRAMA + EPIGRAFES de oposicion.html → {id: {c, e, l}}."""
    global _PROG
    if _PROG is None:
        import subprocess
        js = r"""const fs=require('fs');const s=fs.readFileSync(process.argv[1],'utf8');
const grab=n=>{const i=s.indexOf('const '+n+' = ');const st=s.indexOf('{',i);let d=0,j=st;for(let k=st;k<s.length;k++){if(s[k]==='{')d++;if(s[k]==='}'){d--;if(!d){j=k+1;break;}}}return eval('('+s.slice(st,j)+')');};
const TP=grab('TEMAS_PROGRAMA'),EP=grab('EPIGRAFES');const out={};for(const b in TP)TP[b].forEach((t,k)=>{out[b+'T'+String(k+1).padStart(2,'0')]={c:t.c,e:t.e,l:EP[t.c]};});console.log(JSON.stringify(out));"""
        _PROG = json.loads(subprocess.run(["node", "-e", js, os.path.join(RAIZ, "oposicion.html")], capture_output=True, text=True, check=True).stdout)
    return _PROG
