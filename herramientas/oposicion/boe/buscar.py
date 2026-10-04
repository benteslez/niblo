import json, sys, urllib.request, urllib.parse
def buscar(q, n=5):
    query = {"query": {"query_string": {"query": q}}}
    url = "https://boe.es/datosabiertos/api/legislacion-consolidada?query=" + urllib.parse.quote(json.dumps(query)) + f"&limit={n}"
    r = urllib.request.Request(url, headers={"Accept": "application/json"})
    d = json.load(urllib.request.urlopen(r, timeout=60))
    return [(x["identificador"], x["titulo"][:150], x.get("vigencia_agotada")) for x in d.get("data", [])]
for q in sys.argv[1:]:
    print("##", q)
    for x in buscar(q): print("  ", x)
