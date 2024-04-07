class PhotoAlbum:
    MAX_PAGES = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = []
    def from_photos_count(self, photos_count):
        return