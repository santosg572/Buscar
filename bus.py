from serpapi import GoogleSearch

params = {
    "q": "cursos de python",       # Tu término de búsqueda
    "location": "Mexico",          # Ubicación
    "api_key": "TU_API_KEY"        # Tu clave secreta
}

search = GoogleSearch(params)
results = search.get_dict()


