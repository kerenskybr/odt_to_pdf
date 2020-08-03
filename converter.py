import os
import subprocess

from pyopendoc import opendocument, writer
from tempfile import NamedTemporaryFile

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to odt files")

ap.add_argument("-o", "--output", required=True, help="path to save the pdfs")

args = vars(ap.parse_args())


def converter(file, output):
	"""Convert a libre office file (odt)
	to a pdf file in bulk"""

	odt_file = writer.OpenWriterDocument(filepath=file)
	odt_bytes = odt_file.save_to_bytes()

	temp_odt_file = NamedTemporaryFile(suffix='.odt', delete=True)
	temp_odt_file.write(odt_bytes)

	subprocess.call(['libreoffice', '--headless', '--convert-to', 'pdf', temp_odt_file.name, '--outdir', str(output)])
	temp_odt_file.close()


if __name__ == "__main__":

	files_dir = os.path.abspath(args['input'])
	
	for files in os.listdir(files_dir):
		converter(os.path.join(files_dir, files), args['output'])
	

