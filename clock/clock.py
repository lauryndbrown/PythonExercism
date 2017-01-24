"""
Date-Independent Clock Implementation 
"""

class Clock:
    """
    Class implementing a clock. 
    """
    MAX_HOUR = 24
    MAX_MINUTE = 60
    def __init__(self, hour, minutes):
        
        self.minutes, additional_hours = Clock._convert_minutes(minutes)
        self.hour = Clock._convert_hour(hour+additional_hours)
    def add(self, minutes):
        """
        Adds minutes to the current clock time

        Given: Int representing minutes
        Returns: Clock
        """
        minutes, additional_hours = Clock._convert_minutes(self.minutes+minutes)
        self.minutes = minutes
        self.hour = Clock._convert_hour(self.hour+additional_hours)
        return self
        
    def _convert_minutes(minutes):
        """
        Private method that converts minutes to minutes and hours
        Given: int minutes
        Returns: int minutes, int additional_hours
        """
        if not isinstance(minutes, int):
            raise ValueError("Minutes Parameter for Clock must be of type int")
        additional_hours = int(minutes/Clock.MAX_MINUTE)
        if minutes < 0:
            additional_hours-=1
        return minutes%Clock.MAX_MINUTE, additional_hours

    def _convert_hour(hours):
        """
        Private method that converts hours to 24 hours
        Given: int hours
        Returns: int hour
        """
        if not isinstance(hours, int):
            raise ValueError("Hour Parameter for Clock must be of type int")
        return hours%Clock.MAX_HOUR

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minutes)

    def __eq__(self, other):
        return self.hour==other.hour and self.minutes==other.minutes

