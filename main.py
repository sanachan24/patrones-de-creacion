from procesador import procesar_informes

# Lista de informes que se van a procesar
informes = [
    "ENT_FAC_001.txt",
    "ENT_COM_001.txt",
    "ENT_PED_001.txt",
    "SAL_FAC_001.txt",
    "SAL_COM_001.txt",
    "MIX_FAC_001.txt",
    "MIX_COM_001.txt"
]

# Ejecutamos el procesamiento
procesar_informes(informes)