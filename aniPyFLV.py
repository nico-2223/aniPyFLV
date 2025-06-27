import subprocess
import sys
import os
import tempfile
from animeflv import AnimeFLV

def stream_with_megadl(url):
    print(f"Descargando episodio desde Mega con megadl...")
    try:
        # Crear un directorio temporal para la descarga
        with tempfile.TemporaryDirectory() as tempdir:
            # Cambiar el directorio actual para descargar ahí
            subprocess.run(["megadl", url], check=True, cwd=tempdir)

            # Listar archivos en tempdir (debería ser solo el descargado)
            archivos = os.listdir(tempdir)
            if not archivos:
                print("No se encontró el archivo descargado.")
                sys.exit(1)

            archivo_descargado = os.path.join(tempdir, archivos[0])
            print(f"Descarga completada: {archivo_descargado}")

            print(f"Abriendo el episodio con mpv...")
            subprocess.run(["mpv", archivo_descargado], check=True)

    except FileNotFoundError as e:
        print(f"Error: No se encontró el comando: {e.filename}. Instala megatools para usar 'megadl'.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Error durante la descarga o reproducción.")
        sys.exit(1)


def seleccionar_episodio(episodios, titulo_serie):
    print(f"\nEpisodios de {titulo_serie}:\n")
    for i, ep in enumerate(episodios):
        print(f"{i} - Episodio {ep.id}")

    while True:
        try:
            seleccion = int(input("\nSelecciona el número de episodio: "))
            if 0 <= seleccion < len(episodios):
                return seleccion
            else:
                print(f"Por favor elige un número entre 0 y {len(episodios)-1}")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


def main():
    try:
        api = AnimeFLV()
        query = input("Nombre del anime: ").strip()
        resultados = api.search(query)

        if not resultados:
            print("No se encontraron resultados.")
            sys.exit(0)

        if len(resultados) > 1:
            print("\nResultados encontrados:")
            for i, r in enumerate(resultados):
                print(f"{i} - {r.title}")
            while True:
                try:
                    seleccion = int(input("\nSelecciona el número de la serie: "))
                    if 0 <= seleccion < len(resultados):
                        break
                except ValueError:
                    pass
        else:
            seleccion = 0

        anime = resultados[seleccion]
        info = api.get_anime_info(anime.id)
        info.episodes.reverse()

        index = seleccionar_episodio(info.episodes, anime.title)
        capitulo = info.episodes[index].id

        enlaces = api.get_links(anime.id, capitulo)
        if not enlaces:
            print("No se encontraron enlaces para este episodio.")
            sys.exit(0)

        mega_link = next((e for e in enlaces if e.server.lower() == "mega"), None)
        if not mega_link:
            print("Este episodio no tiene enlace Mega disponible para descarga.")
            sys.exit(0)

        stream_with_megadl(mega_link.url)

    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
