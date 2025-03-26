# Image Inverter

This script inverts the colors of all images in the `Original` folder and saves the modified images in the `Edited` folder.

## Requirements
- Python 3
- OpenCV library (`cv2`)

### Install Dependencies
```bash
pip install opencv-python
```

## How to Use
1. Create two folders in the same directory as `main.py`:
   - `Original` (place your images here)
   - `Edited` (the processed images will be saved here)
2. Run the script:
```bash
python main.py
```
3. The script will process all `.png`, `.jpg`, and `.jpeg` images from the `Original` folder and save the inverted versions in `Edited`.
4. The terminal will display the names of the processed images.

## Notes
- If an image fails to load, an error message will be printed.
- Make sure the `Original` folder contains valid image files.

