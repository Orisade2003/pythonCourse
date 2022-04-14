def my_mp4_playlist(file_path, new_song):
    """
    :param file_path:path to songs file
    :type file_path: string
    :param new_song: new song to add the third line
    if there are more than 3 lines in the songs file, the name of song at the third line is changed to
    new_song, if there are less than 3 lines, then empty lines are added unti there are 3 lines
    and the name of the new song is added there
    :type new_song: string
    """
    opened_file = open(file_path,'r')
    read_file = opened_file.read()
    songs_list = read_file.split("\n")
    if len(songs_list) >=3:
        third_song = songs_list[2]
        third_song_list = third_song.split(";")
        third_song_list[0] = new_song
        songs_list[2] = ";".join(third_song_list)
        opened_file.close()
        opened_file = open(file_path, 'w')
        joined_list = "\n".join(songs_list)
        opened_file.write(joined_list)
    else:
        opened_file.close()
        opened_file = open(file_path,'w')
        print(len(songs_list))
        while len(songs_list) <2:
            songs_list.append("")
        songs_list.append(new_song)
        joined_list = "\n".join(songs_list)
        opened_file.write(joined_list)
    opened_file.close()
    opened_file = open(file_path,'r')
    print(opened_file.read())
    opened_file.close()

def main():
    my_mp4_playlist(r"file1", "python song")

if __name__ == '__main__':
    main()
