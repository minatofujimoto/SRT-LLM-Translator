import srt
from typing import List

def load_srt_file(file_path: str) -> List[srt.Subtitle]:
    """
    Loads and parses the SRT file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_content = file.read()
    return list(srt.parse(srt_content))

def save_str_file(output_path: str, subtitles: List[srt.Subtitle]):
    """
    Saves the translated subtitles to an SRT file.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(srt.compose(subtitles))
# Unit feature implementation - 20250203_0001
# Unit feature implementation - 20250204_0005
# Unit feature implementation - 20250206_0010
# Unit feature implementation - 20250207_0011
# Unit feature implementation - 20250211_0016
# Unit feature implementation - 20250211_0017
# Unit feature implementation - 20250212_0018
# Unit feature implementation - 20250213_0022
# Unit feature implementation - 20250224_0036
# Unit feature implementation - 20250227_0043
