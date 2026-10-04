# -*- coding: utf-8 -*-
"""Texto legal LITERAL y comprobación plantilla ↔ ley del examen GACE-P 2025
(promoción interna), primer ejercicio. Formato: ver verif_examen.py y leyes25L.py."""
from leyes25L import NOMBRE as _N

NOMBRE = dict(_N,
  CE="Constitución Española", LJCA="Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa",
  L2_2014="Ley 2/2014, de la Acción y del Servicio Exterior del Estado",
  RD951="Real Decreto 951/2005, marco general para la mejora de la calidad en la Administración General del Estado",
  LGOB="Ley 50/1997, del Gobierno",
  RD615="Real Decreto 615/2024, Estatuto del Consejo de Transparencia y Buen Gobierno",
  RD1026="Real Decreto 1026/2024, medidas para la igualdad y no discriminación de las personas LGTBI en las empresas",
  RD725="Real Decreto 725/1989, sobre anticipos de Caja fija",
  RD203="Real Decreto 203/2021, Reglamento de actuación y funcionamiento del sector público por medios electrónicos",
  RD1118="Real Decreto 1118/2024, Estatuto de la Agencia Estatal de Administración Digital",
  RD126_2026="Real Decreto 126/2026, por el que se fija el salario mínimo interprofesional para 2026",
  ET="Texto refundido de la Ley del Estatuto de los Trabajadores (RDLeg 2/2015)",
)

LEY, SI, NO, SIN_LEY = {}, {}, {}, {}

# ---- 1 a 19 -----------------------------------------------------------------
LEY[1] = [("L2_2014", "a6", [6], "artículo 6.5", ["El Ministro de Asuntos Exteriores y de Cooperación", "planifica y ejecuta la Política Exterior del Estado"])]
SI[1] = [("Al Ministro de Asuntos Exteriores y de Cooperación", "L2_2014", "a6", "El Ministro de Asuntos Exteriores y de Cooperación, en el marco de la superior dirección del Gobierno y de su Presidente, planifica y ejecuta la Política Exterior del Estado")]
LEY[2] = [("L40", "Artículo 55", [14], "artículo 55.4", ["son órganos directivos tanto los Delegados del Gobierno en las Comunidades Autónomas, que tendrán rango de Subsecretario"])]
SI[2] = [("órganos directivos", "L40", "Artículo 55", "son órganos directivos tanto los Delegados del Gobierno en las Comunidades Autónomas"),
         ("Subsecretario", "L40", "Artículo 55", "que tendrán rango de Subsecretario")]
LEY[3] = [("L40", "Artículo 55", [6, 7, 8, 9, 10, 11, 12, 13], "artículo 55.3", ["Órganos superiores", "Los Ministros.", "Los Secretarios de Estado."])]
SI[3] = [("Los Ministros y Secretarios de Estado", "L40", "Artículo 55", "a) Órganos superiores: 1.º Los Ministros. 2.º Los Secretarios de Estado.")]
LEY[4] = [("L40", "Artículo 95", [3, 4, 5, 6, 7, 8, 9], "artículo 95.2", ["Publicaciones"])]
SI[4] = [("Las publicaciones", "L40", "Artículo 95", "e) Publicaciones.")]
LEY[5] = [("L40", "Artículo 108 ter", [11], "artículo 108 ter.4", ["en el plazo de tres meses desde su constitución"])]
SI[5] = [("tres meses", "L40", "Artículo 108 ter", "aprueba la propuesta de contrato inicial de gestión, en el plazo de tres meses desde su constitución")]
LEY[6] = [("L40", "a99", [1], "artículo 99", ["en su ley de creación", "derecho administrativo general y especial"])]
SI[6] = [("ley de creación", "L40", "a99", "en esta Ley, en su ley de creación"), ("Derecho administrativo", "L40", "a99", "el resto de las normas de derecho administrativo general y especial")]
LEY[7] = [("L40", "a103", [1], "artículo 103.1", ["con personalidad jurídica propia, patrimonio propio", "se financian con ingresos de mercado"])]
SI[7] = [("personalidad jurídica propia y patrimonio propio", "L40", "a103", "con personalidad jurídica propia, patrimonio propio")]
LEY[8] = [("TFUE", "Artículo 3", [1, 2, 3, 4, 5, 6], "artículo 3.1", ["la política comercial común"])]
SI[8] = [("La política comercial común", "TFUE", "Artículo 3", "e) la política comercial común")]
LEY[9] = [("TUE", "Artículo 49", [1], "artículo 49, párrafo primero", ["dirigirá su solicitud al Consejo, que se pronunciará por unanimidad"])]
SI[9] = [("Al Consejo, que se pronunciará por unanimidad", "TUE", "Artículo 49", "El Estado solicitante dirigirá su solicitud al Consejo, que se pronunciará por unanimidad")]
SIN_LEY[10] = "«Derecho primario» es una categoría doctrinal: ningún artículo de los Tratados lo dice literalmente."
LEY[11] = [("TFUE", "Artículo 247", [1], "artículo 247", ["que deje de reunir las condiciones necesarias para el ejercicio de sus funciones o haya cometido una falta grave"])]
SI[11] = [("dejar de reunir las condiciones necesarias para el ejercicio de sus funciones", "TFUE", "Artículo 247", "Todo miembro de la Comisión que deje de reunir las condiciones necesarias para el ejercicio de sus funciones")]
LEY[12] = [("TFUE", "Artículo 255", [1, 2], "artículo 255", ["antes de que", "siete personalidades", "El Consejo adoptará una decisión por la que se establezcan las normas de funcionamiento del comité"])]
SI[12] = [("El Consejo adoptará una decisión por la que se establezcan sus normas de funcionamiento", "TFUE", "Artículo 255", "El Consejo adoptará una decisión por la que se establezcan las normas de funcionamiento del comité")]
LEY[13] = [("TUE", "Artículo 17", [1], "artículo 17.1", ["La Comisión promoverá el interés general de la Unión", "Velará por que se apliquen los Tratados"])]
SI[13] = [("Promueve el interés general de la Unión", "TUE", "Artículo 17", "La Comisión promoverá el interés general de la Unión"),
          ("vela por la aplicación de los Tratados", "TUE", "Artículo 17", "Velará por que se apliquen los Tratados")]
LEY[14] = [("TFUE", "Artículo 297", [1], "artículo 297.1, párrafo primero", ["firmados por el Presidente del Parlamento Europeo y por el Presidente del Consejo"])]
SI[14] = [("Al Presidente del Parlamento Europeo y al Presidente del Consejo", "TFUE", "Artículo 297", "serán firmados por el Presidente del Parlamento Europeo y por el Presidente del Consejo")]
LEY[15] = [("TFUE", "Artículo 59", [1], "artículo 59.1", ["con arreglo al procedimiento legislativo ordinario y previa consulta al Comité Económico y Social, decidirán mediante directivas"])]
SI[15] = [("Directivas", "TFUE", "Artículo 59", "decidirán mediante directivas"), ("procedimiento legislativo ordinario", "TFUE", "Artículo 59", "con arreglo al procedimiento legislativo ordinario")]
SIN_LEY[16] = "Jurisprudencia del TJUE (sentencia Costa/ENEL, 1964): no hay artículo de los Tratados que la recoja literalmente."
LEY[17] = [("TFUE", "Artículo 177", [2], "artículo 177, párrafo segundo", ["proporcionará una contribución financiera a proyectos en los sectores del medio ambiente"])]
SI[17] = [("proyectos en los sectores", "TFUE", "Artículo 177", "Un Fondo de Cohesión, creado con arreglo al mismo procedimiento, proporcionará una contribución financiera a proyectos en los sectores del medio ambiente")]
LEY[18] = [("TFUE", "Artículo 26", [2], "artículo 26.2", ["un espacio sin fronteras interiores"])]
SI[18] = [("Un espacio sin fronteras interiores", "TFUE", "Artículo 26", "El mercado interior implicará un espacio sin fronteras interiores")]
LEY[19] = [("TFUE", "Artículo 3", [1, 2, 3, 4, 5, 6], "artículo 3.1", ["la política monetaria de los Estados miembros cuya moneda es el euro"])]
SI[19] = [("Exclusiva de la Unión", "TFUE", "Artículo 3", "La Unión dispondrá de competencia exclusiva en los ámbitos siguientes: a) la unión aduanera; b) el establecimiento de las normas sobre competencia necesarias para el funcionamiento del mercado interior; c) la política monetaria de los Estados miembros cuya moneda es el euro")]

# ---- 20 a 55 ----------------------------------------------------------------
LEY[20] = [("RD1118", "a1", [4], "Estatuto, artículo 1.4", ["sede en Madrid"])]
SI[20] = [("Madrid", "RD1118", "a1", "La Agencia tiene su sede en Madrid.")]
# 21 = pregunta 32 del examen L (misma redacción y respuesta)
LEY[21] = [("RD931", "a3", [2], "artículo 3.2", ["listado de las normas que quedan derogadas"])]
SI[21] = [("Listado de las normas que quedan derogadas", "RD931", "a3", "listado de las normas que quedan derogadas")]
LEY[22] = [("RD951", "Artículo 9", [9, 10, 14, 15, 16], "artículo 9 b) (compromisos de calidad)", ["Niveles o estándares de calidad que se ofrecen", "Medidas que aseguren la igualdad de género", "Indicadores utilizados para la evaluación de la calidad"])]
NO[22] = ([("a", "Niveles o estándares de calidad que se ofrecen", "RD951", "Artículo 9", "1.º Niveles o estándares de calidad que se ofrecen"),
           ("b", "Medidas que aseguren la igualdad de género", "RD951", "Artículo 9", "2.º Medidas que aseguren la igualdad de género"),
           ("d", "Indicadores utilizados para la evaluación de la calidad", "RD951", "Artículo 9", "4.º Indicadores utilizados para la evaluación de la calidad")],
          ("análisis de la demanda", "RD951", "Artículo 9"))
LEY[23] = [("LOEP", "Artículo 25", [3, 4], "artículo 25.1 b)", ["Si en el plazo de 3 meses desde la constitución del depósito"])]
SI[23] = [("Tres meses", "LOEP", "Artículo 25", "Si en el plazo de 3 meses desde la constitución del depósito no se hubiera presentado o aprobado el plan, o no se hubieran aplicado las medidas, el depósito no devengará intereses")]
LEY[24] = [("TREBEP", "a49", [2, 34], "artículo 49 a) y c) (funcionarios)", ["diecinueve semanas"]),
           ("ET", "a48", [5], "artículo 48.4 (personal laboral)", ["durante diecinueve semanas"])]
SI[24] = [("19 semanas", "TREBEP", "a49", "Permiso por nacimiento para la madre biológica: tendrá una duración de diecinueve semanas"),
          (None, "TREBEP", "a49", "Permiso del progenitor diferente de la madre biológica por nacimiento, guarda con fines de adopción, acogimiento o adopción de un hijo o hija: tendrá una duración de diecinueve semanas"),
          (None, "ET", "a48", "suspenderá el contrato de trabajo de la madre biológica y el del progenitor distinto de la madre biológica durante diecinueve semanas")]
LEY[25] = [("RD126_2026", "Artículo 1", [1], "artículo 1", ["40,70 euros/día o 1 221 euros/mes"])]
SI[25] = [("40,70 euros/día", "RD126_2026", "Artículo 1", "queda fijado en 40,70 euros/día o 1 221 euros/mes")]
LEY[26] = [("CE", "Artículo 135", [1], "artículo 135.1", ["adecuarán sus actuaciones al principio de estabilidad presupuestaria"])]
SI[26] = [("principio de estabilidad presupuestaria", "CE", "Artículo 135", "Todas las Administraciones Públicas adecuarán sus actuaciones al principio de estabilidad presupuestaria")]
LEY[27] = [("CE", "Artículo 149", [1, 24], "artículo 149.1.23.ª", ["Legislación básica sobre protección del medio ambiente"])]
SI[27] = [("Legislación básica sobre protección del medio ambiente", "CE", "Artículo 149", "23.ª Legislación básica sobre protección del medio ambiente")]
LEY[28] = [("CE", "Artículo 149", [1, 18], "artículo 149.1.17.ª", ["Legislación básica y régimen económico de la Seguridad Social"])]
SI[28] = [("Legislación básica y régimen económico de la Seguridad Social", "CE", "Artículo 149", "17.ª Legislación básica y régimen económico de la Seguridad Social")]
LEY[29] = [("LGSS", "Artículo 121", [1], "artículo 121.1", ["con carácter exclusivo a la financiación de las pensiones de carácter contributivo"])]
SI[29] = [("Pensiones de carácter contributivo.", "LGSS", "Artículo 121", "se destinará con carácter exclusivo a la financiación de las pensiones de carácter contributivo")]
# 30 = L35, 31 = L36, 34 = L101, 35 = L41 (misma redacción y respuesta)
LEY[30] = [("LGSS", "a125", [9], "artículo 125.3", ["conocerá semestralmente de la evolución y composición del Fondo de Reserva"])]
SI[30] = [("Semestralmente", "LGSS", "a125", "conocerá semestralmente")]
LEY[31] = [("L22_2009", "preambulo", None, "preámbulo", ["El Fondo de Suficiencia Global opera como recurso de cierre del sistema"])]
SI[31] = [("Fondo de Suficiencia Global", "L22_2009", "preambulo", "El Fondo de Suficiencia Global opera como recurso de cierre del sistema")]
SIN_LEY[32] = "Contenido de un plan (Plan Director de la Cooperación Española 2024-2027), no de una norma publicada en el BOE."
LEY[33] = [("CE", "Artículo 149", [1, 3], "artículo 149.1.2.ª", ["El Estado tiene competencia exclusiva", "Nacionalidad, inmigración, emigración, extranjería y derecho de asilo"])]
SI[33] = [("Al Estado con carácter exclusivo", "CE", "Artículo 149", "El Estado tiene competencia exclusiva sobre las siguientes materias"),
          (None, "CE", "Artículo 149", "2.ª Nacionalidad, inmigración, emigración, extranjería y derecho de asilo.")]
LEY[34] = [("RD345", "a4", [1, 2, 3, 4, 5, 6, 7, 8], "artículo 4.1", ["dieciséis vocales"])]
SI[34] = [("Dieciséis", "RD345", "a4", "formarán parte del mismo dieciséis vocales")]
LEY[35] = [("LOPD", "Artículo 88", [1], "artículo 88.1", ["el respeto de su tiempo de descanso, permisos y vacaciones, así como de su intimidad personal y familiar"])]
SI[35] = [("tiempo de descanso", "LOPD", "Artículo 88", "el respeto de su tiempo de descanso"), ("intimidad personal y familiar", "LOPD", "Artículo 88", "de su intimidad personal y familiar"),
          ("fuera del tiempo de trabajo", "LOPD", "Artículo 88", "fuera del tiempo de trabajo")]
SIN_LEY[36] = "Contenido de un plan (Plan Estratégico de la AEPD 2025-2030), no de una norma publicada en el BOE."
# 37 = L40, 42 = L43, 43 = L42
LEY[37] = [("RD389", "a6", [2], "artículo 6.2", ["persona titular de la Adjuntía a la Presidencia de la Agencia Española de Protección de Datos o el Subdirector General o Director de División correspondiente"])]
SI[37] = [("Adjuntía a la Presidencia", "RD389", "a6", "suscrito por la persona titular de la Adjuntía a la Presidencia"),
          ("Subdirector General", "RD389", "a6", "o el Subdirector General o Director de División correspondiente"), ("Director de División", "RD389", "a6", "Director de División correspondiente")]
SIN_LEY[38] = "Dato de un plan (V Plan de Gobierno Abierto 2025-2029), no de una norma publicada en el BOE."
LEY[39] = [("RD615", "Artículo 20", [3], "artículo 20.3", ["al menos una vez al trimestre"])]
SI[39] = [("Trimestre", "RD615", "Artículo 20", "La comisión se reunirá al menos una vez al trimestre")]
SIN_LEY[40] = "Dato de una estrategia (Estrategia de Desarrollo Sostenible 2030, revisión de 2026), no de una norma publicada en el BOE."
LEY[41] = [("RD1026", "ai", [4, 6, 20], "anexo I", ["cláusulas de igualdad de trato y no discriminación que contribuyan a crear un contexto favorable a la diversidad", "erradicar estereotipos", "garantizando el acceso"])]
SI[41] = [("cláusulas de igualdad de trato y no discriminación que contribuyan a crear un contexto favorable a la diversidad", "RD1026", "ai",
           "Los convenios colectivos o acuerdos de empresa recogerán en su articulado cláusulas de igualdad de trato y no discriminación que contribuyan a crear un contexto favorable a la diversidad")]
LEY[42] = [("L4_2023", "Artículo 3", [8], "artículo 3 d)", ["Acoso discriminatorio"])]
SI[42] = [("con el objetivo o la consecuencia de atentar contra la dignidad de una persona o grupo en que se integra y de crear un entorno intimidatorio, hostil, degradante, humillante u ofensivo",
           "L4_2023", "Artículo 3", "Acoso discriminatorio: Cualquier conducta realizada por razón de alguna de las causas de discriminación previstas en esta ley, con el objetivo o la consecuencia de atentar contra la dignidad de una persona o grupo en que se integra y de crear un entorno intimidatorio, hostil, degradante, humillante u ofensivo")]
LEY[43] = [("RD1051", "anii", [1, 2, 3, 4], "anexo II", ["Grado II: De 38 a 64 horas mensuales"])]
SI[43] = [("De 38 a 64 horas mensuales", "RD1051", "anii", "Grado II: De 38 a 64 horas mensuales")]
LEY[44] = [("CE", "Artículo 30", [2], "artículo 30.2", ["La ley fijará las obligaciones militares de los españoles"])]
SI[44] = [("obligaciones militares de los españoles", "CE", "Artículo 30", "La ley fijará las obligaciones militares de los españoles")]
LEY[45] = [("CE", "Artículo 87", [1, 2, 3], "artículo 87", ["al Gobierno, al Congreso y al Senado", "remitir a la Mesa del Congreso una proposición de ley", "no menos de 500.000 firmas", "tributarias"])]
SI[45] = [("Las Asambleas de las Comunidades Autónomas podrán remitir a la Mesa del Congreso una proposición de ley", "CE", "Artículo 87", "Las Asambleas de las Comunidades Autónomas podrán solicitar del Gobierno la adopción de un proyecto de ley o remitir a la Mesa del Congreso una proposición de ley")]
LEY[46] = [("CE", "Artículo 90", [3], "artículo 90.3", ["veinte días naturales"])]
SI[46] = [("Veinte días", "CE", "Artículo 90", "se reducirá al de veinte días naturales en los proyectos declarados urgentes por el Gobierno o por el Congreso de los Diputados")]
LEY[47] = [("CE", "Artículo 85", [1], "artículo 85", ["Decretos Legislativos"])]
SI[47] = [("Decretos Legislativos", "CE", "Artículo 85", "Decretos Legislativos")]
LEY[48] = [("CE", "Artículo 87", [2], "artículo 87.2", ["solicitar del Gobierno la adopción de un proyecto de ley o remitir a la Mesa del Congreso una proposición de ley", "un máximo de tres miembros"])]
SI[48] = [("remitir a la Mesa del Congreso una proposición de ley", "CE", "Artículo 87", "remitir a la Mesa del Congreso una proposición de ley"), ("máximo de tres miembros", "CE", "Artículo 87", "un máximo de tres miembros de la Asamblea encargados de su defensa")]
LEY[49] = [("LGOB", "Artículo 24", [1, 5], "artículo 24.1 d)", ["Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto"])]
SI[49] = [("Acuerdos del Consejo de Ministros", "LGOB", "Artículo 24", "d) Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto")]
LEY[50] = [("CC", "a1", [6], "artículo 1.5", ["mediante su publicación íntegra en el «Boletín Oficial del Estado»"])]
SI[50] = [("Oficial del Estado", "CC", "a1", "en tanto no hayan pasado a formar parte del ordenamiento interno mediante su publicación íntegra en el «Boletín Oficial del Estado»")]
LEY[51] = [("CE", "Artículo 9", [3], "artículo 9.3", ["la interdicción de la arbitrariedad de los poderes públicos", "no favorables o restrictivas de derechos individuales"])]
SI[51] = [("La interdicción de la arbitrariedad de los poderes públicos", "CE", "Artículo 9", "la interdicción de la arbitrariedad de los poderes públicos")]
LEY[53] = [("L39", "Artículo 35", [1, 2, 4, 6, 7], "artículo 35.1 a), c), e) y f)", ["Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias"])]
SI[53] = [("tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias", "L39", "Artículo 35", "e) Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias.")]
LEY[54] = [("L39", "Artículo 52", [1, 2, 3, 4], "artículo 52", ["actos anulables", "desde su fecha", "la convalidación podrá realizarse por el órgano competente cuando sea superior jerárquico del que dictó el acto viciado", "podrá ser convalidado"])]
SI[54] = [("la convalidación podrá realizarse por el órgano competente cuando sea superior jerárquico del que dictó el acto viciado", "L39", "Artículo 52",
           "Si el vicio consistiera en incompetencia no determinante de nulidad, la convalidación podrá realizarse por el órgano competente cuando sea superior jerárquico del que dictó el acto viciado")]
# 55: solo se convalidan los anulables (52.1); la incompetencia jerárquica no es causa de nulidad (47.1 b) solo nombra materia y territorio) y la convalida el superior (52.3).
LEY[55] = [("L39", "Artículo 52", [1, 3], "artículo 52.1 y 3", ["los actos anulables", "superior jerárquico"]),
           ("L39", "Artículo 47", [1, 3, 5, 6], "artículo 47.1 b), d) y e) (nulidad: no convalidables)", ["por razón de la materia o del territorio", "se dicten como consecuencia de ésta", "prescindiendo total y absolutamente del procedimiento legalmente establecido"])]
SI[55] = [("jerarquía", "L39", "Artículo 52", "cuando sea superior jerárquico del que dictó el acto viciado")]

# ---- 56 a 82 ----------------------------------------------------------------
NOMBRE["LOFAGE"] = "Ley 6/1997, de Organización y Funcionamiento de la Administración General del Estado (LOFAGE), DEROGADA por la Ley 40/2015"
LEY[56] = [("LCSP", "a3", [10], "artículo 3.1 f) (sector público)", ["Las Mutuas colaboradoras con la Seguridad Social"]),
           ("LCSP", "a5", [11], "artículo 5.1 b) (excluido: estacionamiento de tropas)", ["estacionamiento de tropas"]),
           ("LCSP", "a1-2", [1], "artículo 10 (excluido: valores e instrumentos financieros)", ["compra, venta o transferencia de valores o de otros instrumentos financieros"]),
           ("LCSP", "a1-3", [5], "artículo 11.5 (excluido: campañas políticas)", ["servicios relacionados con campañas políticas"])]
SI[56] = [("Mutua colaboradora con la Seguridad Social", "LCSP", "a3", "f) Las Mutuas colaboradoras con la Seguridad Social.")]
# 57 (en negativo). Umbrales vigentes desde el 1-1-2026 (arts. 20-22 LCSP): obras y concesiones,
# 5.404.000 €; suministros y servicios de la AGE, sus organismos autónomos y entidades gestoras,
# 140.000 €. a) 5.410.000 ≥ 5.404.000; b) 158.500 ≥ 140.000; d) 6.840.000 ≥ 5.404.000: armonizados.
# c) FOGASA es organismo autónomo (art. 33.1 ET): 139.000 < 140.000 → NO armonizado (plantilla c).
LEY[57] = [("LCSP", "Artículo 20", [1], "artículo 20.1 (obras y concesiones)", ["5.404.000 euros"]),
           ("LCSP", "Artículo 21", [1, 2], "artículo 21.1 a) (suministros)", ["140.000 euros", "sus Organismos Autónomos"]),
           ("LCSP", "Artículo 22", [1, 2], "artículo 22.1 a) (servicios)", ["140.000 euros"]),
           ("ET", "Artículo 33", [1], "artículo 33.1 (naturaleza del FOGASA)", ["organismo autónomo"])]
NO[57] = ([("a", "contrato de obras", "LCSP", "Artículo 20", "los contratos de obras, de concesión de obras y de concesión de servicios cuyo valor estimado sea igual o superior a 5.404.000 euros"),
           ("b", "contrato de servicios", "LCSP", "Artículo 22", "a) 140.000 euros, cuando los contratos hayan de ser adjudicados por la Administración General del Estado"),
           ("d", "concesión de servicios", "LCSP", "Artículo 20", "de concesión de servicios cuyo valor estimado sea igual o superior a 5.404.000 euros")],
          ("139.000", "LCSP", "Artículo 21"))
LEY[58] = [("LCSP", "Artículo 323", [1, 2], "artículo 323.1", ["corresponderá al Ministro, salvo en los casos en que la misma se atribuya a la Junta de Contratación"])]
SI[58] = [("El Ministro, salvo en los casos", "LCSP", "Artículo 323", "corresponderá al Ministro, salvo en los casos en que la misma se atribuya a la Junta de Contratación")]
LEY[59] = [("LCSP", "Artículo 18", [6], "artículo 18.1 a), párrafo segundo", ["el objeto principal se determinará en función de cuál sea el mayor de los valores estimados de los respectivos servicios o suministros"])]
SI[59] = [("el mayor de los valores estimados", "LCSP", "Artículo 18", "el objeto principal se determinará en función de cuál sea el mayor de los valores estimados de los respectivos servicios o suministros")]
LEY[60] = [("LCSP", "Artículo 304", [1], "artículo 304.1", ["serán de cuenta del contratista"])]
SI[60] = [("son de cuenta del contratista", "LCSP", "Artículo 304", "Salvo pacto en contrario, los gastos de la entrega y transporte de los bienes objeto del suministro al lugar convenido serán de cuenta del contratista"),
          ("Salvo pacto en contrario", "LCSP", "Artículo 304", "Salvo pacto en contrario")]
LEY[61] = [("LGS", "Artículo 22", [4, 5], "artículo 22.2 a)", ["Podrán concederse de forma directa", "Las previstas nominativamente en los Presupuestos Generales del Estado"])]
SI[61] = [("La concesión directa", "LGS", "Artículo 22", "Podrán concederse de forma directa las siguientes subvenciones: a) Las previstas nominativamente en los Presupuestos Generales del Estado")]
LEY[62] = [("L39", "Artículo 100", [1, 2, 3, 4, 5], "artículo 100.1", ["Ejecución subsidiaria"])]
SI[62] = [("Ejecución subsidiaria", "L39", "Artículo 100", "b) Ejecución subsidiaria.")]
LEY[63] = [("LGS", "Artículo 57", [1, 4], "artículo 57 c) (grave)", ["La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación"]),
           ("LGS", "Artículo 56", [1, 3, 7, 12], "artículo 56 b), d) 2.º y g) (leves)", ["La presentación de cuentas justificativas inexactas o incompletas", "El incumplimiento de la obligación de llevar o conservar la contabilidad", "La resistencia, obstrucción, excusa o negativa a las actuaciones de control financiero"])]
SI[63] = [("La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación", "LGS", "Artículo 57", "c) La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación.")]
LEY[64] = [("LGS", "Artículo 6", [1, 2], "artículo 6", ["por las normas comunitarias aplicables en cada caso y por las normas nacionales de desarrollo o transposición", "tendrán carácter supletorio respecto de las normas de aplicación directa"])]
SI[64] = [("normas comunitarias aplicables", "LGS", "Artículo 6", "se regirán por las normas comunitarias aplicables en cada caso y por las normas nacionales de desarrollo o transposición de aquéllas"),
          ("supletoria", "LGS", "Artículo 6", "tendrán carácter supletorio respecto de las normas de aplicación directa")]
LEY[65] = [("LGS", "Artículo 54", [1, 2, 3, 4], "artículo 54", ["Cuando concurra fuerza mayor", "para quienes hubieran salvado su voto o no hubieran asistido a la reunión"])]
SI[65] = [("Cuando concurra fuerza mayor", "LGS", "Artículo 54", "b) Cuando concurra fuerza mayor.")]
# 66: la LEF atribuye la resolución al «Gobernador civil» (art. 20). La LOFAGE suprimió los
# Gobernadores civiles y dispuso que el Delegado del Gobierno asumiera sus demás competencias
# (DA 4.ª). La LOFAGE está derogada por la Ley 40/2015, que no repite esa cláusula: se muestran
# ambos textos y se advierte de ello. La plantilla (c) casa con esa equivalencia.
LEY[66] = [("LEF", "aveinte", [1], "artículo veinte", ["el Gobernador civil", "resolverá, en el plazo máximo de veinte días, sobre la necesidad de la ocupación"]),
           ("LOFAGE", "dacuarta", [3], "disposición adicional cuarta (origen de la equivalencia; ley hoy derogada)", ["el Delegado del Gobierno desempeñará las demás competencias que la legislación vigente atribuye a los Gobernadores Civiles"])]
SI[66] = [("Delegado del Gobierno", "LOFAGE", "dacuarta", "el Delegado del Gobierno desempeñará las demás competencias que la legislación vigente atribuye a los Gobernadores Civiles"),
          (None, "LEF", "aveinte", "el Gobernador civil, previas las comprobaciones que estime oportunas, resolverá, en el plazo máximo de veinte días, sobre la necesidad de la ocupación")]
LEY[67] = [("LEF", "asegundo", [1], "artículo segundo.1", ["el Estado, la Provincia o el Municipio"])]
SI[67] = [("El Estado, la Provincia y el Municipio", "LEF", "asegundo", "La expropiación forzosa sólo podrá ser acordada por el Estado, la Provincia o el Municipio.")]
LEY[68] = [("LEF", "aseptimo", [1], "artículo séptimo", ["no impedirán la continuación de los expedientes", "Se considerará subrogado el nuevo titular"])]
SI[68] = [("No impiden la continuación del expediente", "LEF", "aseptimo", "no impedirán la continuación de los expedientes de expropiación forzosa"), ("subrogada", "LEF", "aseptimo", "Se considerará subrogado el nuevo titular en las obligaciones y derechos del anterior")]
LEY[69] = [("CE", "Artículo 132", [3], "artículo 132.3", ["Por ley se regularán"])]
SI[69] = [("Por Ley.", "CE", "Artículo 132", "3. Por ley se regularán el Patrimonio del Estado y el Patrimonio Nacional, su administración, defensa y conservación.")]
LEY[70] = [("LPAP", "a9", [2], "artículo 9.2", ["corresponderán al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado"])]
SI[70] = [("Al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado", "LPAP", "a9", "corresponderán al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado")]
LEY[71] = [("L39", "Artículo 67", [1], "artículo 67.1", ["prescribirá al año de producido el hecho o el acto que motive la indemnización o se manifieste su efecto lesivo"])]
SI[71] = [("Al año de producido el hecho", "L39", "Artículo 67", "El derecho a reclamar prescribirá al año de producido el hecho o el acto que motive la indemnización o se manifieste su efecto lesivo")]
LEY[72] = [("L39", "Artículo 5", [3], "artículo 5.3", ["desistir de acciones", "Para los actos y gestiones de mero trámite se presumirá aquella representación"])]
SI[72] = [("Para desistir de acciones", "L39", "Artículo 5", "interponer recursos, desistir de acciones y renunciar a derechos en nombre de otra persona, deberá acreditarse la representación")]
LEY[73] = [("L39", "Artículo 84", [1, 2], "artículo 84", ["la resolución, el desistimiento, la renuncia al derecho", "la declaración de caducidad", "la imposibilidad material de continuarlo por causas sobrevenidas"])]
SI[73] = [("la declaración de caducidad", "L39", "Artículo 84", "Pondrán fin al procedimiento la resolución, el desistimiento, la renuncia al derecho en que se funde la solicitud, cuando tal renuncia no esté prohibida por el ordenamiento jurídico, y la declaración de caducidad")]
LEY[74] = [("L39", "Artículo 114", [1, 4, 5, 9, 11, 12], "artículo 114.1 c) y d) y 114.2 b) y c)", ["en materia de personal"])]
NO[74] = ([("b", "finalizadores del procedimiento", "L39", "Artículo 114", "d) Los acuerdos, pactos, convenios o contratos que tengan la consideración de finalizadores del procedimiento."),
           ("c", "Ministros y Secretarios de Estado", "L39", "Artículo 114", "b) Los emanados de los Ministros y los Secretarios de Estado en el ejercicio de las competencias que tienen atribuidas los órganos de los que son titulares."),
           ("d", "carezcan de superior jerárquico", "L39", "Artículo 114", "c) Las resoluciones de los órganos administrativos que carezcan de superior jerárquico, salvo que una Ley establezca lo contrario.")],
          ("en el ámbito de su Dirección General", "L39", "Artículo 114"))
LEY[75] = [("L39", "Artículo 53", [1, 2], "artículo 53.1 a)", ["A conocer, en cualquier momento, el estado de la tramitación de los procedimientos en los que tengan la condición de interesados"])]
SI[75] = [("Conocer, en cualquier momento, el estado de la tramitación", "L39", "Artículo 53", "A conocer, en cualquier momento, el estado de la tramitación de los procedimientos en los que tengan la condición de interesados")]
LEY[76] = [("LJCA", "Artículo 10", [1, 3], "artículo 10.1 b)", ["en única instancia", "Las disposiciones generales emanadas de las Comunidades Autónomas y de las Entidades locales"])]
SI[76] = [("disposiciones generales emanadas de las Entidades Locales", "LJCA", "Artículo 10", "Las disposiciones generales emanadas de las Comunidades Autónomas y de las Entidades locales")]
LEY[77] = [("LJCA", "Artículo 46", [1], "artículo 46.1", ["será de dos meses contados desde el día siguiente"])]
SI[77] = [("dos meses", "LJCA", "Artículo 46", "El plazo para interponer el recurso contencioso-administrativo será de dos meses contados desde el día siguiente")]
LEY[78] = [("TREBEP", "Artículo 10", [1], "artículo 10.1", ["con carácter temporal para el desempeño de funciones propias de funcionarios de carrera"])]
SI[78] = [("con carácter temporal para el desempeño de funciones propias de funcionarios de carrera", "TREBEP", "Artículo 10", "son nombrados como tales con carácter temporal para el desempeño de funciones propias de funcionarios de carrera")]
LEY[79] = [("CONV", "a8", [1, 2, 3, 4, 5, 6, 7], "artículo 8.1", ["Grupo profesional E2: Título de Bachiller o Técnico o equivalentes"])]
SI[79] = [("E2", "CONV", "a8", "Grupo profesional E2: Título de Bachiller o Técnico o equivalentes")]
LEY[80] = [("CONV", "a1-3", [2], "artículo 11.2", ["sólo podrá ser aprobada por la Comisión Negociadora del Convenio"])]
SI[80] = [("La Comisión Negociadora del Convenio", "CONV", "a1-3", "Dicha modificación sólo podrá ser aprobada por la Comisión Negociadora del Convenio")]
LEY[81] = [("TREBEP", "Artículo 7", [1, 2], "artículo 7", ["además de por la legislación laboral y por las demás normas convencionalmente aplicables, por los preceptos de este Estatuto que así lo dispongan", "se regirá por lo previsto en el presente Estatuto"])]
SI[81] = [("por los preceptos del TREBEP que así lo dispongan", "TREBEP", "Artículo 7", "por los preceptos de este Estatuto que así lo dispongan"),
          ("legislación laboral, las normas convencionales aplicables", "TREBEP", "Artículo 7", "además de por la legislación laboral y por las demás normas convencionalmente aplicables")]
LEY[82] = [("TREBEP", "Artículo 19", [1, 2], "artículo 19", ["tendrá derecho a la promoción profesional", "a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos"])]
SI[82] = [("procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos aplicables", "TREBEP", "Artículo 19", "se hará efectiva a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos")]

# ---- 83 a 105 ---------------------------------------------------------------
LEY[83] = [("LOEP", "Artículo 13", [1, 2], "artículo 13.1", ["44 por ciento para la Administración central, 13 por ciento para el conjunto de Comunidades Autónomas y 3 por ciento para el conjunto de Corporaciones Locales"])]
SI[83] = [("44 %", "LOEP", "Artículo 13", "44 por ciento para la Administración central"), ("13 %", "LOEP", "Artículo 13", "13 por ciento para el conjunto de Comunidades Autónomas")]
LEY[84] = [("LGP", "a2", [18], "artículo 2.3, párrafo segundo", ["esta Ley no será de aplicación a las Cortes Generales"]),
           ("LGP", "a2", [11, 13, 15], "artículo 2.2 d), f) y h) (sí incluidos)", ["Los consorcios adscritos", "Los fondos sin personalidad jurídica", "las mutuas colaboradoras con la Seguridad Social"])]
SI[84] = [("Las Cortes Generales", "LGP", "a2", "esta Ley no será de aplicación a las Cortes Generales")]
LEY[85] = [("CE", "Artículo 134", [1, 4, 6, 7], "artículo 134.1, 4, 6 y 7", ["Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea", "a las Cortes Generales, su examen, enmienda y aprobación", "antes del primer día del ejercicio económico", "aumento de los créditos"])]
SI[85] = [("podrá modificar tributos cuando una ley tributaria sustantiva así lo prevea", "CE", "Artículo 134", "La Ley de Presupuestos no puede crear tributos. Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea.")]
SIN_LEY[86] = "La lectura de los códigos de una aplicación presupuestaria (sección, servicio, programa, concepto) no figura literal en la LGP (art. 40 solo enumera las clasificaciones)."
LEY[87] = [("LGP", "a43", [1], "artículo 43.1", ["los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo"])]
SI[87] = [("Artículo.", "LGP", "a43", "salvo los créditos destinados a gastos de personal y los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo")]
LEY[88] = [("LGP", "a54", [16], "artículo 54.4", ["No podrán ampliarse créditos que hayan sido previamente minorados"]),
           ("LGP", "a54", [3, 4, 6, 11], "artículo 54.2 a), c) y h) (sí ampliables)", ["pensiones de todo tipo", "capitales-renta para el pago de pensiones", "sistema de protección por cese de actividad"])]
SI[88] = [("previamente minorados", "LGP", "a54", "No podrán ampliarse créditos que hayan sido previamente minorados")]
LEY[89] = [("LGP", "a51", [1, 2, 3, 4, 5, 6], "artículo 51", ["Transferencias", "Generaciones", "Incorporaciones"])]
NO[89] = ([("a", "transferencias", "LGP", "a51", "a) Transferencias."), ("b", "generaciones", "LGP", "a51", "b) Generaciones."), ("c", "incorporaciones", "LGP", "a51", "e) Incorporaciones.")],
          ("redistribuciones", "LGP", "a51"))
LEY[90] = [("LOTCu", "adiez", [1], "artículo diez", ["por delegación, de las Cortes Generales", "dentro del plazo de seis meses"])]
SI[90] = [("Las Cortes Generales delegan", "LOTCu", "adiez", "por delegación, de las Cortes Generales"), ("seis meses", "LOTCu", "adiez", "dentro del plazo de seis meses, a partir de la fecha en que se haya rendido")]
# 91 (en negativo: «¿cuál SÍ se fiscaliza?»): a), b) y c) están en la lista de no sujeción del art. 151;
# d) no (el ACF solo exime gastos menores de 5.000 €, art. 151 c). Aviso: si ese pago fuera un contrato
# menor, también estaría exento (151 a); la plantilla definitiva da d), que es la única no listada.
LEY[91] = [("LGP", "Artículo 151", [1, 2, 4, 5, 6, 7], "artículo 151", ["las subvenciones con asignación nominativa", "los contratos de acceso a bases de datos", "procesos electorales", "menores de 5.000 euros"])]
NO[91] = ([("a", "subvención con asignación nominativa", "LGP", "Artículo 151", "e) las subvenciones con asignación nominativa"),
           ("b", "acceso a bases de datos no sujeto a regulación armonizada", "LGP", "Artículo 151", "f) los contratos de acceso a bases de datos y de suscripción a publicaciones que no tengan el carácter de contratos sujetos a regulación armonizada"),
           ("c", "celebración de procesos electorales", "LGP", "Artículo 151", "d) los gastos correspondientes a la celebración de procesos electorales")],
          ("9.000", "LGP", "Artículo 151"))
LEY[92] = [("LGP", "a74", [6, 10], "artículo 74.5", ["superior a doce millones de euros", "La autorización del Consejo de Ministros implicará la aprobación del gasto"])]
SI[92] = [("El Consejo de Ministros autoriza", "LGP", "a74", "necesitarán autorización del Consejo de Ministros cuando el importe del gasto que de aquellos se derive sea superior a doce millones de euros"),
          ("implica la aprobación del gasto", "LGP", "a74", "La autorización del Consejo de Ministros implicará la aprobación del gasto que se derive del convenio o contrato-programa")]
LEY[93] = [("LGP", "Artículo 75", [1], "artículo 75.1", ["Director General del Tesoro y Política Financiera"])]
SI[93] = [("El Director General del Tesoro y Política Financiera", "LGP", "Artículo 75", "competen al Director General del Tesoro y Política Financiera las funciones de Ordenador General de pagos del Estado")]
LEY[94] = [("RD725", "a1", [1], "artículo 1", ["de carácter extrapresupuestario y permanente"])]
SI[94] = [("de carácter extrapresupuestario y permanente", "RD725", "a1", "las provisiones de fondos de carácter extrapresupuestario y permanente")]
LEY[95] = [("RD725", "a7", [1], "artículo 7.1", ["necesariamente, en el mes de diciembre de cada año"])]
SI[95] = [("En diciembre de cada año", "RD725", "a7", "y, necesariamente, en el mes de diciembre de cada año")]
LEY[96] = [("RES2014", "ai-2", [169, 170, 171, 172, 173], "anexo II (clasificación económica del gasto)", ["23. Indemnizaciones por razón del servicio"])]
SI[96] = [("23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")]
LEY[97] = [("LGT", "a2", [5], "artículo 2.2 b)", ["Contribuciones especiales"])]
SI[97] = [("Contribuciones especiales", "LGT", "a2", "Contribuciones especiales son los tributos cuyo hecho imponible consiste en la obtención por el obligado tributario de un beneficio o de un aumento de valor de sus bienes")]
LEY[98] = [("LGT", "Artículo 20", [1], "artículo 20.1", ["El hecho imponible"])]
SI[98] = [("Hecho imponible", "LGT", "Artículo 20", "El hecho imponible es el presupuesto fijado por la ley para configurar cada tributo y cuya realización origina el nacimiento de la obligación tributaria principal")]
LEY[99] = [("TREBEP", "Artículo 23", [1, 2, 3], "artículo 23", ["única y exclusivamente", "El sueldo", "Los trienios"])]
SI[99] = [("El sueldo y los trienios", "TREBEP", "Artículo 23", "estarán integradas única y exclusivamente por: a) El sueldo asignado a cada Subgrupo o Grupo de clasificación profesional, en el supuesto de que éste no tenga Subgrupo. b) Los trienios")]
LEY[100] = [("TREBEP", "Artículo 26", [1], "artículo 26", ["como mínimo, se corresponderán a las del sueldo del Subgrupo o Grupo"])]
SI[100] = [("A las del sueldo del Subgrupo en que aspiren a ingresar.", "TREBEP", "Artículo 26", "como mínimo, se corresponderán a las del sueldo del Subgrupo o Grupo, en el supuesto de que éste no tenga Subgrupo, en que aspiren a ingresar")]
LEY[101] = [("LGOB", "a6", [2, 3, 4, 5, 6, 7], "artículo 6.2", ["El régimen interno de funcionamiento y en particular el de convocatorias y suplencias", "en su caso, Secretarios de Estado"])]
SI[101] = [("El régimen interno de funcionamiento y en particular el de convocatorias y suplencias", "LGOB", "a6", "e) El régimen interno de funcionamiento y en particular el de convocatorias y suplencias.")]
LEY[102] = [("RD203", "Artículo 11", [11, 14, 15, 16, 20], "artículo 11.2 c), d), e) e i)", ["procedimiento de reclamación"])]
NO[102] = ([("a", "directorio geográfico de oficinas de asistencia en materia de registros", "RD203", "Artículo 11", "i) Un servicio de consulta del directorio geográfico de oficinas de asistencia en materia de registros"),
            ("b", "verificación de los certificados de la sede electrónica", "RD203", "Artículo 11", "d) Un sistema de verificación de los certificados de la sede electrónica."),
            ("d", "verificación de los sellos electrónicos", "RD203", "Artículo 11", "e) Un sistema de verificación de los sellos electrónicos de los órganos")],
           ("procedimiento de verificación establecidos", "RD203", "Artículo 11"))
LEY[103] = [("RD203", "Artículo 21", [11, 16], "artículo 21.4 e)", ["Este plazo será al menos de cinco años"])]
SI[103] = [("Al menos de cinco años", "RD203", "Artículo 21", "Este plazo será al menos de cinco años")]
LEY[104] = [("CONV", "a1-8", [3], "artículo 16.2", ["cuando lo soliciten al menos siete de las personas que componen la parte social o de la Administración"])]
SI[104] = [("al menos siete", "CONV", "a1-8", "cuando lo soliciten al menos siete de las personas que componen la parte social o de la Administración")]
SIN_LEY[105] = "PENDIENTE: la Resolución de 25 de mayo de 2010 (nóminas de los funcionarios) no está en la base consolidada del BOE; falta su texto (pedirlo al usuario)."

# Tema del programa de cada pregunta: solo cuando el epígrafe la cubre sin duda (None = sin clasificar).
TEMA = {1:"III.10", 2:"I.8", 3:"I.8", 4:"I.9", 5:"I.9", 6:"I.9", 7:"I.9", 8:None, 9:"II.1", 10:"II.4",
  11:"II.2", 12:"II.3", 13:"II.2", 14:"II.2", 15:"II.6", 16:"II.4", 17:"II.5", 18:"II.6", 19:None, 20:"III.1",
  21:"III.1", 22:"III.1", 23:"VI.1", 24:None, 25:None, 26:"VI.1", 27:"III.3", 28:"III.4", 29:"III.4", 30:"III.4",
  31:None, 32:"III.10", 33:"III.6", 34:"III.6", 35:"III.8", 36:"III.8", 37:"III.8", 38:"III.7", 39:"III.7", 40:"III.10",
  41:"III.9", 42:"III.9", 43:None, 44:"IV.2", 45:"I.5", 46:"I.5", 47:"IV.2", 48:"I.5", 49:"I.6", 50:"IV.3",
  51:None, 52:"IV.4", 53:"IV.4", 54:"IV.4", 55:"IV.4", 56:"IV.5", 57:"IV.5", 58:"IV.5", 59:"IV.6", 60:"IV.6",
  61:"IV.7", 62:"IV.4", 63:"IV.7", 64:"IV.7", 65:"IV.7", 66:"IV.8", 67:"IV.8", 68:"IV.8", 69:"IV.9", 70:"IV.9",
  71:"IV.10", 72:"IV.11", 73:"IV.11", 74:"IV.12", 75:"IV.12", 76:"IV.13", 77:"IV.13", 78:"V.1", 79:"V.7", 80:"V.7",
  81:"V.1", 82:"V.4", 83:"VI.1", 84:"VI.1", 85:"VI.2", 86:"VI.2", 87:"VI.2", 88:"VI.3", 89:"VI.3", 90:"VI.4",
  91:"VI.4", 92:"VI.5", 93:"VI.5", 94:"VI.6", 95:"VI.6", 96:None, 97:"VI.7", 98:"VI.7", 99:"V.6", 100:"V.6",
  101:"I.6", 102:"III.1", 103:"III.1", 104:"V.7", 105:"VI.8"}
assert sorted(TEMA) == list(range(1, 106))
