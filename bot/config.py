#    This file is part of the Compressor distribution.

#    Copyright (c) 2021 Danish_00

#

#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU General Public License as published by

#    the Free Software Foundation, version 3.

#

#    This program is distributed in the hope that it will be useful, but

#    WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU

#    General Public License for more details.

#

# License can be found in <

# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:

    APP_ID = 8858279

    

    API_HASH = "ef28c3f458143cbcb4271a98a2e9d596"

    BOT_TOKEN = "6746742657:AAF9JhuGmYCYbX28fhKXoqu1I_S79CoOzSY"

    DEV = 1322549723

    OWNER = "5894098166"

    FFMPEG = config(

        "FFMPEG",

       default='''ffmpeg -i "{}" -c:v copy -map 0:v -c:a aac -b:a 96k -map 0:a -c:s copy -map 0:s? "{}"''',




    )

    THUMB = config(

        "THUMBNAIL", default="www.google.com"

    )

except Exception as e:

    print("Environment vars Missing")

    print("something went wrong")

    print(str(e))

    exit()
