import csv
import ast
from utils import writeToCSV

def readPlotSummaries(file):
    movie_plots_data = {}
    with open(file, 'r', encoding='utf-8') as text_file:
        for line in text_file:
            movie_data = line.strip().split("\t")
            movie_id = movie_data[0]
            movie_plot = movie_data[1]
            movie_plots_data[movie_id] = movie_plot
    return movie_plots_data


def readMovieDetails(file):
    movie_details = {}
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter='\t')
        for movie_data in csv_reader:
            movie_id = movie_data[0]
            name = movie_data[2]
            year = movie_data[3].split('-')[0]
            genres = list(ast.literal_eval(movie_data[8]).values())
            movie_details[movie_id] = {"name": name, "year": year, "genres": genres}
    return movie_details


def readCharDetails(file):
    char_details = {}
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter='\t')
        for char_data in csv_reader:
            movie_id = char_data[0]
            name = char_data[8]
            if movie_id not in char_details:
                char_details[movie_id] = {"actor_name": [name]}
            else:
                char_details[movie_id]["actor_name"].append(name)
    return char_details


def createMovieDataset(movie_plots_data, movie_details, char_details):
    movie_dataset = {}
    for movie_id in movie_plots_data:
        if movie_id not in movie_details:
            continue
        modified_plot = f"Film Genre:{movie_details[movie_id]['genres']}, Starring the actors: {char_details.get(movie_id,{}).get('actor_name', 'information not available')}, Released in the year: {movie_details.get(movie_id, {}).get('year', 'information not available')}, Summary of the movie plot: {movie_plots_data[movie_id]}"
        movie_dataset[movie_details[movie_id]["name"]] = modified_plot
    return movie_dataset


def createTrainingDataset():
    movie_plots_data = readPlotSummaries('Dataset/plot_summaries.txt')
    movie_details = readMovieDetails('Dataset/movie.metadata.tsv')
    char_details = readCharDetails('Dataset/character.metadata.tsv')
    movie_dataset = createMovieDataset(movie_plots_data, movie_details, char_details)
    output_csv_path = 'Dataset/movie_dataset.csv'
    # writeToCSV(output_csv_path, movie_dataset) - uncomment this line to save CSV
