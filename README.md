# Attendance System using Face Recognition

This project is an attendance system that uses face recognition to mark the presence of individuals. The system is built using Python and OpenCV, and it captures real-time video from a webcam to recognize and log attendance.

## Features

- Real-time face detection and recognition
- Automatic attendance logging
- Easy-to-use interface
- Scalable and customizable for different environments

## Requirements

- Python 3.6+
- OpenCV
- NumPy
- Pandas

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/attendance-system-face-recognition.git
    cd attendance-system-face-recognition
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) If you need to install OpenCV separately, use:

    ```sh
    pip install opencv-python
    ```

## Usage

1. **Capture and Register Faces**

    Before starting the attendance system, you need to register the faces of individuals. Run the following script to capture and store face images:

    ```sh
    python capture_faces.py
    ```

    Follow the on-screen instructions to capture face images and label them with the person's name.

2. **Train the Face Recognition Model**

    Once you have captured and labeled the faces, train the face recognition model:

    ```sh
    python train_model.py
    ```

3. **Run the Attendance System**

    After training the model, you can start the attendance system:

    ```sh
    python attendance_system.py
    ```

    The system will start the webcam and recognize faces in real-time, logging the attendance in an output file (`attendance.csv`).

## Project Structure

- `capture_faces.py`: Script to capture and store face images.
- `train_model.py`: Script to train the face recognition model.
- `attendance_system.py`: Main script to run the attendance system.
- `dataset/`: Directory where captured face images are stored.
- `models/`: Directory where the trained models are saved.
- `attendance.csv`: Output file where attendance is logged.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests to contribute.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- This project uses the OpenCV library for computer vision tasks.
- Inspiration and resources from various online tutorials and documentation.

## Contact

For any questions or suggestions, please contact bhushanmaheshwari100@gmail.com

------------------------------------------------------------------------------------------

Feel free to modify the content according to your specific needs and details.
