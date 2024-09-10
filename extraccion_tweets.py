import twint

# Configuración de búsqueda
c = twint.Config()
c.Username = "nombre_de_usuario"  # Especifica el usuario de Twitter (opcional)
c.Search = "palabra clave"        # Especifica la palabra clave que deseas buscar
c.Lang = "es"                     # Idioma (ejemplo: español)
c.Limit = 100                     # Número de tweets a extraer
c.Since = "2024-01-01"            # Fecha desde
c.Until = "2024-09-01"            # Fecha hasta
c.Store_csv = True                # Guardar resultados en un archivo CSV
c.Output = "tweets.csv"           # Nombre del archivo de salida

# Ejecutar la búsqueda
twint.run.Search(c)
