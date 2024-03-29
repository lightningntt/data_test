def read_from_csv(file_name):
    csv_filename = file_name
    with open(csv_filename) as f:
        # Python read text file from second line 
        lines = f.readlines()[1:50]
        lst = [tuple(line.strip().split(',')) for line in lines]
    return lst