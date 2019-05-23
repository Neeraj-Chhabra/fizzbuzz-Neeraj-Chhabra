#assuming the text to be copied is in a file
import string
import os
if __name__ == "__main__":
	try:
		init_page=int(input("Enter the initial page number to  be copied = "))
		end_page=int(input("Enter the final page to be copied = "))
		target_file_name=input("Enter the file name where text to be copied = ")
		target_location=input("Enter the target location(optional) = ")
	
		if target_location=='':
			tl=target_file_name
			print("Target location is ", tl)
		else:
			tl=target_location/target_file_name
			print("Target location is ", tl)

	except:
		pass
	tl='text.txt'
	def copy_pages(ip,ep,tl):
		end_line=25*ep
		start_line=25*ip+1
		os.system("sed -n '%s,75p' Book1.txt >> text.txt" %ip )
		print("the new file created is text.txt")
		
	copy_pages(init_page,end_page,tl)

def L33t(word):
	for char in word:
		if char == 'o' or char == 'O':
			char.replace(char,'0')
		elif word =='e' or word == 'E':
			char.replace(char,'3')
		else:
			pass
	if word.endswith('er'):
		word.replace('er','x0r')
	return(word)


myfile=open("text.txt", 'r')
for line in myfile:
	line.strip()
	line.split()
	for word in line:
		word=L33t(word)
myfile.close()
