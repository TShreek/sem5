import requests
import openai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from pytesseract import image_to_string
from PIL import Image
import os
# dont forget to install dependencies, ask chatgpt for help if u want

# Load environment variables from .env file
load_dotenv()

# Access API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

def simplify_content(raw_text):
    """
    Simplify a given text using OpenAI's GPT API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Explain this concept in simple terms: {raw_text}"}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error simplifying content: {e}"

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def extract_text_from_image(image_path):
    """
    Extract text from an image file using Tesseract OCR.
    """
    try:
        text = image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Error extracting text from image: {e}"

def search_articles(query):
    """
    Search for articles using the Google Custom Search API.
    """
    try:
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": query,
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Extract article titles, links, and descriptions
        results = []
        for item in data.get("items", []):
            title = item.get("title")
            link = item.get("link")
            snippet = item.get("snippet")
            results.append({"title": title, "link": link, "snippet": snippet})

        return results
    except Exception as e:
        return f"Error fetching articles: {e}"

def search_youtube_videos(query):
    """
    Search for relevant YouTube videos using the YouTube Data API.
    """
    try:
        url = f"https://www.googleapis.com/youtube/v3/search"
        params = {
            "key": YOUTUBE_API_KEY,
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": 5
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Extract video titles and links
        results = []
        for item in data.get("items", []):
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            video_id = item["id"]["videoId"]
            link = f"https://www.youtube.com/watch?v={video_id}"
            results.append({"title": title, "description": description, "link": link})

        return results
    except Exception as e:
        return f"Error fetching YouTube videos: {e}"

def calculate_relevance(topic, text):
    """
    Calculate relevance of a YouTube video to the topic using OpenAI's GPT API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"How relevant is this text to the topic '{topic}'? Rate it on a scale of 0 to 10: {text}"}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error calculating relevance: {e}"

def main():
    print("Welcome to the Advanced Topic Simplifier!")
    choice = input("Enter '1' for text, '2' for PDF, '3' for image: ")

    raw_text = ""
    if choice == "1":
        topic = input("Enter your topic: ")
        raw_text = topic
    elif choice == "2":
        pdf_path = input("Enter the PDF file path: ")
        raw_text = extract_text_from_pdf(pdf_path)
    elif choice == "3":
        image_path = input("Enter the image file path: ")
        raw_text = extract_text_from_image(image_path)
    else:
        print("Invalid choice. Exiting.")
        return

    print("\nFetching related articles...")
    articles = search_articles(raw_text)

    print("Fetching related YouTube videos...")
    videos = search_youtube_videos(raw_text)

    print("Simplifying the explanation...")
    simplified_text = simplify_content(raw_text)

    print("\n=== Simplified Explanation ===")
    print(simplified_text)

    print("\n=== Related Articles ===")
    if isinstance(articles, list):
        for idx, article in enumerate(articles[:5], start=1):  # Limit to top 5 articles
            print(f"{idx}. {article['title']} ({article['link']}) - {article['snippet']}")
    else:
        print(articles)

    print("\n=== Related YouTube Videos (with relevance) ===")
    if isinstance(videos, list):
        for idx, video in enumerate(videos, start=1):
            relevance = calculate_relevance(raw_text, f"{video['title']} {video['description']}")
            print(f"{idx}. {video['title']} ({video['link']}) - Relevance: {relevance}")
    else:
        print(videos)

if __name__ == "__main__":
    main()