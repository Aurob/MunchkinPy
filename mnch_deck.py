import cv2
def show(title, im):
        cv2.imshow(title, im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def sliceim(file, w, h, i):
    img = cv2.imread(file) 
    x1,y1 = 0,0
    _y, _x, _ = img.shape
    slices = []
    card = 0
    info = []
    for y in range (0, _y, int(_y/h)):
        x1 = 0
        for x in range(0, _x, int(_x/w)):
            if (w*h)-card != i:
                sliced = img[y:y1+int(_y/h), x:x1+int(_x/w)]
                slices.append(sliced)
                x1 = x+ int(_x/w)
            card+=1
        y1 = y+ int(_y/h)
    return slices

def get_deck():
    door_decks = [
        [6,4,1],[6,4,1],
        [6,4,1],[7,4,2],
        [6,4,1],[6,4,1],
        [7,4,1]
    ]
    c=0
    d=[]
    t=[]
    for o in range(1,8):
        if o < 4:
            deck = door_decks
        else:
            deck = door_decks
        w,h,i = deck[o-1]
        cards = sliceim(str(o)+".jpg",w,h,i)
        if o < 4:
            d  += cards
        else:
            t += cards
        c+=o-1
    return d+t
