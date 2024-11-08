# Naruto Hand Sign Classifier

A computer vision project that can identify 13 different Naruto hand signs in real-time using a webcam feed. The model is built using transfer learning with VGG16 architecture.

The final model has not been uploaded as it exceeds github size limits

## Dataset

This project uses the [Naruto Hand Sign Dataset](https://www.kaggle.com/datasets/vikranthkanumuru/naruto-hand-sign-dataset) created by Vikranth Kanumuru. Special thanks to the creator for providing this dataset which enables the training of hand sign classification models.

The dataset includes 13 different Naruto hand signs:
- Bird
- Boar
- Dog
- Dragon
- Hare
- Horse
- Monkey
- Ox
- Ram
- Rat
- SNake
- Tiger
- Zero

## Installation

### Linux (Ubuntu 22.04+)
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download dataset
kaggle datasets download vikranthkanumuru/naruto-hand-sign-dataset
unzip naruto-hand-sign-dataset.zip -d ./data
rm naruto-hand-sign-dataset.zip

# Correct path
mv Pure\ Naruto\ Hand\ Sign\ Data/train/ .
mv Pure\ Naruto\ Hand\ Sign\ Data/test/ .
rm -r Pure\ Naruto\ Hand\ Sign\ Data/
```

### Windows (not tested)
```powershell
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download dataset
kaggle datasets download vikranthkanumuru/naruto-hand-sign-dataset
Expand-Archive -Path naruto-hand-sign-dataset.zip -DestinationPath .\data
Remove-Item naruto-hand-sign-dataset.zip

# Correct path
Move-Item -Path "data\Pure Naruto Hand Sign Data\train" -Destination "."
Move-Item -Path "data\Pure Naruto Hand Sign Data\test" -Destination "."
Remove-Item -Recurse -Force "data\Pure Naruto Hand Sign Data"
```

### macOS
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download dataset
kaggle datasets download vikranthkanumuru/naruto-hand-sign-dataset
unzip naruto-hand-sign-dataset.zip -d ./data
rm naruto-hand-sign-dataset.zip

# Correct path
mv "data/Pure Naruto Hand Sign Data/train" .
mv "data/Pure Naruto Hand Sign Data/test" .
rm -r "data/Pure Naruto Hand Sign Data/"
```

## Dependencies

Full list of dependencies can be found in `requirements.txt`
**NOTE** This was developed on Ubuntu 22.04, hence the dependencies might change on different operating systems.

## Usage

Run the application using:
```bash
python3 app.py
```

This will access your webcam, process the frames and feed it through the trained CNN. The CNN returns the prediction which is then processed to display the hand sign.

## Model Architecture

- Base Model: VGG16
- Transfer Learning: Pre-trained weights on ImageNet
- Additional layers added for hand sign classification
- Training details can be found in `training.ipynb`
- Separate testing notebook (`testing.ipynb`) for model evaluation

## Project Structure

```
.
├── app.py                  # Main application file
├── training.ipynb          # Model training notebook
├── testing.ipynb          # Model testing notebook
├── requirements.txt       # Project dependencies
├── data/                 # Dataset directory
│   ├── test/            # Test dataset
│   └── train/           # Training dataset
└── models/               # Saved model files
```

## Development

The project was originally developed on Ubuntu 22.04 with Python 3.10.12. It has been tested and verified to work on:
- Ubuntu 22.04
- Python 3.10.12
- TensorFlow 2.18.0

## Acknowledgments

- Dataset created by Vikranth Kanumuru on Kaggle
- Based on VGG16 architecture developed by Visual Geometry Group at Oxford