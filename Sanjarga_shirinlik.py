import pygame
import math

pygame.init()
screen = pygame.display.set_mode((901, 622))
display_surface = pygame.display.set_mode((901, 622))
pygame.display.set_caption('Sanjarga shirinlik')
font = pygame.font.SysFont('Arial', 18, bold=False)

x_bosh, y_bosh = 0, 0
def ekr_yozuv(letter, x_bosh, y_bosh):
    text = font.render(str(letter), True, (255, 255, 255))
    display_surface.blit(text, (x_bosh, y_bosh))


x_boluvchi = 10
y_boluvchi = 20
satr = 622 // y_boluvchi
ustun = 901 // x_boluvchi
x_offset = ustun / 2
y_offset = satr / 2
teta_aylanish = 10
fi_aylanish = 3
simvol = ".,-~:;=!*#$@"
ekran_olchami = satr * ustun
kondalang, tik_aylanish = 0, 0

go = True

while go:

    screen.fill((0, 0, 0))
    z = [0] * ekran_olchami
    b = [' '] * ekran_olchami

    for j in range(0, 628, teta_aylanish):
        for i in range(0, 628, fi_aylanish):
            tepada = math.sin(i)
            keyingi_tepada = math.cos(j)
            ortadagi_tepada = math.sin(kondalang)
            ortadan_tepa = math.sin(j)
            ortadan_tepa_chap = math.cos(kondalang)
            ortadan_tepa_ong = keyingi_tepada + 2
            orta_animatsiya = 1 / (tepada * ortadan_tepa_ong * ortadagi_tepada + ortadan_tepa * ortadan_tepa_chap + 5)
            ortadan_tepa_orta = math.cos(i)
            ortadan_tepa_orta_chap = math.cos(tik_aylanish)
            ortadan_tepa_orta_ong = math.sin(tik_aylanish)
            ortadan_orta = tepada * ortadan_tepa_ong * ortadan_tepa_chap - ortadan_tepa * ortadagi_tepada
            ortadan_orta_animatsiya_old = int(x_offset + 40 * orta_animatsiya * (ortadan_tepa_orta * ortadan_tepa_ong * ortadan_tepa_orta_chap - ortadan_orta * ortadan_tepa_orta_ong))
            ortadan_orta_animatsiya_qayta = int(y_offset + 20 * orta_animatsiya * (ortadan_tepa_orta * ortadan_tepa_ong * ortadan_tepa_orta_ong + ortadan_orta * ortadan_tepa_orta_chap))
            burchak_animatsiya = int(ortadan_orta_animatsiya_old + ustun * ortadan_orta_animatsiya_qayta)
            umumiy_animatsiya = int(8 * ((ortadan_tepa * ortadagi_tepada - tepada * keyingi_tepada * ortadan_tepa_chap) * ortadan_tepa_orta_chap - tepada * keyingi_tepada * ortadagi_tepada - ortadan_tepa * ortadan_tepa_chap - ortadan_tepa_orta * keyingi_tepada * ortadan_tepa_orta_ong))
            if satr > ortadan_orta_animatsiya_qayta and ortadan_orta_animatsiya_qayta > 0 and ortadan_orta_animatsiya_old > 0 and ustun > ortadan_orta_animatsiya_old and orta_animatsiya > z[burchak_animatsiya]:
                z[burchak_animatsiya] = orta_animatsiya
                b[burchak_animatsiya] = simvol[umumiy_animatsiya if umumiy_animatsiya > 0 else 0]

    if y_bosh == satr * y_boluvchi - y_boluvchi:
        y_bosh = 0

    for i in range(len(b)):
        kondalang += 0.00005
        tik_aylanish += 0.00004
        if i == 0 or i % ustun:
            ekr_yozuv(b[i], x_bosh, y_bosh)
            x_bosh += x_boluvchi
        else:
            y_bosh += y_boluvchi
            x_bosh = 0
            ekr_yozuv(b[i], x_bosh, y_bosh)
            x_bosh += x_boluvchi

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
