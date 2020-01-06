def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def convert_to_mp4(url):
    dic = {
        'd1': 'v',
        ',240p,360p,480p,,/': '',
        ',240p,,/': '',
        ',360p,,/': '',
        ',480p,,/': '',
        '/vne/master.m3u8': '.mp4',
        '/index-v1-a1.m3u8': '.mp4'
    }

    return replace_all(url, dic).split('/')


def get_new_url(url):
    formatted_video = convert_to_mp4(url)

    new_url = []
    for index, item in enumerate(formatted_video):
        if item == 'video' and item not in new_url or item != 'video':
            new_url.append(item)

    return '/'.join(new_url), formatted_video[-1]
