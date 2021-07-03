import os
import pandas as pd

raw_dir = './dataset/train'
csv_path = './dataset/csv'

def read_from_dir(dir):
    file_name = dir.split("/")[-1]
    # conver label to snake_case   
    file_name = "_".join(file_name.lower().split()) # snake_case
    data = []
    file_paths = os.listdir(dir)
    if file_paths and len(file_paths):
        for file in file_paths:
            with open(f"{dir}/{file}", mode='r', encoding= 'utf-16') as f:
                text = f.read()
                data.append(text.strip())
    return file_name, data

def save_to_csv(file_name, data):
    df = pd.DataFrame(data, columns=['text'])
    df.to_csv(f"{csv_path}/{file_name}.csv")

if __name__ == '__main__':
    folders = os.listdir(raw_dir)
    for dir in folders:
        file_name, data = read_from_dir(f"{raw_dir}/{dir}")
        save_to_csv(file_name, data)
