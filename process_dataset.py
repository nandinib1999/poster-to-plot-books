import pandas as pd
import json

def process_book_genre(row):
    if len(row) == 0:
        return ""
    
    genre_list = []
    row_dict = json.loads(row)
    for key, genre in row_dict.items():
        genre_list.append(genre)
    return ", ".join(genre_list)

def text_file_to_csv():
    '''
    Processing the raw dataset of book summaries to a CSV file for easy data handling
    '''
    with open('Dataset/booksummaries.txt') as text:
        data = text.readlines()
    data = [x.split("\t") for x in data]
    df = pd.DataFrame(data, columns=['Wiki ID', 'Freebase ID', 'Book Title', 'Author', 'Publication Date', 'Book genre', 'Plot summary'])
    df['book_genre'] = df['Book genre'].apply(lambda x: process_book_genre(x))
    df.to_csv('Dataset/book_summaries.csv', index=False)


if __name__ == "__main__":
    text_file_to_csv()