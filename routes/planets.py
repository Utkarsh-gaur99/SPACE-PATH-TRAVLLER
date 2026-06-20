from fastapi import APIRouter

router = APIRouter()

PLANETS_DATA = [
    {
        "name": "Earth",
        "gravity": "9.8 m/s²",
        "temperature": "15°C",
        "distance_from_sun": "149.6 million km",
        "description": "Our home planet, the only known place in the universe to harbor life."
    },
    {
        "name": "Moon",
        "gravity": "1.62 m/s²",
        "temperature": "-233 to 123°C",
        "distance_from_sun": "150 million km (avg with Earth)",
        "description": "Earth's only natural satellite."
    },
    {
        "name": "Mars",
        "gravity": "3.71 m/s²",
        "temperature": "-65°C",
        "distance_from_sun": "227.9 million km",
        "description": "The Red Planet, a prime candidate for future human colonization."
    },
    {
        "name": "Venus",
        "gravity": "8.87 m/s²",
        "temperature": "464°C",
        "distance_from_sun": "108.2 million km",
        "description": "Earth's toxic twin, with a runaway greenhouse effect."
    },
    {
        "name": "Jupiter",
        "gravity": "24.79 m/s²",
        "temperature": "-110°C",
        "distance_from_sun": "778.5 million km",
        "description": "The largest planet in our solar system, a gas giant."
    }
]

@router.get("/")
def get_planets():
    return PLANETS_DATA
