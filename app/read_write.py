import pandas as pd
import os.path

def download_files():

    path = './data/raw/sentiment_analysis.pq'

    if not os.path.isfile(path):
        print('Downloading files...')
        df = pd.read_csv('https://query.data.world/s/kxyvqvqejaoki3nxfnmjgwfjyl7ncr?dws=00000', encoding='latin-1')
        df.to_parquet(path)
        print('Download completed')
    else:
        print('Files were already downloaded. Using cached files.')