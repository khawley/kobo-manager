# Kobo File and DB Manager

## Purpose

To be able to remove damaged, large or old books from my Kobo ereader device programmatically.  As my Kobo ([Kobo Wifi](https://www.kobo.com/help/category/kobo-ereaders/original-kobo-ereader-/-kobo-wi-fi)) only has a D-pad and poor software interface, I wanted more efficiency and accuracy.  (Similarly, the Desktop app doesn't seem to communicate with it well about deleting things either.)

## Basic Start

I did a fair amount of reading on [mobileread.com](mobileread.com) about my model of Kobo (Kobo Wifi, Model N647, circa 2010) and on Kobo systems in general.  I found a very helpful dive at [kobodb-schema.sourceforge.net](http://kobodb-schema.sourceforge.net/) where someone had dissected their kobo device db and determined the schema and relations.  I took that a step further and used a tool called [sqlacodegen](https://pypi.python.org/pypi/sqlacodegen) to generate a sqlalchemy mapping of my personal device db.  Now I can start using object oriented mappings to manuplate and update the data in my db.

(For those of you wondering why I didn't just SQL this jazz, my SQL foo is poor and rusty.  My Python foo is much better.  And its easier to share a project if its got code associated with it :D )
