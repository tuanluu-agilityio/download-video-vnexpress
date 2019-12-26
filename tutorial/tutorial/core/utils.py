def convert_to_mp4(url):
    return url.replace('d1', 'v').replace(',240p,360p,480p,,/', '').replace('/vne/master.m3u8', '.mp4').split('/')


def get_new_url(url):
    formatted_video = convert_to_mp4(url)

    new_url = []
    for index, item in enumerate(formatted_video):
        if item not in new_url:
            new_url.append(item)

    return '/'.join(new_url), formatted_video[-1]
