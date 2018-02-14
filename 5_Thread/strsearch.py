# function to search for text string in a file
import mmap

def strIsInFile(string, fname):
    """Determine if string is in file of any type"""
    try :
        with open(fname, 'rb', 0) as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s :
            return s.find(bytes(string, 'utf-8')) != -1
    
    except ValueError :         # file is empty
        return False    
    except PermissionError :    # no permission
        return False
    except Exception as e:     # any other exception
        print(str(e))          # print exception reason so we can fix error 
        return False
