#!/usr/bin/env python3

import re

with open('451.txt', 'r') as story:
	text = story.read()

pages = text.split('\f')
pages_lines = [page.split('\n') for page in pages]

with open('encoded.txt', 'r') as encoded:
	encoded_text = encoded.read()

decoded_text = encoded_text

pattern = re.compile(r'\[\d+\:\d+:\d+\]')

for match in re.findall(pattern, encoded_text):
	clean_match = match[1:-1]
	(page, line, char) = clean_match.split(':')
	page = int(page)
	line = int(line)
	char = int(char)
	decoded_char = pages_lines[page - 1][line - 1][char - 1]
	print(match, '\t->\t', decoded_char)
	decoded_text = decoded_text.replace(match, decoded_char)

print()
print()
print('DECODED:')
print(decoded_text)
