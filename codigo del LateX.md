\documentclass[12pt]{article}

\usepackage{xcolor}
\usepackage[svgnames]{xcolor}
\usepackage[margin=1in]{geometry}
\usepackage{setspace}\doublespacing
\usepackage[spanish]{babel}
\usepackage[utf8]{inputenc}
\usepackage{indentfirst}
\usepackage{ragged2e}
\usepackage{listings}
\usepackage{amsmath}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{backcolour}{rgb}{0.97,0.97,0.97}
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{codegray},
    basicstyle=\ttfamily\footnotesize,
    breaklines=true,
    numbers=left,
    numbersep=5pt,
    language=Python
}
\lstset{style=mystyle}

\title{\textbf{Proyecto Programado II: Resolución de Laberintos} \\
\large Instituto Tecnológico de Costa Rica \\
\large Sede Interuniversitaria de Alajuela}
\author{Santiago Escamilla Sanabria}
\date{29/05/2026}

\begin{document}

\maketitle

% ============================================================
\newpage
\RaggedRight
\textcolor{black!40!blue}{\section*{Resumen Ejecutivo}}

\hspace{0.5cm} Este proyecto es un programa en Python que resuelve laberintos dados como matrices de texto. La idea es encontrar un camino desde el punto de inicio hasta el punto final usando backtracking con una pila, retrocediendo cada vez que se llega a un callejón sin salida.
\newline\hspace{0.5cm} El programa lee el laberinto desde la entrada, encuentra el camino (si existe) y lo marcas. Si no hay ningun camino posible simplemente dice que no existe solución. Lo probé con 5 casos distintos y todos funcionaron..

% ============================================================
\newpage
\textcolor{black!40!green}{\section*{Introducción}}

\hspace{0.5cm} Resolver un laberinto es basicamente encontrar una ruta entre dos puntos evitando obstáculos, usando búsqueda exhaustiva y backtracking para llegar a la meta (objetivo).
\newline\hspace{0.5cm} El objetivo de este proyecto es implementar ese algoritmo en Python, recibiendo el laberinto como una matriz de caracteres y devolviendo el camino encontrado marcado con asteriscos, o indicando que no existe solución si es el caso.

% ============================================================
\newpage
\textcolor{Gold}{\section*{Marco Teórico}}

\textcolor{Sienna}{\subsection*{Matrices}}
Una matriz es una estructura de datos organizada en filas y columnas. En este proyecto el laberinto es una lista de listas en Python, donde cada celda tiene un caracter que indica si es espacio libre, pared, inicio o fin.

\textcolor{Sienna}{\subsection*{Pilas}}
Una pila es una estructura en el que el último en entrar es el primero en salir. En Python se puede simular con una lista normal usando append para agregar elementos y pop para sacarlos. Acá la use para guardar las celdas que faltan por explorar junto con el camino recorrido hasta ese punto.

\textcolor{Sienna}{\subsection*{Backtracking}}
El backtracking es una tecnica que consiste en explorar todas las posibilidades de forma ordenada, y cuando un camino no lleva a ningún lado simplemente se abandona y se vuelve atrás. En el caso del laberinto ese retroceso ocurre de forma automática cuando se hace pop de la pila, ya que eso nos devuelve a la celda anterior que todavía tenía opciones sin explorar.
\newpage
\textcolor{Sienna}{\subsection*{Búsqueda Exhaustiva}}
La búsqueda exhaustiva recorre todos los caminos posibles hasta encontrar la solución o que no existe ninguna. Usando una la matriz de visitados, intenta que ninguna celda se procese muchas veces lo que da una complejidad de $O(F \times C)$ donde F es el número de filas y C el de columnas.

% ============================================================
\newpage
\textcolor{DarkOrchid}{\section*{Descripción de la Solución}}

\hspace{0.5cm} El programa lo dividí en funciones pequeñas donde cada una hace una cosa. Hay funciones para leer el laberinto, buscar el inicio, verificar si una celda es valida, resolver el laberinto con backtracking, marcar el camino encontrado y imprimirlo. La función main es la principal.
\newline\hspace{0.5cm} El algoritmo principal crea una matriz de visitados para no repetir celdas, luego mete el punto de inicio en la pila y empieza a explorar. En cada iteración saca la celda del tope de la pila, revisa si es el destino, y si no, agrega a la pila todos los vecinos validos con el camino actualizado. Si la pila se vacia sin haber encontrado el destino, significa que no hay solución.

\begin{lstlisting}[caption={Función principal de backtracking}] 

def resolver(mapa, filas, cols, inicio):
    # backtracking con pila y los 4 movimientos posibles
    # si llega a donde no pueda seguir, retrocede automaticamente al hacer pop
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # arriba, abajo, izq, der
    visitados = [[False] * cols for _ in range(filas)]

    # cada elemento de la pil
    pila = [(inicio[0], inicio[1], [inicio])]
    visitados[inicio[0]][inicio[1]] = True

    while pila:
        f, c, camino = pila.pop()  #si no hay saliday volver hasta atras

        if mapa[f][c] == 'E':
            return camino  #para encontrar el fin

        for df, dc in dirs:
            nf, nc = f + df, c + dc
            if es_valida(nf, nc, filas, cols, mapa, visitados):
                visitados[nf][nc] = True
                pila.append((nf, nc, camino + [(nf, nc)]))

    return None  # pila vacia por si no hay solucion
    # Agradecimientos a un compa que me ayudo a hacer esto 
\end{lstlisting}

% ============================================================
\newpage
\textcolor{FireBrick}{\section*{Resultados de Pruebas}}

% cinco casos cubriendo todo lo que pide el enunciado

\textcolor{Sienna}{\subsection*{Prueba 1 --- Camino directo}}
Entrada:
\begin{verbatim}
3 5
S...E
#####
.....
\end{verbatim}
Salida :
\begin{verbatim}
S***E
#####
.....
\end{verbatim}
El camino es directo en la primera fila y el algoritmo lo encontró sin necesidad de retroceder.

\textcolor{Sienna}{\subsection*{Prueba 2 --- Sin solución}}
Entrada:
\begin{verbatim}
3 3
S.#
###
#.E
\end{verbatim}
Salida:
\begin{verbatim}
No existe solución
\end{verbatim}
Las paredes bloquean completamente el paso entre S y E, la pila se vacia sin encontrar el destino.

\textcolor{Sienna}{\subsection*{Prueba 3 --- Camino con retrocesos}}
Entrada:
\begin{verbatim}
5 5
S.#..
.####
.....
####.
....E
\end{verbatim}
Salida:
\begin{verbatim}
S.#..
*####
*****
####*
....E
\end{verbatim}
Acá el algoritmo tuvo que explorar hacia abajo y serpentear por el laberinto, demostrando el retroceso cuando intentaba caminos sin salida.

\textcolor{Sienna}{\subsection*{Prueba 4 --- Laberinto grande}}
Entrada:
\begin{verbatim}
8 10
S.........
.########.
..........
.########.
..........
.########.
..........
.........E
\end{verbatim}
Salida:
\begin{verbatim}
S*********
.########*
**********
*########.
**********
.########*
.........*
.........E
\end{verbatim}
Sirve para verificar que el programa funciona bien con laberintos mas grandes y no se cae.

\textcolor{Sienna}{\subsection*{Prueba 5 --- Múltiples caminos}}
Entrada:
\begin{verbatim}
4 6
S....E
......
......
......
\end{verbatim}
Salida:
\begin{verbatim}
S****E
......
......
......
\end{verbatim}
Hay muchos caminos posibles en este caso. El algoritmo elige el camino directo por la primera fila dependiendo del orden en que la pila explora las direcciones.

% ============================================================
\newpage
\textcolor{PaleVioletRed}{\section*{Conclusiones}}

\begin{itemize}
    \item El backtracking con pila es una forma limpia de resolver este tipo de problemas porque el retroceso ocurre solo con el pop, sin nada más.
    \item La matriz de visitados es esencial para que el algoritmo no entre en ciclos y sea eficiente.
    \item El programa maneja bien todos los casos que se piden, con solución, sin solución, caminos largos, laberintos grandes y múltiples caminos posibles.
    \item La complejidad es $O(F \times C)$ en el peor caso ya que cada celda se visita a lo sumo una vez.
\end{itemize}

% ============================================================
\newpage
\textcolor{orange}{\section*{Aprendizajes}}

\begin{itemize}
    \item Aprendí a implementar backtracking de forma iterativa con pila en vez de recursión.
    \item Me di cuenta que es mejor usar funciones aux.
    \item Empece a usar casos de prueba que cubran todos (o casi todos) los escenarios posibles.
\end{itemize}

\end{document}
