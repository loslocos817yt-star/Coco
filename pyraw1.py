import re
import sys
import subprocess
import os

# Diccionario de traducción de PyRaw
REEMPLAZOS = {
    r'\bimprimir\b': 'print',
    r'\bsi\b': 'if',
    r'\bsino_si\b': 'elif',
    r'\bsino\b': 'else',
    r'\bmientras\b': 'while',
    r'\bpara\b': 'for',
    r'\ben\b': 'in',
    r'\bfuncion\b': 'def',
    r'\bretornar\b': 'return',
    r'\bclase\b': 'class',
    r'\bimportar\b': 'import',
    r'\bdesde\b': 'from',
    r'\bcomo\b': 'as',
    r'\bintentar\b': 'try',
    r'\bexcepto\b': 'except',
    r'\bfinalmente\b': 'finally',
    r'\bcon\b': 'with',
    r'\bromper\b': 'break',
    r'\bcontinuar\b': 'continue',
    r'\bpasar\b': 'pass',
    r'\bVerdadero\b': 'True',
    r'\bFalso\b': 'False',
    r'\bNada\b': 'None',
    r'\by\b': 'and',
    r'\bo\b': 'or',
    r'\bno\b': 'not',
    r'\brango\b': 'range'
}

def mini_nano(archivo):
    print(f"\n--- Editando: {archivo} ---")
    print("(Escribe 'GUARDAR' en una línea vacía para finalizar)")
    lineas = []
    while True:
        linea = input("> ")
        if linea.strip() == "GUARDAR":
            break
        lineas.append(linea)
    
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))
    print(f"Archivo '{archivo}' guardado con éxito.\n")

def traducir_codigo(codigo):
    for patron, reemplazo in REEMPLAZOS.items():
        codigo = re.sub(patron, reemplazo, codigo)
    return codigo

def ejecutar_pyraw(archivo):
    if not os.path.exists(archivo):
        print(f"Error PyRaw: No existe el archivo '{archivo}'")
        return

    archivo_temp = "__pyraw_temp__.py"
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            codigo = f.read()

        codigo_traducido = traducir_codigo(codigo)

        with open(archivo_temp, "w", encoding="utf-8") as f:
            f.write(codigo_traducido)

        subprocess.run([sys.executable, archivo_temp])
    
    except Exception as e:
        print(f"Error de ejecución: {e}")
    finally:
        if os.path.exists(archivo_temp):
            os.remove(archivo_temp)

def main():
    print("=== PyRaw Console 1.0 ===")
    print("por el PattitexTEC")
    
    while True:
        ruta_actual = os.getcwd()
        entrada = input(f"PyRaw@{ruta_actual} $ ").strip()

        if not entrada:
            continue
        
        cmd = entrada.lower()

        # Comandos básicos
        if cmd in ['salir', 'exit']:
            break
        elif cmd in ['ls', 'dir']:
            print("  \n".join(os.listdir('.')))
            continue

        # Lógica de CD
        if cmd.startswith("cd "):
            destino = entrada[3:].strip()
            try:
                os.chdir(destino)
            except Exception as e:
                print(f"Error: {e}")
            continue

        # Lógica de NANO (Editor)
        if cmd.startswith("nano "):
            archivo_a_editar = entrada[5:].strip()
            mini_nano(archivo_a_editar)
            continue

        # Ejecutar archivo
        ejecutar_pyraw(entrada)

if __name__ == "__main__":
    main()

