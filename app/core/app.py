from typing import Dict

from core.settings import  app, logger
from core.utils import analyze_data, fetch_data


@app.get("/analysis")
async def get_analysis() -> Dict:
    """Retrieves user and post data, analyzes it,
    and returns the analysis results as JSON.

    Returns:
        A dictionary containing the analysis results,
        or an error message if data retrieval fails.
    """
    users, posts = await fetch_data()

    if users is None or posts is None:
        logger.error("Error fetching data, analysis failed.")
        return {"error": "Failed to retrieve data"}

    analysis_results = analyze_data(users, posts)
    return analysis_results
