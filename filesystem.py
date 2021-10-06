#  The following program represents a file manager system.
#  The disk storage is 100KB with blocks of 1KB each. The user
#  can save a file to the disk with given fileID and fileSize.
#  The user can also read a given fileID from the disk or
#  delete a fileID from the disk.
#
#  MINIMISING FRAGMENTATION:
#
#  When saving a file to the disk, the program will check if
#  it's possible to store the file in continuous blocks in the
#  disk. If possible the file will be stored in continuous
#  blocks,  if not possible the file will be split up into
#  several continuous blocks.

#  The user can interact with the program via the terminal where
#  the current status of the disk is displayed. Empty blocks are
#  colored blue displaying 0 while occupied blocks are colored grey
#  displaying the fileID stored at the block.
#  All error messages are displayed in red text.


import numpy as np
import math
from colorama import init
from termcolor import colored
init()


blocks = np.zeros(100)


def consecutive(empty, numBlocks):
    start, end = 0, 0
    empty = empty[0]
    for i in range(1, len(empty)):
        if empty[i] - empty[i-1] == 1:
            end += 1
        else:
            start = i
            end = i

        if end - start == numBlocks - 1:
            return int(empty[start])

    return 1.1


def save(fileID, fileSize):
    numBlocks = int(math.ceil(fileSize/1024))

    empty = np.where(blocks == 0)

    if len(empty[0]) < numBlocks:
        print("No space on disk for this file size")
        return False

    if numBlocks == 1:
        blocks[empty[0][0]] = fileID
        return True

    start = consecutive(empty, numBlocks)
    if isinstance(start, int):
        for i in range(0, numBlocks):
            blocks[start + i] = fileID
        return True

    else:
        for i in range(0, numBlocks):
            print(i)
            blocks[empty[0][i]] = fileID
        return True


def delete(fileID):
    global blocks
    indices = np.where(blocks == fileID)
    if len(indices[0]) == 0:
        print("File with given ID doesn't exist on disk")
        return False
    blocks = np.where(blocks == fileID, 0, blocks)


def read(fileID):
    global blocks
    indices = np.where(blocks == fileID)
    if len(indices[0]) == 0:
        print("File with given ID doesn't exist on disk")
        return False
    print("File " + str(fileID) + " exists at blocks " + ' '.join(map(str, indices)))


def printdisk():
    for i in range(1, 101):
        if blocks[i-1]==0:
            if i % 10 == 0:
                print(colored(" " + str(blocks[i-1].astype(int)), 'green', 'on_blue'))
            else:
                print(colored(" " + str(blocks[i-1].astype(int)), 'green', 'on_blue'), end="")
        else:
            if i % 10 == 0:
                print(colored(" " + str(blocks[i-1].astype(int)), 'red', 'on_white'))
            else:
                print(colored(" " + str(blocks[i-1].astype(int)), 'red', 'on_white'), end="")


if __name__ == "__main__":

    cont = True

    print("\n")
    print("\033[1m" + "Welcome to the file system manager!" + "\033[0m")
    print("The disk storage is 100KB with blocks of size 1KB")
    print("The following 10x10  grid represents the memory blocks")
    printdisk()

    while cont:
        print("\033[1m" + "Choose from the following list of operations:" + "\033[0m")
        print("1. Save a file to disk")
        print("2. Delete a file from disk")
        print("3. Read a file from disk")
        print("4. Exit file system")


        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(colored("\033[1m" + "Please choose from [1/2/3]" + "\033[0m", 'red'))
            continue

        if choice == 1:
            print("\033[1m" + "SAVING FILE TO DISK" + "\033[0m")
            try:
                fileID = int(input("Enter file id (must be non-zero): "))
            except ValueError:
                print(colored(
                    "\033[1m" + "fileID must be integer" + "\033[0m",
                    'red'))
                continue

            indices = np.where(blocks == fileID)

            if len(indices[0]) != 0:
                print("File with given ID already exists on disk")
                fileID = int(input("Enter file id (must be non-zero): "))

            try:
                fileSize = int(input("Enter file size in bytes: "))
            except ValueError:
                print(colored(
                    "\033[1m" + "fileSize must be integer" + "\033[0m",
                    'red'))
                continue

            result = save(fileID, fileSize)
            if result !=  False:
                print("Updated disk looks like: ")
                printdisk()
            ans = input("Do you wish to continue? [y/n]: ")
            if ans ==  'y':
                cont = True
            elif ans == 'n':
                cont = False
                print("Thank you!")
            else:
                print(colored(
                    "\033[1m" + "Please choose from [y/n]" + "\033[0m",
                    'red'))

        elif choice == 2:
            print("\033[1m" + "DELETING FILE FROM DISK" + "\033[0m")
            try:
                fileID = int(input("Enter file id (must be non-zero): "))
            except ValueError:
                print(colored(
                    "\033[1m" + "fileID must be integer" + "\033[0m",
                    'red'))
                continue
            result = delete(fileID)
            if result !=  False:
                print("Updated disk looks like: ")
                printdisk()
            ans = input("Do you wish to continue? [y/n]: ")
            if ans ==  'y':
                cont = True
            elif ans == 'n':
                cont = False
                print("Thank you!")
            else:
                print(colored(
                    "\033[1m" + "Please choose from [y/n]" + "\033[0m",
                    'red'))

        elif choice == 3:
            print("\033[1m" + "READING FILE FROM DISK" + "\033[0m")
            try:
                fileID = int(input("Enter file id (must be non-zero): "))
            except ValueError:
                print(colored(
                    "\033[1m" + "fileID must be integer" + "\033[0m",
                    'red'))
                continue
            result = read(fileID)
            ans = input("Do you wish to continue? [y/n]: ")
            if ans ==  'y':
                cont = True
            elif ans == 'n':
                cont = False
                print("Thank you!")
            else:
                print(colored(
                    "\033[1m" + "Please choose from [y/n]" + "\033[0m",
                    'red'))

        elif choice ==4:
            print("Thank you!")
            exit(0)

        else:
            print(colored("\033[1m" + "Please choose from [1/2/3]" + "\033[0m",
                          'red'))






