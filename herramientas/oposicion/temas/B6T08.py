# -*- coding: utf-8 -*-
"""Tema VI.8 (B6T08): Retribuciones de los funcionarios públicos. Nóminas: estructura y
normas de confección. Altas y bajas, su justificación. Ingresos en formalización. Devengo
y liquidación de derechos económicos.
Método del I.2. Normas (BOE): TREBEP (RDLeg 5/2015), arts. 22, 23 y 30; Ley 30/1984, art. 23;
Orden de 30 de julio de 1992 sobre instrucciones para la confección de nóminas (texto
consolidado); Orden de 1 de febrero de 1996, Instrucción de operatoria contable (reglas 66,
67, 69, 70 y 93); Resolución de 25 de mayo de 2010 de la Secretaría de Estado de Hacienda y
Presupuestos (instrucciones sobre nóminas; texto del diario, BOE-A-2010-8386, con su corrección
de errores BOE-A-2010-8782, que no afecta a los apartados citados). Los anexos XIV y XV de
esa Resolución solo vienen como imagen en el XML del BOE: su texto se toma de la capa de
texto del PDF oficial del BOE (boe.es) y se comprueba igual que el resto."""
import os, sys, re, subprocess, tempfile, urllib.request
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"TREBEP": "TREBEP", "L30": "Ley 30/1984", "ONOM1992": "Orden de 30-7-1992",
              "OIOC": "Orden de 1-2-1996, Instrucción de operatoria contable", "RES2010N": "Resolución de 25-5-2010"})

# --- Anexos XIV y XV de la Resolución de 25-5-2010: texto del PDF oficial del BOE -------------
PDF_URL = "https://boe.es/boe/dias/2010/05/26/pdfs/BOE-A-2010-8386.pdf"
def _pdf_texto():
    pdf = os.path.join(tempfile.gettempdir(), "BOE-A-2010-8386.pdf")
    if not os.path.exists(pdf):
        open(pdf, "wb").write(urllib.request.urlopen(PDF_URL, timeout=120).read())
    t = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
    return " ".join(t.split())
def _trozo(T, ini, fin, desde=0):
    i = T.index(ini, desde); j = T.index(fin, i) + len(fin)
    s = T[i:j]; assert "cve:" not in s and "BOLETÍN" not in s, s
    return s
_T = _pdf_texto()
_i14 = _T.index("ANEXO XIV"); _i15 = _T.index("ANEXO XV ", _i14)
_L = boe.ley("RES2010N")
_L["anexoXIV"] = ("Anexo XIV", [("articulo", "Anexo XIV. Cuotas mensuales de derechos pasivos")] + [("parrafo", _trozo(_T, "En los meses de junio y diciembre se abonará", "presente Resolución.", _i14))])
_L["anexoXV"] = ("Anexo XV", [("articulo", "Anexo XV. Indemnización por residencia en territorio nacional")] + [("parrafo", _trozo(_T, a, b, _i15)) for a, b in [
    ("Los importes anteriores experimentarán", "en cada grupo."),
    ("De acuerdo con la normativa vigente se deberá tener en cuenta:", "tener en cuenta:"),
    ("En lo que se refiere al personal de la Administración de Justicia", "trienio reconocido."),
    ("La indemnización por residencia comprende", "pagas extraordinarias."),
    ("El personal que perciba su sueldo", "misma proporción."),
    ("Quienes vinieran percibiendo", "estas últimas.")]])
assert _L["anexoXIV"][1][1][1].endswith("número 3.3 de la presente Resolución."), _L["anexoXIV"]
# El anexo XIII (cuotas a MUFACE, ISFAS y MUGEJU) repite la frase de la cuota doble (se cita en la ficha de IV.2.2).
_i13 = _T.index("ANEXO XIII")
assert "MUTUALIDAD GENERAL DE FUNCIONARIOS CIVILES DEL ESTADO, AL INSTITUTO SOCIAL DE LAS FUERZAS ARMADAS Y A LA MUTUALIDAD GENERAL JUDICIAL" in _T[_i13:_i14]
assert _trozo(_T, "En los meses de junio y diciembre se abonará", "presente Resolución.", _i13) == _L["anexoXIV"][1][1][1] and _T.index("En los meses de junio", _i13) < _i14

# Resolución de 25-5-2010: el XML del diario no tiene artículos; los apartados son párrafos del bloque «preambulo».
R = "preambulo"
def res(solo, ap, resaltar=()):
    return lit("RES2010N", R, resaltar, solo=solo, titulo=f"Resolución de 25-5-2010 (nóminas de los funcionarios), {ap}")
def orden(ap, rub, resaltar=(), solo=None):
    return lit("ONOM1992", ap, resaltar, solo=solo, titulo=f"Orden de 30-7-1992 (confección de nóminas), apartado {ap[1:]}" + (f". {rub}" if rub else ""))

T = Tema("B6T08",
  "Cinco preguntas: I. Qué retribuciones lleva la nómina (TREBEP, arts. 22 y 23; Ley 30/1984, art. 23; régimen completo en el tema V.6) · II. Cómo es una nómina y cómo se confecciona y se paga (Orden de 30-7-1992, aps. 1 y 5 a 8; Instrucción de operatoria contable, reglas 66, 67 y 69) · III. Cómo se justifican las altas, las bajas y las modificaciones (Orden de 1992, aps. 2 a 4) · IV. Qué se descuenta y se ingresa en formalización (Orden de 1992, ap. 5.1.5 a 5.1.8; Resolución de 25-5-2010, aps. A.3 y A.4.4 y anexo XIV; reglas 70 y 93) · V. Cómo se devengan y liquidan los derechos económicos (TREBEP, art. 30; Resolución de 25-5-2010). Cada artículo: texto literal del BOE y ficha.",
  ["Nómina", "Orden de 30-7-1992", "Habilitado", "Cierre el día 5", "Altas en nómina", "Bajas en nómina", "Modificaciones", "Deducciones formalizables", "Ingreso en formalización", "Importe líquido", "Devengo", "Liquidación por días", "Valor hora", "Pagas extraordinarias", "Indemnización por residencia", "Resolución de 25-5-2010"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 8):
> Retribuciones de los funcionarios públicos. Nóminas: estructura y normas de confección. Altas y bajas, su justificación. Ingresos en formalización. Devengo y liquidación de derechos económicos.

### El hilo conductor

El epígrafe tiene **cinco frases**; cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Qué retribuciones lleva la nómina? | TREBEP, arts. 22 y 23; Ley 30/1984, art. 23 (régimen completo: tema V.6) |
| **II** | ¿Cómo es una nómina y cómo se confecciona y se paga? | Orden de 30-7-1992, aps. 1, 5, 6, 7 y 8; Instrucción de operatoria contable (Orden de 1-2-1996), reglas 66, 67 y 69 |
| **III** | ¿Cómo se justifican las altas, las bajas y las modificaciones? | Orden de 30-7-1992, aps. 2, 3 y 4 |
| **IV** | ¿Qué se descuenta en la nómina y se ingresa en formalización? | Orden de 30-7-1992, ap. 5.1.5 a 5.1.8; Resolución de 25-5-2010, aps. A.3 y A.4.4 y anexo XIV; reglas 70 y 93 |
| **V** | ¿Cómo se devengan y se liquidan los derechos económicos? | TREBEP, art. 30; Resolución de 25-5-2010, aps. A.2, A.4.3 y C.1 y anexo XV; Orden de 1992, ap. 8 |

!> **La idea que une los cinco bloques:** el funcionario tiene derecho a unas **retribuciones** (I). Se le pagan **cada mes** a través de una **nómina** que confecciona el **habilitado** con una estructura fija (II). Cada **cambio** respecto de la nómina del mes anterior (alta, baja o modificación) se **justifica** con un documento (III). Del importe **íntegro** se **descuentan** deducciones; las **formalizables** se ingresan **en formalización** en el Tesoro (IV). Y las reglas de **devengo** dicen **cuánto** corresponde cada mes: mensualidad completa o por días, pagas extraordinarias, deducciones (V).

### Las normas, en una línea

- **Orden de 30 de julio de 1992** sobre instrucciones para la confección de nóminas: texto **consolidado** del BOE (vigente). Es la base de los bloques II a IV.
- **Resolución de 25 de mayo de 2010**, de la Secretaría de Estado de Hacienda y Presupuestos: la citan **dos** preguntas oficiales de 2025. No está consolidada: se cita el **texto publicado en el BOE** (BOE-A-2010-8386). Sus **cuantías** son las de 2010 y no se reproducen; ella misma dice que {c('RES2010N', R, 'sustituye, a partir de 1 de junio de 2010, a la Resolución de 4 de enero de 2010')} (ap. D.8): son instrucciones que se dictan para cada ejercicio. Sus **reglas de devengo** son las que se preguntan.
- **Instrucción de operatoria contable** (Orden de 1 de febrero de 1996): tramitación contable y pago de las nóminas (el resto, en el tema VI.5).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (preguntas oficiales de 2025) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué retribuciones lleva la nómina? (TREBEP, arts. 22 y 23; Ley 30/1984, art. 23)", donde(
  "Primera frase del epígrafe. El régimen retributivo completo se estudia en el **tema V.6**; aquí solo lo que hace falta para entender la nómina: **qué conceptos** se pagan y **cuándo** se devengan las pagas extraordinarias.",
  ["1 Básicas, complementarias y pagas extraordinarias (TREBEP, arts. 22 y 23; Ley 30/1984, art. 23)"]))

T.ap("s1", "I.1 Básicas, complementarias y pagas extraordinarias (TREBEP, arts. 22 y 23; Ley 30/1984, art. 23)", f"""
{unidad("1.1 Clases de retribuciones y pagas extraordinarias (TREBEP, art. 22.1 a 4)",
  lit("TREBEP", "Artículo 22", ["se clasifican en básicas y complementarias", "Las pagas extraordinarias serán dos al año"], solo=[1, 2, 3, 4]),
  fichab("Los conceptos que la nómina paga a un funcionario de carrera",
         "Funcionarios de carrera",
         ["Básicas: por el Subgrupo o Grupo y la antigüedad (sueldo y trienios)", "Complementarias: puesto, carrera profesional y desempeño", "Pagas extraordinarias: dos al año"],
         f"Cada paga extraordinaria: {c('TREBEP', 'Artículo 22', 'una mensualidad de retribuciones básicas y de la totalidad de las retribuciones complementarias')}, salvo las del art. 24 c) y d)",
         "Detalle de cada concepto: tema V.6. En la nómina cada uno tiene su **clave** (→ II.2.3)."))}

{unidad("1.2 Retribuciones básicas (TREBEP, art. 23)",
  lit("TREBEP", "Artículo 23", ["única y exclusivamente", "El sueldo", "Los trienios"]),
  fichab("Las únicas retribuciones básicas",
         "Funcionarios de carrera (cuantías en la Ley de Presupuestos Generales del Estado)",
         ["Sueldo del Subgrupo o Grupo", "Trienios: cantidad igual por Subgrupo o Grupo por cada tres años de servicio"],
         "Trienio: cada **tres años** de servicio",
         "Las básicas son «única y exclusivamente» sueldo y trienios: el complemento de destino **no** es básico. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.3 La versión de la Ley 30/1984: devengo de las pagas extraordinarias (art. 23.2 c y 23.4)",
  lit("L30", "aveintitres", ["se devengarán los meses de junio y diciembre", "Los funcionarios percibirán las indemnizaciones correspondientes por razón del servicio"], solo=[2, 7, 15]),
  fichab("Cuándo se devengan las pagas extraordinarias y el derecho a indemnizaciones",
         "Funcionarios a los que se aplica el régimen retributivo de la Ley 30/1984 (Administración del Estado: tema V.6)",
         "Dos pagas al año, de **al menos** una mensualidad del sueldo y trienios",
         c("L30", "aveintitres", "se devengarán los meses de junio y diciembre"),
         "**Junio y diciembre** (no julio). La Resolución de 2010 precisa el día: el **primer día hábil** de esos meses (→ V.3.2)."))}

{resumen([
  "Retribuciones **básicas** (sueldo y trienios, **única y exclusivamente**) y **complementarias**; **dos** pagas extraordinarias al año (TREBEP, arts. 22 y 23).",
  "Ley 30/1984: las pagas extraordinarias se devengan en **junio y diciembre**; además, **indemnizaciones** por razón del servicio (art. 23.2 c y 4).",
  "El régimen completo (complementos, interinos, indemnizaciones) está en el **tema V.6**."],
  "Siguiente: II. ¿Cómo es una nómina y cómo se confecciona y se paga?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo es una nómina y cómo se confecciona y se paga? (Orden de 30-7-1992; Instrucción de operatoria contable)", donde(
  "Segunda frase del epígrafe: **estructura y normas de confección** de la nómina. La Orden de 1992 dice qué contiene y cuándo se cierra; la Instrucción de operatoria contable, cómo se tramita su gasto y su pago.",
  ["1 Ámbito: la nómina como vía de pago (Orden, ap. 1; regla 66)", "2 Estructura de la nómina (Orden, ap. 5)", "3 Normas de confección: cierre, redondeo y treintavo (Orden, aps. 6 a 8)", "4 Tramitación contable y pago (reglas 67 y 69)"]))

T.ap("s2", "II.1 Ámbito: la nómina como vía de pago (Orden de 1992, ap. 1; regla 66)", f"""
{unidad("1.1 A quién se aplica la Orden (ap. 1)",
  orden("A1", "", ["se regirá por las presentes instrucciones"]),
  fichab("Instrucciones para confeccionar las nóminas de retribuciones",
         "Personal al servicio de la Administración del Estado del ámbito de la Ley 30/1984",
         f"Nóminas {c('ONOM1992', 'A1', 'que hayan de ser satisfechas con cargo a créditos consignados en el Presupuesto del Estado')}",
         "—",
         "La Orden regula la confección de las nóminas **pagadas con el Presupuesto del Estado**."))}

{unidad("1.2 Todo el personal en activo cobra por nómina (regla 66)",
  lit("OIOC", "regla66", ["se efectuará, en todos los casos, a través de las nóminas formuladas por los correspondientes habilitados", "la totalidad de los empleados públicos que se encuentren en situación activa"]),
  fichab("La nómina como único cauce de pago de las retribuciones del personal en activo",
         "Los **habilitados** formulan las nóminas",
         ["Cada nómina incluye a todos los empleados en activo del Departamento, Organismo o Servicio con derecho a cobro", "Personal con cargo al **capítulo primero** o personal laboral eventual con cargo al **capítulo sexto**"],
         "—",
         "«En **todos** los casos» a través de nómina; la formulan los **habilitados**."))}
""", 2)

T.ap("s3", "II.2 Estructura de la nómina (Orden de 1992, ap. 5)", f"""
{unidad("2.1 Formatos y modelos (ap. 5, párrafo inicial)",
  orden("A5", "Nóminas", ["UNE A4 (297 por 210 milímetros) o UNE A3 (297 por 420 milímetros)", "Modelo N1. Nómina de personal, para reclamar todas las retribuciones.", "Modelo RN. Hoja resumen de nómina."], solo=list(range(1, 15))),
  fichab("Las tres partes de una nómina",
         "El habilitado la confecciona",
         ["**Cuerpo** de la nómina: modelo N1 (anexo IV)", "**Resúmenes**: RN, RRD, RRX y REN (anexo V)", "**Estados justificativos**: VR1 a VR4 (retribuciones) y VD1 a VD4 (deducciones) (anexo VI)"],
         "—",
         "VR = variación de **retribuciones**; VD = variación de **deducciones**; 1 altas, 2 bajas, 3 modificaciones, 4 resumen."))}

{unidad("2.2 Cuerpo de la nómina: orden, cabecera y datos personales (ap. 5.1.1 a 5.1.3)",
  orden("A5", "", ["será el alfabético de apellidos y nombre", "Con la fecha del inicio y finalización del mes de devengo"], solo=list(range(15, 38))),
  fichab("Cómo se rellena el cuerpo de la nómina",
         "El habilitado (y su suplente, en su caso)",
         ["Perceptores numerados correlativamente desde la unidad, por orden **alfabético** de apellidos y nombre", "Cabecera: Ministerio u Organismo, Habilitación, clase de nómina, número, mes-año-agrupación, habilitado, período de liquidación y presupuesto", "Datos personales obligatorios: apellidos y nombre, DNI y número de Registro de personal"],
         f"Período de liquidación: {c('ONOM1992', 'A5', 'Con la fecha del inicio y finalización del mes de devengo')}",
         "Cuatro clases de nómina: funcionarios, funcionarios en el extranjero, contratados laborales y contratados laborales en el extranjero."))}

{unidad("2.3 Retribuciones y sus claves (ap. 5.1.4)",
  orden("A5", "", ["mediante 17 dígitos", "Deberá ser única para cada perceptor y concepto retributivo durante la totalidad del período de liquidación", "01: Sueldo.", "02: Antigüedad (trienios).", "03: Paga extraordinaria.", "09: Indemnización por residencia."], solo=list(range(38, 66))),
  fichab("Cada retribución, con su código, concepto y aplicación presupuestaria",
         "El habilitado",
         ["Código: la clave de cada retribución", "Concepto: su literal", "Aplicación presupuestaria: 17 dígitos (Sección, Organismo, Servicio, programa y subprograma, concepto y subconcepto)"],
         "Claves no reservadas: de la **14 a la 29** (funcionarios) y de la **31 a 59** (laborales)",
         "01 sueldo, 02 trienios, 03 paga extraordinaria, 04 destino, 05 específico, 06 productividad, 07 gratificaciones. La aplicación presupuestaria es **única** por perceptor y concepto en todo el período."))}

{unidad("2.4 Resúmenes, estados justificativos y justificantes (ap. 5.2 a 5.4)",
  orden("A5", "", ["Deberá ir firmada por el Habilitado y el Jefe del Centro o de la Dependencia correspondiente", "figurando sólo cantidades íntegras", "ejemplo: 3/VR1 ó 235/VR3"], solo=list(range(89, 109))),
  fichab("Lo que acompaña al cuerpo de la nómina",
         "Firma la hoja resumen el **Habilitado** y el **Jefe** del Centro o Dependencia",
         ["Hoja resumen: íntegro, líquido y neto iguales a los totales de la nómina", "Resumen de retribuciones y deducciones: por aplicaciones presupuestarias; por conceptos: por orden creciente de claves", "Estados justificativos: solo cantidades **íntegras**; altas, bajas y modificaciones respecto del mes anterior", "Columna de variación: MD-A, MD-D, MT-A, MT-D (y BD-D o BD-A por baja prevista el mes siguiente)"],
         "—",
         "Los justificantes se numeran con el número correlativo y la clave del estado (p. ej., 3/VR1) (→ III.3)."))}

{unidad("2.5 Nómina ordinaria y otras nóminas del mes (ap. 5.5)",
  orden("A5", "", ["tendrán asignado 01 como número de nómina", "Existirá una única nómina ordinaria para cada mes", "serán considerados como altas en nómina"], solo=[109, 110, 111]),
  fichab("Qué es la nómina ordinaria",
         "—",
         ["Número **01**; al menos las remuneraciones fijas en su cuantía y periódicas en su vencimiento", "Incluye en su mes de devengo las pagas extraordinarias de junio y diciembre", "Las demás nóminas del mes: números desde el **02**; sus perceptores cuentan como **altas**"],
         "Una única nómina ordinaria por mes, clase de nómina y agrupación",
         "Ordinaria = **01**; en las nóminas 02 y siguientes todos los perceptores son **altas** a efectos de los estados justificativos."))}
""", 2)

T.ap("s4", "II.3 Normas de confección: cierre, redondeo y treintavo (Orden de 1992, aps. 6 a 8)", f"""
{unidad("3.1 Cierre de la nómina ordinaria (ap. 6)",
  orden("A6", "", ["se cerrarán el día 5 de dicho mes"]),
  fichab("Fecha de cierre de la nómina ordinaria", "—", "—", c("ONOM1992", "A6", "el día 5 de dicho mes"),
         "Día **5** del propio mes. Cayó en 2025 (→ Cierre 1): ni el 1, ni el 28, ni el 30."))}

{unidad("3.2 Redondeo (ap. 7)",
  orden("A7", "", ["despreciando los decimales de cada partida inferior a cincuenta céntimos"]),
  fichab("Regla de redondeo de retribuciones y deducciones", "—",
         "Fracciones inferiores a la unidad: por debajo de cincuenta céntimos se desprecian; desde cincuenta, se sube a la unidad",
         "—", "El texto vigente de la Orden sigue expresado en **pesetas**; la regla es la del redondeo a la unidad más próxima."))}

{unidad("3.3 Liquidación por días efectivos: un treintavo (ap. 8)",
  orden("A8", "", ["un treintavo del importe mensual"]),
  fichab("Importe diario cuando los derechos se liquidan por días", "—",
         c("ONOM1992", "A8", "el importe diario equivalente a un treintavo del importe mensual del concepto retributivo correspondiente"),
         "—", "Regla de la Orden de 1992. La Resolución de 2010 da otra base de cálculo para las deducciones y las liquidaciones por días: **días naturales del mes** (→ V.1.2). Lee el enunciado: dice qué norma pregunta."))}
""", 2)

T.ap("s5", "II.4 Tramitación contable y pago de la nómina (Instrucción de operatoria contable, reglas 67 y 69)", f"""
{unidad("4.1 El compromiso del gasto al inicio del ejercicio (regla 67.1 y 4)",
  lit("OIOC", "regla67", ["al inicio del ejercicio, el Servicio gestor competente formulará un documento AD", "podrá efectuarse a partir de las cantidades que se incluyan en la nómina del mes de enero", "se podrá aceptar la expedición de documentos ADOK por cada una de las nóminas que se aprueben"], solo=[1, 2, 4, 12]),
  fichab("Contabilización del gasto de retribuciones del capítulo primero",
         "El **Servicio gestor** competente",
         ["Retribuciones fijas y periódicas: documento **AD** al inicio del ejercicio por el gasto previsto", "Si la estimación resulta inadecuada: documentos AD positivos o negativos", "Excepcionalmente: un **ADOK** por cada nómina"],
         "La estimación puede hacerse con la **nómina de enero**",
         "AD al **inicio** del ejercicio; luego, cada mes, el reconocimiento de la obligación (→ II.4.2). Documentos contables: tema VI.5."))}

{unidad("4.2 Reconocimiento de la obligación y pago (regla 69)",
  lit("OIOC", "regla69", ["confeccionarán, con arreglo a las normas vigentes, las nóminas de haberes de personal, que se aprobarán por el órgano competente del Servicio gestor", "antes del día 7 de cada mes", "al menos, con cinco días de antelación al correspondiente vencimiento", "mediante el pago en formalización de las mismas"]),
  fichab("Del habilitado al pago de la nómina",
         "**Habilitados** o cajeros pagadores (confeccionan y presentan); **órgano competente del Servicio gestor** (aprueba); **oficinas de contabilidad** (registran)",
         ["Documento **OK**, o **ADOK** si no hubo compromiso previo, con los «Resúmenes de nómina»", "Si en las Delegaciones Provinciales no llegan a tiempo las órdenes de pago: **pagos no presupuestarios** por el importe **líquido**, que se cancelan después con el **pago en formalización**"],
         "Presentación: **antes del día 7** de cada mes. Pago: al menos **cinco días** antes del vencimiento",
         "Día **5**: cierre de la nómina (→ II.3.1); día **7**: presentación del OK/ADOK; **cinco días** de antelación para el pago."))}

{resumen([
  "Todo el personal en activo cobra **por nómina**, formulada por los **habilitados** (regla 66); la Orden de 1992 regula su confección.",
  "Tres partes: **cuerpo** (N1), **resúmenes** (RN, RRD, RRX, REN) y **estados justificativos** (VR y VD); ordinaria **01**, las demás desde la **02**.",
  "Cierre de la ordinaria: **día 5**; redondeo a la unidad; liquidación por días: **un treintavo** (Orden, aps. 6 a 8).",
  "Gasto: **AD** al inicio del ejercicio; cada mes **OK** (o ADOK) **antes del día 7**; pago al menos **5 días** antes del vencimiento."],
  "Siguiente: III. ¿Cómo se justifican las altas, las bajas y las modificaciones?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se justifican las altas, las bajas y las modificaciones? (Orden de 1992, aps. 2 a 4)", donde(
  "Tercera frase del epígrafe. La nómina de cada mes se compara con la del **mes anterior**: quien entra es un **alta**, quien sale es una **baja** y quien cobra distinto tiene una **modificación**. Cada variación se **justifica** con un documento.",
  ["1 Altas (ap. 2)", "2 Bajas (ap. 3)", "3 Modificaciones (ap. 4)", "4 Cuadro de altas, bajas y modificaciones"]))

T.ap("s6", "III.1 Altas en nómina (Orden de 1992, ap. 2)", f"""
{unidad("1.1 Concepto y funcionarios (ap. 2, párrafo inicial y 2.1 a 2.9)",
  orden("A2", "Altas en nómina", ["la inclusión en la nómina de un perceptor que no figuraba en la del mes anterior", "Copia del título administrativo.", "Formalización de la toma de posesión en el puesto de trabajo, según modelo F.2R.", "Certificado de baja en nómina, conforme al anexo III.a)."], solo=list(range(1, 27))),
  fichab("Alta: inclusión de un perceptor que no figuraba en la nómina del mes anterior",
         "El habilitado la incluye; los documentos los expiden los órganos de personal",
         ["Nuevo ingreso: título administrativo, nombramiento (F.1 o BOE) y toma de posesión (F.2R)", "Con servicios previos en otros Cuerpos: además, **liquidación de trienios** (anexo II), sobre certificaciones de servicios (anexo I)", "Reingreso: nombramiento (o F.6R si había reserva de plaza), toma de posesión y liquidación de trienios", "Comisión de servicios y traslado: nombramiento y toma de posesión (o F.5R) y **certificado de baja en nómina** (anexo III.a)", "Prácticas, empleo eventual e interinos: nombramiento y toma de posesión (o certificación del inicio de las prácticas)"],
         "—",
         "El **certificado de baja en nómina** acompaña al alta del que **viene de otra nómina** (comisión, traslado)."))}

{unidad("1.2 Personal laboral (ap. 2.10 a 2.13)",
  orden("A2", "", ["Copia del plan, propuesta o expediente de contratación sobre el que fue ejercida la fiscalización del gasto."], solo=list(range(27, 40))),
  fichab("Altas de contratados laborales",
         "—",
         ["Nuevo ingreso: hoja de servicios, contrato laboral y copia del expediente de contratación fiscalizado", "Reingreso: L.2R y certificación de antigüedad", "Traslado: L.3R o L.2R y certificado de baja en nómina (anexo III.b)", "Reincorporación tras licencia con baja en nómina: L.14R y certificación de la fecha"],
         "—",
         "Los modelos del personal laboral empiezan por **L**; los de funcionarios, por **F**."))}
""", 2)

T.ap("s7", "III.2 Bajas en nómina (Orden de 1992, ap. 3)", f"""
{unidad("2.1 Concepto y supuestos (ap. 3)",
  orden("A3", "Bajas en nómina", ["la exclusión de la nómina de un perceptor que figuraba en la del mes anterior", "Acuerdo de jubilación, según modelo F.15R.", "En los casos de fallecimiento, renuncia y pérdida de la nacionalidad española, se unirán los modelos F.3 y F.4R."]),
  fichab("Baja: exclusión de un perceptor que figuraba en la nómina del mes anterior",
         "—",
         ["Cambio de puesto: cese (F.3) y su formalización (F.4R), o F.5R; en comisión de servicios, F.7", "Cambio de situación administrativa: F.6R y F.4R (suspensión de funciones: F.14R y F.4R)", "Jubilación: F.15R y F.4R", "Pérdida de la condición de funcionario: F.3 y F.4R (fallecimiento, renuncia, pérdida de la nacionalidad); separación del servicio: F.12R y F.4R", "Licencia: F.17R", "Laborales: L.1R (y L.12R jubilación, L.11R suspensión, L.9R sanción, L.14R licencia)"],
         "—",
         "El **F.4R** (formalización del cese) aparece en casi todas las bajas de funcionarios."))}
""", 2)

T.ap("s8", "III.3 Modificaciones en nómina (Orden de 1992, ap. 4)", f"""
{unidad("3.1 Concepto y clases (ap. 4, párrafos iniciales)",
  orden("A4", "Modificaciones en nómina", ["los aumentos o disminuciones en las retribuciones y deducciones", "Modificaciones definitivas son las que producen cambios que van a persistir en nóminas futuras.", "Modificaciones transitorias son las que producen cambios que no van a persistir en nóminas futuras."], solo=[1, 2, 3, 4, 5]),
  fichab("Modificación: aumento o disminución respecto del mes anterior",
         "—",
         ["**Definitivas**: persisten en nóminas futuras", "**Transitorias**: no persisten"],
         "—",
         "Se comparan retribuciones **y deducciones** con las del **mes anterior**."))}

{unidad("3.2 Aumentos (ap. 4.1)",
  orden("A4", "", ["Reconocimiento de trienios por cómputo ordinario", "Complemento de productividad: Se acompañará certificación expedida por la autoridad competente.", "Certificación del habilitado por la que se acredite que no han sido incluidos en nóminas anteriores."], solo=list(range(6, 42))),
  fichab("Aumentos definitivos y transitorios",
         "—",
         ["Definitivos: reincorporación tras licencia o a la jornada normal, trienios (F.8R o L.5R), grado (F.16R o F.20R), cambio de nivel o específico del puesto, cambio de puesto, Ley de Presupuestos o convenio", "Transitorios: productividad y gratificaciones (certificación de la autoridad competente), pagas extraordinarias (certificación global del habilitado), atrasos"],
         "—",
         "**Atrasos** en una nómina posterior a la del alta: documentación del alta + **certificación del habilitado** de que no se incluyeron antes."))}

{unidad("3.3 Disminuciones y otras modificaciones (ap. 4.2 a 4.5)",
  orden("A4", "", ["Por el ejercicio del derecho de huelga: Se acompañará certificación expedida por el órgano competente", "Por reducción de jornada de trabajo"], solo=list(range(42, 59))),
  fichab("Disminuciones y modificaciones en las deducciones",
         "—",
         ["Definitivas: excedencia forzosa, suspensión provisional, licencias parcialmente retribuidas, reducción de jornada", "Transitorias: **huelga** (certificación del órgano competente con el personal y el tiempo) y licencias no retribuidas o parcialmente retribuidas", "No previstas: el documento del acto o hecho o la norma que la disponga", "Deducciones: justificadas por la variación del íntegro, por la norma (generales) o por el documento (personales)"],
         "—",
         "La **huelga** es una disminución **transitoria** (la deducción, sin carácter de sanción: → V.1.1)."))}
""", 2)

T.ap("s9", "III.4 Cuadro de altas, bajas y modificaciones (esquema)", f"""
*Esquema de elaboración propia: resume los apartados 2 a 5 de la Orden de 30-7-1992; no es texto legal.*

| Variación | Qué es (respecto del mes anterior) | Estado justificativo | Ejemplos de justificante |
|---|---|---|---|
| **Alta** | Perceptor que **no figuraba** | VR1 / VD1 | Título, nombramiento (F.1), toma de posesión (F.2R), certificado de baja en nómina |
| **Baja** | Perceptor que **figuraba** y sale | VR2 / VD2 | Cese (F.3, F.4R), jubilación (F.15R), cambio de situación (F.6R) |
| **Modificación definitiva** | Cambio que **persiste** | VR3 / VD3 (MD-A, MD-D) | Trienio (F.8R), grado (F.16R), cambio de puesto |
| **Modificación transitoria** | Cambio que **no persiste** | VR3 / VD3 (MT-A, MT-D) | Productividad, gratificaciones, pagas extraordinarias, huelga |

{resumen([
  "**Alta**: entra quien no figuraba el mes anterior; **baja**: sale quien figuraba; **modificación**: cambia lo que cobra o lo que se le descuenta (aps. 2 a 4).",
  "Cada variación se **justifica** con su documento (modelos F para funcionarios, L para laborales) y se relaciona en los estados VR y VD.",
  "Modificaciones **definitivas** (persisten) y **transitorias** (no persisten)."],
  "Siguiente: IV. ¿Qué se descuenta en la nómina y se ingresa en formalización?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué se descuenta en la nómina y se ingresa en formalización?", donde(
  "Cuarta frase del epígrafe. De lo que se paga al funcionario se **retienen** cantidades (IRPF, derechos pasivos, mutualidades…). Las que se ingresan **en formalización** en el Tesoro Público son las **deducciones formalizables**.",
  ["1 Deducciones formalizables y no formalizables; íntegro, líquido y neto (Orden, ap. 5.1.5 a 5.1.8)", "2 Lo que se retiene en la nómina: cuotas y anticipos (Resolución de 2010, aps. A.3 y A.4.4 y anexo XIV; reglas 70 y 93)", "3 Pendiente (temario)"]))

T.ap("s10", "IV.1 Deducciones formalizables y no formalizables; íntegro, líquido y neto (Orden de 1992, ap. 5.1.5 a 5.1.8)", f"""
{unidad("1.1 Deducciones formalizables y no formalizables (ap. 5.1.5 y 5.1.6)",
  orden("A5", "", ["Son las deducciones cuyo ingreso se realiza en formalización en el Tesoro Público."], solo=list(range(66, 73))),
  fichab("Qué es una deducción formalizable",
         "—",
         [f"Formalizable: {c('ONOM1992', 'A5', 'deducciones cuyo ingreso se realiza en formalización en el Tesoro Público')}", "No formalizable: el resto; se cumplimenta igual (código, concepto, base, porcentaje, importe)"],
         "—",
         "El **ingreso en formalización** es el de las deducciones **formalizables**, y se hace en el **Tesoro Público**."))}

{unidad("1.2 Códigos de las deducciones (ap. 5.1.7)",
  orden("A5", "", ["01: IRPF.", "02: Derechos pasivos.", "03: MUFACE.", "09: Cuota obrera del RGSS.", "20: Anticipo reintegrable."], solo=list(range(73, 85))),
  fichab("Las deducciones de la nómina y sus códigos",
         "—",
         ["01 IRPF · 02 derechos pasivos · 03 MUFACE · 04 ISFAS · 05 MUNPAL · 06 MUGEJU · 09 cuota obrera del RGSS", "20 anticipo reintegrable · 21 retención judicial · 22 reintegro de préstamo de MUFACE"],
         "Códigos libres para otras deducciones: **23 a 98**",
         "No confundas los códigos de **deducciones** (01 IRPF) con las claves de **retribuciones** (01 sueldo) (→ II.2.3)."))}

{unidad("1.3 Importe íntegro, líquido y neto (ap. 5.1.8)",
  orden("A5", "", ["restar al importe íntegro la suma de los importes de todas las deducciones formalizables", "restar al importe líquido la suma de los importes de todas las deducciones no formalizables"], solo=[85, 86, 87, 88]),
  fichab("Los tres importes de cada perceptor",
         "—",
         ["**Íntegro** = suma de todas las retribuciones", "**Líquido** = íntegro − deducciones **formalizables**", "**Neto** = líquido − deducciones **no formalizables**"],
         "—",
         "Íntegro → (−formalizables) → líquido → (−no formalizables) → neto. Al pagar la nómina en las Delegaciones se anticipa el importe **líquido** (→ II.4.2)."))}
""", 2)

T.ap("s11", "IV.2 Lo que se retiene en la nómina: cuotas y anticipos (Resolución de 2010, aps. A.3 y A.4.4 y anexo XIV; reglas 70 y 93)", f"""
{unidad("2.1 Cuotas de mutualidades y de derechos pasivos (Resolución de 2010, ap. A.3.1 a 3.4)",
  res([56, 58, 62, 63, 64], "apartado A.3", ["que los habilitados de personal deben retener en nómina cada mes", "cualquiera que sea su antigüedad en el servicio del Estado, la cuota supone una cantidad única e idéntica", "no experimentarán reducción en su cuantía"]),
  fichab("Cuotas que el habilitado retiene a los funcionarios",
         "Los **habilitados** de personal retienen; mutualistas de MUFACE, ISFAS y MUGEJU",
         ["Mutualidades: un porcentaje sobre el **haber regulador** a efectos de derechos pasivos", "Derechos pasivos: un porcentaje de los **haberes reguladores**, igual para todo el Cuerpo, Escala, Empleo o Categoría, cualquiera que sea la antigüedad", "En pagas extraordinarias reducidas por servicios parciales: las cuotas se reducen en la misma proporción"],
         "Porcentajes de 2010: 1,69 % (mutualidades) y 3,86 % (derechos pasivos), según la Resolución citada",
         "La cuota de derechos pasivos **no depende de la antigüedad**. En las **licencias sin retribución** las cuotas **no** se reducen."))}

{unidad("2.2 Cuota doble en junio y diciembre (Resolución de 2010, anexo XIV)",
  lit("RES2010N", "anexoXIV", ["cuota doble"], titulo="Resolución de 25-5-2010, anexo XIV (texto del PDF oficial del BOE)"),
  fichab("Cuotas de derechos pasivos en los meses de paga extraordinaria",
         "Todos los funcionarios",
         "Cuota doble en junio y diciembre",
         "—",
         "Salvo las pagas reducidas por servicios parciales del ap. 3.3 (→ IV.2.1). El anexo XIII (cuotas a MUFACE, ISFAS y MUGEJU, texto del PDF oficial del BOE) repite la misma frase: también la cuota de mutualidades es **doble** en junio y diciembre."))}

{unidad("2.3 Cuotas obreras de la Seguridad Social (regla 70.4)",
  lit("OIOC", "regla70", ["junto con las retenciones de las cuotas obreras"], solo=[5, 6]),
  fichab("Pago de las cuotas sociales y de las cuotas obreras retenidas",
         "Las **Habilitaciones o Pagadurías de Personal** pagan a la **Tesorería General de la Seguridad Social**",
         "OK (o ADOK) a favor de la Habilitación, que paga la aportación de la Administración **junto con** las cuotas obreras retenidas",
         "Los plazos del sistema de liquidación directa de cuotas",
         "El documento contable de las cuotas sociales se expide a favor de la **Habilitación**, no de la Tesorería General."))}

{unidad("2.4 Concesión y reintegro de anticipos: descuento en nómina (regla 93.1 y 3; Resolución de 2010, ap. A.4.4)",
  lit("OIOC", "regla93", ["se efectuará el oportuno descuento en la nómina de personal en activo"], solo=[1, 3]),
  res([69], "apartado A.4.4", ["a las retribuciones básicas líquidas"]),
  fichab("Anticipos reintegrables a funcionarios",
         "El centro gestor concede; la nómina descuenta",
         "Reintegro mediante **descuento en la nómina** del mes en que toque devolver (código de deducción 20: → IV.1.2)",
         f"Límite de cálculo: los haberes líquidos se entienden referidos {c('RES2010N', R, 'a las retribuciones básicas líquidas')}",
         "Los «haberes líquidos» para el anticipo = **retribuciones básicas líquidas** (no todas las retribuciones)."))}
""", 2)

T.ap("s12", "IV.3 Pendiente (temario)", f"""
Lo que sigue lo pide el epígrafe («Ingresos en formalización») pero **no está en las normas citadas** de forma completa ni se ha encontrado otra norma o fuente oficial que lo desarrolle. Se completará con el temario del usuario:

- **Procedimiento contable del ingreso en formalización** de las deducciones de la nómina (cómo se aplican al presupuesto de ingresos o a conceptos no presupuestarios y qué documentos se usan). En el BOE consolidado solo consta lo citado: las deducciones formalizables se ingresan {c('ONOM1992', 'A5', 'en formalización en el Tesoro Público')} (→ IV.1.1) y el pago en formalización de la regla 69.5 (→ II.4.2).

{resumen([
  "Deducción **formalizable**: su ingreso se hace **en formalización en el Tesoro Público**; el resto, no formalizables (ap. 5.1.5 y 5.1.6).",
  "**Íntegro − formalizables = líquido; líquido − no formalizables = neto** (ap. 5.1.8). Códigos: 01 IRPF, 02 derechos pasivos, 03 MUFACE… (ap. 5.1.7).",
  "El habilitado retiene **mutualidades** y **derechos pasivos** (cuota igual sea cual sea la antigüedad; **doble** en junio y diciembre) y las **cuotas obreras** de la Seguridad Social; los anticipos se reintegran **descontándolos en nómina**."],
  "Siguiente: V. ¿Cómo se devengan y se liquidan los derechos económicos?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se devengan y se liquidan los derechos económicos? (TREBEP, art. 30; Resolución de 25-5-2010)", donde(
  "Quinta frase del epígrafe: **cuánto** corresponde cobrar cada mes. Regla general: mensualidades **completas** referidas al **primer día hábil** del mes; excepciones que se **liquidan por días**; reglas propias de las **pagas extraordinarias** y de las **deducciones**.",
  ["1 Deducción proporcional y valor hora (TREBEP, art. 30; Resolución, ap. A.2.1 y 2.2)", "2 Mensualidades completas y liquidación por días (ap. A.2.3)", "3 Pagas extraordinarias (ap. A.2.4 y 2.6)", "4 Cambio de puesto y supresión del puesto (aps. A.2.7 y A.4.3)", "5 Indemnización por residencia (ap. C.1 y anexo XV)", "6 Cuadro del devengo"]))

T.ap("s13", "V.1 Deducción proporcional y valor hora (TREBEP, art. 30; Resolución de 2010, ap. A.2.1 y 2.2)", f"""
{unidad("1.1 Deducción de retribuciones (TREBEP, art. 30)",
  lit("TREBEP", "Artículo 30", ["dará lugar a la deducción proporcional de haberes, que no tendrá carácter sancionador", "no devengarán ni percibirán las retribuciones correspondientes al tiempo en que hayan permanecido en esa situación"]),
  fichab("Deducción por jornada no realizada y por huelga",
         "Personal incluido en el ámbito del TREBEP",
         ["Jornada no realizada → deducción **proporcional** de haberes", "Huelga → no se devengan ni perciben las retribuciones de ese tiempo"],
         "—",
         "La deducción **no es sanción** (pero no excluye la sanción disciplinaria) y, en huelga, **no afecta** a las prestaciones sociales. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Valor hora y liquidaciones por días (Resolución de 2010, ap. A.2.1)",
  res([26, 27, 28], "apartado A.2.1", ["salvo justificación, a la correspondiente deducción proporcional de haberes", "dividida entre el número de días naturales del correspondiente mes", "en el de licencias sin derecho a retribución"]),
  fichab("Cómo se calcula la deducción y cualquier liquidación por días",
         "El habilitado, al confeccionar la nómina",
         ["Diferencia mensual entre jornada **reglamentaria** y **efectivamente realizada** → deducción proporcional, salvo justificación", "Valor hora = retribuciones íntegras mensuales ÷ **días naturales** del mes ÷ horas diarias de obligado cumplimiento (de media)", "El mismo cálculo se aplica a la toma de posesión del primer destino, el cese en el servicio activo, las licencias sin retribución y toda liquidación por días"],
         "Cómputo **mensual**",
         "**Días naturales** (no hábiles) y la **totalidad** de las retribuciones **íntegras** mensuales; la consecuencia es una **deducción** de haberes (no un complemento). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.3 Jornada reducida (Resolución de 2010, ap. A.2.2)",
  res([29, 30, 31, 32, 33, 34, 35], "apartado A.2.2", ["sobre la totalidad de sus retribuciones, tanto básicas como complementarias, con inclusión de los trienios", "entre 182 (183 en años bisiestos) ó 183 días"]),
  fichab("Retribuciones con jornada inferior a la normal",
         "Funcionarios con jornada reducida",
         ["Reducción sobre la **totalidad** de las retribuciones, básicas y complementarias, **incluidos los trienios**", "Paga extraordinaria afectada: suma de los periodos con y sin reducción de los seis meses computables"],
         "Paga ÷ **182** (183 en bisiesto) o **183** días, según sea la de junio o la de diciembre, × días de cada periodo",
         "La reducción alcanza también a los **trienios**."))}
""", 2)

T.ap("s14", "V.2 Mensualidades completas y liquidación por días (Resolución de 2010, ap. A.2.3)", f"""
{unidad("2.1 La regla general y sus excepciones (ap. A.2.3)",
  res([36, 37, 38, 39, 40], "apartado A.2.3", ["por mensualidades completas y con referencia a la situación y derechos del funcionario referidos al primer día hábil del mes", "En el mes de iniciación de licencias sin derecho a retribución.", "salvo que sea por motivos de fallecimiento, jubilación o retiro"]),
  fichab("Devengo de las retribuciones fijas y de periodicidad mensual",
         "Funcionarios (régimen de la Ley 30/1984)",
         ["**Regla**: mensualidades completas, según la situación y derechos del **primer día hábil** del mes", "**Por días**: mes de toma de posesión del primer destino, de reingreso y de incorporación tras licencia sin retribución", "**Por días**: mes de **iniciación** de licencias sin retribución", "**Por días**: mes de cambio a una Administración distinta de la del Estado", "**Por días**: mes de cese en el servicio activo (incluido el cambio de Cuerpo o Escala)"],
         "—",
         "El cese por **fallecimiento, jubilación o retiro** (de Clases Pasivas o regímenes que pagan desde el mes siguiente) **no** se liquida por días: mes completo. Cálculo de los días: → V.1.2 (la Orden de 1992 usa un treintavo: → II.3.3)."))}

{unidad("2.2 El complemento específico en catorce pagas (ap. A.2.3, párrafos finales)",
  res([41, 42], "apartado A.2.3, párrafos finales", ["sin modificación de su devengo, que seguirá siendo en doce"]),
  fichab("Devengo del complemento específico",
         "—",
         "Se percibe en catorce mensualidades, pero se **devenga en doce**; en cambio o cese del puesto se liquida la parte de la **paga adicional** de junio o diciembre",
         "Según el semestre en que se produzca el cambio",
         "Percepción (14) y devengo (12) del específico **no coinciden**."))}
""", 2)

T.ap("s15", "V.3 Pagas extraordinarias (Resolución de 2010, ap. A.2.4 y 2.6)", f"""
{unidad("3.1 Trienios en cualquier situación (ap. A.2.4)",
  res([43], "apartado A.2.4", ["la parte proporcional que, por dicho concepto, corresponda a las pagas extraordinarias"]),
  fichab("Parte de las pagas extraordinarias por trienios",
         "Funcionarios en cualquier situación con derecho a percibir trienios",
         "Perciben además la parte proporcional de trienios de las pagas extraordinarias", "—",
         "Vale para **cualquier situación administrativa** con derecho a trienios."))}

{unidad("3.2 Devengo de las pagas extraordinarias (ap. A.2.6)",
  res([45, 46, 47, 48, 49, 50, 51], "apartado A.2.6", ["se devengarán el primer día hábil de los meses de junio y diciembre", "se reducirá proporcionalmente", "la última paga extraordinaria se devengará el día de cese", "no tendrá la consideración de servicios efectivamente prestados"]),
  fichab("Cuándo y cuánto se devenga cada paga extraordinaria",
         "Funcionarios del Estado",
         ["**Regla**: primer día hábil de **junio y diciembre**, según la situación y derechos de esa fecha", "Menos de seis meses de servicios: reducción proporcional (paga ÷ 182 o 183 días × días de servicio)", "Licencia sin retribución en esa fecha: se devenga, pero reducida", "Cese: la última paga se devenga **el día del cese**, proporcional; en jubilación, fallecimiento o retiro, el mes del cese cuenta **completo**"],
         "Seis meses inmediatos anteriores; divisor **182** (183 en bisiesto) para junio y **183** para diciembre",
         "Las licencias sin retribución **no** son servicios efectivamente prestados. Junio y diciembre (no julio)."))}
""", 2)

T.ap("s16", "V.4 Cambio de puesto y supresión del puesto (Resolución de 2010, aps. A.2.7 y A.4.3)", f"""
{unidad("4.1 Plazo posesorio y acceso a un nuevo Cuerpo (ap. A.2.7)",
  res([52, 53, 54], "apartado A.2.7", ["durante el plazo posesorio, a la totalidad de las retribuciones", "un permiso retribuido de tres días hábiles", "de un mes si lo comporta"]),
  fichab("Retribuciones durante el plazo posesorio",
         "Funcionarios de carrera que cambian de puesto (y los que acceden a un nuevo Cuerpo o Escala)",
         ["Plazo posesorio: totalidad de las retribuciones básicas y complementarias fijas y de periodicidad mensual", "Si el plazo acaba en el mes del cese: paga la Dependencia que diligencia el cese", "Si acaba en otro mes: el segundo mes lo paga la Dependencia del nuevo puesto"],
         "Nuevo Cuerpo o Escala: permiso retribuido de **tres días hábiles** (sin cambio de residencia) o de **un mes** (con cambio)",
         "Tres días **hábiles** / un mes."))}

{unidad("4.2 Supresión del puesto (ap. A.4.3)",
  res([68], "apartado A.4.3", ["durante un plazo máximo de tres meses", "sin que proceda reintegro alguno"]),
  fichab("Retribuciones del titular de un puesto suprimido",
         "Titulares de puestos suprimidos en las relaciones o catálogos",
         "Siguen cobrando las complementarias del puesto suprimido **a cuenta** de las del nuevo",
         "Hasta su nuevo nombramiento y como máximo **tres meses** desde los efectos económicos de la supresión",
         "Si lo cobrado supera lo del nuevo puesto, **no** se reintegra."))}
""", 2)

T.ap("s17", "V.5 Indemnización por residencia (Resolución de 2010, ap. C.1 y anexo XV)", f"""
{unidad("5.1 Devengo y mensualidades (ap. C.1 y anexo XV)",
  res([98], "apartado C.1", ["continuará devengándose en las áreas del territorio nacional que la tienen reconocida"]),
  lit("RES2010N", "anexoXV", ["doce mensualidades, sin repercusión en pagas extraordinarias", "disminuida en la misma proporción"], solo=[4, 5], titulo="Resolución de 25-5-2010, anexo XV (texto del PDF oficial del BOE)"),
  fichab("Indemnización por residencia en territorio nacional",
         "Personal en activo del sector público estatal con derecho a ella, en las áreas que la tienen reconocida (el anexo XV recoge Ceuta y Melilla, Canarias, Illes Balears y Valle de Arán)",
         ["**Doce** mensualidades", "**Sin** repercusión en pagas extraordinarias", "Sueldo inferior al general → indemnización disminuida en la misma proporción"],
         "—",
         "**Doce**, no catorce; **sin** repercusión en las pagas extraordinarias. En la nómina es la clave **09** (→ II.2.3). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s18", "V.6 Cuadro del devengo (esquema)", f"""
*Esquema de elaboración propia: resume el apartado A.2 de la Resolución de 25-5-2010, el apartado 8 de la Orden de 30-7-1992 y el art. 30 del TREBEP; no es texto legal.*

| Situación | Cómo se liquida | Fuente |
|---|---|---|
| Mes normal | Mensualidad **completa**, según el **primer día hábil** | Res. A.2.3 |
| Toma de posesión del primer destino, reingreso, vuelta de licencia sin retribución | **Por días** | Res. A.2.3 a) |
| Inicio de licencia sin retribución | **Por días** | Res. A.2.3 b) |
| Cese en el servicio activo | **Por días**, salvo fallecimiento, jubilación o retiro (mes completo) | Res. A.2.3 d) |
| Jornada no realizada | **Deducción proporcional**; valor hora sobre **días naturales** | TREBEP 30; Res. A.2.1 |
| Paga extraordinaria | Primer día hábil de **junio y diciembre**; proporcional si hay menos de seis meses | Res. A.2.6 |
| Indemnización por residencia | **Doce** mensualidades, sin repercusión en pagas | Res. anexo XV |
| Importe diario en la Orden de 1992 | **Un treintavo** del importe mensual | Orden, ap. 8 |

{resumen([
  "Regla: **mensualidad completa** según el **primer día hábil** del mes; excepciones **por días** (primer destino, reingreso, licencias sin retribución, cambio de Administración, cese).",
  "Deducción **proporcional** sin carácter sancionador (TREBEP 30); valor hora = íntegras mensuales ÷ **días naturales** ÷ horas diarias.",
  "Pagas extraordinarias: **primer día hábil de junio y diciembre**; proporcionales (÷ 182/183 días) si no hay seis meses de servicios.",
  "Indemnización por residencia: **doce** mensualidades, **sin** repercusión en pagas extraordinarias."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L100 = examen("L", 100, {
  "a": f"Cambia el día: la Orden de 30-7-1992 dice que se cerrarán {c('ONOM1992', 'A6', 'el día 5 de dicho mes')}, no el 28.",
  "b": f"Cambia el día: {c('ONOM1992', 'A6', 'Las nóminas ordinarias de cada mes se cerrarán el día 5 de dicho mes')}; el día 1 no aparece.",
  "c": f"Literal del apartado 6 de la Orden de 30-7-1992: {c('ONOM1992', 'A6', 'Las nóminas ordinarias de cada mes se cerrarán el día 5 de dicho mes')}.",
  "d": f"Inventa una regla de fin de mes con excepción de febrero; la Orden fija un único día: {c('ONOM1992', 'A6', 'el día 5 de dicho mes')}."},
  [("día 5", "ONOM1992", "A6", "Las nóminas ordinarias de cada mes se cerrarán el día 5 de dicho mes")])
EX_P105 = examen("P", 105, {
  "a": f"Literal del ap. A.2.3 b): se liquidan por días, entre otros, {c('RES2010N', R, 'En el mes de iniciación de licencias sin derecho a retribución.')}; la regla afecta a {c('RES2010N', R, 'Las retribuciones básicas y complementarias que se devenguen con carácter fijo y periodicidad mensual')}.",
  "b": f"Cambia el mes: las pagas extraordinarias {c('RES2010N', R, 'se devengarán el primer día hábil de los meses de junio y diciembre')} (ap. A.2.6), no en julio.",
  "c": f"Cambia una palabra: el divisor son los días **naturales**, no hábiles: {c('RES2010N', R, 'dividida entre el número de días naturales del correspondiente mes')} (ap. A.2.1).",
  "d": f"Cambia la consecuencia: la diferencia de jornada da lugar {c('RES2010N', R, 'salvo justificación, a la correspondiente deducción proporcional de haberes')} (ap. A.2.1), no a un complemento de productividad."},
  [("mes de iniciación de licencias sin derecho a retribución", "RES2010N", R, "En el mes de iniciación de licencias sin derecho a retribución."),
   ("se liquidarán por días", "RES2010N", R, "salvo en los siguientes casos, en que se liquidarán por días")])
EX_X100 = examen("X", 100, {
  "a": f"Cambia dos datos: son doce mensualidades y {c('RES2010N', 'anexoXV', 'sin repercusión en pagas extraordinarias')}.",
  "b": f"Cambia el número: {c('RES2010N', 'anexoXV', 'La indemnización por residencia comprende doce mensualidades')}; el anexo no descuenta ningún mes por permisos, licencias o vacaciones.",
  "c": f"Literal del anexo XV: {c('RES2010N', 'anexoXV', 'La indemnización por residencia comprende doce mensualidades, sin repercusión en pagas extraordinarias')}.",
  "d": f"Cambia el número: son **doce** mensualidades, no catorce prorrateadas: {c('RES2010N', 'anexoXV', 'comprende doce mensualidades')}."},
  [("doce mensualidades", "RES2010N", "anexoXV", "La indemnización por residencia comprende doce mensualidades"),
   ("sin repercusión en pagas extraordinarias", "RES2010N", "anexoXV", "sin repercusión en pagas extraordinarias")])
EX_P99 = examen("P", 99, {
  "a": f"El complemento de destino **no** es retribución básica: las básicas están integradas {c('TREBEP', 'Artículo 23', 'única y exclusivamente por')} sueldo y trienios.",
  "b": "Añade el complemento de destino, que es complementario; la fórmula «única y exclusivamente» excluye cualquier otro concepto.",
  "c": f"Literal del art. 23: {c('TREBEP', 'Artículo 23', 'El sueldo asignado a cada Subgrupo o Grupo')} y {c('TREBEP', 'Artículo 23', 'Los trienios, que consisten en una cantidad')}.",
  "d": f"Destino y específico son complementarios: retribuyen {c('TREBEP', 'Artículo 22', 'las características de los puestos de trabajo')} (art. 22.3)."},
  [("sueldo", "TREBEP", "Artículo 23", "El sueldo asignado a cada Subgrupo o Grupo de clasificación profesional"),
   ("trienios", "TREBEP", "Artículo 23", "Los trienios, que consisten en una cantidad"),
   ("El sueldo y los trienios", "TREBEP", "Artículo 23", "estarán integradas única y exclusivamente por")])
EX_X99 = examen("X", 99, {
  "a": f"Literal del art. 30.1: {c('TREBEP', 'Artículo 30', 'dará lugar a la deducción proporcional de haberes, que no tendrá carácter sancionador')}.",
  "b": f"Sí hay deducción: {c('TREBEP', 'Artículo 30', 'la parte de jornada no realizada dará lugar a la deducción proporcional de haberes')}, sin perjuicio de la sanción disciplinaria.",
  "c": f"Cambia una palabra: la deducción {c('TREBEP', 'Artículo 30', 'no tendrá carácter sancionador')}.",
  "d": f"El art. 30 del TREBEP no prohíbe la deducción, la regula: {c('TREBEP', 'Artículo 30', 'la parte de jornada no realizada dará lugar a la deducción proporcional de haberes')}. La norma de la Unión que cita la opción no aparece en él."},
  [("que no tendrá carácter sancionador", "TREBEP", "Artículo 30", "que no tendrá carácter sancionador")])

T.ap("s19", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema (cierre de la nómina, devengo y liquidación por días, indemnización por residencia) y **dos** relacionadas del tema V.6 (retribuciones básicas y deducción de haberes). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 100 · Cierre de las nóminas ordinarias (→ II.3.1)", EX_L100,
  "### GACE-P 2025, pregunta 105 (reserva) · Devengo y liquidación por días (→ V.2.1)", EX_P105,
  "### GACE-L 2025 extraordinario, pregunta 100 · Indemnización por residencia (→ V.5.1)", EX_X100,
  "### GACE-P 2025, pregunta 99 · Retribuciones básicas (relacionada, tema V.6; → I.1.2)", EX_P99,
  "### GACE-L 2025 extraordinario, pregunta 99 · Deducción de retribuciones (relacionada, tema V.6; → V.1.1)", EX_X99,
  "### Cómo se pregunta",
  "!> Las preguntas de nóminas citan la **norma exacta** (Orden de 1992 o Resolución de 25 de mayo de 2010) y cambian **un dato**: un día (5), un mes (junio y no julio), una palabra (días **naturales**, no hábiles), un número (**doce** mensualidades) o la consecuencia (**deducción** de haberes, no complemento).",
]))

T.ap("s20", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Retribuciones | Básicas (sueldo y trienios) y complementarias; dos pagas extraordinarias | Básicas «**única y exclusivamente**» sueldo y trienios |
| II. Nómina | Cuerpo N1, resúmenes y estados justificativos; ordinaria 01; regla 69 | Cierre el **día 5**; OK antes del **día 7**; pago **5 días** antes |
| III. Altas y bajas | Alta: no figuraba el mes anterior; baja: figuraba; modificaciones definitivas y transitorias | Certificado de **baja en nómina** para el alta por traslado o comisión |
| IV. Formalización | Formalizables: ingreso **en formalización en el Tesoro**; íntegro, líquido, neto | **Líquido** = íntegro − formalizables |
| V. Devengo | Mes completo (primer día hábil) o por días; deducción proporcional; pagas; residencia | Días **naturales**; **junio y diciembre**; **doce** mensualidades |

?> **Trampas frecuentes:** «las nóminas se cierran el día **1** / **28** / **30**» (el **día 5**); «valor hora sobre días **hábiles**» (días **naturales**); «pagas extraordinarias en **julio** y diciembre» (**junio** y diciembre); «la diferencia de jornada da lugar a un **complemento**» (a una **deducción** proporcional); «la indemnización por residencia comprende **catorce** mensualidades» (**doce**, sin repercusión en pagas); «la deducción **tiene** carácter sancionador» (no lo tiene); «el neto es el íntegro menos las deducciones formalizables» (eso es el **líquido**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
q = T.q
q("ONOM1992", "A6", "Confección de nóminas", "Según la Orden de 30 de julio de 1992, las nóminas ordinarias de cada mes se cerrarán:",
  ["El día 5 de dicho mes.", "El día 7 de dicho mes.", "El último día hábil del mes anterior.", "El día 1 del mes siguiente."],
  "Ap. 6 de la Orden: «se cerrarán el día 5 de dicho mes».", "se cerrarán el día 5 de dicho mes")
q("ONOM1992", "A8", "Confección de nóminas", "Según el apartado 8 de la Orden de 30 de julio de 1992, cuando los derechos económicos se deban liquidar por días efectivos, el importe diario equivale a:",
  ["Un treintavo del importe mensual del concepto retributivo correspondiente.", "Un trescientos sesenta y cincoavo del importe anual.", "La parte proporcional según los días hábiles del mes.", "Un treintaiunavo del importe mensual en los meses de treinta y un días."],
  "Ap. 8 de la Orden.", "el importe diario equivalente a un treintavo del importe mensual del concepto retributivo correspondiente")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, el orden en el que han de figurar los perceptores en las nóminas será:",
  ["El alfabético de apellidos y nombre.", "El de número de Registro de personal.", "El de antigüedad en el Cuerpo o Escala.", "El del grupo de clasificación, de mayor a menor."],
  "Ap. 5.1.1 de la Orden.", "será el alfabético de apellidos y nombre")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, el «Período de liquidación» de la cabecera de la nómina se cumplimentará:",
  ["Con la fecha del inicio y finalización del mes de devengo.", "Con la fecha de cierre de la nómina.", "Con la fecha de pago de la nómina.", "Con el numeral del año del presupuesto correspondiente."],
  "Ap. 5.1.2 de la Orden.", "Período de liquidación: Con la fecha del inicio y finalización del mes de devengo")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, la aplicación presupuestaria de cada retribución se consigna mediante:",
  ["17 dígitos.", "12 dígitos.", "9 dígitos.", "21 dígitos."],
  "Ap. 5.1.4 de la Orden: «mediante 17 dígitos».", "mediante 17 dígitos")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, ¿qué clave tiene asignada en la nómina la retribución «Complemento específico»?",
  ["05.", "04.", "06.", "09."],
  "Ap. 5.1.4: 04 complemento de destino, 05 complemento específico, 06 productividad, 09 indemnización por residencia.", "05: Complemento específico.")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, la clave 09 de las retribuciones corresponde a:",
  ["Indemnización por residencia.", "Gratificación por servicios extraordinarios.", "Complemento personal transitorio.", "Horas extraordinarias."],
  "Ap. 5.1.4 de la Orden.", "09: Indemnización por residencia.")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, para las retribuciones de personal funcionario no contempladas en la tabla de claves se utilizarán las claves no reservadas:",
  ["De la 14 a la 29.", "De la 31 a la 59.", "De la 23 a la 98.", "De la 60 a la 79."],
  "Ap. 5.1.4 de la Orden: de la 14 a la 29 (funcionarios); de la 31 a 59 (laborales).", "se utilizarán las claves no reservadas de la 14 a la 29, para retribuciones de personal funcionario")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, la hoja resumen de nómina deberá ir firmada por:",
  ["El Habilitado y el Jefe del Centro o de la Dependencia correspondiente.", "El Habilitado y el Interventor Delegado.", "El Jefe del Centro y el Subsecretario del Departamento.", "Solo el Habilitado."],
  "Ap. 5.2 de la Orden.", "Deberá ir firmada por el Habilitado y el Jefe del Centro o de la Dependencia correspondiente")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, los estados justificativos de la nómina se cumplimentarán figurando:",
  ["Sólo cantidades íntegras.", "Sólo cantidades líquidas.", "Cantidades íntegras y líquidas.", "Sólo cantidades netas."],
  "Ap. 5.3 de la Orden.", "figurando sólo cantidades íntegras")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, las nóminas ordinarias tendrán asignado como número de nómina:",
  ["01.", "00.", "02.", "El del mes de devengo."],
  "Ap. 5.5 de la Orden: ordinarias 01; las demás, a partir del 02.", "Las nóminas ordinarias tendrán asignado 01 como número de nómina")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, los perceptores incluidos en las nóminas distintas de la ordinaria que se confeccionen durante el mes, a efectos de los estados justificativos:",
  ["Serán considerados como altas en nómina.", "Serán considerados como modificaciones transitorias.", "Serán considerados como modificaciones definitivas.", "No figurarán en los estados justificativos."],
  "Ap. 5.5 de la Orden.", "serán considerados como altas en nómina")
q("ONOM1992", "A5", "Estructura de la nómina", "Según la Orden de 30 de julio de 1992, en el cuerpo de la nómina el modelo N1 es:",
  ["La nómina de personal, para reclamar todas las retribuciones.", "La hoja resumen de nómina.", "El resumen de retribuciones y de deducciones.", "La variación mensual de retribuciones-Altas."],
  "Ap. 5 de la Orden: N1 cuerpo de la nómina; RN hoja resumen; RRD resumen; VR1 altas.", "Modelo N1. Nómina de personal, para reclamar todas las retribuciones.")
q("ONOM1992", "A2", "Altas y bajas", "Según la Orden de 30 de julio de 1992, se considerará como alta:",
  ["La inclusión en la nómina de un perceptor que no figuraba en la del mes anterior.", "La inclusión en la nómina de un perceptor que no figuraba en la del mismo mes del año anterior.", "Cualquier aumento de retribuciones respecto del mes anterior.", "La toma de posesión de un funcionario en un nuevo puesto, aunque figurase en la nómina del mes anterior."],
  "Ap. 2 de la Orden.", "Se considerará como alta la inclusión en la nómina de un perceptor que no figuraba en la del mes anterior")
q("ONOM1992", "A3", "Altas y bajas", "Según la Orden de 30 de julio de 1992, se considerará como baja:",
  ["La exclusión de la nómina de un perceptor que figuraba en la del mes anterior.", "Cualquier disminución de retribuciones respecto del mes anterior.", "La exclusión de un perceptor que figuraba en la nómina del mismo mes del año anterior.", "El pase a una licencia parcialmente retribuida."],
  "Ap. 3 de la Orden.", "Se considerará como baja la exclusión de la nómina de un perceptor que figuraba en la del mes anterior")
q("ONOM1992", "A2", "Altas y bajas", "Según la Orden de 30 de julio de 1992, al alta en nómina de un funcionario de carrera de nuevo ingreso se unirá, entre otros documentos:",
  ["Copia del título administrativo.", "Certificado de baja en nómina.", "Liquidación de trienios en todo caso.", "Copia de la hoja de servicios."],
  "Ap. 2.1 de la Orden: título administrativo, nombramiento (F.1) y toma de posesión (F.2R). El certificado de baja es para comisión de servicios o traslado; la hoja de servicios, para interinos y laborales.", "Copia del título administrativo.")
q("ONOM1992", "A2", "Altas y bajas", "Según la Orden de 30 de julio de 1992, en el alta de un funcionario en comisión de servicios se unirá, además del nombramiento y la toma de posesión:",
  ["Certificado de baja en nómina, conforme al anexo III.a).", "Copia del título administrativo.", "Liquidación de trienios.", "Acuerdo de cambio de situación administrativa, según modelo F.6R."],
  "Ap. 2.4 b) de la Orden.", "Certificado de baja en nómina, conforme al anexo III.a).")
q("ONOM1992", "A3", "Altas y bajas", "Según la Orden de 30 de julio de 1992, la baja en nómina por jubilación se justificará con:",
  ["El acuerdo de jubilación, según modelo F.15R, y la formalización de cese, según modelo F.4R.", "El acuerdo de jubilación, según modelo F.15R, únicamente.", "El acuerdo de cambio de situación administrativa, según modelo F.6R.", "La anotación de sanción disciplinaria, según modelo F.12R."],
  "Ap. 3.3 de la Orden.", ["Acuerdo de jubilación, según modelo F.15R.", "Formalización de cese, según modelo F.4R."])
q("ONOM1992", "A4", "Modificaciones", "Según la Orden de 30 de julio de 1992, las modificaciones en nómina que producen cambios que no van a persistir en nóminas futuras son:",
  ["Modificaciones transitorias.", "Modificaciones definitivas.", "Bajas en nómina.", "Modificaciones en las deducciones."],
  "Ap. 4 de la Orden.", "Modificaciones transitorias son las que producen cambios que no van a persistir en nóminas futuras.")
q("ONOM1992", "A4", "Modificaciones", "Según la Orden de 30 de julio de 1992, la disminución por el ejercicio del derecho de huelga se justificará con:",
  ["Certificación expedida por el órgano competente en la que se determine el personal en huelga y el tiempo de duración de la misma.", "Acuerdo de licencia o permiso, según modelo F.17R.", "Anotación de sanción disciplinaria, según modelo F.12R.", "Certificación del habilitado."],
  "Ap. 4.2.2.1 de la Orden.", "Por el ejercicio del derecho de huelga: Se acompañará certificación expedida por el órgano competente en el que se determine el personal en huelga y el tiempo de duración de la misma.")
q("ONOM1992", "A4", "Modificaciones", "Según la Orden de 30 de julio de 1992, los atrasos que se incluyen en una nómina posterior a la que recoge el alta o aumento definitivo se justifican con la documentación del alta o aumento y con:",
  ["Certificación del habilitado por la que se acredite que no han sido incluidos en nóminas anteriores.", "Informe de la Intervención Delegada.", "Resolución del Subsecretario del Departamento.", "Declaración responsable del perceptor."],
  "Ap. 4.1.2.4 b) de la Orden.", "Certificación del habilitado por la que se acredite que no han sido incluidos en nóminas anteriores.")
q("ONOM1992", "A5", "Ingresos en formalización", "Según la Orden de 30 de julio de 1992, las deducciones formalizables son:",
  ["Las deducciones cuyo ingreso se realiza en formalización en el Tesoro Público.", "Las deducciones cuyo ingreso se realiza directamente por el perceptor.", "Las deducciones que no son consecuencia de variaciones en el íntegro.", "Las deducciones voluntarias autorizadas por el perceptor."],
  "Ap. 5.1.5 de la Orden.", "Son las deducciones cuyo ingreso se realiza en formalización en el Tesoro Público.")
q("ONOM1992", "A5", "Ingresos en formalización", "Según la Orden de 30 de julio de 1992, el importe líquido de cada perceptor es la cantidad resultante de restar al importe íntegro:",
  ["La suma de los importes de todas las deducciones formalizables.", "La suma de los importes de todas las deducciones no formalizables.", "La suma de todas las deducciones, formalizables y no formalizables.", "Solo la retención del IRPF."],
  "Ap. 5.1.8: líquido = íntegro − formalizables; neto = líquido − no formalizables.", "Importe líquido: Con la cantidad resultante de restar al importe íntegro la suma de los importes de todas las deducciones formalizables.")
q("ONOM1992", "A5", "Ingresos en formalización", "Según la Orden de 30 de julio de 1992, el código de deducción 02 corresponde a:",
  ["Derechos pasivos.", "IRPF.", "MUFACE.", "Cuota obrera del RGSS."],
  "Ap. 5.1.7: 01 IRPF, 02 derechos pasivos, 03 MUFACE, 09 cuota obrera del RGSS.", "02: Derechos pasivos.")
q("OIOC", "regla69", "Tramitación y pago", "Según la regla 69 de la Instrucción de operatoria contable, los habilitados o cajeros pagadores deberán presentar los documentos OK o ADOK de las nóminas en las oficinas de contabilidad:",
  ["Antes del día 7 de cada mes.", "Antes del día 5 de cada mes.", "Antes del día 15 de cada mes.", "Dentro de los cinco días siguientes al cierre de la nómina."],
  "Regla 69.2: «antes del día 7 de cada mes».", "antes del día 7 de cada mes")
q("OIOC", "regla69", "Tramitación y pago", "Según la regla 69 de la Instrucción de operatoria contable, el pago de los importes de las nóminas se efectuará:",
  ["Al menos, con cinco días de antelación al correspondiente vencimiento.", "Al menos, con siete días de antelación al correspondiente vencimiento.", "El mismo día del vencimiento.", "Dentro de los cinco días siguientes al vencimiento."],
  "Regla 69.4.", "se efectúe, al menos, con cinco días de antelación al correspondiente vencimiento")
q("OIOC", "regla66", "Tramitación y pago", "Según la regla 66 de la Instrucción de operatoria contable, el pago de las retribuciones del personal en activo al servicio de la Administración General del Estado se efectuará:",
  ["En todos los casos, a través de las nóminas formuladas por los correspondientes habilitados.", "A través de nóminas o mediante anticipos de caja fija, a elección del Servicio gestor.", "Mediante pagos a justificar.", "A través de las nóminas formuladas por las oficinas de contabilidad."],
  "Regla 66.1.", "se efectuará, en todos los casos, a través de las nóminas formuladas por los correspondientes habilitados")
q("OIOC", "regla67", "Tramitación y pago", "Según la regla 67 de la Instrucción de operatoria contable, para las retribuciones de carácter fijo y vencimiento periódico, al inicio del ejercicio el Servicio gestor formulará:",
  ["Un documento AD por el importe que se prevea gastar durante el ejercicio.", "Un documento RC por el importe de la nómina de enero.", "Un documento OK por cada mensualidad.", "Un documento A por el crédito total del capítulo primero."],
  "Regla 67.1.", "al inicio del ejercicio, el Servicio gestor competente formulará un documento AD por el importe que se prevea gastar durante dicho ejercicio")
q("RES2010N", R, "Ingresos en formalización", "Según la Resolución de 25 de mayo de 2010, la cuota de derechos pasivos que los habilitados retienen en nómina, para todos los funcionarios del mismo Cuerpo, Escala, Empleo o Categoría:",
  ["Supone una cantidad única e idéntica, cualquiera que sea su antigüedad en el servicio del Estado.", "Varía según los trienios reconocidos a cada funcionario.", "Se calcula sobre la totalidad de las retribuciones íntegras de cada funcionario.", "Solo se retiene en las pagas extraordinarias."],
  "Ap. A.3.2 de la Resolución.", "cualquiera que sea su antigüedad en el servicio del Estado, la cuota supone una cantidad única e idéntica")
q("RES2010N", R, "Ingresos en formalización", "Según la Resolución de 25 de mayo de 2010, las cuotas de derechos pasivos y de mutualidades de los periodos en que se disfruten licencias sin derecho a retribución:",
  ["No experimentarán reducción en su cuantía.", "Se reducirán proporcionalmente.", "No se devengarán.", "Se duplicarán en el mes de reincorporación."],
  "Ap. A.3.3 de la Resolución.", "no experimentarán reducción en su cuantía")
q("RES2010N", R, "Ingresos en formalización", "Según la Resolución de 25 de mayo de 2010, las referencias a haberes líquidos para el cálculo de los anticipos reintegrables a funcionarios se entenderán hechas a:",
  ["Las retribuciones básicas líquidas.", "La totalidad de las retribuciones líquidas.", "Las retribuciones íntegras mensuales.", "Las retribuciones complementarias líquidas."],
  "Ap. A.4.4 de la Resolución.", "se entenderán siempre hechas a las retribuciones básicas líquidas")
q("TREBEP", "Artículo 30", "Devengo y liquidación", "Según el artículo 30.2 del TREBEP, la deducción de haberes de quienes ejerciten el derecho de huelga:",
  ["No tendrá carácter de sanción ni afectará al régimen respectivo de sus prestaciones sociales.", "Tendrá carácter de sanción, pero no afectará a sus prestaciones sociales.", "No tendrá carácter de sanción, pero afectará a sus prestaciones sociales.", "Solo procederá si la huelga es declarada ilegal."],
  "Art. 30.2 TREBEP.", "sin que la deducción de haberes que se efectúe tenga carácter de sanción, ni afecte al régimen respectivo de sus prestaciones sociales")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, para el cálculo del valor hora aplicable a la deducción proporcional de haberes, la totalidad de las retribuciones íntegras mensuales se divide entre:",
  ["El número de días naturales del correspondiente mes.", "El número de días hábiles del correspondiente mes.", "Treinta, en todo caso.", "El número de días laborables del correspondiente mes."],
  "Ap. A.2.1 de la Resolución.", "dividida entre el número de días naturales del correspondiente mes")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, las retribuciones básicas y complementarias que se devenguen con carácter fijo y periodicidad mensual se harán efectivas por mensualidades completas y con referencia a la situación y derechos del funcionario referidos:",
  ["Al primer día hábil del mes a que correspondan.", "Al último día hábil del mes a que correspondan.", "Al día 5 del mes a que correspondan.", "Al primer día natural del mes siguiente."],
  "Ap. A.2.3 de la Resolución.", "referidos al primer día hábil del mes a que correspondan")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, ¿en cuál de los siguientes casos NO se liquidan por días las retribuciones del mes de cese en el servicio activo?",
  ["Cuando el cese sea por jubilación de un funcionario sujeto al régimen de Clases Pasivas del Estado.", "Cuando el cese derive de un cambio de Cuerpo o Escala de pertenencia.", "Cuando el cese sea por pase a excedencia voluntaria.", "Cuando el cese sea por pase a servicios especiales."],
  "Ap. A.2.3 d): se liquida por días el mes de cese, incluido el cambio de Cuerpo o Escala, «salvo que sea por motivos de fallecimiento, jubilación o retiro» de funcionarios de Clases Pasivas.", "salvo que sea por motivos de fallecimiento, jubilación o retiro de funcionarios sujetos al régimen de Clases Pasivas del Estado")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, las pagas extraordinarias de los funcionarios del Estado se devengarán:",
  ["El primer día hábil de los meses de junio y diciembre.", "El último día hábil de los meses de junio y diciembre.", "El primer día hábil de los meses de julio y diciembre.", "El día 15 de los meses de junio y diciembre."],
  "Ap. A.2.6 de la Resolución.", "se devengarán el primer día hábil de los meses de junio y diciembre")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, a efectos del devengo de las pagas extraordinarias, el tiempo de duración de licencias sin derecho a retribución:",
  ["No tendrá la consideración de servicios efectivamente prestados.", "Tendrá la consideración de servicios efectivamente prestados.", "Computará al cincuenta por ciento.", "Computará solo si no supera un mes."],
  "Ap. A.2.6 de la Resolución.", "el tiempo de duración de licencias sin derecho a retribución no tendrá la consideración de servicios efectivamente prestados")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, los funcionarios de carrera en servicio activo que accedan a un nuevo Cuerpo o Escala tendrán derecho, a partir de la toma de posesión, si el destino no implica cambio de residencia, a un permiso retribuido de:",
  ["Tres días hábiles.", "Un mes.", "Tres días naturales.", "Quince días hábiles."],
  "Ap. A.2.7: tres días hábiles sin cambio de residencia; un mes si lo comporta.", "un permiso retribuido de tres días hábiles, si el destino no implica cambio de residencia")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, los titulares de puestos de trabajo que se supriman continuarán percibiendo, a cuenta, las retribuciones complementarias del puesto suprimido durante un plazo máximo de:",
  ["Tres meses.", "Un mes.", "Seis meses.", "Un año."],
  "Ap. A.4.3 de la Resolución.", "durante un plazo máximo de tres meses")
q("RES2010N", R, "Devengo y liquidación", "Según la Resolución de 25 de mayo de 2010, los funcionarios que realicen una jornada disminuida conforme al artículo 48.1.g) y h) del Estatuto Básico experimentarán la reducción:",
  ["Sobre la totalidad de sus retribuciones, tanto básicas como complementarias, con inclusión de los trienios.", "Solo sobre las retribuciones complementarias.", "Sobre las retribuciones básicas y complementarias, con exclusión de los trienios.", "Solo sobre el complemento específico."],
  "Ap. A.2.2 de la Resolución.", "sobre la totalidad de sus retribuciones, tanto básicas como complementarias, con inclusión de los trienios")
q("RES2010N", "anexoXV", "Devengo y liquidación", "Según el anexo XV de la Resolución de 25 de mayo de 2010, el personal que perciba su sueldo en cuantía inferior a la establecida con carácter general percibirá la indemnización por residencia:",
  ["Disminuida en la misma proporción.", "En su cuantía íntegra.", "Disminuida en un cincuenta por ciento.", "Solo en las pagas extraordinarias."],
  "Anexo XV (texto del PDF oficial del BOE).", "percibirá la indemnización por residencia disminuida en la misma proporción")
q("L30", "aveintitres", "Retribuciones", "Según el artículo 23.2 c) de la Ley 30/1984, las pagas extraordinarias de los funcionarios se devengarán:",
  ["Los meses de junio y diciembre.", "Los meses de julio y diciembre.", "Los meses de junio y noviembre.", "Prorrateadas en las doce mensualidades."],
  "Art. 23.2 c) Ley 30/1984.", "se devengarán los meses de junio y diciembre")
for cod, n, cat in [("L", 100, "Confección de nóminas"), ("P", 105, "Devengo y liquidación"), ("X", 100, "Devengo y liquidación")]:
    T.real(cod, n, cat)

# Flashcards
for q_, a_, cat in [
  ("¿Qué norma regula la confección de las nóminas del personal de la Administración del Estado?", "La Orden de 30 de julio de 1992 sobre instrucciones para la confección de nóminas (texto consolidado del BOE).", "Confección de nóminas"),
  ("¿Quién formula las nóminas del personal en activo? (regla 66)", "Los habilitados; el pago se efectúa en todos los casos a través de nómina.", "Tramitación y pago"),
  ("¿Qué día se cierran las nóminas ordinarias? (ap. 6)", "El día 5 de cada mes.", "Confección de nóminas"),
  ("¿Antes de qué día se presentan los OK/ADOK de la nómina? (regla 69.2)", "Antes del día 7 de cada mes, junto con los «Resúmenes de nómina».", "Tramitación y pago"),
  ("¿Con cuánta antelación se paga la nómina? (regla 69.4)", "Al menos cinco días antes del vencimiento.", "Tramitación y pago"),
  ("Partes de la nómina (ap. 5)", "Cuerpo (N1), resúmenes (RN, RRD, RRX, REN) y estados justificativos (VR1-VR4 y VD1-VD4).", "Estructura de la nómina"),
  ("Número de la nómina ordinaria y de las demás (ap. 5.5)", "Ordinaria: 01; las demás del mes, desde el 02 (sus perceptores son altas).", "Estructura de la nómina"),
  ("Claves 01 a 07 de las retribuciones (ap. 5.1.4)", "01 sueldo, 02 trienios, 03 paga extraordinaria, 04 destino, 05 específico, 06 productividad, 07 gratificaciones.", "Estructura de la nómina"),
  ("Alta y baja en nómina (aps. 2 y 3)", "Alta: incluir a quien no figuraba en la nómina del mes anterior. Baja: excluir a quien figuraba.", "Altas y bajas"),
  ("Modificaciones definitivas y transitorias (ap. 4)", "Definitivas: cambios que persisten en nóminas futuras. Transitorias: los que no persisten.", "Modificaciones"),
  ("¿Qué documento acompaña al alta del funcionario que llega en comisión de servicios o por traslado?", "Nombramiento y toma de posesión (o F.5R) y el certificado de baja en nómina (anexo III.a).", "Altas y bajas"),
  ("Deducción formalizable (ap. 5.1.5)", "La deducción cuyo ingreso se realiza en formalización en el Tesoro Público.", "Ingresos en formalización"),
  ("Íntegro, líquido y neto (ap. 5.1.8)", "Íntegro: suma de retribuciones. Líquido: íntegro − deducciones formalizables. Neto: líquido − no formalizables.", "Ingresos en formalización"),
  ("Códigos de deducción 01, 02, 03 y 09 (ap. 5.1.7)", "01 IRPF, 02 derechos pasivos, 03 MUFACE, 09 cuota obrera del RGSS.", "Ingresos en formalización"),
  ("¿Depende de la antigüedad la cuota de derechos pasivos? (Res. 2010, A.3.2)", "No: es una cantidad única e idéntica para todo el Cuerpo, Escala, Empleo o Categoría.", "Ingresos en formalización"),
  ("Valor hora para la deducción proporcional (Res. 2010, A.2.1)", "Retribuciones íntegras mensuales ÷ días naturales del mes ÷ horas diarias de obligado cumplimiento (de media).", "Devengo y liquidación"),
  ("Regla general de devengo de las retribuciones mensuales (Res. 2010, A.2.3)", "Mensualidades completas, según la situación y derechos del primer día hábil del mes.", "Devengo y liquidación"),
  ("¿Qué meses se liquidan por días? (Res. 2010, A.2.3)", "Toma de posesión del primer destino, reingreso, vuelta e inicio de licencias sin retribución, cambio a otra Administración y cese (salvo fallecimiento, jubilación o retiro).", "Devengo y liquidación"),
  ("Devengo de las pagas extraordinarias (Res. 2010, A.2.6)", "Primer día hábil de junio y diciembre; proporcionales si no hay seis meses de servicios (÷ 182/183 días).", "Devengo y liquidación"),
  ("Indemnización por residencia (anexo XV)", "Doce mensualidades, sin repercusión en pagas extraordinarias.", "Devengo y liquidación"),
  ("Puesto suprimido (Res. 2010, A.4.3)", "Complementarias del puesto suprimido a cuenta, máximo tres meses, sin reintegro del exceso.", "Devengo y liquidación"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Nómina", "Documento por el que se pagan, en todos los casos, las retribuciones del personal en activo de la Administración General del Estado; la formulan los habilitados (Instrucción de operatoria contable, regla 66).", "s2", "Nóminas")
T.glos("Habilitado", "Quien confecciona las nóminas, retiene las cuotas y presenta los documentos OK o ADOK con los resúmenes de nómina (regla 69; Resolución de 2010, ap. A.3.2).", "s5", "Nóminas")
T.glos("Nómina ordinaria", "Nómina número 01 de cada mes, con las remuneraciones fijas y periódicas y, en su mes, las pagas extraordinarias; se cierra el día 5 (Orden de 1992, aps. 5.5 y 6).", "s3", "Nóminas")
T.glos("Estados justificativos", "Modelos VR (retribuciones) y VD (deducciones) que relacionan altas, bajas y modificaciones, solo con cantidades íntegras (Orden de 1992, ap. 5.3).", "s3", "Nóminas")
T.glos("Alta en nómina", "Inclusión de un perceptor que no figuraba en la nómina del mes anterior (Orden de 1992, ap. 2).", "s6", "Altas y bajas")
T.glos("Baja en nómina", "Exclusión de la nómina de un perceptor que figuraba en la del mes anterior (Orden de 1992, ap. 3).", "s7", "Altas y bajas")
T.glos("Modificación transitoria", "Cambio en retribuciones o deducciones que no va a persistir en nóminas futuras (Orden de 1992, ap. 4).", "s8", "Altas y bajas")
T.glos("Deducción formalizable", "Deducción cuyo ingreso se realiza en formalización en el Tesoro Público (Orden de 1992, ap. 5.1.5).", "s10", "Ingresos en formalización")
T.glos("Importe líquido", "Importe íntegro menos las deducciones formalizables (Orden de 1992, ap. 5.1.8).", "s10", "Ingresos en formalización")
T.glos("Valor hora", "Retribuciones íntegras mensuales divididas entre los días naturales del mes y las horas diarias de obligado cumplimiento; base de la deducción proporcional (Resolución de 2010, ap. A.2.1).", "s13", "Devengo y liquidación")
T.glos("Liquidación por días", "Excepción a la mensualidad completa en los supuestos del ap. A.2.3 de la Resolución de 2010 (primer destino, reingreso, licencias sin retribución, cambio de Administración, cese).", "s14", "Devengo y liquidación")
T.glos("Indemnización por residencia", "Indemnización del personal destinado en áreas que la tienen reconocida; doce mensualidades sin repercusión en pagas extraordinarias (Resolución de 2010, anexo XV).", "s17", "Devengo y liquidación")

# Cronología (fechas de los metadatos del BOE)
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Art. 23: conceptos retributivos; pagas extraordinarias en junio y diciembre", "normativo", "s1")
T.hito("1992", "Orden de 30 de julio de 1992 sobre instrucciones para la confección de nóminas (BOE de 13-8-1992)", "Estructura de la nómina, altas, bajas, modificaciones, deducciones y cierre el día 5", "normativo", "s3")
T.hito("1996", "Orden de 1 de febrero de 1996, Instrucción de operatoria contable a seguir en la ejecución del gasto del Estado (BOE de 8-2-1996)", "Reglas 66 a 70: tramitación y pago de las nóminas", "normativo", "s5")
T.hito("2010", "Resolución de 25 de mayo de 2010, de la Secretaría de Estado de Hacienda y Presupuestos, instrucciones sobre nóminas (BOE de 26-5-2010; corrección de errores en el BOE de 2-6-2010)", "Devengo de retribuciones, cuotas e indemnización por residencia", "normativo", "s14")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Arts. 22, 23 y 30: retribuciones y deducción de haberes", "normativo", "s13")

T.publicar()
