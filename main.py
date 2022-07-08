import argparse
from osint import search_osint_files
import os

if __name__ == 'main':
	if not os.path.isdir('downloads'):
		base_yara = 'downloads/yara/'
		base_sigma = 'downloads/sigma/'
		base_code = 'downloads/any'
		os.makedirs(base_sigma+'highly_ranked')
		os.mkdir(base_sigma+'ranked')
		os.mkdir(base_sigma + 'other')
		os.makedirs(base_yara+'highly_ranked')
		os.mkdir(base_yara+'ranked')
		os.mkdir(base_yara + 'other')
		os.makedirs(base_code + 'highly_ranked')
		os.mkdir(base_code + 'ranked')
		os.mkdir(base_code + 'other')
		print(f'Created the directories {base_yara}, {base_sigma} and {base_code}')

	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file_type', help='File type. Either yara, sigma, or any.')
	parser.add_argument('-c', '--code', help='Code to search in github repositories.')

	args = parser.parse_args()

	if args.file_type:
		if args.code:
			search_osint_files(file_type=args.file_type, code=args.code)
		else:
			search_osint_files(file_type=args.file_type)
	elif args.code and args.file_type=='any':
		search_osint_files(code=args.code)
