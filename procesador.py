
from fabricas import FabricaEntrada, FabricaSalida, FabricaMixta


def procesar_informes(lista_informes):

    # Asociamos cada categoría con su fábrica
    fabricas = {
        "ENT": FabricaEntrada(),
        "SAL": FabricaSalida(),
        "MIX": FabricaMixta()
    }

    # Procesamos cada archivo de la lista
    for nombre_archivo in lista_informes:

        try:
            # Separamos categoría, tipo y nombre
            partes = nombre_archivo.split("_", 2)

            if len(partes) != 3:
                raise ValueError("Formato de archivo incorrecto")

            categoria = partes[0]
            tipo = partes[1]
            nombre = partes[2]

            # Comprobamos que el archivo sea válido
            if not nombre.endswith(".txt") or nombre == ".txt":
                raise ValueError("El archivo debe tener extensión .txt")

            if categoria not in fabricas:
                raise ValueError("Categoría de informe desconocida")

            fabrica = fabricas[categoria]

            # Creamos el informe según su tipo
            if tipo == "FAC":
                informe = fabrica.crear_factura()

            elif tipo == "COM":
                informe = fabrica.crear_compra()

            elif tipo == "PED":
                if categoria != "ENT":
                    raise ValueError(
                        "PEDIDO solo está disponible para ENTRADA"
                    )
                informe = fabrica.crear_pedido()

            else:
                raise ValueError("Tipo de informe desconocido")

            # Procesamos el informe
            informe.procesar()

        except ValueError as error:
            print(f"Error al procesar {nombre_archivo}: {error}")
