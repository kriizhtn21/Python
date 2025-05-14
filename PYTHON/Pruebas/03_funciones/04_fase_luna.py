#cristiano

def fase_lunar(fase):
    """
    devuelve el emoji correspondiente a la fase lunar
    """
    if fase == "nueva":
        return "🌑"
    elif fase == "creciente":
        return "🌒"
    elif fase == "llena":
        return "🌕"
    elif fase == "menguante":
        return "🌖"
    else:
        return "Fase lunar no válida"
    
# Ejemplo de uso
respuesta = fase_lunar("llena")
print(respuesta)
