import forca
print('s vc joga forca\nn vc sai')
forca.msg('Menu')
d = input('Quer jogar? ')
if 's' == d:
	forca.msg('Bem vindo ao jogo da forca')
	forca.jogar()
forca.msg('Fim de jogo')
