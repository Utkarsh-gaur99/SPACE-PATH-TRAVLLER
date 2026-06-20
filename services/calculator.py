PLANET_DISTANCES = {
    "Earth": 0,
    "Moon": 384400,
    "Mars": 225000000,
    "Venus": 41000000,
    "Jupiter": 778000000,
}

def calculate_distance(source: str, destination: str) -> float:
    # Simplified straight-line distance relative to Earth as 0
    src_dist = PLANET_DISTANCES.get(source, 0)
    dst_dist = PLANET_DISTANCES.get(destination, 0)
    return abs(src_dist - dst_dist)

def calculate_travel_time(distance: float, speed: float) -> dict:
    if speed <= 0:
        return {"hours": 0, "days": 0, "years": 0}
        
    hours = distance / speed
    days = hours / 24
    years = days / 365.25
    
    return {
        "hours": round(hours, 2),
        "days": round(days, 2),
        "years": round(years, 2)
    }
