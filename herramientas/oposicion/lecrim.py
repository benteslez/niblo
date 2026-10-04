import re
RUIDO = re.compile(r"^(BOLETÍN OFICIAL DEL ESTADO|LEGISLACIÓN CONSOLIDADA|Página \d+)$")
ESTR = re.compile(r"^(LIBRO|TÍTULO|CAPÍTULO|Sección \d|Disposici)")
CAB = re.compile(r"^(Artículo \d+(?: (?:bis|ter|quáter|quater|quinquies|sexies|septies|octies)(?: [a-z](?: \d)?)?)?)\.(.*)$")
def articulos(ruta='lecrim.txt'):
    L=[l.rstrip() for l in open(ruta,encoding='utf-8').read().split('\n')]
    L=L[[i for i,l in enumerate(L) if l.strip()=='LEY DE ENJUICIAMIENTO CRIMINAL'][-1]:]
    out={}; rub={}; act=None; ps=[]
    def cerrar():
        if act: out[act]=ps[:]
    for l in L:
        t=l.strip()
        if not t or RUIDO.match(t): continue
        m=CAB.match(t)
        if m:
            cerrar(); act=m.group(1)+'.'; ps=[]; r=m.group(2).strip()
            if r: rub[act]=r
            continue
        if act is None: continue
        if ESTR.match(t): cerrar(); act=None; ps=[]; continue
        nuevo = not ps or re.match(r"^(\d+\.(?:º|ª)? |[a-z]\) |\d+\.ª |\d+\.º )",t) or (re.search(r"[.:;]$",ps[-1][-1]) and len(ps[-1][-1])<84)
        if nuevo: ps.append([t])
        else: ps[-1].append(t)
    cerrar()
    res={}
    for k,v in out.items():
        pp=[]
        for p in v:
            s=p[0]
            for x in p[1:]:
                s = s[:-1]+x if s.endswith('-') and not s.endswith(' -') else s+' '+x
            pp.append(s)
        res[k]=pp
    return res, rub
if __name__=='__main__':
    a,r=articulos()
    print(len(a))
    for k in ['Artículo 384 bis.','Artículo 509.','Artículo 520 bis.','Artículo 527.','Artículo 553.','Artículo 579.','Artículo 588 ter d.','Artículo 520.']:
        print('##',k,r.get(k,'')); [print('  ',p) for p in a[k]]
