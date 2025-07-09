import pandas as pd
from datetime import datetime

fb_file_path = "/Users/faitusjelinejoseph/Documents/Project/Social/Final_Facebook_Posts_With_Captions.xlsx"
ig_file_path = "/Users/faitusjelinejoseph/Documents/Project/Social/Instagram captions.xlsx"
report_file_path = "/Users/faitusjelinejoseph/Documents/Project/Social/Digital Engagement Report 2024-25.xlsx"

fb_df = pd.read_excel(fb_file_path, sheet_name='Sheet1')
ig_df = pd.read_excel(ig_file_path, sheet_name='Sheet1')
report_data = pd.read_excel(report_file_path, sheet_name=None)
activity_df = report_data['Social Activity Tracker']

fb_df_cleaned = fb_df.rename(columns={
    'Post Date': 'post_date',
    'Museum Name': 'museum_name',
    'Formatted Facebook Caption': 'caption'
})
fb_df_cleaned['platform'] = 'Facebook'

ig_df_cleaned = ig_df.rename(columns={
    'Date Posted': 'post_date',
    'Museum Site': 'museum_name',
    'Full Caption': 'caption'
})
ig_df_cleaned['platform'] = 'Instagram'

fb_df_cleaned = fb_df_cleaned[['post_date', 'museum_name', 'caption', 'platform']]
ig_df_cleaned = ig_df_cleaned[['post_date', 'museum_name', 'caption', 'platform']]
combined_posts = pd.concat([fb_df_cleaned, ig_df_cleaned], ignore_index=True)
combined_posts['post_date'] = pd.to_datetime(combined_posts['post_date'], errors='coerce')

start_date = datetime(2024, 4, 11)
end_date = datetime(2025, 3, 21)
combined_posts = combined_posts[
    (combined_posts['post_date'] >= start_date) &
    (combined_posts['post_date'] <= end_date)
].dropna(subset=['caption', 'post_date'])

activity_df_cleaned = activity_df.rename(columns={
    'Day': 'day',
    'Month': 'month',
    'Site': 'site',
    'Content Type': 'content_type',
    'Total Active Engagements (Like, Comment, Share, Video >15s)': 'engagements',
    'Total Reach': 'reach'
})
activity_df_cleaned = activity_df_cleaned.dropna(subset=['site', 'month'])

month_str_to_num = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
activity_df_cleaned['month'] = activity_df_cleaned['month'].map(month_str_to_num)
activity_df_cleaned['day'] = activity_df_cleaned['day'].fillna(15).astype(int)
activity_df_cleaned['post_date'] = pd.to_datetime({
    'year': 2024,
    'month': activity_df_cleaned['month'],
    'day': activity_df_cleaned['day']
}, errors='coerce')

site_to_museum = {
    'UFM': 'Ulster Museum',
    'UTM': 'Transport Museum',
    'AFP': 'American Folk Park'
}
activity_df_cleaned['museum_name'] = activity_df_cleaned['site'].map(site_to_museum)

activity_df_cleaned['platform'] = activity_df_cleaned['content_type'].apply(
    lambda x: 'Facebook' if isinstance(x, str) and 'Facebook' in x else 'Instagram'
)

merged_df = pd.merge(
    combined_posts,
    activity_df_cleaned[['post_date', 'museum_name', 'platform', 'engagements', 'reach']],
    on=['post_date', 'museum_name', 'platform'],
    how='left'
)

output_csv = "/Users/faitusjelinejoseph/Documents/Project/Social/cleaned_posts_with_engagement.csv"
merged_df.to_csv(output_csv, index=False)

print("Cleaned dataset with engagement exported to:")
print(output_csv)

#################################################


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime

file_path = "/Users/faitusjelinejoseph/Documents/Project/Social/cleaned_posts_with_engagement.csv"
df = pd.read_csv(file_path, parse_dates=['post_date'])

tfidf = TfidfVectorizer(max_features=100)
tfidf_matrix = tfidf.fit_transform(df['caption'].fillna("")).toarray()
tfidf_df = pd.DataFrame(tfidf_matrix, columns=[f'tfidf_{word}' for word in tfidf.get_feature_names_out()])

df['hashtag_count'] = df['caption'].str.count('#')
df['day_of_week'] = df['post_date'].dt.day_name()
df['hour_of_day'] = df['post_date'].dt.hour
df['month'] = df['post_date'].dt.month

def get_season(month):
    return (
        'Spring' if month in [3, 4, 5] else
        'Summer' if month in [6, 7, 8] else
        'Autumn' if month in [9, 10, 11] else
        'Winter'
    )

df['season'] = df['month'].apply(get_season)

museum_counts = df['museum_name'].value_counts()
hot_museums = museum_counts[museum_counts >= museum_counts.median()].index.tolist()
df['is_hot_museum'] = df['museum_name'].apply(lambda x: 1 if x in hot_museums else 0)

final_df = pd.concat([
    df[['post_date', 'caption', 'museum_name', 'platform', 'engagements', 'reach',
        'hashtag_count', 'day_of_week', 'hour_of_day', 'month', 'season', 'is_hot_museum']],
    tfidf_df
], axis=1)

output_csv = "/Users/faitusjelinejoseph/Documents/Project/Social/feature_engineered_posts.csv"
final_df.to_csv(output_csv, index=False)

print("Feature engineering complete. Saved to:")
print(output_csv)
