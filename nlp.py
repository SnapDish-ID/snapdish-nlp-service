import pandas as pd
import tensorflow as tf

def cosine_similarity(a, b):
    a = tf.constant(a, dtype=tf.float32)
    b = tf.constant(b, dtype=tf.float32)
    dot_product = tf.reduce_sum(a * b, axis=1)
    norm_a = tf.sqrt(tf.reduce_sum(a**2, axis=1))
    norm_b = tf.sqrt(tf.reduce_sum(b**2, axis=1))
    similarity = dot_product / (norm_a * norm_b)
    return similarity

def recipes_recommendation(main_ingredient, ingredients_list):
    csv_file = "./dataset.csv"
    df = pd.read_csv(csv_file)

    ingredients = ", ".join(ingredients_list)

    category = df[df['category'] == main_ingredient]
    dataset_ingredients = category["ingredients_cleaned"].astype(str).tolist()

    max_vocab_size = 10000
    sequence_length = 50

    vectorizer = tf.keras.layers.TextVectorization(
        max_tokens=max_vocab_size,
        output_mode="int",
        output_sequence_length=sequence_length,
    )

    vectorizer.adapt(dataset_ingredients)
    encoded_dataset = vectorizer(dataset_ingredients).numpy()
    encoded_input = vectorizer([ingredients]).numpy()

    similarity_scores = cosine_similarity(encoded_dataset, encoded_input).numpy()
    category['similarities'] = similarity_scores
    
    results = category.sort_values('similarities',ascending=False).drop_duplicates(subset=['title'], keep='first').iloc[:3][["recipe_id","title", "category"]]

    recipes = results.to_dict(orient='records')

    return recipes
