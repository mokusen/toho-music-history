def create_param(song, form, num):
    max = len(song)
    display_min = 25 * (num - 1)
    display_max = 25 * num if num >= max % 25 else max
    param = {
        "form": form,
        'song': song,
        'max': max,
        "display_min": display_min,
        "display_max": display_max,
    }
    return param