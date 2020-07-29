import pyshorteners

#creating instance
shorten=pyshorteners.Shortener()

#using tinyurl to shorten
print(shorten.tinyurl.short(".....URL....."))
