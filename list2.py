import wrap
import random

sprites=[]

width=700
heith=500
wrap.world.create_world(width,heith)

mar= wrap.sprite.add("mario-1-big",width/2,heith/2,"walk1")
arm= wrap.sprite.add("mario-enemies",width/2,heith/2,"armadillo_go")
cloud= wrap.sprite.add("mario-enemies",width/2,heith/2,"cloud")
crab= wrap.sprite.add("mario-enemies",width/2,heith/2,"crab")
plant= wrap.sprite.add("mario-enemies",width/2,heith/2,"plant_blue")

sprites.append(mar)
sprites.append(arm)
sprites.append(cloud)
sprites.append(crab)
sprites.append(plant)
print(sprites)

for hi in sprites:
    x= random.randint(100,300)
    y= random.randint(100,400)
    wrap.sprite.move_to(hi,x,y)
    s_width=random.randint(20,50)
    s_heith = random.randint(20, 50)
    wrap.sprite.set_size(hi,s_width,s_heith)

