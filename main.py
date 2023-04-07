import os


default_path = "/Users/juhyeonnam/Desktop/a-PyTorch-Tutorial-to-Image-Captioning-master/"
checkpoint_name = "BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar"
wordmap_name = "WORDMAP_coco_5_cap_per_img_5_min_word_freq.json"

image_list = "||".join(os.listdir(default_path+"data/"))
image_name = "dog1"

if image_name in image_list:
    pos = image_list.find(image_name)
    pos2 = image_list.find("||", pos)
    
    image_name = image_list[pos:pos2]

os.system(f"python caption.py --img='{default_path}data/{image_name}' --model='{default_path+checkpoint_name}' --word_map='{default_path+wordmap_name}' --beam_size=5")


