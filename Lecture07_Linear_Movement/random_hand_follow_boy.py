from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')


alive =True

while alive:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    character.draw(500, 500)
    hand.draw(400,400)

    
    update_canvas()
    handle_events()


    delay(2)





close_canvas()
