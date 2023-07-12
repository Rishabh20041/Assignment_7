def update_file(file="data.txt"):
    try:
        f = open(file, "a")
        Roll_no = "47"
        Name = "Vishesh"
        Class_name = "TYCO_A"
        f.writelines([Roll_no + "\n", Name + "\n", Class_name + "\n"])
        f = open(file, "r")
        print(f.readlines())
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
update_file()