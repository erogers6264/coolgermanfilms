#!/usr/bin/python
# -*- coding: UTF-8 -*-
import media
import fresh_tomatoes

# My Movie instances
goodbyelenin = media.Movie(
	"Goodbye Lenin",
	"A man keeps his mother from realizing the fall of the Berlin wall.",
	"https://www.movieposter.com/posters/archive/main/60/MPW-30406",
	"https://youtu.be/iJb4efZcFUM",
	7.7)

gegendiewand = media.Movie(
	"Gegen die Wand",
	"Hartes Leben, schwierige Liebe",
	"http://movieposters.2038.net/p/Gegen-Die-Wand-(Head-On).jpg",
	"https://youtu.be/OoEskub6VdY",
	8.0)

lola = media.Movie(
	"Lola",
	"Fascinating representations of capitalism in early 20th century Germany",
	"https://www.movieposter.com/posters/archive/main/108/MPW-54276",
	"https://youtu.be/EbymV9kqSrw",
	7.7)

ausderferne = media.Movie(
	"The Marriage of Maria Braun",
	"A woman's family life is challenged during the post-WWII era",
	"https://upload.wikimedia.org/wikipedia/en/6/6b/Original-poster-marriage-of-maria-braun.jpg", # noqa
	"https://youtu.be/iFeEa5ijFLU",
	7.9)

imjuli = media.Movie(
	"Im Juli",
	"Eine Liebesgeschichte, lustig, im Sommer",
	"http://rymimg.com/lk/f/l/4cefe4ddaa9e035dbf737610ca4caab0/1007166.jpg",  # noqa
	"https://youtu.be/S5PzL-M3aWM",
	7.8)

metropolis = media.Movie(
	"Metropolis",
	"A pioneer film in showing the bridge between class, man and machine",
	"http://i.imgur.com/GlMid.jpg",
	"https://youtu.be/ZSExdX0tds4",
	8.3)

keinohrhasen = media.Movie(
	"Keinohrhasen",
	"Ein arroganter Typ und eine pikante Frau",
	"https://upload.wikimedia.org/wikipedia/az/c/c8/Keinohrhasen-poster.jpg",
	"https://youtu.be/2GuO_M7gEgc",
	6.7)

liebeingedanken = media.Movie(
	"Was nützt die Liebe in Gedanken",
	"Dangerous love does not end up very nicely",
	"http://www.filmposter-archiv.de/filmplakat/2004/was_nuetzt_die_liebe_in_gedanken.jpg",  # noqa
	"https://youtu.be/urvp9lbvHJc",
	7.1)

# Arrange instances of Movie into a list.
movies = [goodbyelenin, gegendiewand, lola, ausderferne, imjuli,
		metropolis, keinohrhasen, liebeingedanken]

# Pass the list into the function in provided module to generate the HTML
# file & open.
fresh_tomatoes.open_movies_page(movies)
