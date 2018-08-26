from PIL import Image
import os
import io
import ui
from scene import Texture


def pil2texture(pil_imgs):
    texture_imgs = []
    for pil_img in pil_imgs:
        with io.BytesIO() as buffer:
            pil_img.save(buffer, format='PNG')
            texture_img = Texture(ui.Image.from_data(buffer.getvalue()))
            img_size = texture_img.size
            texture_imgs.append((texture_img, img_size))
    return texture_imgs


def load_sprite_sheet(sheet_name, nx, ny, scale_x=-1, scale_y=-1, list_wanted=None):
    # 第一个代码起始index，第二个是长度,只支持横着粘连且ny为1
    # list_wanted = [(0, 1), (0, 2), (2, 1), (2, 2), (3, 3)]
    
    img_path = os.path.join('sprites', sheet_name)
    img = Image.open(img_path)
    size_x, size_y = img.size
    
    sub_size_x = int(size_x / nx)
    sub_size_y = int(size_y / ny)
    
    if scale_x == -1 or scale_y == -1:
        scale_x = sub_size_x
        scale_y = sub_size_y
    # img.transform((100, 100), Image.EXTENT, (0, 0, 100, 90)).show()
    sub_imgs = []
    if sheet_name == 'cloud.png':
        for i in range(nx):
            for j in range(ny):
                img_coord = (i*sub_size_x, j*sub_size_y, (i+1)*sub_size_x, (j+1)*sub_size_y)
                sub_img = img.transform((scale_x, scale_y), Image.EXTENT, img_coord)
                # sub_img = sub_img.convert('RGB')

                split_img = sub_img.split()
                split_imgr = split_img[0].point(lambda x: 128 if x == 255 else 0)
                split_imgg = split_img[1].point(lambda x: 128 if x == 255 else 0)
                split_imgb = split_img[2].point(lambda x: 128 if x == 255 else 0)
                
                sub_img = Image.merge(sub_img.mode, [split_imgr, split_imgg, split_imgb, split_img[3]])    
                sub_imgs.append(sub_img)
    else:
        for i in range(nx):
            for j in range(ny):
                img_coord = (i*sub_size_x, j*sub_size_y, (i+1)*sub_size_x, (j+1)*sub_size_y)
                sub_img = img.transform((scale_x, scale_y), Image.EXTENT, img_coord)
                # sub_img = sub_img.convert('RGB')
                # sub_img.show()
                sub_imgs.append(sub_img)
        
    if list_wanted is None:
        textures = pil2texture(sub_imgs)
        return textures
    
    combine_imgs = []
    for i, length in list_wanted:
        new_image = Image.new('RGBA', (scale_x * length, scale_y))
        for add_i in range(length):
            coord = (add_i * scale_x, 0, scale_y, (add_i + 1) * scale_x)
            coord = (add_i * scale_x, 0)
            new_image.paste(sub_imgs[i + add_i], coord)
        # new_image.show()
        combine_imgs.append(new_image)

    return pil2texture(combine_imgs)
             
    
# load_sprite_sheet('cacti-small.png', 6, 1, 10, 23)
# load_sprite_sheet('dino.png', 5, 1)
