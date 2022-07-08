import argparse
from osint import search_osint_files

if __name__ == 'main':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file_type', help='File type. Either yara or sigma.')
	parser.add_argument('-c', '--code', help='Code to search in github repositories.')

	args = parser.parse_args()

	if args.file_type:
		if args.code:
			search_osint_files(file_type=args.file_type, code=args.code)
		else:
			search_osint_files(file_type=args.file_type)
	elif args.code:
		if args.code:
			search_osint_files(file_type=args.file_type, code=args.code)
		else:
			search_osint_files(code=args.code)
