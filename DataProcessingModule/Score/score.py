import pandas as pd
import os


class  Preprocessing:

    def load_excel(self, filename):
        df = pd.read_excel(filename)
        print("Read the file Successfully")
        return df

    def save_back(self, df, filename):
        df.to_excel(filename, index=False)
        print("Saved the file Successfully")

    def replace_delimitors(self, df, attribute):
        delimitors = list(string.punctuation + string.whitespace)
        df[attribute] = df[attribute].apply(lambda x: x.replace(d,repl))
        return df

    def filter_colomns(self, df, colomns):
        df = df[colomns]
        return df

    def drop_null(self, df, Attr):
        df = df.dropna()
        return df

    def remove_duplicates(self, df):
        df.drop_duplicates(keep='first',inplace=True)
        return df

    def join_files(self, folder):
        dfs = pd.DataFrame()
        for files in os.listdir(files):
            df = pd.read_excel(os.path.join(folder,files))
            dfs.append(df)
        return dfs


