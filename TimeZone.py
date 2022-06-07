from datetime import timedelta, datetime

class TimeZone:
    
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).str()) == 0:
            raise ValueError("TimeZone name cannot be empty")
        self.name = name.strip()
        
        if not isinstance(offset_hours, int):
            raise ValueError("offset_hours must be an integer")

        if not isinstance(offset_minutes, int):
            raise ValueError("offset_minutes must be an integer")

        if offset_hours < -12 or offset_hours > 14:
            raise ValueError("offset_hours must be between -12 and 14")
        
        if offset_minutes < 0 or offset_minutes > 59:
            raise ValueError("offset_minutes must be between 0 and 59")
        
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
    
        # if everything is ok, set the offset
        self.offset = offset
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes

        @property
        def offset_hours(self):
            return self._offset_hours
        
        @property
        def offset_minutes(self):
            return self._offset_minutes
        
    def __eq__(self, other: object) -> bool:
        return (isinstance(other, TimeZone) and
        self.name == other.name and
        self.offset_hours == other.offset_hours and
        self.offset_minutes == other.offset_minutes)
    
    def __repr__(self) -> str:
        # return a string representation of the TimeZone object
        return f"TimeZone({self.name}, {self.offset_hours}, {self.offset_minutes})"      
