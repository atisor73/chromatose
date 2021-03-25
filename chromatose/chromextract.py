
import argparse
from .extraction import *

from PIL import Image

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_palette(path, n_colors, method, resize, sort):
    return extract(path,
                   n_colors=n_colors,
                   method=method,
                   resize=resize,
                   sort=sort,
                   )

def imager(n, palette):
    img = Image.new('RGB', size=(50 * n, 50))
    arr = np.asarray(img).copy()
    for i in range(n):
        c = palette[i]
        arr[:, i*50:(i+1)*50, :] = c
    img = Image.fromarray(arr, "RGB")
    return img

def main():
    parser = argparse.ArgumentParser(description='Palette extraction from image path using both k-means and median cut algorithms. \nDefaults to 5 colors.')
    parser.add_argument('path', help="path to image", type=str)
    parser.add_argument('-n','--ncolors', help="length of palette     (int)",
                        type=int, default=5, metavar='')
    parser.add_argument('-r','--resize',  help="resize for efficiency (bool)",
                        type=str2bool, default=True, metavar='')
    parser.add_argument('-s','--sort',    help="sort by luminance     (bool)",
                        type=str2bool, default=False, metavar='')
    parser.add_argument('-d','--display', help="serve panel object    (bool)",
                        type=str2bool, default=False, metavar='')

    args = parser.parse_args()

    km, mc = get_palette(args.path, args.ncolors, "both", args.resize, args.sort)
    if args.display:
        print(f"K-Means    (left):  {km}")
        print(f"Median Cut (right): {mc}")
        km, mc = hex_to_rgb(km), hex_to_rgb(mc)
        img1, img2 = imager(args.ncolors, km), imager(args.ncolors, mc)
        blank = imager(1, (235, 235, 235))
        img = Image.fromarray(np.hstack((np.array(img1), np.array(blank), np.array(img2))))
        img.show()
    else:
        print(f"K-Means:    {km}")
        print(f"Median Cut: {mc}")
