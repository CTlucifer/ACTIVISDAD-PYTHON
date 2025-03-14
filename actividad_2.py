# Definimos el perfil del usuario con datos anidados

# Definimos el perfil del usuario con datos anidados

perfil = {
    "nombre": "Sebastián",
    "edad": 18,
    "ciudad": "Barcelona",
    
    "amigos": [
        {"nombre": "Carlos", "tiempo_amistad": "2 años"},
        {"nombre": "Lucía", "tiempo_amistad": "1 año"},
        {"nombre": "Andrés", "tiempo_amistad": "6 meses"}
    ],
    
    "posts": [
        {
            "contenido": "¡Disfrutando de un gran día!",
            "likes": 25,
            "comentarios": ["¡Genial!", "Disfruta"]
        },
        {
            "contenido": "Nuevo proyecto en marcha",
            "likes": 40,
            "comentarios": ["¡Mucha suerte!", "Suena interesante"]
        }
    ]
}

# Agregar un nuevo post

nuevo_post = {
    "contenido": "Probando mi nuevo código en Python",
    "likes": 10,
    "comentarios": ["¡Qué bueno!", "Enséñanos"]
}

perfil["posts"].append(nuevo_post)

# Modificar la ciudad del usuario a "Madrid"

perfil["ciudad"] = "Madrid"

# Eliminar el segundo amigo de la lista usando .remove()

amigo_a_eliminar = perfil["amigos"][1]
perfil["amigos"].remove(amigo_a_eliminar)

# Imprimir el perfil actualizado

print(perfil)
