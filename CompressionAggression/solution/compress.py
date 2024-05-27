import os
import zipfile
import bz2
import tarfile
import gzip
import shutil
import random

def compress_file(file_path, zip_count, bzip_count, tar_count, gzip_count):
    # Create a list of compressions to apply
    compressions = ['zip'] * zip_count + ['bzip'] * bzip_count + ['tar'] * tar_count + ['gzip'] * gzip_count
    random.shuffle(compressions)
    
    # Create a working copy of the original file
    current_file = 'flag'
    shutil.copyfile(file_path, current_file)

    for i, comp in enumerate(compressions):
        if comp == 'zip':
            current_file = zip_file(current_file, "flag")
        elif comp == 'bzip':
            current_file = bzip_file(current_file, "flag")
        elif comp == 'tar':
            current_file = tar_file(current_file, "flag")
        elif comp == 'gzip':
            current_file = gzip_file(current_file, "flag")
        print(f"Step {i + 1}: {comp.upper()} compression applied, current file: {current_file}")
    
    print(f"Final compressed file: {current_file}")

def zip_file(input_file, output_file):
    with zipfile.ZipFile(output_file + '.zip', 'w') as zipf:
        zipf.write(input_file, os.path.basename(input_file))
    os.remove(input_file)
    os.rename(output_file + '.zip', output_file)
    return output_file

def bzip_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with bz2.open(output_file + '.bz2', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(input_file)
    os.rename(output_file + '.bz2', output_file)
    return output_file

def tar_file(input_file, output_file):
    with tarfile.open(output_file + '.tar', 'w') as tarf:
        tarf.add(input_file, arcname=os.path.basename(input_file))
    os.remove(input_file)
    os.rename(output_file + '.tar', output_file)
    return output_file

def gzip_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(input_file)
    os.rename(output_file + '.gz', output_file)
    return output_file

if __name__ == "__main__":
    # Specify the counts for each compression type
    zip_count = 30
    bzip_count = 30
    tar_count = 30
    gzip_count = 30

    # Input file to compress
    input_file = 'flag.enc'

    # Perform the compressions
    compress_file(input_file, zip_count, bzip_count, tar_count, gzip_count)
