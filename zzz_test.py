import random
#print(random.choice((1,-1)))

r1=[1,2,3,4 ] #(x, y, largeur, hauteur)
r2=[3,2,3,4]
if not r1[0] + r1[2] <= r2[0] or r1[0] >= r2[0] + r2[2] or r1[1] + r1[3] <= r2[1] or r1[1] >= r2[1] + r2[3]:
    print("colision")
else:
    print("pas de collision")



# def choose_platform_type(green_probability, blue_probability, spring_probability):
#     nbr_aleatoire=random.random()
#     if nbr_aleatoire < green_probability:
#         return "green"
#     nbr_aleatoire-=green_probability
#     if nbr_aleatoire < blue_probability:
#         return "blue"
#     nbr_aleatoire-= blue_probability
#     if nbr_aleatoire < spring_probability:
#         return "spring"
    
#     return "brown"
# print(choose_platform_type(0.65,0.15,0.10))
# ech=[]
# for i in range (10000):
#    type_de_platforme=choose_platform_type(0.65,0.15,0.10) 
#    ech.append(type_de_platforme)
# print("green", (ech.count("green")/ len(ech)))
# print("blue", (ech.count("blue")/ len(ech)))
# print("spring", (ech.count("spring")/ len(ech)))
# print("brown", (ech.count("brown")/ len(ech)))
   
