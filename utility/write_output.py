def write_output_file(output_file_address, output):
    """
    Takes two strings as output file address and output and writes the output to the output file
    Written by: Parsa
    """
    with open(output_file_address, 'w') as f:
        f.write(output)
