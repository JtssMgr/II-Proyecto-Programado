# Proyecto Programado II: Resolucion de Laberintos
# Curso: IC-1803 - Taller de Programacion
# Profesor: Jose Rodolfo Godinez Solano
# Periodo: I Semestre 2026
# Santiago Escamilla Sanabria


import sys
# indices del jugador (pos actual en el laberinto)
PF, PC = 0, 1  # fila, columna

def leer_laberinto():
    # lee filas, columnas y el mapa desde stdin
    f, c = map(int, input().split())
    mapa = [list(input()) for _ in range(f)]
    return f, c, mapa

def buscar_inicio(mapa, f, c):
    # busca la S en el mapa, retorna (fila, col) o None
    for i in range(f):
        for j in range(c):
            if mapa[i][j] == 'S':
                return (i, j)
    return None

def es_valida(f, c, filas, cols, mapa, visitados):
    # verifica que la celda exista, no sea pared y no haya sido visitada (revisar en pruebas, me da mucho error)
    if f < 0 or f >= filas or c < 0 or c >= cols: return False
    if mapa[f][c] == '#': return False
    if visitados[f][c]: return False
    return True

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

def marcar_camino(mapa, camino):
    # pone * en el camino, sin tocar S ni E
    for f, c in camino:
        if mapa[f][c] != 'S' and mapa[f][c] != 'E':
            mapa[f][c] = '*'

def imprimir(mapa):
    for fila in mapa:
        print(''.join(fila))

def main():
    filas, cols, mapa = leer_laberinto()
    inicio = buscar_inicio(mapa, filas, cols)

    if inicio is None:
        print("No existe solución")
        return

    camino = resolver(mapa, filas, cols, inicio)

    if camino is None:
        print("No existe solución")
    else:
        marcar_camino(mapa, camino)
        imprimir(mapa)
main()
