def mins_to_sec(song_len):
    """
    :param song_len: a string representing the length of a song in minutes, for example '5:07"
    :type song_len:string
    :return: the length of the song in seconds
    :rtype: int
    """
    songs_det = song_len.split(":")
    return int(songs_det[0]) * 60 + int(songs_det[1])


def my_mp3_playlist(file_path):
    """
    :param file_path:a file containing different songs, their names, artist and length
    :type file_path: string
    :return: The function returns a tuple in which the first item is the longest song in the file, the second
            item in then amount of songs and the third item is the artist which appears the most times
             in the file
    :rtype: tuple
    """
    file = open(file_path, 'r')
    returned_tup = ()
    file_content = file.read()
    first_format = file_content.split("\n")
    songs_dict = {}
    for i in first_format:
        temp_list = i.split(";")
        songs_dict[temp_list[0]] = mins_to_sec(temp_list[2])
    print(songs_dict)
    max_len = 0
    max_len_song = ""
    for i in first_format:
        temp_list = i.split(";")
        if (mins_to_sec(temp_list[2]) > max_len):
            max_len = mins_to_sec(temp_list[2])
            max_len_song = temp_list[0]
    returned_tup = returned_tup + (max_len_song,)
    returned_tup = returned_tup + (len(songs_dict.keys()),)
    artist_list = []
    for i in first_format:
        temp_list = i.split(";")
        artist_list.append(temp_list[1])
    max_times = 0
    max_artist = artist_list[0]
    for artist in artist_list:
        if (artist_list.count(artist) > max_times):
            max_artist = artist
            max_times = artist_list.count(artist)
    returned_tup = returned_tup + (max_artist,)
    return returned_tup


def main():
    print(my_mp3_playlist(r"file1"))


if __name__ == '__main__':
    main()
