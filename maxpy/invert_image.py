from PIL import Image
import numpy as np
from colorspacious import cspace_convert


def invert_lightness_image(input_path, output_path, k=1.0):
    """
    Invert the lightness of an image while preserving colors.
    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the output image.
        k (float): Contrast control parameter (0 = no change, 1 = full inversion).
    """
    img = Image.open(input_path).convert("RGB")
    arr = np.asarray(img, dtype=float) / 255.0

    flat = arr.reshape(-1, 3)

    lch = cspace_convert(flat, "sRGB1", "CIELCh")
    L = lch[:, 0]

    # Contrast controlled inversion
    L_new = (1.0 - k) * L + k * (100.0 - L)
    lch[:, 0] = L_new

    rgb_new = cspace_convert(lch, "CIELCh", "sRGB1")
    rgb_new = np.clip(rgb_new, 0.0, 1.0)

    out = (rgb_new.reshape(arr.shape) * 255).astype(np.uint8)
    Image.fromarray(out, mode="RGB").save(output_path)


if __name__ == "__main__":
    # Example
    invert_lightness_image(
        "/home/max/Nextcloud/Physik/Projects/MRVIS/Revision01/plots/num_points_lines.png", "darkmode.png", k=0.5
    )
