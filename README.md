# Evaluaci-n-en-Contacto-con-el-Docente
Juego del ahorcado
EVALUACION.png
Instrucciones: 
PROYECTO INTEGRADOR 

Nombre del proyecto (JUEGO DEL AHORCADO): 
 
Realizado por DIEGO CÓRDOVA

Objetivo del sistema

El objetivo del sistema (el programa o software) en un juego del ahorcado temático de Python es gestionar la lógica del juego de forma automática, evaluando el progreso del usuario y reforzando conceptos clave de programación mediante la interacción.

descripcion de funcionalidades

Para que el sistema del juego del ahorcado funcione correctamente, debe cumplir con una serie de tareas automatizadas. A continuación, se describen las funcionalidades clave del sistema, detallando cómo se aplican las variables, condicionales y listas en cada una:

1. Inicialización del Juego
El sistema debe preparar el entorno antes de que el usuario empiece a jugar.

Selección aleatoria: El sistema elige una palabra al azar de una lista de conceptos de Python (ej. ["bucle", "funcion", "booleano"]).

Configuración del estado: Se inicializan las variables de control: el número de intentos (generalmente 6) y una lista de guiones bajos (['_', '_', '_', '_']) que representa la palabra oculta.

2. Captura y Validación de la Entrada del Usuario
El sistema recibe la letra que el jugador escribe y asegura que sea válida.

Control de errores: Usa condicionales (if) para verificar que el usuario haya ingresado exactamente una letra y que no sea un número o un carácter especial.

Evitar duplicados: El sistema revisa si la letra ya existe en la lista de letras intentadas para avisar al jugador y no penalizarlo doblemente.

3. Evaluación de la Letra (Lógica del Juego)
Esta es la funcionalidad central donde el sistema decide qué pasa con la jugada.

Caso de Acierto: Si (if) la letra está en la palabra secreta, el sistema recorre la palabra y reemplaza los guiones bajos (_) en las posiciones (índices) correctas dentro de la lista de progreso.

Caso de Error: Si no (else) está en la palabra, el sistema reduce en 1 la variable de intentos_restantes y añade la letra a una lista de "letras incorrectas" para mostrársela al usuario.

4. Actualización del Estado Visual (Interfaz en Consola)
El sistema refresca la pantalla en cada turno para mostrar los avances.

Dibujo del progreso: Muestra la lista de la palabra oculta convertida en texto legible (ej: v _ r _ _ b l e).

Estadísticas actuales: Muestra el valor de la variable de intentos disponibles y el monigote del ahorcado correspondiente al número de fallos.

5. Verificación del Fin de la Partida
Después de cada intento, el sistema evalúa si el juego debe continuar o terminar mediante condicionales:

Condición de Victoria: Si ya no quedan guiones bajos (_) en la lista de progreso, el sistema detiene el juego y muestra un mensaje de felicitación.

Condición de Derrota: Si la variable intentos_restantes llega a 0, el sistema detiene el bucle, dibuja el ahorcado completo y revela la palabra secreta que el usuario no pudo adivinar.

Fecha de Entrega 28-06-2026


