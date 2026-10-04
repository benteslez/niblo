# Progreso: desarrollo de temas y tests reales

Encargo del usuario (4-10-2026): desarrollar todos los temas «Solo BOE», los
«BOE + temario» (al menos la parte legal) y los del bloque II con la legislación
de la UE, con el método del tema I.2 (ver `CLAUDE.md`). Orden acordado: primero
los «Solo BOE» empezando por el bloque IV; después V, I, VI, II y III.
Si la sesión se para, una rutina la reanuda cada 4 h: retomar aquí el primer
punto pendiente.

Herramientas: `herramientas/oposicion/` (ver su `LEEME.md`). Cada tema se
publica en `temas/<id>.json` y se apunta en `temas/indice.json`.

## 0. Infraestructura

- [x] Temas en archivos aparte (`temas/`), etiquetas de fuente (`[[COD]]`),
      herramientas en el repo.

## 1. Tests reales (petición intercalada del usuario)

- [x] GACE-P 2025 (promoción interna): 96 con texto legal, 8 sin norma literal
      (105 PENDIENTE: Resolución de 25-5-2010 sobre nóminas; pedir al usuario).
- [x] GACE-X 2025 (extraordinaria): 95 con texto legal, 10 sin norma literal.
      **96 RETENIDA** (la plantilla da b; el art. 78.3 LGP no casa): esperar
      decisión del usuario. Pendientes de fuente: 31, 91, 100 (Res. 25-5-2010).
      Sin condiciones oficiales (minutos/penalización) hasta tener su convocatoria.

## 2. Temas «Solo BOE»

Bloque IV: - [x] IV.2 - [x] IV.4 - [x] IV.5 - [x] IV.6 - [x] IV.8 - [x] IV.10
- [x] IV.11 - [x] IV.12 - [x] IV.13

Bloque V: - [x] V.1 - [x] V.2 - [x] V.3 - [x] V.4 - [x] V.5 - [ ] V.6 - [x] V.7
- [ ] V.8 - [x] V.10

Bloque I: - [x] I.2 - [ ] I.1 - [ ] I.3 - [ ] I.4 - [ ] I.5 - [ ] I.6 - [ ] I.8
- [ ] I.9 - [ ] I.10 - [ ] I.11

Bloque VI: - [ ] VI.3 - [ ] VI.6 - [ ] VI.7

Bloque III: - [ ] III.8

## 3. Temas «BOE + temario» y bloque II

- [ ] I.7 - [ ] II.1 - [ ] II.2 - [ ] II.3 - [ ] II.4 - [ ] II.5 - [ ] II.6
- [ ] III.4 - [ ] III.5 - [ ] III.6 - [ ] III.7 - [ ] III.9
- [ ] IV.1 - [ ] IV.3 - [ ] IV.7 - [ ] IV.9 - [ ] V.9
- [ ] VI.1 - [ ] VI.2 - [ ] VI.4 - [ ] VI.5 - [ ] VI.8

## Notas

- Fuentes con acceso en el entorno: boe.es (API de datos abiertos), EUR-Lex
  (con navegador), *.europa.eu, *.gob.es, *.congreso.es,
  *.tribunalconstitucional.es, *.poderjudicial.es, *.seg-social.es, *.sepe.es,
  *.muface.es, *.tcu.es, *.airef.es, *.defensordelpueblo.es,
  *.consejodetransparencia.es, *.senado.es.
