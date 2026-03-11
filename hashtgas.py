post_a = ["#python","#programacion","#ia","#python","#infotec"]
post_b = ["#infotec","#tecnologia","#desarrollo","#ia","#ia"]

tags_a = set(post_a)
tags_b = set(post_b)

print(tags_a)
print(tags_b)

interseccion = tags_a & tags_b #.intersection()
union = tags_a.union(tags_b)

print("Union:", union) 

print(interseccion)

#---
union = tags_a.union(tags_b)
inter = tags_a.intersection(tags_b)


print("Union:", union)
print("|:", tags_a | tags_b)

print("Intersección:", inter)
print("&:", tags_a & tags_b)