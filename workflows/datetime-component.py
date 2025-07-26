from typing import Dict, Any
from datetime import datetime
import pytz

class DateTimeComponent:
    """
    A Langflow component to handle time-related queries.
    Supports getting current date, time, and timezone information.
    """
    def __init__(self, timezone: str = 'UTC'):
        """
        Initialize the DateTimeComponent with a specific timezone.
        
        :param timezone: Timezone string (default is 'UTC')
        """
        try:
            self.timezone = pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            self.timezone = pytz.UTC

    def run(self, query: str) -> Dict[str, Any]:
        """
        Process time-related queries and return relevant information.
        
        :param query: Natural language query about date/time
        :return: Dictionary with time-related information
        """
        current_time = datetime.now(self.timezone)
        
        # Lowercase query for case-insensitive matching
        query = query.lower()
        
        result = {
            "original_query": query,
            "current_datetime": current_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "date": current_time.strftime("%Y-%m-%d"),
            "time": current_time.strftime("%H:%M:%S"),
            "timezone": str(self.timezone),
            "year": current_time.year,
            "month": current_time.strftime("%B"),
            "day": current_time.day,
            "day_of_week": current_time.strftime("%A")
        }

        # Process specific query types
        if "today" in query:
            result["answer"] = f"Today is {current_time.strftime('%A, %B %d, %Y')}"
        elif "time" in query:
            result["answer"] = f"The current time is {current_time.strftime('%I:%M %p')}"
        elif "timezone" in query:
            result["answer"] = f"The current timezone is {str(self.timezone)}"
        else:
            result["answer"] = "I can help with queries about date, time, or timezone."
        
        return result
