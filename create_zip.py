import os
import zipfile

def zipdir(path, ziph):
    # Recursively add files to the zip file.
    for root, dirs, files in os.walk(path):
        for file in files:
            # Skip the zip file if it already exists.
            if file == "project-repo.zip":
                continue
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, path)
            ziph.write(filepath, arcname)

if __name__ == '__main__':
    project_dir = os.path.dirname(os.path.abspath(__file__))
    zip_filename = os.path.join(project_dir, "project-repo.zip")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(project_dir, zipf)
    print(f"Created zip file: {zip_filename}")
