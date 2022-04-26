import os
# Function to rename multiple files
def main():
   i = 1
   path = "metal_stamp_dataset/Training/"

   for filename in os.listdir(path):
      my_dest = "" + str(i) + ".jpg"
      my_source = path + filename
      my_dest = path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()
   