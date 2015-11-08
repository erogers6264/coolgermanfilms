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
	"Shortbus",
	"A story of multiple sexual journeys",
	"http://www.impawards.com/2006/posters/shortbus_ver3_xlg.jpg",
	"https://youtu.be/H8A1dwEhSMY",
	6.6)

ausderferne = media.Movie(
	"The Grand Budapest Hotel",
	"A story of history, passion, and marvel",
	"http://www.grandbudapesthotel.com/images/gbhmulti3.jpg",
	"https://youtu.be/1Fg5iWmQjwk",
	8.1)

imjuli = media.Movie(
	"Coraline",
	"A deeper movie than one would first assume",
	"http://www.movie-poster-artwork-finder.com/posters/coraline-poster-artwork-dakota-fanning-teri-hatcher-jennifer-saunders.jpg",  # noqa
	"https://youtu.be/LO3n67BQvh0",
	7.7)

metropolis = media.Movie(
	"Metropolis",
	"A pioneer film in showing the bridge between class, man and machine",
	"http://i.imgur.com/GlMid.jpg",
	"https://youtu.be/ZSExdX0tds4",
	8.3)

keinohrhasen = media.Movie(
	"Fack ju Göhte",
	"I have not seen it but I heard it's good",
	"http://i.jeded.com/i/fack-ju-ghte-fck-you-goethe.24286.jpg",
	"https://youtu.be/8H_gk-4bX6o",
	7.1)

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
