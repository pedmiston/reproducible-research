from unipath import Path
from psychopy.visual import ImageStim

class DynamicMask(object):
    def __init__(self, win, **kwargs):
        """A collection of psychopy ImageStims.

        Expects a directory of images to load in this file's directory.

        Args:
            **kwargs: args to pass to visual.ImageStim
        """
        exp_root = Path(__file__).absolute().parent
        mask_files = Path(exp_root, 'dynamic_mask').listdir('*.png')
        self.masks = [ImageStim(win, image=str(pth), **kwargs)
                      for pth in mask_files]
        self.cur_ix = 0

    def draw(self):
        """Draw a single mask."""
        self.masks[self.cur_ix].draw()
        self.cur_ix = (self.cur_ix+1) % len(self.masks)

    def setPos(self, pos):
        """Set the position for all masks."""
        for mask in self.masks:
            mask.setPos(pos)

    def reset(self):
        """Reset the mask index counter."""
        self.cur_ix = 0
