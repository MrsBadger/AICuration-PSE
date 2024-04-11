from asyncio import sleep
from collections import Counter
from typing import Dict, List, Optional

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError

from core.settings import (
        USERS_URL,
        POSTS_URL,
        logger,
    )


async def get_data(
        url: str,
        retries: int = 4) -> Optional[Dict]:
    """Asynchronously fetches data from the provided URL
        using the given session with retry mechanism.

    Args:
        url: The URL to fetch data from.
        retries (int): Number of retries in case of failure. Default is 3.

    Returns:
        A dictionary containing the fetched data if successful,
        or None if an error occurs.
    """
    backoff_time = 1  # Initial backoff time

    for i in range(retries):
        try:
            async with ClientSession() as session:
                async with session.get(url=url) as response:
                    return await response.json()
        except ClientError as e:
            if i == retries - 1:
                raise e
            logger.info(f"Retrying in {backoff_time} seconds...")
            await sleep(backoff_time)
            backoff_time *= 2  # Exponential backoff

    return None


async def fetch_data() -> Optional[tuple[List[Dict], List[Dict]]]:
    """Fetches data for users and posts from their respective endpoints.

    Returns:
        A tuple containing a list of users and a list of posts if successful,
            or None if an error occurs.
    """

    if not USERS_URL or not POSTS_URL:
        logger.error("Missing environment variables USERS_URL or POSTS_URL")
        return None

    try:
        users = await get_data(USERS_URL)
        posts = await get_data(POSTS_URL)
        return users, posts
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return None, None


def analyze_data(users: List[Dict], posts: List[Dict]) -> Dict:
    """Analyzes the user data and post data to identify user with most posts,
    average post title length, and common words.

    Args:
        users: A list of dictionaries containing user data.
        posts: A list of dictionaries containing post data.

    Returns:
        A dict containing the analysis results.
    """
    user_post_counts = {user["id"]: 0 for user in users}
    for post in posts:
        user_post_counts[post["userId"]] += 1

    # Find user with most posts
    most_posts_user = max(user_post_counts, key=user_post_counts.get)
    most_posts_count = user_post_counts[most_posts_user]

    # Calculate average post title length
    total_title_length = 0
    title_count = 0

    for post in posts:
        if "title" in post:
            total_title_length += len(post["title"])
            title_count += 1
    avg_title_length = total_title_length / title_count if title_count > 0 else 0

    # Find most common words
    all_titles = [post["title"] for post in posts if "title" in post]
    word_counts = Counter(" ".join(all_titles).lower().split())
    most_common_words = word_counts.most_common(10)  # Top 10 most common words

    return {
        "userWithMostPosts": most_posts_user,
        "mostPostsCount": most_posts_count,
        "avgPostTitleLength": avg_title_length,
        "mostCommonWords": most_common_words,
    }
