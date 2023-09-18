from PIL import Image

imgs = []
imgs.append(Image.open("../imageset/100년묵은탑셰프/origin/01.jpeg"))
imgs.append(Image.open("../imageset/100년묵은탑셰프/origin/02.jpeg"))
imgs.append(Image.open("../imageset/100년묵은탑셰프/case/01.jpeg"))
imgs.append(Image.open("../imageset/100년묵은탑셰프/case/02.jpeg"))
imgs.append(Image.open("../imageset/아카데미에위장취업당했다/origin/01.jpeg"))
imgs.append(Image.open("../imageset/어느날공주가되어버렸다/origin/01.jpeg"))

default_width = 500
for i,img in enumerate(imgs):
    img = img.resize((default_width , int(img.size[1]*default_width/img.size[0])))
    print(img.size)
    img.save(f"../imageset/100년묵은탑셰프/resize/{i}.jpeg")
    #img.show()

