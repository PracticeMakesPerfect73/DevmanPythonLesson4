from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
width, height = image.size

middle_coordinates = (25, 0, width - 25, height)

red_left_coordinates = (50, 0, width, height)
red_left = red.crop(red_left_coordinates)
red_middle = red.crop(middle_coordinates)
red_blend = Image.blend(red_left, red_middle, 0.5)

blue_right_coordinates = (0, 0, width - 50, height)
blue_right = blue.crop(blue_right_coordinates)
blue_middle = blue.crop(middle_coordinates)
blue_blend = Image.blend(blue_right, blue_middle, 0.5)

green_crop = green.crop(middle_coordinates)

merge_image = Image.merge("RGB", (red_blend, green_crop, blue_blend))
merge_image.thumbnail((80,80))
avatar_image = merge_image.save("avatar_image.jpg")
