from pathlib import Path
import os

command = ""

def run(command):
  while command != "Q":
    file_list = []
    directory_list = []
    command = input("\nPlease input something, to quit: press Q\n\n")
    if command[0] == "Q":
      quit
    ### L
    elif command[0] == "L":
      command_split = command.split()
      if len(command_split) == 2:
        p = Path(command_split[1])
        for obj in p.iterdir():
          if FileNotFoundError == True:
            pass
          if obj.is_file():
            file_list.append(str(obj))
          elif obj.is_dir():
            directory_list.append(str(obj))
          else:
            print("ERROR")
        for x in file_list:
          print(x)
        for x in directory_list:
          print(x)
      else:   
        for x in command_split[2:]:
          ### L, -r
          if x == "-r" and command_split.count("-f") == 0 and command_split.count("-e") == 0 and command_split.count("-s") == 0:
            printing_list = []
            p = Path(command_split[1])
            for obj in p.iterdir():
              if obj.is_file():
                printing_list.insert(0, str(obj))
              elif obj.is_dir:
                printing_list.append(str(obj))
                for y in obj.iterdir():
                  printing_list.append(str(y))
              else:
                print("ERROR")
            for z in printing_list:
              print(z)
          ### L, -r, -f
          elif x == "-r" and command_split.count("-f") == 1:
            printing_list = []
            p = Path(command_split[1])
            for obj in p.iterdir():
              if obj.is_file():
                printing_list.insert(0, str(obj))
              elif obj.is_dir:
                for y in obj.iterdir():
                  if y.is_file():
                    printing_list.append(str(y))
              else:
                print("ERROR")
            for z in printing_list:
              print(z)
          ### L, -f
          elif x == "-f" and command_split.count("-r") == 0:
            p = Path(command_split[1])
            for obj in p.iterdir():
              if obj.is_file():
                file_list.append(str(obj))
              elif obj.is_dir():
                directory_list.append(str(obj))
              else:
                print("ERROR")
            for x in file_list:
              print(x)
          ### L, -e
          elif x == "-e" and command_split.count("-r") == 0:
            printing_list = []
            p = Path(command_split[1])
            for obj in p.iterdir():
              literal_obj = str(obj)
              if obj.is_file():
                if command_split[-1] in literal_obj[-2:]:
                  printing_list.append(str(obj))
              else:
                print("ERROR")
            for x in printing_list:
              print(x)
          ### L, -r, -e
          elif x == "-e" and command_split.count("-r") == 1:
            printing_list = []
            p = Path(command_split[1])
            for obj in p.iterdir():
              literal_obj = str(obj)
              if obj.is_file():
                if command_split[-1] in literal_obj[-2:]:
                  printing_list.append(str(obj))
              elif obj.is_dir():
                for y in obj.iterdir():
                  literal_y = str(y)
                  if command_split[-1] in literal_y[-2:]:
                    printing_list.append(str(y))
              else:
                print("ERROR")
            for x in printing_list:
              print(x)
          ### L, -s
          elif x == "-s" and command_split.count("-r") == 0:
            printing_list = []
            p = Path(command_split[1])
            for obj in p.iterdir():
              same_name = str(obj)
              if command_split[-1] in same_name:
                printing_list.append(str(obj))
              else:
                print("ERROR")
            for x in printing_list:
              print(x)
          ### L, -r, -s
          elif x == "-s" and command_split.count("-r") == 1:
            printing_list = []
            p = Path(command_split[1])
            for obj in p.iterdir():
              same_name = str(obj)
              if command_split[-1] in same_name:
                printing_list.append(str(obj))
              if obj.is_dir():
                for y in obj.iterdir():
                  same_name1 = str(y)
                  if command_split[-1] in same_name1:
                    printing_list.append(str(y))
              else:
                print("ERROR")
            for x in printing_list:
              print(x)
    ### C
    elif command[0] == "C":
      command_split = command.split()
      np = Path(command_split[1] + "/" + command_split[-1] + ".dsu")
      np.touch()
    ### D
    elif command[0] == "D":
      command_split = command.split()
      if command.count(".dsu") >= 1:
        os.remove(command_split[1])
        print(command_split[1], "DELETED")
      else:
        print("ERROR")
    ### R
    elif command[0] == "R":
      if command.count(".dsu") >= 1:
        command_split = command.split()
        if os.stat(command_split[1]).st_size == 0:
          print("EMPTY")
        else:
          file = open(command_split[1])
          print(file.readline())
      else:
        print("ERROR")
        command = input("Please put new input")
    ### Invalid Input
    else:
      print("ERROR")


run(command)
