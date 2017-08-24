import PyPDF2

def get_all_uri(pdf):
	reader = PyPDF2.PdfFileReader(pdf)

	uris_list = []
	pages_list = reader.getNumPages()
	for page in [reader.getPage(i) for i in range(pages_list)]:
		for Iobj in [page['/Annots'][i].getObject() for i in range(pages_list)]:
			uris_list.append(Iobj.get('/A').get('/URI'))
	return uris_list

def save_to_file(file_path, urls_list):
	with open(file_path, 'w+') as f:
			f.write('\n'.join(urls_list))

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('pdf', help='pdf to squeeze')
	parser.add_argument('-f', '--file', help='saving file')
	parser.add_argument('-p', '--print', help='prints on tty', action='store_true')
	args = parser.parse_args()

	pdf = args.pdf
	uris = get_all_uri(pdf)

	if args.print:
		print('\n'.join(uris))
	if args.file:
		save_to_file(output_file, uris)




