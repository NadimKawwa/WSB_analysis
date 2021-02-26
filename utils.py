import json #JSON manipulation


def readSubDir(sub_dir):
    """
    reads a submission directory and returns data
    """
    with open(sub_dir, 'r') as f:
        raw_data = json.load(f)
    data = raw_data['data']
    return data