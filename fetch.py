import requests

def fetch_comments(api_key, video_id):
    URL = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part" : "snippet",
        "videoId" : video_id,
        "key" : api_key,
        "maxResults" : 20
    }

    comments = []

    response = requests.get(URL, params)
    if response.status_code == 200:
        for item in response.json().get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
    else:
        print(f"Error : {response.json()}")

    return comments