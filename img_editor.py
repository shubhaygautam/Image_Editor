from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

path = './img'
exitPath = './edited'

def apply_editing_features(img, selected_features):
    for feature in selected_features:
        if feature == 1:
            contrast_factor = 1.5
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_factor)
            
        elif feature == 2:
            brightness_factor = 1.2
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_factor)
            
        elif feature == 3:
            rotation_angle = 45
            img = img.rotate(rotation_angle)
            
        elif feature == 4:
            width, height = img.size
            left = width / 4
            top = height / 4
            right = 3 * width / 4
            bottom = 3 * height / 4
            img = img.crop((left, top, right, bottom))
            
        elif feature == 5:
            new_width = 300
            new_height = 300
            img = img.resize((new_width, new_height))
            
        elif feature == 6:
            img = img.filter(ImageFilter.BLUR)
            
        elif feature == 7:
            img = img.filter(ImageFilter.SHARPEN)
            
        elif feature == 8:
            img = img.convert('L')
            
        elif feature == 9:
            img = ImageOps.invert(img)
    
    return img

selected_features = []
print("Enter the numbers corresponding to the editing features you want to apply (1 to 9):")
print("1: Enhance Contrast")
print("2: Enhance Brightness")
print("3: Rotate Image")
print("4: Crop Image")
print("5: Resize Image")
print("6: Apply Blur Filter")
print("7: Apply Sharpen Filter")
print("8: Convert to Grayscale")
print("9: Invert Colors")
user_input = input("Enter numbers separated by space: ")
selected_features = list(map(int, user_input.split()))

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    edited_img = apply_editing_features(img, selected_features)

    clean_name = os.path.splitext(filename)[0]
    edited_img.save(f'{exitPath}/{clean_name}_edited.jpg')
