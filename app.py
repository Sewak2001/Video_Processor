from flask import Flask, render_template, request, send_file, url_for, redirect
import os
import cv2
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# function for process video
def process_video(input_file, zoom=1.0, contrast=1.0, brightness=0):
  output_path = 'processed_videos'
  os.makedirs(output_path, exist_ok=True)
  temp_output_file = os.path.join(output_path, f"temp_processed_{os.path.basename(input_file)}")
  final_output_file = os.path.join(output_path, f"processed_{os.path.basename(input_file)}")

  cap = cv2.VideoCapture(input_file)
  if not cap.isOpened():
    print(f"Error: Could not open video '{input_file}'")
    return

  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fps = cap.get(cv2.CAP_PROP_FPS)

  fourcc = cv2.VideoWriter_fourcc(*'X264')
  out = cv2.VideoWriter(temp_output_file, fourcc, fps, (width, height))

  while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
      break

    if zoom != 1.0:
      frame = cv2.resize(frame, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_LINEAR)
      frame_height, frame_width = frame.shape[:2]
      center_x, center_y = frame_width // 2, frame_height // 2
      x1, y1 = center_x - width // 2, center_y - height // 2
      frame = frame[y1:y1 + height, x1:x1 + width]

    frame = cv2.flip(frame, 1)
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)
    out.write(frame)

  cap.release()
  out.release()
  cv2.destroyAllWindows()

  original_clip = VideoFileClip(input_file)
  processed_clip = VideoFileClip(temp_output_file)
  final_clip = processed_clip.set_audio(original_clip.audio)
  final_clip.write_videofile(final_output_file, codec='libx264')

  os.remove(temp_output_file)
  return final_output_file

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if 'video_file' not in request.files:
      return redirect(request.url)
    file = request.files['video_file']
    if file.filename == '':
      return redirect(request.url)
    
    if file:
      filename = secure_filename(file.filename)
      input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      file.save(input_path)

      zoom = float(request.form['zoom'])
      contrast = float(request.form['contrast'])
      brightness = int(request.form['brightness'])

      processed_file_path = process_video(input_path, zoom, contrast, brightness)
      return send_file(processed_file_path, as_attachment=True)

  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
