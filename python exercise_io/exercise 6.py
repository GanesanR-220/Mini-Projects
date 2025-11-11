# Write all content of a file into a new file by skipping line number 5

with open("test.txt", "r") as fp:
    lines = fp.readlines()

with open("new_file.txt", "w") as fp:
    count = 1
    for line in lines:

        if count == 5:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1
