#perfil de usuario con añadidos
perfil = {
    "nombre": "sergio", 
    "edad": "19", 
    "ciudad": "medellin",
    "amigos": [
        {"nombre": "andres", "tiempo_amistad": "2años"},
        {"nombre": "julio", "tiempo_amistad": "8 meses"},
        {"nombre": "mauricio", "tiempo_amistad": "3 año"}
        
    ],
    "posts": [
        {"contenido": "disfrutando del dia", "likes": 28, "comentarios": ["buen dia", "no tan bueno"]},
        {"contenido": "nuevo integrane de la familia", "likes": 40, "comentarios": ["que lindo", "que raza es el perro?"]},
       
        
    ] # type: ignore
}
#agregar un nuevo posts

nuevo_post = {
    "contenido": "un dia de salida", "likes": 39, "comentarios": ["que ricooo ", "nombre del retaurante?"]
}
perfil["posts"].append(nuevo_post)

#modificar la ciudad del usuario

perfil["ciudad"] = "Madrid"

#eliminar un amigo de la lista (indice 1)

amigo_a_eliminar = perfil["amigos"][1]
perfil["amigos"].remove(amigo_a_eliminar)

# Imprimir el perfil actualizado con saltos de línea
print("Perfil del usuario:\n")
print(f"Nombre: {perfil['nombre']}")
print(f"Edad: {perfil['edad']}")
print(f"Ciudad: {perfil['ciudad']}\n")

print("Amigos:")
for amigo in perfil["amigos"]:
    print(f"- {amigo['nombre']} (Tiempo de amistad: {amigo['tiempo_amistad']})")
print()

print("Posts:")
for post in perfil["posts"]:
    print(f"- Contenido: {post['contenido']}")
    print(f"  Likes: {post['likes']}")
    print("  Comentarios:")
    for comentario in post["comentarios"]:
        print(f"    - {comentario}")
    print()

