from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def show_station(station: SpaceStation) -> None:
    status = "Operational" if station.is_operational else "Offline"

    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last maintenance: {station.last_maintenance.isoformat()}")
    print(f"Status: {status}")
    if station.notes is not None:
        print(f"Notes: {station.notes}")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-06-15T09:30:00",
            notes="All systems within expected operating range.",
        )
        print("Valid station created:")
        show_station(station)
    except ValidationError as error:
        print(f"Unexpected validation error: {error}")

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD001",
            name="Overcrowded Relay",
            crew_size=25,
            power_level=75.0,
            oxygen_level=88.0,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
