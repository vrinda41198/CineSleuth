import csv


def readTestDataset(file):
    test_movie_plots_data = {}
    counter = 0
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter='\t')
        for movie_data in csv_reader:
            movie_name = movie_data[1]
            movie_plot = movie_data[0]
            # print(movie)
            if movie_name in test_movie_plots_data:
                counter += 1
                print(movie_name)
            test_movie_plots_data[movie_name] = movie_plot
    print("Duplicate movie count", counter)
    return test_movie_plots_data


def testDataset():
    test_movie_plots_data = readTestDataset('Dataset/final_test_data.csv')
    print(test_movie_plots_data["Gone Girl"])
    print(len(test_movie_plots_data))
