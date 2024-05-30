import csv
import ast
from utils import writeToCSV

def readMovieDetails(file):
    movie_data_dict = {}
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for movie_data in csv_reader:
            genres_dict = list(ast.literal_eval(movie_data[3]))
            genres = [genre['name'] for genre in genres_dict]
            title = movie_data[8]
            movie_id = movie_data[5]
            plot = movie_data[9]
            if len(movie_data) < 14:
                year = "information not available"
            else:
                year = movie_data[14].split('-')[0]
            movie_data_dict[movie_id] = {"name": title, "plot": plot, "year": year, "genres": genres}
    return movie_data_dict


def readCharDetails(file):
    char_details = {}
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for char_data in csv_reader:
            movie_id = char_data[2]
            # print(char_data[0])
            # break
            actors_dict = list(ast.literal_eval(char_data[0]))
            name = [name['name'] for name in actors_dict]
            if movie_id not in char_details:
                char_details[movie_id] = {"actor_name": [name]}
            else:
                char_details[movie_id]["actor_name"].append(name)
    return char_details


def createMovieDataset(movie_data_dict, char_details):
    movie_dataset = {}
    for movie_id in movie_data_dict:
        # if movie_id not in char_details:
        #     continue
        modified_plot = f"Film Genre:{movie_data_dict[movie_id]['genres']}, Starring the actors: {char_details.get(movie_id,{}).get('actor_name', 'information not available')}, Released in the year: {movie_data_dict.get(movie_id, {}).get('year', 'information not available')}, Summary of the movie plot: {movie_data_dict[movie_id]['plot']}"
        movie_dataset[movie_data_dict[movie_id]["name"]] = modified_plot
    return movie_dataset


def createRAGDataset():
    movie_data = readMovieDetails('Dataset/RAG/movies_metadata.csv')
    char_data = readCharDetails('Dataset/RAG/credits.csv')
    movie_dataset = createMovieDataset(movie_data, char_data)
    output_csv_path = 'Dataset/RAG/rag_movie_dataset.csv'
    writeToCSV(output_csv_path, movie_dataset)
