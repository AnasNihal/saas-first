import requests
from pathlib import Path

def download_to_local(url: str, destination: Path, parent_mkdir:bool=True) :
    if not isinstance(destination, Path):
        raise ValueError(f"{destination}must be a valid pathlib path object")
    if parent_mkdir:
        destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        destination.write_bytes(response.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file {url}: {e}")
        return False