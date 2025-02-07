# File Comparator with Semantic Similarity

This project is a web application built with Flask that compares two files (supported formats: `.txt`, `.html`, `.xlsx`, `.docx`, `.pdf`, `.pptx`) using AI/ML techniques. It extracts text from files, calculates semantic similarity using a pre-trained SentenceTransformer model, generates a diff, and presents the similarity score along with a pie chart visualization using Matplotlib.

## Features

- **File Upload:** Upload two files to compare.
- **Text Extraction:** Extracts text from multiple file formats.
- **Semantic Similarity:** Uses a machine learning model to compute how similar two files are.
- **Diff Generation:** Displays the differences between the files.
- **Graphical Representation:** Visualizes the similarity score as a colorful pie chart.
- **Modern UI:** Uses Flask and Bootstrap for a responsive and modern web interface.

## Prerequisites

- Python 3.8.10 (or newer)
- [Git](https://git-scm.com/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git

2. 
cd your-repository-name
3. **Create and Activate a Virtual Environment:**
 python -m venv venv
** NEXT STEP **
venv\Scripts\activate

4. **Install the Required Libraries:**
 pip install -r requirements.txt
