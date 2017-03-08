


def main():
    names = []
    with open("names.txt", "r") as infile:
        for name in infile:
            full_name = name.strip().split("\t")
            first_name = full_name[0]
            if first_name in names:
                continue
            else:

                names.append(first_name)

    names_string = ",".join(names)
    print(names)

if __name__ == "__main__":
    main()
