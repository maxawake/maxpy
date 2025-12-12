import os
import glob
import imageio
import matplotlib.pyplot as plt
import shutil
import tqdm
import warnings
import numpy as np
import multiprocessing as mp


def make_gif(callback: callable, data: np.array, gifpath=None, fps=25, frame=True):
    """Wrapper function for imageio to create a gif from any python package
    which is able to save PNG files

    Args:
        callback (callable): Callback function. This function needs exactly two inputs
        data and name. It should use the data to plot whatever needs to be plottet in each time step
        and name should be given to the save function
        data (np.array): List of data which is needed in each frame
        gifpath (str, optional): Path where gif should be saved. Defaults to None.
        fps (int, optional): Frames per second. Defaults to 25.
    """
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Use unique time-stamp for name is no path is given
    if gifpath is None:
        from datetime import datetime

        eventid = datetime.now().strftime("%Y%m-%d%H-%M%S")
        gifpath = f"./{eventid}.gif"

    # create temp if not already existing
    if "temp" not in os.listdir("./"):
        os.mkdir("temp")

    # Some constants
    nimages = len(data)
    zfill_param = int(np.ceil(np.log10(nimages)))

    # Save images in parallel
    print("Save Images...")
    idxs = np.arange(nimages, dtype=int)
    names = [f"temp/pic{str(i).zfill(zfill_param)}.png" for i in idxs]
    args = [(data[i], names[i]) for i in range(nimages)]
    with mp.Pool() as p:
        p.starmap(callback, tqdm.tqdm(args, total=nimages))
    print("Done.")

    # Use imageio to create gif from images
    images = []
    print("Make Gif...")
    for filename in tqdm.tqdm(sorted(glob.glob("temp/pic*"))):
        images.append(imageio.imread(filename))
    imageio.mimsave(gifpath, images, format="GIF", duration=(1000 / fps), loop=0)

    # Remove temporary folder
    shutil.rmtree("./temp")
    print("Done.")


if __name__ == "__main__":

    def cback(data, name, frame=False):
        if not frame:
            fig = plt.figure(frameon=False)

            ax = plt.Axes(fig, [0.0, 0.0, 1.0, 1.0])
            ax.set_axis_off()
            fig.add_axes(ax)

        ax.imshow(
            data,
            cmap=plt.get_cmap("cmr.lavender"),
            aspect="auto",
            origin="lower",
            extent=[0, 1, 0, 1],
        )
        fig.savefig(name, dpi=200)
        return 0

    xlin = np.linspace(0, 1, 100)
    x, y = np.meshgrid(xlin, xlin)

    data = [np.sin(2 * np.pi * (x - 0.01 * i)) * np.cos(2 * np.pi * (y - 0.01 * i)) for i in range(100)]
    make_gif(cback, data, gifpath="./sinewave.gif", fps=25)
