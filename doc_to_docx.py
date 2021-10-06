import os

rootdir = "path/to/dir"

for file in os.listdir(rootdir):
    if file.endswith(".doc"):
        filepath = os.path.join(rootdir, file)
        base = os.path.splitext(file)[0:-1][0]
        new_filepath = os.path.join(rootdir, base + '.docx')
        if not os.path.exists(new_filepath):
            os.rename(filepath, new_filepath)
