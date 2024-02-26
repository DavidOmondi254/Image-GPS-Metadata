import exifread
tags=exifread.process_file(open('philip.jpeg','rb'))
geo={(tags[i]) for i in tags.keys() if i.startswith('GPS')}
print(geo["GPS GPSLatitude"])
print(geo["GPS GPSLongitude"])
print(geo["GPS GPSDate"])