"""
Work with files
"""
from pathlib import Path

IMAGES = []
VIDEO = []
DOCUMENTS = []
AUDIO = []
ARCHIVES = []
OTHERS = []
KNOWN_EXT = []
UNKNOWN_EXT = []
FOLDERS = []

IMAGES_EXT = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO_EXT = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENTS_EXT = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
AUDIO_EXT = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVES_EXT = ('ZIP', 'GZ', 'TAR')

EXT = [IMAGES_EXT, VIDEO_EXT, DOCUMENTS_EXT, AUDIO_EXT, ARCHIVES_EXT]

REGISTER_EXTENSIONS = {
    IMAGES_EXT: IMAGES,
    VIDEO_EXT: VIDEO,
    DOCUMENTS_EXT: DOCUMENTS,
    AUDIO_EXT: AUDIO,
    ARCHIVES_EXT: ARCHIVES
}

EXCLUSION_SET = ('archives', 'video', 'audio', 'documents', 'images', 'others')


def pick_ext(file: Path):
    """
    Sorts files by the extensions
    :param file: Path
    :return: None
    """
    ext = file.suffix[1:].upper()
    if not ext:
        OTHERS.append(file)
        return
    for item in EXT:
        if ext in item:
            REGISTER_EXTENSIONS[item].append(file)
            KNOWN_EXT.append(ext)
            return
    OTHERS.append(file)
    UNKNOWN_EXT.append(ext)
    return


def scan_folder(folder: Path):
    """
    Goes through the folder and sorts the files
    :param folder: Path
    :return: None
    """
    if not folder.exists():
        print(f'No folder "{folder}" in current directory')
        return None
    for file in folder.iterdir():
        if file.is_dir():
            if file.name not in EXCLUSION_SET:
                scan_folder(file)
                FOLDERS.append(file)
            continue
        if file.is_file():
            pick_ext(file)
    return None


def print_lst():
    """
    Prints the lists with sorted files
    """
    if IMAGES:
        print('IMAGES:')
        for image in IMAGES:
            print(f'\t{image.name}')

    if VIDEO:
        print(f'VIDEO:')
        for video in VIDEO:
            print(f'\t{video.name}')

    if DOCUMENTS:
        print(f'DOCUMENTS:')
        for doc in DOCUMENTS:
            print(f'\t{doc.name}')

    if AUDIO:
        print(f'AUDIO:')
        for audio in AUDIO:
            print(f'\t{audio.name}')

    if ARCHIVES:
        print(f'ARCHIVES:')
        for arch in ARCHIVES:
            print(f'\t{arch.name}')

    if OTHERS:
        print(f'OTHERS:')
        for other in OTHERS:
            print(f'\t{other.name}')

    if FOLDERS:
        print(f'FOLDERS:')
        for folder in FOLDERS:
            print(f'\t{folder.name}')
    print()
    if KNOWN_EXT:
        print(f'Known extensions: {" ".join(set(KNOWN_EXT))}')
    if UNKNOWN_EXT:
        print(f'Unknown extensions: {" ".join(set(UNKNOWN_EXT))}')
