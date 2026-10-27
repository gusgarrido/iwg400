# Documentación con respecto al uso de la IA

Este documento tiene como fin transparentar el uso de la Inteligencia Artificial (IA) utilizada a lo largo del proyecto.

Tanto el prompt como la respuesta dada por la IA serán copiados y pegados textualmente. Luego, se puede justificar y/o informar qué se hizo con ello.

Por lo general, este documento sigue el siguiente formato:
1. Mención de archivos creados, modificados, y/o eliminados.
2. Prompt utilizado.
3. Respuesta de la IA.
4. _[Opcional]_ Justificación, acciones tomadas, etc. con respecto a la respuesta obtenida.

Se da por entendido que el código generado por la IA puede ser levemente modificado con el único objetivo de asegurar compatibilidad con la interfaz actual del proyecto. Tales modificaciones no serán redactadas por temas de redundancia e innecesariedad.

> [!IMPORTANT]
> Este documento está hecho exclusivamente para la documentación de **código fuente** generado por la IA.  
> Ayuda con respecto a la organización, estructuración, etc. del proyecto (e.i. que no cambien directamente el código fuente de la página) no serán reportados.

***

> Por temas de espacio y legibilidad, los archivos resultantes de esta interacción no se incluyen en este apartado.
> 1. El archivo HTML generado se encuentra en `src/apps/reports/templates/reports/index.html`.
> 2. El archivo CSS generado se encuentra en `src/apps/reports/static/reports/index.css`

<details>
    <summary>Prompt</summary>

```
Genera un archivo HTML para una página de un proyecto Django. Si es necesario, incluye también el archivo CSS.

La página debe estar dividida en dos secciones. A la izquierda, debe incluir un foro donde se puedan hacer reportes de incidentes. Los campos que deben existir, junto al tipo de campo como tal, son los siguientes:

1. Tipo de incidente (menú drop-down con las opciones de tipo)
2. Descripción (texto)
3. Fecha (hora y fecha del incidente. Predeterminado debería ser el actual)
4. Severidad (menú drop-down con las opciones de severidad)
Al final del foro, debe haber un botón "Reportar" que esté en gris a menos que todos los campos sean llenados. En tal caso, el botón se volvería verde y se podrá hacerle clic.

A la derecha de la página, debe haber un listado de los reportes más actuales. Debe haber una barra de scroll para poder buscar reportes y un campo de búsqueda donde se pueda buscar un reporte en específico. A la derecha del campo de búsqueda, debe haber un botón de filtrar. Al apretarlo, debe abrir una ventanita donde se puedan seleccionar los filtros, y luego aplicarlos. Los filtros deben estar de acuerdo a la información expuesta en cada ítem del listado. Cada ítem del listado debe incluir información breve del reporte que se asimile a lo de la parte de la izquierda. Debe haber un botón llamado "Visualizar Estadísticas" siempre visible al inferior del listado que siempre pueda recibir una acción.
```

</details>

<details>
    <summary>Respuesta</summary> 

```
Listo, generé la plantilla foro_incidentes.html y su hoja de estilos incidentes.css.

Dónde colocarlos

foro_incidentes.html va en templates/ (por ejemplo incidentes/templates/incidentes/).
incidentes.css va en static/css/, que es la ruta que usa {% static 'css/incidentes.css' %}.

Qué incluye

Izquierda: el formulario con tipo (menú), descripción, fecha y hora (se rellena con la actual) y severidad (menú). El botón “Reportar” está gris y deshabilitado hasta que todos los campos estén llenos. Entonces se pone verde y se puede hacer clic.
Derecha: el listado con barra de scroll, el campo de búsqueda y el botón “Filtrar” a su derecha. Ese botón abre una ventana con filtros por tipo, severidad y rango de fechas, con los botones Aplicar, Limpiar y Cancelar. Cada ítem muestra tipo, severidad, descripción resumida y fecha, que son los mismos datos del formulario.
Abajo del listado: el botón “Visualizar Estadísticas”, siempre visible y habilitado.
La búsqueda y los filtros funcionan en el navegador con JavaScript, sin recargar la página.

Lo que debes conectar en Django

Las URLs reportar_incidente (recibe el POST del formulario) y estadisticas.
Una variable reportes en el contexto de la vista, con objetos que tengan los campos tipo, descripcion, fecha y severidad. Los campos tipo y severidad deben usar choices, porque la plantilla llama a get_tipo_display y get_severidad_display.
Los valores de los menús son seguridad, infraestructura, servicio, accidente y otro para el tipo, y baja, media, alta y critica para la severidad. Cámbialos por los de tu modelo; hay que editarlos tanto en el formulario como en la ventana de filtros.
```

</details>

***

> El único archivo modificado fue `src/apps/reports/templates/reports/index.html` con las indicaciones propuestas.

<details>
    <summary>Prompt</summary>

```
Los filtros aplicados deben luego ser mandados a "generate_stats" a partir de un request GET, por lo que los parámetros deben tener la forma de "generate_stats?kind=...&severity=..."
```

</details>

<details>
    <summary>Respuesta</summary>

```
Para eso hay que hacer que el enlace de “Visualizar Estadísticas” se reconstruya cada vez que cambian los filtros. Así sigue siendo un <a> normal, siempre habilitado, y hace un GET con la URL correcta.

Reemplaza el enlace actual por este (cambia el nombre de la URL de estadisticas a generate_stats):
```

```html
<a href="{% url 'generate_stats' %}"
id="btn-estadisticas"
class="btn-estadisticas"
data-base="{% url 'generate_stats' %}">Visualizar Estadísticas</a>
```

```
Añade esta función dentro del script, junto a aplicar():
```

```js
function actualizarEnlaceStats() {
    const params = new URLSearchParams();
    if (filtros.tipo)      params.set('kind', filtros.tipo);
    if (filtros.severidad) params.set('severity', filtros.severidad);
    if (filtros.desde)     params.set('date_from', filtros.desde);
    if (filtros.hasta)     params.set('date_to', filtros.hasta);

    const q = buscador.value.trim();
    if (q) params.set('q', q);

    const btnStats = document.getElementById('btn-estadisticas');
    const qs = params.toString();
    btnStats.href = btnStats.dataset.base + (qs ? '?' + qs : '');
}
```

```
Y llámala al final de aplicar(), que ya se ejecuta al buscar, al aplicar filtros y al limpiarlos:
```

```js
function aplicar() {
    // ... código existente ...
    actualizarEnlaceStats();
}
```

```
Solo se envían los parámetros que tienen valor. Por ejemplo, con tipo “seguridad” y severidad “alta” el enlace queda:

/generate_stats/?kind=seguridad&severity=alta

Con los filtros vacíos, el enlace es simplemente /generate_stats/.
```

</details>

> [!NOTE]
> _Nótese que la IA añadió el campo `q`, representando el query de búsqueda de la lista de reportes. Este campo no es relevante al momento de generar los modelos estadísticos, por lo que será omitido en la versión final._
