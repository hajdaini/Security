import exifread
import sys

try:
    image = open(sys.argv[1], 'rb')
except Exception as e:
    print(e)
    exit(1)

tags = exifread.process_file(image)
latitude = tags.get('GPS GPSLatitude')
latitude_ref = tags.get('GPS GPSLatitudeRef')
longitude = tags.get('GPS GPSLongitude')
longitude_ref = tags.get('GPS GPSLongitudeRef')


def get_metadata():
    global tags
    for k, v in tags.items():
        if k not in ('JPEGThumbnail', 'TIFFThumbnail'):
            print("{}: {}".format(k, v))


def convert_to_degress(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)


def gps_handle():
    if latitude:
        lat_value = convert_to_degress(latitude)
        if latitude_ref.values != 'N':
            lat_value = -lat_value
    else:
        return None
    if longitude:
        lon_value = convert_to_degress(longitude)
        if longitude_ref.values != 'E':
            lon_value = -lon_value
    else:
        return None
    return '\nGPS INFO :\nLatitude: {} | Longitude: {}'.format(lat_value, lon_value)


get_metadata()
has_gps_info = gps_handle()

if has_gps_info is not None:
    print(has_gps_info)
