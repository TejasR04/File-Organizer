import shutil
import os

fileType = {"Audio": [".mp3", ".wav"],
            "Documents": [".docx", ".html", ".odt", ".pdf", ".pptx", ".txt", ".xlsx"],
            "Pictures": [".ico", ".gif", ".jpg", ".jpeg", ".png", ".svg"],
            "Videos": [".avi", ".h264", ".m4v", ".mp4", ".mpeg", ".wmv"],
            "Zipped": [".7z", ".pkg", ".rar", ".zip"],
	    "Executables": [".apk", ".bat", ".bin", ".cmd", ".com", ".exe", ".reg", ".run"]}

path = input("Enter the path to the directory you want to organize: ")

if path == "":
	path = os.getcwd()
	
while not os.path.exists(path):
	print("This path does not exist. Please check for errors and try again.")
	path = input("Enter the path to the directory you want to organize: ")
	if path == "": path = os.getcwd()
		
sortType = input("Enter 1 if you want to sort all files, or 2 if you want to sort only a specific category, like documents or videos: ")

if sortType == "1":
	pass

elif sortType == "2":
	category = input("Choose one of the categories to sort: Audio, Documents, Pictures, Videos, Zipped, Executables - ")
	try:
		fileType = {category: fileType.get(category)}
	except KeyError as e:
		print("Error! ", e)
		
else:
	print("Not a valid number. Sorting entire directory.")
	
def organize(path, fileType):
	if os.path.exists(path):
		for f in os.listdir(path):
			fPath = os.path.join(path, f)
			fName, fExt = os.path.splitext(fPath)
			
			if any(fExt in i for i in fileType.values()):
				for folder in fileType:
					destination = os.path.join(path, folder)
					
					if fExt in fileType[folder]:
						if not os.path.exists(destination):
							os.makedirs(destination)
						try:
							shutil.move(fPath, destination)
						except OSError as e:
							print("Error! ", e)
		print("\nSorted!")

if __name__ == "__main__":
    organize(path, fileType)
