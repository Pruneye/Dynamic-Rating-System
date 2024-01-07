import csv
# Initial value can be anything since we normalise them between 0-100 in the end 
# Explain prinicple behind algo
def convert(ratings, initial=50):
    overall_average = sum(ratings)/len(ratings)
    dynamic_ratings = [ratings[0] * initial / overall_average]
    for rating in ratings[1:]:
        current_average = sum(dynamic_ratings) / len(dynamic_ratings)
        dynamic_rating = rating * current_average / overall_average
        dynamic_ratings.append(dynamic_rating)
    return dynamic_ratings

def normalize(input):
    return [round(((value - min(input)) / (max(input) - min(input))) * 100,2) for value in input]

titles, years, imdb, meta = [], [], [], []
with open('imdb_top_1000.csv', 'r') as file:
    csv_file = csv.reader(file)
    next(csv_file)
    for row in csv_file:
        titles.append(row[0])
        years.append(int(row[1]))
        imdb.append(int(row[2]))
        meta.append(int(row[3]))

rating_average = [round((a + b) / 2,2) for a, b in zip(imdb, meta)]
dynamic_imdb = normalize(convert(imdb))
dynamic_meta = normalize(convert(meta))
dynamic_average = [round((a + b) / 2,2) for a, b in zip(dynamic_imdb, dynamic_meta)]
rating_diff = [round(a - b,2) for a, b in zip(dynamic_average, rating_average)]
imdb_diff = [round(a - b,2) for a, b in zip(dynamic_imdb, imdb)]
meta_diff = [round(a - b,2) for a, b in zip(dynamic_meta, meta)]

with open("dynamic_top_1000.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Title', 'Year', 'IMDB','Dynamic IMDB','IMDB Difference', 'Metacritic', 'Dynamic Metacritic',
                         'Metacritic Difference', 'Original Rating', 'Dynamic Rating', 'Rating Difference'])
    rows = zip(titles,years, imdb, dynamic_imdb,imdb_diff, meta, dynamic_meta, meta_diff, rating_average, dynamic_average, rating_diff)
    sorted_rows = sorted(rows, key=lambda x: x[9], reverse= True)
    csv_writer.writerows(sorted_rows)