from modul.base_text import BaseText


class Comment(BaseText):

    # Ez nem is kellene, egy sima pass elég lenen, akkor is lefut az ős init!!
    def __init__(self):
        super().__init__()
        print("Comment init")
