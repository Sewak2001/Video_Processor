# Video Processor with Flask and MoviePy

This is a simple Flask application that allows users to upload a video, apply processing (zoom, contrast, and brightness adjustments), and download the processed video. The application uses `moviepy` and `OpenCV` for video manipulation.

## Features

- **Upload video**: Users can upload a video file through a web interface.
- **Zoom**: Users can apply a zoom effect to the video.
- **Contrast**: Users can adjust the contrast of the video.
- **Brightness**: Users can modify the brightness of the video.
- **Download processed video**: After processing, the user can download the modified video.

## Requirements

- Python 3.10 or higher
- Flask
- OpenCV
- MoviePy
- Pillow
- Other dependencies as listed in the `requirements.txt` file.

## Installation

### 1. Clone the repository
Clone the project to your local machine:

```bash
git clone https://github.com/yourusername/video-processor.git
cd video-processor
```

### 2. Set up a virtual environment
Create and activate a Python virtual environment:

#### Windows
```bash
python -m venv myenv
myenv\Scripts\activate
```

#### Mac/Linux
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies
Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries including `Flask`, `moviepy`, `opencv-python`, and others.

### 4. Install MoviePy and Pillow dependencies
Ensure that you have compatible versions of `moviepy` and `Pillow`:

```bash
pip install moviepy pillow==10.0.0
```

## Usage

### 1. Run the Flask App
Run the Flask application:

```bash
python app.py
```

This will start the Flask development server, usually accessible at `http://127.0.0.1:5000/`.

### 2. Access the Web Interface
Open a web browser and go to `http://127.0.0.1:5000/`. You will see the video upload form.

### 3. Upload and Process Video
- **Choose a video file** to upload.
- **Set the Zoom, Contrast, and Brightness** options.
- Click **Submit** to start the processing. The app will apply the changes to the video and allow you to download the processed file.

## Code Overview

### `app.py`

This is the main Flask application file. It handles:
- The file upload process.
- Video processing using OpenCV and MoviePy (`process_video` function).
- Video playback (by preserving audio and applying visual effects).

### `process_video(input_file, zoom, contrast, brightness)`
This function performs the actual video processing:
- **Zoom**: Resizes the video frame and crops it to maintain the original resolution.
- **Contrast**: Adjusts the contrast using `cv2.convertScaleAbs`.
- **Brightness**: Modifies the video brightness.
- After processing, the function uses MoviePy to combine the processed frames with the original audio and saves the final output.

### `index.html`
This is the template for the upload form. Users can select a video file and adjust the processing parameters (Zoom, Contrast, Brightness).

## Troubleshooting

### `ModuleNotFoundError`
If you encounter a `ModuleNotFoundError` related to `moviepy.editor`, ensure that the `moviepy` library is properly installed. You can check installed packages using:

```bash
pip list
```

If `moviepy` is not listed, install it with:

```bash
pip install moviepy
```

### Version Conflicts
Ensure that you have compatible versions of dependencies, especially `moviepy` and `Pillow`. If there are conflicts, downgrade `Pillow` to `10.0.0` using:

```bash
pip install pillow==10.0.0
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
