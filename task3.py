import string
import operator
def depunct(line):
	for word in string.punctuation:
		line=line.replace(word,"")
	return(line)


def get_uniq_words(book,bookw):
		mylst=[]
		myfile=open(book,'r')	
		for line in myfile:
			line=line.strip()
			line=depunct(line)
			line=line.split()
			for word in line:
				if word in mylst:
				        pass	
				else:
					mylst.append(word)

		myfin=open("20k.txt","r")
		myfin2=open(bookw,"w+")
		for line in myfin:
				line=line.strip()
				line=depunct(line)
				line=line.split()
				for word in line:
					if word in mylst:
						pass
					else:
						myfin2.write(word)
						myfin2.write("\n")

get_uniq_words("Book1.txt", "book1uniqu.list")
get_uniq_words("Book2.txt", "book2uniqu.list")
get_uniq_words("Book3.txt", "book3uniqu.list")


booklist=["Book1.txt","Book2.txt","Book3.txt"]

def get_rare_words(books):
        mylist=[]
        for book in books:
                myfile=open(book,'r')
                for line in myfile:
                        line=line.strip()
                        line=depunct(line)
                        line=line.split()
                        for word in line:
                                if word in mylist:
                                        pass
                                else:
                                        mylist.append(word)
        myfin=open("20k.txt",'r')
        myfin2=open("rarewords.list", "w+")
        for line in myfin:
                        line=line.strip()
                        line=depunct(line)
                        line=line.split()
                        for word in line:
                                if word in mylist:
                                        pass
                                else:
                                        myfin2.write(word)
                                        myfin2.write("\n")

get_rare_words(booklist)
