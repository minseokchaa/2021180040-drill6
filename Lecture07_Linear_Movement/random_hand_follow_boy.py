from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def draw_boy():\
    #현재 위치랑 hand위치를 이용해 직선의 방정식을 만들고 x,y 좌표 이동
    #hand 위치에 도달하면 hand위치 바뀜 -> hand_on = 1
    #x값이 줄어들면 왼쪽 애니메이션, x값이 커지면 오른쪽 애니메이션
    #x값이 그대로면 바뀌지 않음
    pass


def draw_hand():
     #hand_on = 0, 랜덤위치에 손을 표시 
     #hand 위치에 도달하면-> hand_on = 1
     #hand_on = 1 일 때, 랜덤위치에 손을 표시, hand_on = 0
    pass


alive =True

while alive:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)

    
    character.draw(500, 500)
    draw_boy()
    
    hand.draw(400,400)
    draw_hand()
    
    update_canvas()

    frame = (frame + 1)%8
    delay(0.15)


close_canvas()
