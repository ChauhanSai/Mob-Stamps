from PIL import Image

def colorAvg(a,b):
  ar, ag, ab, ax = a
  br, bg, bb, bx = b
  r = round((ar+br)/2)
  g = round((ag+bg)/2)
  b = round((ab+bb)/2)
  string=str(r)
  string+=', '
  string+=str(g)
  string+=', '
  string+=str(b)
  string+=', 255'
  return eval(string)

mobs = ['axolotl.png', 'bat.png', 'bee.png', 'blaze.png', 'rabbit.png', 'cat.png', 'cave_spider.png', 'chicken.png', 'clownfish.png', 'cod.png', 'cow.png', 'creeper.png', 'dolphin.png', 'donkey.png', 'drowned.png', 'enderman.png', 'evoker.png', 'fox.png', 'ghast.png', 'glow_squid.png', 'goat.png', 'hoglin.png', 'horse.png', 'husk.png', 'iron_golem.png', 'llama.png', 'magmacube.png', 'mooshroom.png', 'mule.png', 'ocelot.png', 'panda.png', 'parrot_green.png', 'phantom.png', 'pig.png', 'piglin.png', 'pillager.png', 'polarbear.png', 'pufferfish.png', 'ravager.png', 'salmon.png', 'sea_turtle.png', 'sheep.png', 'shulker.png', 'skeleton.png', 'slime.png', 'snow_golem.png', 'spider.png', 'squid.png', 'stray.png', 'strider.png', 'vex.png', 'vindicator.png', 'witch.png', 'wither_skeleton.png', 'wolf.png', 'zombie.png']

for i in range(len(mobs)):
  mob=mobs[i]
  print(mob)
  
  mobTexture='entity/'
  mobTexture+=mob
  mobImage = Image.open(mobTexture, 'r')
  mobIm = mobImage.load()

  width, height = mobImage.size

  a = (255,255,255,255)
  e = (0,0,0,0)

  for y in range(height):
    for x in range(width):
      pixel = mobIm[x,y]
      if e < pixel:
        ea, eb, ec, ex = pixel
        if ea > 235 and eb > 235 and ec > 235 or ex == 0:
          pass
        else:
          e = mobIm[x,y]
      if a > pixel:
        aa, ab, ac, ax = pixel
        if aa < 20 and ab < 20 and ac < 20 or ax == 0:
          pass
        else:
          a = mobIm[x,y]

  y = list(a)
  y[3] = 255
  a = tuple(y)
  
  y = list(e)
  y[3] = 255
  e = tuple(y)
  
  c = colorAvg(a,e)
  b = colorAvg(a,c)
  d = colorAvg(c,e)

  stampName='items/stamp_'
  stampName+=mob
  stampImage = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
  stampIm = stampImage.load()
  stampTemplate = Image.open('stamp_empty.png')
  stampTemplate = stampTemplate.load()

  for y in range(16):
    for x in range(16):
      stampIm[x,y] = stampTemplate[x,y]

  stampIm[5,4] = b
  stampIm[6,4] = b
  stampIm[7,4] = b
  stampIm[8,4] = b
  stampIm[9,4] = b
  stampIm[10,4] = b
  stampIm[5,5] = b
  stampIm[6,5] = b
  stampIm[7,5] = b
  stampIm[8,5] = b
  stampIm[9,5] = b
  stampIm[10,5] = b
  stampIm[5,6] = b
  stampIm[6,6] = c
  stampIm[7,6] = c
  stampIm[8,6] = b
  stampIm[9,6] = b
  stampIm[10,6] = b
  stampIm[5,7] = c
  stampIm[6,7] = c
  stampIm[7,7] = c
  stampIm[8,7] = c
  stampIm[9,7] = c
  stampIm[10,7] = c
  stampIm[5,8] = c
  stampIm[6,8] = d
  stampIm[7,8] = d
  stampIm[8,8] = d
  stampIm[9,8] = d
  stampIm[10,8] = c
  stampIm[5,9] = d
  stampIm[6,9] = d
  stampIm[7,9] = d
  stampIm[8,9] = d
  stampIm[9,9] = d
  stampIm[10,9] = d
  stampIm[5,10] = e
  stampIm[6,10] = e
  stampIm[7,10] = e
  stampIm[8,10] = e
  stampIm[9,10] = d
  stampIm[10,10] = d
  ##stampIm[5,11] = e
  stampIm[6,11] = e
  stampIm[7,11] = e
  stampIm[8,11] = e
  stampIm[9,11] = e
  ##stampIm[10,11] = e
  
  stampImage.save(stampName)

  inkName='items/ink_bottle_'
  inkName+=mob
  inkImage = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
  inkIm = inkImage.load()
  inkTemplate = Image.open('ink_bottle.png')
  inkTemplate = inkTemplate.load()

  for y in range(16):
    for x in range(16):
      inkIm[x,y] = inkTemplate[x,y]

  inkIm[8,11] = a
  inkIm[8,12] = b
  inkIm[8,10] = b
  inkIm[9,8] = c
  inkIm[9,9] = c
  inkIm[9,10] = c
  inkIm[8,9] = c
  inkIm[9,12] = c
  inkIm[7,10] = c
  inkIm[7,11] = c
  inkIm[7,12] = c
  inkIm[5,10] = c
  inkIm[5,11] = c
  inkIm[5,12] = c
  inkIm[10,11] = d
  inkIm[10,12] = d
  inkIm[8,8] = d
  inkIm[7,8] = d
  inkIm[6,10] = d
  inkIm[6,9] = d
  inkIm[6,8] = e
  inkIm[6,12] = e
  inkIm[6,11] = e
  inkIm[10,10] = e
  
  inkImage.save(inkName)

  coinName='items/coin_'
  coinName+=mob
  coinImage = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
  coinIm = coinImage.load()
  coinTemplate = Image.open('coin_empty.png')
  coinTemplate = coinTemplate.load()

  for y in range(16):
    for x in range(16):
      coinIm[x,y] = coinTemplate[x,y]

  coinIm[6,4] = b
  coinIm[7,4] = b
  coinIm[8,4] = b
  coinIm[9,4] = b
  coinIm[5,5] = b
  coinIm[6,5] = b
  coinIm[7,5] = b
  coinIm[8,5] = b
  coinIm[9,5] = b
  coinIm[10,5] = b
  coinIm[4,6] = b
  coinIm[5,6] = b
  coinIm[10,6] = b
  coinIm[11,6] = b
  coinIm[6,6] = c
  coinIm[7,6] = c
  coinIm[8,6] = c
  coinIm[9,6] = c
  coinIm[4,7] = c
  coinIm[5,7] = c
  coinIm[6,7] = c
  coinIm[7,7] = c
  coinIm[8,7] = c
  coinIm[9,7] = c
  coinIm[10,7] = c
  coinIm[11,7] = c
  coinIm[4,8] = c
  coinIm[5,8] = c
  coinIm[7,8] = c
  coinIm[6,8] = d
  coinIm[8,8] = d
  coinIm[9,8] = d
  coinIm[10,8] = d
  coinIm[11,8] = d
  coinIm[4,9] = d
  coinIm[5,9] = d
  coinIm[6,9] = d
  coinIm[7,9] = d
  coinIm[8,9] = d
  coinIm[9,9] = d
  coinIm[10,9] = d
  coinIm[11,9] = d
  coinIm[5,10] = d
  coinIm[6,10] = e
  coinIm[7,10] = e
  coinIm[8,10] = e
  coinIm[9,10] = e
  coinIm[10,10] = e
  coinIm[6,11] = e
  coinIm[7,11] = e
  coinIm[8,11] = e
  coinIm[9,11] = e
  
  coinImage.save(coinName)
  
  print('Successfully wrote',stampName,',',inkName,'&',coinName)
  print()
