import struct
import argparse
import sys

def process_binary_file(input_filename, output_filename, start_offset, jmp_offset, entities_num, verbose):
	print(f'Processing file: {input_filename}')
	
	# Open the input binary file in read mode and the output binary file in write mode
	with open(input_filename, 'rb') as infile, open(output_filename, 'wb') as outfile:
		# Copy the content from the input file to the output file
		outfile.write(infile.read())
		
		# Go back to the start offset
		infile.seek(start_offset)
		outfile.seek(start_offset)
		
		current_address = start_offset
		for _ in range(entities_num):
			# Read 4 bytes from the current position in the input file
			float_bytes = infile.read(4)
			# Unpack the bytes to a little-endian float value
			float_value = struct.unpack('<f', float_bytes)[0]
			# Multiply the float value by 4
			multiplied_value = float_value * 4
			# Pack the modified float value into bytes
			modified_bytes = struct.pack('<f', multiplied_value)
			
			# Print the address, original value, and multiplied value if verbose
			if verbose:
				print(f'Address: 0x{current_address:X}, Original Value: {float_value}, Multiplied Value: {multiplied_value}')
			else:
				print('.', end='', flush=True)
			
			# Seek to the correct position in the output file and write the modified bytes
			outfile.seek(current_address)
			outfile.write(modified_bytes)
			
			# Update the address and seek to the next position in the input file
			current_address += jmp_offset
			infile.seek(current_address)

		if not verbose:
			print()  # Move to the next line after the progress dots

def process_multiple_files(config_filename, verbose):
	with open(config_filename, 'r') as config_file:
		for line in config_file:
			parts = line.strip().split()
			if len(parts) != 5:
				print(f'Invalid line in config file: {line.strip()}')
				continue

			input_filename = parts[0]
			output_filename = parts[1]
			start_offset = int(parts[2], 0)
			jmp_offset = int(parts[3], 0)
			entities_num = int(parts[4])
			
			process_binary_file(input_filename, output_filename, start_offset, jmp_offset, entities_num, verbose)

def main():
	parser = argparse.ArgumentParser(description='Process and edit binary files.')
	parser.add_argument('-f', '--filelist', type=str, help='The name of the configuration file with processing details.')
	parser.add_argument('input_filename', nargs='?', type=str, help='The name of the input binary file to process.')
	parser.add_argument('output_filename', nargs='?', type=str, help='The name of the output binary file to save the edited content.')
	parser.add_argument('start_offset', nargs='?', type=lambda x: int(x, 0), help='The start offset in hex.')
	parser.add_argument('jmp_offset', nargs='?', type=lambda x: int(x, 0), help='The jump offset in hex.')
	parser.add_argument('entities_num', nargs='?', type=int, help='The number of entities to process.')
	parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
	
	args = parser.parse_args()
	
	if args.filelist:
		process_multiple_files(args.filelist, args.verbose)
	elif args.input_filename and args.output_filename and args.start_offset is not None and args.jmp_offset is not None and args.entities_num is not None:
		process_binary_file(args.input_filename, args.output_filename, args.start_offset, args.jmp_offset, args.entities_num, args.verbose)
	else:
		parser.print_help()
		sys.exit(1)

if __name__ == '__main__':
	main()
