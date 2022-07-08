import argparse
from osint import search_osint_files

if __name__ == 'main':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file_type', help='File type. Default Yara.')
	parser.add_argument('-c', '--code', help='Code to search in github repositories.')

	args = parser.parse_args()

	if args.file_type:
		search_osint_files(file_type=args.file_type)
	elif args.code:
		search_osint_files(code=args.code)
