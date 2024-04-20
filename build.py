import os

main_path = os.path.dirname(os.path.abspath(__file__))

print(main_path)

out_file = main_path+"//viper.src"

paths = [
    main_path+"//libs",
    main_path+"//functions",
    main_path+"//core_commands",
    main_path+"//commands",
    main_path+"//main"
]

print('\x1b[32m'+"Building..."+'\x1b[0m')

out = ""
for path in paths:

    files = os.listdir(path)
    for file in files:
        
        with open(path+"//"+file, "r") as f:
            out += f.read()+"\n"

with open(out_file, "w") as f:
    f.write(out)

print('\x1b[32m'+"Done building!"+'\x1b[0m')
