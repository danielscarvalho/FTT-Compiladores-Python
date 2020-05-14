# Site do PIP, página da biblioteca
# https://pypi.org/project/lyricwikia/

# Comando para instalar a biblioteca, rodar no terminal
# pip install lyricwikia
# sudo python3 -m pip install spotify-cli-linux

import lyricwikia
       
lyrics = lyricwikia.get_lyrics('Led Zeppelin', 'Stairway to heaven')

print(lyrics)