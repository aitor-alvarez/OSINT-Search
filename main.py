import argparse

if __name__ == 'main':
	parser = argparse.ArgumentParser()
	parser.add_argument('-rd', '--root_directory', help='Root directory to be scanned.')
	parser.add_argument('-yr', '--yara_rules', help='Compiled Yara rules file. Provide full path. Compiled file will be stored in rules directory.')
	parser.add_argument('-yd', '--yara_directory', help='Directory with Yara rules to be compiled. Output will be stored in output directory.')
	parser.add_argument('-fs', '--file_to_scan', help='Single file to be scanned and extract static data. Provide full path.')
	parser.add_argument('-fe', '--file_to_extract', help='Single file to extract static data. Provide full path.')

	args = parser.parse_args()

	if args.yara_directory:
		print()
