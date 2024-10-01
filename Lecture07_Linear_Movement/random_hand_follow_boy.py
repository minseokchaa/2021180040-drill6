from pico2d import*
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def draw_boy(xc, yc, xy, yy):
    #현재 위치랑 hand위치를 이용해 직선의 방정식을 만들고 x,y 좌표 이동
    
    
    if xc > xh:         #오른쪽                            x값이 줄어들면 왼쪽 애니메이션, x값이 커지면 오른쪽 애니메이션
        character.clip_draw(frame * 100, 100, 100, 100, xc, yc)
        run = 1
    elif xc < xh :      #왼쪽
        character.clip_draw(frame * 100, 0, 100, 100, xc, yc)
        run =2
                                
    #x값이 그대로면 바뀌지 않음       
    if xc == xh and run == 1:         #오른쪽                            
        character.clip_draw(frame * 100, 100, 100, 100, xc, yc)
        run = 1
    elif xc == xh and run == 2 :      #왼쪽
        character.clip_draw(frame * 100, 0, 100, 100, xc, yc)
        run = 2



    if xc == xh and yc == yh:           #hand 위치에 도달하면 hand상태 바뀜 -> hand_on = 0
        hand_on = 0
    pass


def draw_hand(xh, yh):
    
     #hand_on == 1 일 때, 랜덤위치에 손을 표시 hand_on == 0 이면 위치 이동
    global hand_on

    if hand_on == 1:
             
        hand.draw(xh, yh)
        
    if hand_on == 0:
        x1, y1 = random.randrange(0,1280), random.randrange(0,1024)
        hand_on =1
    
    pass


alive =True
frame = 0
run = 1
hand_on = 1


xh, yh = random.randrange(0,1280), random.randrange(0,1024)   #손 위치

xc, yc = TUK_WIDTH // 2, TUK_HEIGHT//2                      #캐릭터 위치

while alive:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)

    
    
    #draw_boy(xc, yc, xh,xh)
    
    draw_hand(xh, yh)
    
    update_canvas()

    frame = (frame + 1)%8
    delay(0.05)


close_canvas()
