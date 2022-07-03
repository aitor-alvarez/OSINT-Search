import requests
from github import Github
import os
from creds import creds
import time

#Find yara or sigma files in github directories and download the files according to their star counts or other predefined criteria.

#Github API credentials
tkn = creds.GITHUB_API
g = Github(tkn)


def search_osint_files(file_type='yara'):
	if file_type == 'yara':

		query = f'in:file language:'+file_type
	elif file_type == 'sigma':
		query = f'title AND logsource AND detection AND condition in:file extension:yml'
	rate_limit = g.get_rate_limit()
	rate = rate_limit.search
	if rate.remaining == 0:
		print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
	else:
		print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

	result = g.search_code(query, order='desc')
	print(f'Found {result.totalCount} file(s)')

	# Since the github API only serves the first 1000 results, pagination is needed.
	for p in range(1, 33):
		result_page = result.get_page(p)
		for file in result_page:
			try:
				if file.size < 1048576:
					filename = file.path.split('/')[-1]
					if file.repository.stargazers_count > 50:
						if filename not in os.listdir(file_type + '/highly_ranked/'):
							r = requests.get(file.download_url)
							open(file_type + '/highly_ranked/' + filename, "w").write(r.text)
					elif file.repository.stargazers_count > 10 and file.repository.stargazers_count <= 50:
						if filename not in os.listdir(file_type + '/ranked/'):
							r = requests.get(file.download_url)
							open(file_type + '/ranked/' + filename, "w").write(r.text)
					elif file.repository.stargazers_count <= 10:
						if filename not in os.listdir(file_type +'/other/'):
							r = requests.get(file.download_url)
							open(file_type + '/other/' + filename, "w").write(r.text)
			except:
				continue
		# Github API has a limit of 30 requests per minute
		time.sleep(61)
