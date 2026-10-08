# Plan de alimentación complementaria de Pablo

Genera el plan diario (bloque `pb-plan-data` de `index.html`) desde el 8 de
octubre de 2026 hasta el 2 de junio de 2027, con la pauta de la pediatra:

- hasta el 4 de noviembre: desayuno, media mañana, almuerzo, merienda, antes de dormir, noche;
- desde el 5 de noviembre: desayuno, media mañana (opcional), almuerzo, merienda, cena, noche.

```
python3 tools/plan_ac/generar.py            # genera, verifica y escribe en index.html
python3 tools/plan_ac/generar.py --solo-ver # solo genera y verifica
```

- `alimentos.py`: catálogo (nombre de Colombia y de España, categoría, alérgeno, forma BLW y a cuchara por edad).
- `recetas.py`: recetario (ingredientes, pasos, BLW, cuchara, conservación).
- `generar.py`: calendario de introducción, menús, batch, lista de la compra y verificación.

Si la verificación encuentra algo (fruta en el almuerzo, alérgenos nuevos demasiado
juntos, arroz más de 3 veces en 7 días, un alimento antes de su edad…), no escribe nada.
Los días anteriores al 8 de octubre se conservan tal cual.
