from PIL import Image
import os
import io
import ui
from scene import Texture


def pil2ui(pil_img):
    with io.BytesIO() as buffer:
        pil_img.save(buffer, format='PNG')
        return ui.Image.from_data(buffer.getvalue())

                
def load_sprite_sheet(sheet_name, nx, ny, scale_x=-1, scale_y=-1):
    img_path = os.path.join('sprites', sheet_name)
    img = Image.open(img_path)
    size_x, size_y = img.size
    # print(size_x, size_y)
    
    sub_size_x = int(size_x / nx)
    sub_size_y = int(size_y / ny)
    # img.transform((100, 100), Image.EXTENT, (0, 0, 100, 90)).show()
    sprites = []
    for i in range(nx):
        for j in range(ny):
            img_coord = (i*sub_size_x, j*sub_size_y, (i+1)*sub_size_x, (j+1)*sub_size_y)
            if scale_x != -1 and scale_y != -1:
                sub_img = img.transform((scale_x, scale_y), Image.EXTENT, img_coord)
            else:
                sub_img = img.transform((sub_size_x, sub_size_y), Image.EXTENT, img_coord)
            # print(sub_img.size)
            # sub_img.show()
            sub_img = Texture(pil2ui(sub_img))
            sub_img_size = sub_img.size
            
            sprites.append((sub_img, sub_img_size))
            # sub_img.save(f'{i}.png')
    return sprites
    
