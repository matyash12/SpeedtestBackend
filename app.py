from flask import Flask, request
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file_data = {}

    # Check if the post request has the file part
    if 'fileToUpload' not in request.files:
        return 'No file part'

    file = request.files['fileToUpload']

    # If the user does not select a file, the browser may submit an empty part without a filename
    if file.filename == '':
        return 'No selected file'

    # Process the file stream as needed
    with io.BytesIO() as buffer:
        print("Buffer?")
        file.save(buffer)
        file_data['originalname'] = file.filename
        file_data['size'] = len(buffer.getvalue())
        file_data['mimetype'] = file.mimetype
        # Example: Do something with the file data, e.g., process it in-memory

    # Example: Respond with a message
    print("File processing complete")
    return 'File processing complete'

if __name__ == '__main__':
    from waitress import serve
    print("Server starting")
    serve(app, host="0.0.0.0", port=8080)
