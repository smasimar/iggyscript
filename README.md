# increase_render_distance.py

## Description
This script processes SR2 map chunks, increasing render distance of individual entities in the map data by 4 times.
It can handle both single file inputs and multiple file configurations through a file list.

## Features
- Processes a single chunk file or multiple chunk files based on a file list.
- Increases render distance by multiplying 32-bit little-endian float values by 4 if they are less than 1,000,000.

## Usage

### Single File Processing
To process a single binary file, use the following command:

```sh
python increase_render_distance.py input_filename.bin output_filename.bin start_offset jmp_offset entities_num [-v]
```

- `input_filename.bin`: The input binary file to process.
- `output_filename.bin`: The output binary file to save the edited content.
- `start_offset`: The start offset in hex.
- `jmp_offset`: The jump offset in hex.
- `entities_num`: The number of entities to process.
- `-v`, `--verbose`: Enable verbose output (optional).

### Multiple File Processing
To process multiple binary files using a file list, use the following command:

```sh
python increase_render_distance.py -f config_file.txt [-v]
```

- `-f`, `--filelist`: The name of the file list file with processing details.
- `-v`, `--verbose`: Enable verbose output (optional).

### File List Format
The file list should contain one file and its parameters per line, with the following format:

```
input_filename output_filename start_offset jmp_offset entities_num
```

Example line:

```
sr2_ug_chunk159_malla.chunk_pc sr2_ug_chunk159_malla.chunk_pc.edited 0x3d247c 80 2609
```

## Example Commands

### Single File
```sh
python increase_render_distance.py sr2_ug_chunk159_malla.chunk_pc sr2_ug_chunk159_malla.chunk_pc.edited 0x3d247c 80 2609 -v
```

### Multiple Files
```sh
python increase_render_distance.py -f config_file.txt
```

## License
This project is licensed under the MIT License.
