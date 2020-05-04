import sys, json

if len(sys.argv) < 3:
	print('\nUSAGE: $ python conversion.py [notebook_to_convert.ipynb] [output_file.py]\n')
else: 
	file1 = open(sys.argv[1], 'r')
	name_of_output = sys.argv[2]
	file_content = file1.read()

	js = json.loads(file_content)

	cells = js['cells']

	out_lines = []

	for cell in cells:
		src = cell['source']
		for line in src:
			out_lines.append(line)


	f = open(name_of_output, "w")
	f.writelines(out_lines)
	f.close()