def save_upload_file(upload_file, destination):
    with open(destination, "wb") as buffer:
        buffer.write(upload_file.file.read())