def convert(ratings, initial_rating=50):
    mapping = {1: 0.5, 2: 1, 3: 1.5}
    dynamic_ratings = [mapping[ratings[0]] * initial_rating]
    for rating in ratings[1:]:
        current_average = sum(dynamic_ratings) / len(dynamic_ratings)
        dynamic_rating = mapping[rating] * current_average
        dynamic_ratings.append(dynamic_rating)
    return dynamic_ratings

def normalize(input):
    normalized = [
        ((value - min(input)) / (max(input) - min(input))) * 100
        for value in input]
    unsorted = {
        str(2009 + i): round(rating,2)
        for i, rating in enumerate(normalized)}
    return dict(sorted(unsorted.items(), key=lambda item: item[1]))

ratings = [2,1,3,3,1,3,3,3,2,2,1,1,2,3,1]
ratings_test = [2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
result = normalize(convert(ratings_test))
for key, value in result.items():
    print(f"{key}: {value}")
