import os

input_dir = "./docs"

for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith(".md") or filename.endswith(".mdx"):
            input_path = os.path.join(root, filename)
            with open(input_path, "r") as input_file:
                contents = input_file.read()
            while True:
                start = contents.find("---")
                if start == -1:
                    break
                end = contents.find("---", start + 3)
                if end == -1:
                    break
                contents = contents[:start] + contents[end + 3 :]
            index = contents.find("##")
            if index >= 0:
                contents = contents[index:]
            contents = f"\n\n# {filename}\n{contents}"

            with open("data.txt", "a") as output_file:
                output_file.write(contents)
